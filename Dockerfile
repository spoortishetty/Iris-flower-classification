# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir flask scikit-learn pandas

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variables to handle Python output in the container
ENV PYTHONUNBUFFERED=1

# Command to run the application and bind it to 0.0.0.0
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000"]
