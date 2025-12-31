# Use python 3.13.2 base image
FROM python:3.13.2


# Set Working Directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of applicarion code
COPY . .

# Expose the application port
EXPOSE 8000

# Command to start FASTAPI application 
CMD ["uvicorn", "app:app","--host", "0.0.0.0","--port","8000"]


