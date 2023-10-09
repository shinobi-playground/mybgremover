# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir Flask && \
    apt-get update && \
    apt-get install -y curl && \
    pip install rembg

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
