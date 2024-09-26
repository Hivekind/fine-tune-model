# Use an official Python runtime as a base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port for Flask
EXPOSE 5000

# Run the Flask server
CMD ["python", "app.py"]
