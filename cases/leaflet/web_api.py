'''
需要安裝 flask、requests
$ pip install -U Flask requests
'''
from flask import Flask, make_response
import requests as req
import json



'''
Flask 初始化
'''
app = Flask(__name__)



'''
Web API (資料來源: https://cafenomad.tw/)
'''
# 臺北 cafe
@app.route('/cafe_taipei', methods=['GET'])
def get_cafe_info_in_taipei():
    # 先對 咖啡廳 Web API 發送 GET 請求 (request)，取得對方伺服器的回應 (response)，
    # 其中回應帶有咖啡廳列表的資訊
    url = 'https://cafenomad.tw/api/v1.2/cafes/taipei'
    res = req.get(url)

    # 自訂回應，同時將咖啡廳列表資訊附加在回應中
    response = make_response(json.dumps(res.json(), ensure_ascii=False))

    # 自訂回應標頭，讓收到回應的 User Agent (例如瀏覽器、手機 APP 等) 可以知道回應相關的訊息與設定
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'

    # 回傳自訂回應
    return response

# 新竹 cafe
@app.route('/cafe_hsinchu', methods=['GET'])
def get_cafe_info_in_hsinchu():
    # 先對 咖啡廳 Web API 發送 GET 請求 (request)，取得對方伺服器的回應 (response)，
    # 其中回應帶有咖啡廳列表的資訊
    url = 'https://cafenomad.tw/api/v1.2/cafes/hsinchu'
    res = req.get(url)

    # 自訂回應，同時將咖啡廳列表資訊附加在回應中
    response = make_response(json.dumps(res.json(), ensure_ascii=False))

    # 自訂回應標頭，讓收到回應的 User Agent (例如瀏覽器、手機 APP 等) 可以知道回應相關的訊息與設定
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

# 高雄 cafe
@app.route('/cafe_kaohsiung', methods=['GET'])
def get_cafe_info_in_kaohsiung():
    # 先對 咖啡廳 Web API 發送 GET 請求 (request)，取得對方伺服器的回應 (response)，
    # 其中回應帶有咖啡廳列表的資訊
    url = 'https://cafenomad.tw/api/v1.2/cafes/kaohsiung'
    res = req.get(url)

    # 自訂回應，同時將咖啡廳列表資訊附加在回應中
    response = make_response(json.dumps(res.json(), ensure_ascii=False))

    # 自訂回應標頭，讓收到回應的 User Agent (例如瀏覽器、手機 APP 等) 可以知道回應相關的訊息與設定
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response



'''
Web API (資料來源: https://data.taipei/dataset/detail?id=6bb3304b-4f46-4bb0-8cd1-60c66dcd1cae)
'''
# 臺北市垃圾車點位路線資訊
@app.route('/garbage_truck_taipei', methods=['GET'])
def get_garbage_truck_in_taipei():
    # 先對 垃圾車點位路線資訊 Web API 發送 GET 請求 (request)，取得對方伺服器的回應 (response)，
    # 其中回應帶有垃圾車點位路線資訊列表的資訊
    
    '''取得部分資料'''
    limit = 1000
    offset = 0
    url = f'https://data.taipei/api/v1/dataset/a6e90031-7ec4-4089-afb5-361a4efe7202?scope=resourceAquire&offset={offset}&limit={limit}'
    res = req.get(url)
    
    # 自訂回應，同時將垃圾車點位路線資訊列表資訊附加在回應中
    response = make_response(json.dumps(res.json()['result']['results'], ensure_ascii=False))



    '''取得所有資料'''
    list_results = []
    pages = 5
    for page in range(1, pages + 1):
        limit = 1000
        offset = (page - 1) * limit
        url = f'https://data.taipei/api/v1/dataset/a6e90031-7ec4-4089-afb5-361a4efe7202?scope=resourceAquire&offset={offset}&limit={limit}'
        res = req.get(url)
        list_results.extend(res.json()['result']['results'])

    # 自訂回應，同時將垃圾車點位路線資訊列表資訊附加在回應中
    response = make_response(json.dumps(list_results, ensure_ascii=False))



    '''自訂回應標頭'''
    # 讓收到回應的 User Agent (例如瀏覽器、手機 APP 等) 可以知道回應相關的訊息與設定
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'

    '''回傳自訂回應'''
    return response



'''
主程式
'''
if __name__ == '__main__':
    app.run(
        # 除錯模式為 True，服務執行期間有錯誤，會將 Traceback 顯示在網頁上，
        # 反之則顯示一般的 Internal Server Error
        debug=True,

        # 127.0.0.1 或 localhost 限定本機使用服務，
        # 0.0.0.0 代表所有知道主機實際 IP 的人都能存取 
        host='0.0.0.0',

        # 網址或 IP 後面附加的 Port 號，代表服務由該 Port 號提供
        port=5000 
    )