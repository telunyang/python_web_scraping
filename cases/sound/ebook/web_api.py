'''
需要安裝 flask、requests
$ pip install -U Flask Flask-Cors

參考連結:
[1] Flask 實現 CORS 跨域請求的方法
ttps://medium.com/@charming_rust_oyster_221/flask-實現-cors-跨域請求的方法-c51b6e49a8b5
'''
from flask import Flask, request, send_from_directory, render_template, jsonify
from flask_cors import CORS
import subprocess
from urllib.parse import quote



'''
Flask 初始化
'''
app = Flask(__name__)
app.json.ensure_ascii = False
CORS(app) # 設定全域 CORS

'''
Templates
'''
# 套用網頁樣版(v1.0)
@app.route('/', methods=['GET'])
def index():
    return render_template('fetch.html')

'''
Web API (資料來源: Google Translation)
'''
# 取得 google 小姐的聲音
@app.route('/sound', methods=['POST'])
def get_sound():
    # 取得 POST data
    q = request.json['q']

    # 放罝回傳資訊的變數
    myDict = {
        'success': False,
        'link': None
    }

    # 轉成符合 url 格式的文字
    encoded_sentence = quote(q)

    # 翻譯的語言 (發音的口音)
    tl = 'zh-TW'

    # 取得聲音檔
    cmd = [
        'curl', 
        '-X', 
        'GET', 
        f'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl={tl}&q={encoded_sentence}',
        '-o',
        f'./tmp/{q}.mp3'
    ]
    
    # 執行指令，回傳 Process 物件，其中的屬性 returncode == 0 代表成功
    std_output = subprocess.run(cmd)
    if std_output.returncode == 0:
        myDict['success'] = True
        myDict['link'] = f'/tmp/{q}.mp3'

    # 回傳回應
    return jsonify(myDict)



''' 檔案路徑 '''
# JS 資料夾
@app.route('/js/<path>')
def get_js_path(path):
    return send_from_directory('js', path)

# CSS 資料夾
@app.route('/css/<path>')
def get_css_path(path):
    return send_from_directory('css', path)

# 暫存檔案路徑
@app.route('/tmp/<path>')
def get_tmp_path(path):
    return send_from_directory('tmp', path)



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