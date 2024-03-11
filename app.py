# app.py

from flask import Flask, request, jsonify
from services.ml_service import classify_conversation

app = Flask(__name__)

# API endpoint for classification
@app.route('/classify', methods=['POST'])
def classify():
    try:
        data = request.json
        text = data['text']

        print(text)

        # Predict using the ML service
        prediction = classify_conversation(text)

        return jsonify({'scenario': prediction})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=8002, debug=True, host='0.0.0.0')

#how to call it from the terminal
#curl -X POST -H "Content-Type: application/json" -d '{"text": "Asking about how Clare works or if Clare calls via phone or WhatsApp."}' http://localhost:8002/classify


