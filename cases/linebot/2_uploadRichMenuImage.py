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

# 上傳 Rich Menu 用的網址
url_upload_rich_menu = f'https://api-data.line.me/v2/bot/richmenu/{richMenuId}/content'

# 請求標頭 (image/png 視需求修改成其它圖片格式，例如 jpeg、gif 等)
my_headers = {
    'Authorization': f'Bearer {config["YOUR_CHANNEL_ACCESS_TOKEN"]}',
    'Content-Type': 'image/jpeg'
}

# 檔案名稱
file_path = './richmenu.jpg'

# 執行請求 (上傳 RichMenu 的圖片)
response = requests.post(url = url_upload_rich_menu, data = open(file_path, 'rb'), headers = my_headers)

# 輸出回應結果
pprint(response.text)
# '{}'