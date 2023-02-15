'''
匯入套件
'''
import twint
import nest_asyncio
nest_asyncio.apply()

# twint 設定，可參考 https://github.com/twintproject/twint/blob/master/twint/config.py
config = twint.Config()

# twint 設定初始化
config.Lang = 'zh-tw' # 語系: https://developer.twitter.com/en/docs/twitter-for-websites/supported-languages
config.Search = '"機器學習" OR "自然語言處理"' # 搜尋關鍵字
config.Limit = 1000000000000 # 限定抓多少筆資料
config.Since = '2020-01-01 00:00:00' # 設定 since 與 until
config.Until = '2022-06-30 23:59:59' # since 與 until 記得至少相差 1 天
# config.Geo = "48.880048,2.385939,5km"
config.Location = True # 加入發文地點
config.Hide_output = False # 是否隱藏輸出 (debug 時可以開啟，正式使用時，建議關閉，可以減少 I/O)
config.Store_csv = True # 儲存在 csv 檔
config.Output = "./twitter.csv" # 輸出儲存資料的路徑
config.Resume = './resume.txt' # 爬取過程會儲存先前取得的 tweet ID，當程式因故中斷時，它會從該 ID 開始

# 進行資料抓取 (注意: 正常來說，執行幾個小時就會被程式自動中斷)
twint.run.Search(config)