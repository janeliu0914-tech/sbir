from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/get-sbir')
def get_sbir():
    # 這裡我先幫你放數位發展部的真實 JSON 當測試
    # 換成台北市產業發展獎勵補助 API
    # 換成台北市產業發展獎勵補助 API
    target_url = "https://data.taipei/api/v1/dataset/5012e8ba-5ace-4821-8482-ee07c147fd0a?scope=resourceAquire"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(target_url, headers=headers, verify=False)
        data = response.json()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# 注意這裡 __name__ 和 __main__ 前後都是「兩個底線」
if __name__ == '__main__':
    print("====== 準備啟動伺服器囉！ ======")
    app.run(debug=True, port=5000)
