# twint - 不用登人帳號密碼和 API key，就能抓取 twitter 資料的利器

## 基本使用教學
- Scraping Twitter with Twint
  - [https://nealcaren.org/lessons/twint/](https://nealcaren.org/lessons/twint/)


## twint 版本
- [官方版本](https://github.com/twintproject/twint)
- [woluxwolu 的版本](https://github.com/woluxwolu/twint)
- [minamotorin 的版本](https://github.com/minamotorin/twint)


## 補充: 有關 woluxwolu 的 twint 版本
woluxwolu 的 twint 版本 README 有寫「Modified by minamotorin.」，我看了一下 minamotorin 的 github，minamotorin 有提到「About problem of Twint from this fork, please open issues on minamotorin/twint.」

minamotorin 的 twint 版本: [連結](https://github.com/minamotorin/twint)

感覺 minamotorin 的 twint 會比 woluxwolu 的版本新，目前先用 woluxwolu 的版本先跑一陣子看看，同時關注 minamotorin 的 twint 修正訊息。

---

# twint 安裝方式：
以下 twint 版本皆可選擇，目前推薦 minamotorin 的版本

## 1. minamotorin 將官方 twint 專案 fork 後，自行修正的版本 (推薦使用)
```bash
$ git clone https://github.com/minamotorin/twint.git
$ cd twint
$ pip install git+https://github.com/minamotorin/twint.git
```
- 將 `basic.py` 複製/移動到 twint 資料夾中
- (Optional) 修改 url.py
  - 如果發現 `config.lang = 'en'` 的設定有問題(例如大量非指定語系的資料)，可以嘗試以下作法:
    - 開啟 `/twint/twint/url.py`
    - 大約在 111 ~ 113 之間，會看到「`if config.Search:`」，在它上面加一個給 lang 用的設定:
    ```python
    if config.Lang:
        q += f" lang:{config.Lang}"
    ```
  - 儲存 url.py
- 安裝 nest_asyncio 套件
  - `$ pip install nest_asyncio`
- 安裝 aiohttp 套件
  - `$ pip install aiohttp==3.7.0`
- 回到的 twint 資料夾，執行程式
  - `$ python basic.py`

## 2. woluxwolu 直接下載官方 twint，再拿 minamotorin 原始碼來套用的版本
[Issue] Search just stops scraping
https://github.com/twintproject/twint/issues/1363
```bash
$ git clone https://github.com/woluxwolu/twint.git
$ cd twint
$ pip install git+https://github.com/woluxwolu/twint.git
```
- 將 `basic.py` 複製/移動到 twint 資料夾中
- (Optional) 修改 url.py
  - 如果發現 `config.lang = 'en'` 的設定有問題(例如大量非指定語系的資料)，可以嘗試以下作法:
    - 開啟 `/twint/twint/url.py`
    - 大約在 111 ~ 113 之間，會看到「`if config.Search:`」，在它上面加一個給 lang 用的設定:
    ```python
    if config.Lang:
        q += f" lang:{config.Lang}"
    ```
  - 儲存 url.py
- 安裝 nest_asyncio 套件
  - `$ pip install nest_asyncio`
- 安裝 aiohttp 套件
  - `$ pip install aiohttp==3.7.0`
- 回到的 twint 資料夾，執行程式
  - `$ python basic.py`

## 3. 官方版本安裝方式
- 第一步：下載 twint
  - `$ git clone https://github.com/twintproject/twint.git`
    - 或是選擇 Download Zip，而後解壓縮，出現 twint 資料夾
  - 進入 twint 資料夾
    -  `$ cd twint`
  - 將 `basic.py` 複製/移動一份到 twint 資料夾中
- 第二步：安裝套件
  - 開啟 requirements.txt
  - 將「aiohttp」改成「aiohttp==3.7.0」後儲存
    - 修正議題參考連結 https://ppt.cc/fJkVDx
  - `pip install -r requirements.txt`
  - `pip install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint`
    - (Install from source code) 此時 twint 資料夾裡面，會自動產生 src 資料夾
  - `pip install aiohttp==3.7.0`
- Optional：修改 url.py
  - 如果發現 `config.lang = 'en'` 的設定有問題(例如大量非指定語系的資料)，可以嘗試以下作法:
    - 開啟 `src/twint/url.py`
    - 大約在 111 ~ 113 之間，會看到「`if config.Search:`」，在它上面加一個給 lang 用的設定:
    ```python
    if config.Lang:
        q += f" lang:{config.Lang}"
    ```
  - 儲存 url.py
- 第三步：執行 basic.py
  - 回到剛開始進入的 twint 資料夾
  - `$ python basic.py`