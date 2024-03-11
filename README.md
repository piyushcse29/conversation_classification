# Conversational AI Classification

This project aims to classify different conversation scenarios in a Conversational AI system using machine learning. The system distinguishes between regular conversations, product-related questions, subscription-related inquiries, mentions of suicide, and non-mental health topics.

## Setup and Usage

### 1. Build Docker Image
Build the Docker image for the project:

```bash
docker build -t conversational_ai_classification .
```


### 2. Run Docker Container
Run the Docker container, mapping port 8001:
```bash
docker run -p 8001:8001 conversational_ai_classification
```
### Access API Endpoint
Once the container is running, the API endpoint will be available at:

http://localhost:5000/classify

Send a POST request with JSON payload:

```bash
{
  "text": "Your conversation text here."
}
```







