
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

fortunes = [
    "วันนี้คุณจะได้พบโอกาสที่ยิ่งใหญ่ 🌟",
    "ระวังเรื่องอารมณ์ในวันนี้นิดนึงนะ ❤️",
    "เงินทองกำลังไหลมาเทมา 💰",
    "ความรักใหม่กำลังมาในชีวิตคุณ 💖",
    "สุขภาพจะแข็งแรงสุด ๆ ปีนี้ 🏋️‍♂️"
]

@app.route('/fortune', methods=['POST'])
def get_fortune():
    data = request.json
    day = data.get('day')
    month = data.get('month')
    year = data.get('year')
    
    result = random.choice(fortunes)
    
    return jsonify({
        "fortune": f"คนที่เกิด {day}/{month}/{year} ได้รับคำทำนาย: {result}"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
