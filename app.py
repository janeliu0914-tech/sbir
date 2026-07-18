import os
import json
from flask import Flask, jsonify

# 1. 這裡先定義 app
app = Flask(__name__)

# 2. 然後才能在 app 下面定義路由
@app.route('/get-sbir')
def get_sbir():
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(basedir, 'data.json')
    
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 3. 最後才是啟動程式的區塊
if __name__ == '__main__':
    app.run()
