# Use the official Ubuntu 20.04 as a parent image
FROM ubuntu:20.04

# Set the working directory in the container to /app
WORKDIR /app

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    python3.9 \
    python3-pip \
    python3-pytest \
    graphviz \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y python3.9-dev

# Install clingo
RUN apt-get install -y gringo

# Upgrade pip
RUN python3.9 -m pip install --upgrade pip

# Install Python packages
RUN python3.9 -m pip install \
    clingo \
    clorm \
    clingraph \
    graphviz

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80
