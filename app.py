from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # allow frontend requests

# Secure API key
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Set OPENROUTER_API_KEY in environment variables.")

def get_ai_response(user_message):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3-8b-instruct",
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are an AI assistant specialized in animal diseases.\n"
                            "Definition:\n<text>\n\n"
                            "Causes:\n- point\n- point\n\n"
                            "Symptoms:\n- point\n- point\n\n"
                            "Prevention:\n- point\n- point\n\n"
                            "Treatment:\n- point\n- point\n\n"
                            "Do not use ** or markdown symbols. Only plain text and bullet points using '-'"
                        )
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            },
            timeout=20
        )

        # Check response status
        if response.status_code != 200:
            print("API ERROR:", response.text)
            return "API error, try again later."

        data = response.json()
        return data['choices'][0]['message']['content']

    except Exception as e:
        print("ERROR:", e)
        return "Server error, try again later."


@app.route('/')
def home():
    return render_template("index.html")


# Chat API
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "Invalid request"}), 400

    user_message = data["message"]
    reply = get_ai_response(user_message)

    return jsonify({"reply": reply})


# Production run
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
