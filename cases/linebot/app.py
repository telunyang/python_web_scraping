from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

# 實體化 flask 物件
app = Flask(__name__)


# 自訂組態檔 (放置 LINE Bot 重要設定)
from config import Config

# LINE BOT 設定
config = Config()
line_bot_api = LineBotApi(config['YOUR_CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(config['YOUR_CHANNEL_SECRET'])



'''
LINE BOT - Webhook
'''
# LINE BOT 的 webhook
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    '''
    官方範例 - 回覆單一文字內容
    '''
    # 取得自己的發送的文字
    str_reply = event.message.text

    # 將文字透過 LINE Bot 回覆給使用者
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=str_reply)
    )
    


    '''
    回覆多個文字內容 (最多 5 個)
    '''
    # # 先整理用到的句子
    # list_sentence = [
    #     '世上最遙遠的距離',
    #     '不是生與死的距離',
    #     '不是天各一方',
    #     '而是我就站在\n你面前',
    #     '你卻不知道...',
    # ]

    # # 初始化 list，用在 reply
    # list_reply = []

    # # 整合 TextSendMessage
    # for sentence in list_sentence:
    #     list_reply.append( TextSendMessage(text=sentence) )

    # # 將所有句子透過 LINE Bot 回覆給使用者
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     list_reply
    # )


'''
主程式
'''
if __name__ == "__main__":
    # 建立 flask web service (使用 ngrok 的情形下)
    app.run(
        threaded=False, # 是否透過多執行緒處理請求
        host="0.0.0.0", # 設定 0.0.0.0 對外開放，讓 Webhook 機制確認 Web API 是否存活
        port=5005       # 啟用 port 號
    )

    # 有自己的 SSL certs 檔案，再開啟下方設定，修正 ssl_context 的值。
    # app.run(
    #     threaded=False, # 是否透過多執行緒處理請求
    #     host="0.0.0.0", # 設定 0.0.0.0 會對外開放
    #     port=5005,      # 啟用 port 號
    #     # ssl_context=('/certs/fullchain4.pem', '/certs/privkey4.pem') # 建立 SSL 證證 for LINE Bot Webhook
    # )