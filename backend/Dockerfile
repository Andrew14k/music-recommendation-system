# Use a Python base image
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt to the container
COPY requirements.txt /app/

# Install the Python dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend directory to the container
COPY . /app/

# Expose the port the backend will run on (e.g., 5000 for Flask)
EXPOSE 5000

# Define the entry point for the container to start the Flask app
CMD ["python", "app.py"]
