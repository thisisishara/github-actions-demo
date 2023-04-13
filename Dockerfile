# Use Python 3.10 slim-bullseye image as the base
FROM python:3.10-slim-bullseye

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000
EXPOSE 5000

# Start the Flask app with Waitress
CMD ["waitress-serve", "--port=5000", "--logger-name=waitress:info", "--call", "app:create_app"]
