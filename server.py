from flask import Flask, request, jsonify
from flask_cors import CORS  # <<< เพิ่มบรรทัดนี้

app = Flask(__name__)
CORS(app)  # <<< เพิ่มบรรทัดนี้ด้วย

@app.route('/fortune', methods=['POST'])
def fortune():
    data = request.json
    birth_date = data.get('birth_date')
    # ตรงนี้ใส่ลอจิกคำทำนายได้
    fortune_text = "วันนี้เป็นวันที่สดใส โอกาสใหม่รออยู่ ✨"
    tip_text = "อย่าลืมยิ้มให้ตัวเองในกระจกนะ! 🍀"
    return jsonify({
        "birth_date": birth_date,
        "fortune": fortune_text,
        "tip": tip_text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
