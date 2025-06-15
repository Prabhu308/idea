FROM python:3.10-slim

# Set working directory in container
WORKDIR /
# Copy requirements and install dependencies
RUN pip install flask

# Copy app code
COPY app.py .

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "main.py"]

