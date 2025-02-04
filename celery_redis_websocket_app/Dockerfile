FROM python:3

# Ensure that output is sent straight to terminal (without buffering)
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /usr/app/

# Install system dependencies (including fping)
RUN apt-get update && apt-get install -y fping && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .
