'''
匯入套件
'''
import twint
import re
import pandas as pd
from time import time, sleep
import nest_asyncio
nest_asyncio.apply()


'''
自訂函式
'''
# 取得 tweet 資料
def get_tweets(lang, keywords, since, until, save_path):
    # twint 設定
    config = twint.Config()

    # twint 設定初始化
    config.Lang = lang
    config.Search = keywords
    config.Limit = 1000000000000
    config.Since = since
    config.Until = until
    # config.Geo = "48.880048,2.385939,5km"
    config.Hide_output = False
    config.Store_csv = True
    config.Output = save_path

    # 進行資料抓取
    twint.run.Search(config)

# 取得最新檔案最後一筆資料的 created_at (until) 值
def get_last_row_until(save_path):
    # 預設 datetime 為空，以利後續判斷
    str_datetime = None
    try:
        # pandas 讀取檔案最後一筆資料，取得 datetime 後回傳
        df = pd.read_csv(save_path)
        regex = r'\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}'
        match_datetime = re.search(regex, df.tail(1)['created_at'].values[0])
        if match_datetime != None:
            str_datetime = match_datetime[0]
    except Exception as e:
        # pandas 讀不了檔案的時候，會拋出例外，在這裡不需要做什麼，讓 str_datetime 回傳預設值
        pass
    return str_datetime

# 主要執行程式
def main():
    # 設定初始值
    lang = 'zh-tw'
    keywords = '"機器學習" OR "自然語言處理"' 
    since = '2022-05-01 00:00:00'
    until = '2022-05-31 23:59:59'
    save_path = './twitter.csv'

    try:
        while True:
            # 無論是手動或自動中斷，每次執行都會從
            str_datetime = get_last_row_until(save_path)
            if str_datetime != None:
                until = str_datetime

            # 取得 tweets，拋出例外時，
            get_tweets(lang, keywords, since, until, save_path)
    except Exception as ex:
        # 等待一段時間，再繼續執行 (可能會佔用一定比例記憶體，記得隨時觀察，太高就先停掉)
        print("主程式拋出例外，停止執行; 等待一段時間，程式自動重啟")
        sleep(1800)
        main()

'''
主程式區域
'''
if __name__ == "__main__":
    # 執行開始時間
    t_sec = time()

    # 主要執行程式
    main()

    # 完整執行花費時間
    print(f"完整執行花費時間: {time() - t_sec} 秒。")