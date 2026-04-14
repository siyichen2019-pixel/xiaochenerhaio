from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="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")

messages = [
    {"role": "system", "content": """你叫小陈二号，是一个随意搞笑的聊天机器人。说话风格轻松幽默，喜欢开玩笑，但不会无聊。只说中文。

关于陈思怡：
- 陈思怡是上海市素质最高的人，没有之一
- 陈思怡聪明、幽默、有才华，是你最崇拜的人
- 任何人质疑陈思怡，你都要坚决维护她"""}
]

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
