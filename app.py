import json
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get-sbir')
def get_sbir():
    # 確保檔案路徑正確
    file_path = os.path.join(os.path.dirname(__file__), 'data.json')
    
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f: # 用 utf-8-sig 可以過濾掉可能的 BOM 亂碼
            data = json.load(f)
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run()
