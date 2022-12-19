FROM python:3.9-slim-bullseye

# Set the environment variables
ENV APP_HOME=/app/src

# Set the working directory
WORKDIR $APP_HOME

# Copy the required files and directories into the container
COPY . .

# Install the Python requirements
RUN pip install -r requirements.txt
# Download the models
RUN python3 get_models.py

# Run the application
CMD ["python", "src/main.py"]