from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello from Godji Oracle! 🌟"

@app.route("/fortune", methods=["POST"])
def fortune():
    data = request.get_json()
    birth_date = data.get("birth_date")

    # ตัวอย่างคำทำนาย (เอาไว้เสกต่อเพิ่มได้)
    fortune_text = "วันนี้เป็นวันที่สดใส โอกาสใหม่รออยู่ ✨"
    tip_text = "อย่าลืมยิ้มให้ตัวเองในกระจกนะ! 🍀"

    response_data = {
        "birth_date": birth_date,
        "fortune": fortune_text,
        "tip": tip_text
    }

    # 👇 สำคัญมาก เพื่อให้ภาษาไทยไม่เพี้ยน
    response = make_response(jsonify(response_data))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
