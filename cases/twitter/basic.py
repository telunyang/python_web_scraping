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
config.Since = '2022-06-01 00:00:00' # 設定 since 與 until
config.Until = '2022-06-02 23:59:59' # since 與 until 記得至少相差 1 天
# config.Geo = "48.880048,2.385939,5km"
config.Hide_output = False
config.Store_csv = True
config.Output = f"./twitter.csv"

# 進行資料抓取 (注意: 正常來說，執行幾個小時就會被程式自動中斷)
twint.run.Search(config)