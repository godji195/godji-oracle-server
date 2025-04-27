from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Godji Oracle! 🌟"

@app.route("/fortune", methods=["POST"])
def fortune():
    data = request.json
    birth_date = data.get("birth_date", "ไม่ระบุวันเกิด")
    
    # ตัวอย่างการตอบกลับง่าย ๆ
    return {
        "birth_date": birth_date,
        "fortune": "วันนี้เป็นวันที่สดใส โอกาสใหม่รออยู่ ✨",
        "tip": "อย่าลืมยิ้มให้ตัวเองในกระจกนะ! 🍀"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
