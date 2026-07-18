import os
import json
# ... 其他程式碼 ...

@app.route('/get-sbir')
def get_sbir():
    # 取得 app.py 所在的絕對路徑
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(basedir, 'data.json')

    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e) + " 找的路徑是: " + file_path}), 500
