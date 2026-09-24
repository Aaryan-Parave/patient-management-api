# Base image
FROM python:3.14-slim

# Working Directory inside container
WORKDIR /app

# Copy requirements 
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#COPY project files

COPY main.py .
COPY patients.json .


# Expose port
EXPOSE 8000

# Run the Application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
