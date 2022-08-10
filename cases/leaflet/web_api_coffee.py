'''
需要安裝 flask、requests
'''
import requests as req
import json
from flask import Flask, make_response


'''
Flask 初始化
'''
app = Flask(__name__)

# 自訂標頭
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
}


'''
Web API (資料來源: https://cafenomad.tw/)
'''
@app.route('/taipei', methods=['GET'])
def taipei():
    url = 'https://cafenomad.tw/api/v1.2/cafes/taipei'
    res = req.get(url, headers = my_headers)
    response = make_response(json.dumps(res.json(), ensure_ascii=False))
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/hsinchu', methods=['GET'])
def hsinchu():
    url = 'https://cafenomad.tw/api/v1.2/cafes/hsinchu'
    res = req.get(url, headers = my_headers)
    response = make_response(json.dumps(res.json(), ensure_ascii=False))
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/kaohsiung', methods=['GET'])
def kaohsiung():
    url = 'https://cafenomad.tw/api/v1.2/cafes/kaohsiung'
    res = req.get(url, headers = my_headers)
    response = make_response(json.dumps(res.json(), ensure_ascii=False))
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


'''
主程式
'''
if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0', 
        port=5000
    )