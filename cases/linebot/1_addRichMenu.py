# 網路請求工具
import requests

# 輸出排版工具
from pprint import pprint

# 自訂組態檔 (放置 LINE Bot 重要設定)
from config import Config

# LINE BOT 設定
config = Config()

# 新增 Rich Menu 用的網址
url_add_rich_menu = f'https://api.line.me/v2/bot/richmenu'

# 聊天機器人的名稱
str_chatbot_name = '我的聊天機器人'

# Rich Menu 規格與設定
str_raw = '''
{
    "size":{
        "width":2500,
        "height":1686
    },
    "selected":false,
    "name":"richmenu_glis_ntnu",
    "chatBarText":"''' + str_chatbot_name + '''",
    "areas":[
        {
          "bounds":{
              "x":0,
              "y":0,
              "width":833.333,
              "height":843
          },
          "action":{
              "type":"message",
              "text":"[[[喜歡]]]"
          }
        },
        {
          "bounds":{
              "x":833.333,
              "y":0,
              "width":833.333,
              "height":843
          },
          "action":{
              "type":"message",
              "text":"[[[悲傷]]]"
          }
        },
        {
          "bounds":{
              "x":1666.666,
              "y":0,
              "width":833.333,
              "height":843
          },
          "action":{
              "type":"message",
              "text":"[[[厭惡噁心]]]"
          }
        },
        {
          "bounds":{
              "x":0,
              "y":843,
              "width":833.333,
              "height":843
          },
          "action":{
              "type":"message",
              "text":"[[[憤怒]]]"
          }
        },
        {
          "bounds":{
              "x":833.333,
              "y":843,
              "width":833.333,
              "height":843
          },
          "action":{
              "type":"message",
              "text":"[[[幸福]]]"
          }
        },
        {
          "bounds":{
              "x":1666.666,
              "y":843,
              "width":833.333,
              "height":843
          },
          "action":{
              "type":"message",
              "text":"[[[其它]]]"
          }
        }
    ]
  }
'''
str_raw = str_raw.encode('utf-8')

# 請求標頭
my_headers = {
    'Authorization': f'Bearer {config["YOUR_CHANNEL_ACCESS_TOKEN"]}',
    'Content-Type': 'application/json'
}

# 執行請求 (新增 RichMenu)
response = requests.post(url = url_add_rich_menu, data = str_raw, headers = my_headers)

# 輸出回應結果 (會取得 Rich Menu Id)
pprint(response.text)
"""
輸出
'{"richMenuId":"RichMenu ID 的值"}'

之後請將 richMenuId 的值，複製到 2_uploadRichMenuImage.py 和 3_setRichMenu.py 當中
"""