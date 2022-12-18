FROM ubuntu:20.04

# Install necessary packages and dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    git \
    curl

# Set the working directory
WORKDIR /app

# Copy the required files and directories into the container
COPY . .

# Install the Python requirements
RUN python3 -m pip install -r requirements.txt

# Expose the default Python debug port
EXPOSE 5678
