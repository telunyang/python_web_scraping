'''
匯入套件
'''
import twint
import os, sys
from random import randint
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
    config.Resume = './resume.txt'

    # 進行資料抓取
    twint.run.Search(config)

# 主要執行程式
def main():
    # 設定初始值
    lang = 'zh-tw'
    keywords = '"機器學習" OR "自然語言處理"'
    since = '2022-01-01 00:00:00'
    until = '2022-06-30 23:59:59'
    save_path = './twitter.csv'
    
    try:
        while True:
            # 取得 tweets
            print("執行中")
            get_tweets(lang, keywords, since, until, save_path)

            print("休息一下")
            sleep(randint(1800, 2400))
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(str(e))

        # 等待一段時間，再繼續執行 (可能會佔用一定比例記憶體，記得隨時觀察，太高就先停掉)
        print("主程式拋出例外，停止執行; 等待一段時間，程式自動重啟")
        sleep(randint(1800, 2400))
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