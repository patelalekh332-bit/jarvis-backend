from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_message = data["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tum ek Hindi bolne wale smart AI assistant ho."},
            {"role": "user", "content": user_message}
        ]
    )

    return jsonify({"reply": response.choices[0].message.content})

app.run(host="0.0.0.0", port=10000)
