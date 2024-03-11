# Use an official Pytorch runtime as a parent image
FROM pytorch/pytorch:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8002

# Run app.py when the container launches
CMD ["python", "app.py"]
