# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
# COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8080

# Expose the port the app runs on
# Run the application
CMD ["flask", "run", "--host=0.0.0.0","--debug", "--port=8080"]