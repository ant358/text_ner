# Text Analyser

Takes in a text file and discovers the entities in the text.

## Installation
Clone the repository

Download and install python 3.9.7 make sure it is added to the path

Create a virtual environment with the right version of python and install the dependencies:

`py -3.9 -m venv venv`

`txt_sum_venv` is already in `.gitignore` - if you change the name then you need to update the  `.gitignore` file

activate the virtual environment
`source venv/bin/activate` or on windows  
`source venv/Scripts/activate`  

Next install the dependencies:  
`pip install -r requirements.txt`

Next install the models  
run the get_models.py script to download the models they need to be saved in `src/models/`

Put data to analyse in `./text_data/`

Run `./src/main.py`

Input which folder the text files are in. This is a placeholder to later code the docker volume.  

For running in a Docker container:  
`docker build -t txt_sum_img .`  
`docker run -it  txt_sum_img bash`  
then  
 `python3 main.py`  


To run the tests  
`python -m pytest` in the root dir  

## New dockerfile usage 
$ docker build -t my-python-dev-image .
$ docker run -it -p 5678:5678 -v $(pwd):/app ner-dev-image

Note the current working directory (pwd) has to have no spaces in it! 
If using git bash on windows you need to add a / to the start of the path.
If using cmd on windows you need to use %cd% instead of $(pwd)
If using powershell on windows you need to use ${PWD} instead of $(pwd)

## References  
https://huggingface.co/dslim/bert-base-NER  
