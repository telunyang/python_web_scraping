'''
匯入套件
'''
import twint
import logging, time
from time import sleep, time
import nest_asyncio
nest_asyncio.apply()

'''
全域設定
'''
# logging 設定
logging.basicConfig(
    filename = 'twitter.log',
    filemode = 'a',
    format = '%(asctime)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    encoding = "utf-8",
    level = logging.INFO
)

'''
自訂函式
'''
# 取得 tweet 資料
def get_tweets():
    # twint 設定，可參考 https://github.com/twintproject/twint/blob/master/twint/config.py
    config = twint.Config()

    # twint 設定初始化
    config.Lang = 'zh-tw' # 語系: https://developer.twitter.com/en/docs/twitter-for-websites/supported-languages
    config.Search = '"機器學習" OR "自然語言處理"' # 搜尋關鍵字
    config.Limit = 1000000000000 # 限定抓多少筆資料
    config.Since = '2019-10-01 00:00:00' # 設定 since 與 until
    config.Until = '2020-12-31 23:59:59' # since 與 until 記得至少相差 1 天
    # config.Geo = "48.880048,2.385939,5km"
    config.Hide_output = False
    config.Store_csv = True
    config.Output = f"./twitter.csv"

    # 進行資料抓取
    twint.run.Search(config)

# 主要執行程式
def main():
    try:   
        # 重複執行
        while True:
            logging.info(f"程式準備啟動...")
            t_sec = time() # 計算時間
            get_tweets()
            logging.info(f"程式執行結束，本次花費時間: {time() - t_sec} 秒。")
    except Exception as ex:
        # 休息一段時間後，重新執行程式
        logging.info(f"程式拋出例範外，已中斷...暫停 1800 秒後重新執行...")
        sleep(1800)
        main() # 再執行一次主程式

'''
主程式區域
'''
if __name__ == "__main__":
    # 執行開始時間
    t_sec = time()

    # 主要執行程式
    main()

    # 完整執行花費時間
    logging.info(f"完整執行花費時間: {time() - t_sec} 秒。")