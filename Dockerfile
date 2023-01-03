FROM python:3.9-slim-bullseye

# Set the environment variables
ENV APP_HOME=/app

# Set the working directory
WORKDIR $APP_HOME

# Copy the requirements file
COPY requirements.txt .

# Install the Python requirements
RUN pip install -r requirements.txt

# Copy the source code
COPY . /app

# Download the models
# RUN python3 /app/src/get_models.py
# expose the port
EXPOSE 5000

# Entrypoint
ENTRYPOINT ["/bin/bash"]

# Run bash
CMD []