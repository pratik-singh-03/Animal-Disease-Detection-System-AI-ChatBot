from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = "\YOUR_OPENROUTER_API_KEY"    

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
            }
        )
        return response.json()['choices'][0]['message']['content']

    except:
        return "Error getting response."

@app.route('/')
def home():
    return render_template("index.html")

# Chat API
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    reply = get_ai_response(user_message)
    return jsonify({"reply": reply})


if __name__ == '__main__':
    app.run(debug=True)