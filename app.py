import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get-sbir')
def get_sbir():
    # 讀取 GitHub 上的 data.json 檔案
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify({"status": "success", "data": data})

if __name__ == '__main__':
    app.run()
