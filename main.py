# note does not run in jupyter notebook, run in the terminal
from fastapi import FastAPI
import uvicorn
import logging
import os
import pathlib
import torch
from datetime import datetime
from transformers import (AutoTokenizer, AutoModelForTokenClassification)
from src.output import NerResults
from src.input import get_document
from src.control import Job_list

# setup logging
# get todays date
datestamp = datetime.now().strftime('%Y%m%d')
container_name = os.getenv('CONTAINER_NAME')
# append date to logfile name
log_name = f'log-{container_name}-{datestamp}.txt'
path = os.path.abspath('./logs/')
# add path to log_name to create a pathlib object
# required for loggin on windows and linux
log_filename = pathlib.Path(path, log_name)

# create log file if it does not exist
if os.path.exists(log_filename) is not True:
    # create the logs folder if it does not exist
    if os.path.exists(path) is not True:
        os.mkdir(path)
    # create the log file
    open(log_filename, 'w').close()

# create logger
logger = logging.getLogger()
# set minimum output level
logger.setLevel(logging.DEBUG)
# Set up the file handler
file_logger = logging.FileHandler(log_filename)

# create console handler and set level to debug
ch = logging.StreamHandler()
# set minimum output level
ch.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter('[%(levelname)s] -'
                              ' %(asctime)s - '
                              '%(name)s : %(message)s')
# add formatter
file_logger.setFormatter(formatter)
ch.setFormatter(formatter)
# add a handler to logger
logger.addHandler(file_logger)
logger.addHandler(ch)
# mark the run
logger.info(f'Lets get started! - logginng in "{log_filename}" today')

# create the FastAPI app
app = FastAPI()

# create the job list
jobs = Job_list()

# load the model
model = AutoModelForTokenClassification.from_pretrained(
    './models/dslim/bert-base-NER')
tokenizer = AutoTokenizer.from_pretrained('./models/dslim/bert-base-NER')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def run():
    while len(jobs) > 0:
        # get the first job
        job = jobs.get_first_job()
        # get the document
        document = get_document(job)
        # run the model
        ner_results = NerResults(document['text'], model, tokenizer, device)
        # save the results
        load_to_graph_db(document, ner_results)
        # log the results
        logger.info(f'Job {job} complete')


# OUTPUT- routes
@app.get("/")
async def root():
    logging.info("Root requested")
    return {"message": "text NER conatiner API to work with text data"}


@app.get("/get_current_jobs")
async def get_current_jobs():
    """Get the current jobs"""
    logging.info("Current jobs list requested")
    return {"Current jobs": jobs.jobs}


# INPUT routes
@app.post("/add_job/{job}")
async def add_job(job: str):
    """Add a job to the list of jobs"""
    jobs.add(job)
    run()
    logging.info(f"Job {job} added")
    return {"message": f"Job {job} added"}


@app.post("/add_jobs_list/{jobs}")
async def add_jobs_list(jobs: str):
    """Add a list of jobs to the list of jobs"""
    jobs.add_list(jobs)
    run()
    logging.info(f"Jobs {jobs} added")
    return {"message": f"Jobs {jobs} added"}


@app.post("/remove_job/{job}")
async def remove_job(job: str):
    """Remove a job from the list of jobs"""
    jobs.remove(job)
    logging.info(f"Job {job} removed")
    return {"message": f"Job {job} removed"}


@app.post("/remove_jobs_list/{jobs}")
async def remove_jobs_list(jobs: str):
    """Remove a list of jobs from the list of jobs"""
    jobs.remove_list(jobs)
    logging.info(f"Jobs {jobs} removed")
    return {"message": f"Jobs {jobs} removed"}


@app.post("/remove_all_jobs")
async def remove_all_jobs():
    """Remove all jobs from the list of jobs"""
    jobs.clear()
    logging.info("All jobs removed")
    return {"message": "All jobs removed"}


if __name__ == "__main__":
    # goto localhost:8080/
    # or localhost:8080/docs for the interactive docs
    uvicorn.run(app, port=8080, host="0.0.0.0")