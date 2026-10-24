# Use Python as the base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install PostgreSQL development headers and build tools
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies (pip >= 26.2.2 ships certifi 2026.10.19 without the compromised emSign CA)
RUN pip install --no-cache-dir --upgrade "pip>=26.2.2" && pip install -r requirements.txt

# Run as an unprivileged user
RUN useradd --create-home --uid 10001 appuser
USER appuser

# Expose the port the app runs on
EXPOSE 5005

# Run the application
CMD ["python", "app.py"]