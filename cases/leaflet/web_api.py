'''
需要安裝 flask、requests
$ pip install -U Flask Flask-Cors

參考連結:
[1] Flask 實現 CORS 跨域請求的方法
ttps://medium.com/@charming_rust_oyster_221/flask-實現-cors-跨域請求的方法-c51b6e49a8b5
'''
from flask import Flask, make_response, request, jsonify
from flask_cors import CORS
import requests as req
import math



'''
Flask 初始化
'''
app = Flask(__name__)
app.json.ensure_ascii = False # 防止中文變成 unicode 編碼
CORS(app) # 設定全域 CORS



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

    # 回傳回應
    return jsonify(res.json())

# 新竹 cafe
@app.route('/cafe_hsinchu', methods=['GET'])
def get_cafe_info_in_hsinchu():
    # 先對 咖啡廳 Web API 發送 GET 請求 (request)，取得對方伺服器的回應 (response)，
    # 其中回應帶有咖啡廳列表的資訊
    url = 'https://cafenomad.tw/api/v1.2/cafes/hsinchu'
    res = req.get(url)

    # 回傳回應
    return jsonify(res.json())

# 高雄 cafe
@app.route('/cafe_kaohsiung', methods=['GET'])
def get_cafe_info_in_kaohsiung():
    # 先對 咖啡廳 Web API 發送 GET 請求 (request)，取得對方伺服器的回應 (response)，
    # 其中回應帶有咖啡廳列表的資訊
    url = 'https://cafenomad.tw/api/v1.2/cafes/kaohsiung'
    res = req.get(url)

    # 回傳回應
    return jsonify(res.json())



'''
Web API (資料來源: https://data.taipei/dataset/detail?id=6bb3304b-4f46-4bb0-8cd1-60c66dcd1cae)
'''
# 臺北市垃圾車點位路線資訊 (取得總筆數)
@app.route('/count_garbage_trucks_in_taipei', methods=['GET'])
def get_count_garbage_trucks_in_taipei():
    # 先對 垃圾車點位路線資訊 Web API 發送 GET 請求 (request)，取得對方伺服器的回應 (response)，
    # 其中回應帶有垃圾車點位路線資訊列表的資訊

    '''取得資料總筆數'''
    url = f'https://data.taipei/api/v1/dataset/a6e90031-7ec4-4089-afb5-361a4efe7202?scope=resourceAquire&offset=0&limit=1'
    res = req.get(url)
    count = res.json()['result']['count']

    # 回傳回應
    return jsonify({'count': count})

# 臺北市垃圾車點位路線資訊 (分頁)
@app.route('/some_garbage_trucks_in_taipei', methods=['GET'])
def get_some_garbage_trucks_in_taipei():
    # 先對 垃圾車點位路線資訊 Web API 發送 GET 請求 (request)，取得對方伺服器的回應 (response)，
    # 其中回應帶有垃圾車點位路線資訊列表的資訊

    '''取得資料總筆數'''
    url = f'https://data.taipei/api/v1/dataset/a6e90031-7ec4-4089-afb5-361a4efe7202?scope=resourceAquire&offset=0&limit=1'
    res = req.get(url)
    count = res.json()['result']['count']

    '''取得總頁數'''
    limit = 1000 # 希望一頁有幾筆
    pages = math.ceil(count / limit) # 取得總頁數

    '''取得 GET 請求的 page 值'''
    page = 1
    if 'page' in request.args:
        page = int(request.args.get('page'))
        if page < 1: page = 1 # 指定頁碼小於 1，則設定成 1
        elif page > pages: page = pages # 指定頁碼大於總頁數，則設定成總頁數 (代表最後一頁)

    '''取得指定分頁資料'''
    offset = (page - 1) * limit
    url = f'https://data.taipei/api/v1/dataset/a6e90031-7ec4-4089-afb5-361a4efe7202?scope=resourceAquire&offset={offset}&limit={limit}'
    res = req.get(url)

    # 回傳回應
    return jsonify(res.json()['result']['results'])

# 臺北市垃圾車點位路線資訊 (全部)
@app.route('/all_garbage_trucks_in_taipei', methods=['GET'])
def get_all_garbage_trucks_in_taipei():
    # 先對 垃圾車點位路線資訊 Web API 發送 GET 請求 (request)，取得對方伺服器的回應 (response)，
    # 其中回應帶有垃圾車點位路線資訊列表的資訊

    '''取得資料總筆數'''
    url = f'https://data.taipei/api/v1/dataset/a6e90031-7ec4-4089-afb5-361a4efe7202?scope=resourceAquire&offset=0&limit=1'
    res = req.get(url)
    count = res.json()['result']['count']

    '''取得總頁數'''
    limit = 1000 # 希望一頁有幾筆
    pages = math.ceil(count / limit) # 取得總頁數

    '''取得全部資料'''
    list_results = []
    for page in range(1, pages + 1):
        offset = (page - 1) * limit
        url = f'https://data.taipei/api/v1/dataset/a6e90031-7ec4-4089-afb5-361a4efe7202?scope=resourceAquire&offset={offset}&limit={limit}'
        res = req.get(url)
        list_results.extend(res.json()['result']['results'])

    # 回傳回應
    return jsonify(list_results)



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