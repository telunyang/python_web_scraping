'''
需要安裝 flask、requests
$ pip install -U Flask requests
'''
import requests as req
import json
from flask import Flask, make_response


'''
Flask 初始化
'''
app = Flask(__name__)


'''
Web API (資料來源: https://cafenomad.tw/)
'''
@app.route('/taipei', methods=['GET'])
def taipei():
    # 先對 咖啡廳 Web API 發送 GET 請求 (request)，取得對方伺服器的回應 (response)，其中回應帶有咖啡廳列表的資訊
    url = 'https://cafenomad.tw/api/v1.2/cafes/taipei'
    res = req.get(url)

    # 自訂回應，同時將咖啡廳列表資訊附加在回應中
    response = make_response(json.dumps(res.json(), ensure_ascii=False))

    # 自訂回應標頭，讓收到回應的 User Agent (例如瀏覽器、手機 APP 等) 可以知道回應相關的訊息與設定
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'

    # 回傳自訂回應
    return response


@app.route('/hsinchu', methods=['GET'])
def hsinchu():
    url = 'https://cafenomad.tw/api/v1.2/cafes/hsinchu'
    res = req.get(url)
    response = make_response(json.dumps(res.json(), ensure_ascii=False))
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/kaohsiung', methods=['GET'])
def kaohsiung():
    url = 'https://cafenomad.tw/api/v1.2/cafes/kaohsiung'
    res = req.get(url)
    response = make_response(json.dumps(res.json(), ensure_ascii=False))
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


'''
主程式
'''
if __name__ == '__main__':
    app.run(
        debug=True, # 除錯模式為 True，服務執行期間有錯誤，會將 Traceback 顯示在網頁上，反正則顯示一般的 Internal Server Error
        host='0.0.0.0', # 127.0.0.1 或 localhost 限定本機使用服務，0.0.0.0 代表所有知道主機實際 IP 的人都能存取
        port=5000 # 網址或 IP 後面附加的 Port 號，代表服務由該 Port 號提供
    )