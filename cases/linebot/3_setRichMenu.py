# 網路請求工具
import requests

# 輸出排版工具
from pprint import pprint

# 自訂組態檔 (放置 LINE Bot 重要設定)
from config import Config

# LINE BOT 設定
config = Config()

# Rich Menu Id
richMenuId = ""

# 設定 Rich Menu 用的網址
url_upload_rich_menu = f'https://api.line.me/v2/bot/user/all/richmenu/{richMenuId}'

# 請求標頭
my_headers = {
    'Authorization': f'Bearer {config["YOUR_CHANNEL_ACCESS_TOKEN"]}'
}

# 執行請求 (設定預設 RichMenu)
response = requests.post(url = url_upload_rich_menu, headers = my_headers)

# 輸出回應結果
pprint(response.text)
# '{}'