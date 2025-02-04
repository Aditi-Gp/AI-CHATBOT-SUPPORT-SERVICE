# X6tO5hT7kEPqSUf0J4uCM7XQqpK1ZVpUlZv8Zjdv

# To run 
# On first terminal:

# cd chatbot_project
# venv\Scripts\activate
# python server.py

# cd chatbot_project
# venv\Scripts\activate
# python -m http.server 8080

import cohere
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize Cohere client
cohere_api_key = 'X6tO5hT7kEPqSUf0J4uCM7XQqpK1ZVpUlZv8Zjdv'  # Replace with your Cohere API key
co = cohere.Client(cohere_api_key)

# Home route
@app.route('/')
def home():
    return 'Welcome to the chatbot server! Use the /chat endpoint to interact with the chatbot.'

# Chat route for processing messages
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the message from the frontend
        user_message = request.json.get('message')
        print(f"User Message: {user_message}")

        # Generate response using Cohere's language model
        response = co.generate(
            model='command-xlarge',  # Replace with the appropriate model
            prompt=user_message,  # Use the user message as the prompt
            max_tokens=50  # Limit the response length (feel free to adjust this)
        )

        # Extract the generated text from the response
        bot_reply = response.generations[0].text.strip()  # Correct way to access the generated text
        print(f"Bot Reply: {bot_reply}")

        # Send the reply back as a JSON response
        return jsonify({"reply": bot_reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "Sorry, something went wrong. Please try again."}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=8000)