# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the client script into the container
COPY zmq_client.py .

# Run client.py when the container launches
CMD ["python", "-u", "./zmq_client.py"]
