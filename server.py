from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello from Godji Oracle! 🌟"

@app.route("/fortune", methods=["POST"])
def fortune():
    data = request.get_json()
    birth_date = data.get("birth_date")

    # ตรงนี้คือคำทำนาย
    fortune_text = "วันนี้เป็นวันที่สดใส โอกาสใหม่รออยู่ ✨"
    tip_text = "อย่าลืมยิ้มให้ตัวเองในกระจกนะ! 🍀"

    response_data = {
        "birth_date": birth_date,
        "fortune": fortune_text,
        "tip": tip_text
    }

    # 👇 ใช้ json.dumps และ Response ตรง ๆ เพื่อไม่ escape ภาษาไทย
    response_json = json.dumps(response_data, ensure_ascii=False)
    return Response(response_json, content_type="application/json; charset=utf-8")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
