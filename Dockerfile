# Use the official Ubuntu 20.04 as a parent image
FROM ubuntu:20.04

# Set the working directory in the container to /app
WORKDIR /app

# No asking for user input
ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip \
    graphviz \
    gringo

# Upgrade pip
RUN python3.9 -m pip install --upgrade pip

# Install Python packages
RUN python3.9 -m pip install \
    clorm \
    clingraph \
    pytest

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80
