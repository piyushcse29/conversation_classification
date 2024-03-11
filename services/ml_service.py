from models.serving_model import predict_scenario

def classify_conversation(text):
    return predict_scenario(text)
