FROM python:3.8.0-buster

# Make a directory for our application
WORKDIR /application
# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy our source code
COPY . .

# Run the application
CMD ["python", "./start_alert.py"]