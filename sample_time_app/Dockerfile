FROM python:3.9-slim

WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Expose port 80 so the container is accessible externally
EXPOSE 80

# Run the application
CMD ["python", "app.py"]
