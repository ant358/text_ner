FROM python:3.9-slim-bullseye

# Set the working directory
WORKDIR /app

# Copy the required files and directories into the container
COPY . .

# Install the Python requirements
RUN python3 -m pip install -r requirements.txt

# Expose the default Python debug port
EXPOSE 5678
