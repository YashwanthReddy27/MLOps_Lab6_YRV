# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the model training script into the container
COPY src/requirements.txt .

# Install Scikit-Learn and joblib
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/
# Run the script when the container launches
CMD ["python", "main.py"]
