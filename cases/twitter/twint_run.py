'''
匯入套件
'''
import twint
import time
from time import time
import nest_asyncio
nest_asyncio.apply()


'''
自訂函式
'''
# 取得 tweet 資料
def get_tweets(since, until):
    # twint 設定
    config = twint.Config()

    # twint 設定初始化
    config.Lang = 'zh-tw'
    config.Search = '"機器學習" OR "自然語言處理"' 
    config.Limit = 1000000000000
    config.Since = since
    config.Until = until
    # config.Geo = "48.880048,2.385939,5km"
    config.Hide_output = False
    config.Store_csv = True
    config.Output = f"./twitter.csv"

    # 進行資料抓取
    twint.run.Search(config)

# 主要執行程式
def main():
    since = '2022-06-01 00:00:00'
    until = '2022-06-19 23:59:59'

    try:   
        get_tweets(since, until)
    except Exception as ex:
        print(ex)

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