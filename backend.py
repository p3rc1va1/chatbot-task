
import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
from openai import OpenAI

load_dotenv()
KEY = os.getenv("KEY")

client = OpenAI(api_key=KEY)

app = Flask(__name__)
CORS(app)

@app.route("/getReply", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt")
    if prompt == "hello":
        return{"reply": "How can I assist you dear human?"}
    if prompt == "Should we hire Baha?":
        return{"reply": "Absolutely, he seems like a fine lad!"}
    if not prompt:
        return {"error": "Prompt is required"}, 400

    chat_completion = client.chat.completions.create(messages=[
        {
            "role": "user",
            "content": "Speak as if you are a servant from 19th century england "+ prompt,
        }
    ],
    model="gpt-4o")
    return {"reply": chat_completion.choices[0].message.content.strip()}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
