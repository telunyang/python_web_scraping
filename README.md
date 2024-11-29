# python_web_scraping
Python 網路爬蟲講義與範例程式碼


## 提問
- 通則
  - 「結業前」可提問、討論，要把多餘時間和資源，留給當前上課的學員。
- 寫信
	- E-mail: `darren@darreninfo.cc`
	- 信件標題寫上你的**班別和姓名**，或是在哪裡參與我的課程，例如 `[資展 BDSEXX] 網路爬蟲問題 - 楊德倫`
	- 提問的內容要與本專案有關，**其它課程的部分，去請益原本授課的老師**。
	- **不要把程式碼寄給我**，可能沒時間看，討論儘量以解決問題的方向為主。
	- 不符合以上幾點，將**直接刪除**，敬請見諒。


## 作業
- 僅限授課學員。
- 使用 `requests` 和 `BeautifulSoup`，或是 `selenium` 來爬取網站資料。
  - [Project Gutenberg](https://www.gutenberg.org/)
    - 爬取[中文](https://www.gutenberg.org/browse/languages/zh)書籍資料 (注意: 只要取得中文字，不要英文。)
      - 可使用選擇器 `li.pgdbetext > a[href]` 來檢視相關連結數量。
      - 取得中文字的正規表示式: [正則表達式-全型英數中文字、常用符號unicode對照表](https://blog.typeart.cc/正則表達式-全型英數中文字、常用符號unicode對照表/)
    - `80` 分條件
      - 新增 `project_gutenberg` 資料夾
      - 將每一本書的中文內容存入 txt 檔，txt 的檔名是超連結名稱，例如 `豆棚閒話.txt`。
      - 每一個 txt 都會被存在 `project_gutenberg` 資料夾內。
      - 至少要有 `200` 本，少 1 本扣 1 分。
      - `錄製`執行過程，並提供`影片連結`，可以放在 `YouTube` 或是 `Google Drive`。
      - 不用給我程式碼。
	  - 參考影片: [古騰堡計劃（Project Gutenberg）中文電子書爬取](https://www.youtube.com/watch?v=gKDBiVvzMfk)
    - `100` 分條件 (基於 `80` 分條件)
      - 使用 `GitHub` 平台來提交作業，並且將 `github repo` 連結寄給我。
        - Git 與 GitHub 使用教學: [程式與網頁開發者必備技能！Git 和 GitHub 零基礎快速上手，輕鬆掌握版本控制的要訣！](https://www.youtube.com/watch?v=FKXRiAiQFiY)
        - Markdown 語法: [如何使用 Markdown 語言撰寫技術文件](https://experienceleague.adobe.com/zh-hant/docs/contributor/contributor-guide/writing-essentials/markdown)
      - `repository` 裡面至少要有 `project_gutenberg` 資料夾，還有你的 `.py` 或 `.ipynb` 檔案，以及 `README.md`。
        ```
        project_gutenberg/
        project_gutenberg.ipynb (或 .py)
        README.md
        ```
      - `README.md` 要有說明 (用 `.py` 執行要額外說明執行指令或方法)，例如:
        ```markdown
        # Project Gutenberg
        爬取中文書籍，共 xxx 本。

        ## 安裝套件
        - requests (版本號)
        - beautifulsoup4 (版本號)
        - selenium (版本號)
        ...
		(版本號可用 pip list，或是 conda list 來檢視)
        ...

        ## 成果
        ![](執行過程的擷圖或說明圖片)
        ...
        [影片名稱或其它標題](你的影片連結)
        ...

        ## 其它標題
        ...
        ...
        ```
	  - 可以參考以前學長的 README 撰寫方式: [FaceBook FanPage Scraper with selenium](https://github.com/nana89823/facebook_scraper)
    - 沒交：`0` 分。
- 繳交時間
  - 原則上最後一堂課結束後 2 週內，準確時間上課說明。


## 教學參考影片
- [資展國際-OJTP01-18小時-Python網路爬蟲](https://www.youtube.com/playlist?list=PLV4FeK54eNbzgcKtC5s3u7Tv2dZ0BnVsW "資展國際-OJTP01-18小時-Python網路爬蟲")
- [資展國際-BDSE33-Python網路爬蟲 - 12/2, 12/3, 12/9, 12/10](https://www.youtube.com/playlist?list=PLV4FeK54eNbxprT9Sn6FWlcb63u8t0HKt "資展國際-BDSE33-Python網路爬蟲")
- [臺大計算機中心 - Python 網路爬蟲 - 2022/06/20 開班](https://www.youtube.com/playlist?list=PLV4FeK54eNbyZ_rvAAkCICYufOtuQZtTI)
- [資展國際 - 養成班 BDSE22 - Python網路爬蟲](https://www.youtube.com/playlist?list=PLV4FeK54eNbwOKHOH4aWR95fo0cU4wH3O "Python網路爬蟲")
- [臺大計算機中心 - Python 網路爬蟲 - 2021/10/01 開班](https://www.youtube.com/playlist?list=PLV4FeK54eNby0rK-Xpex6baRXE3DG-leg "Python網路爬蟲")
- [資展國際 - 在職班 20210925 至 20210926 - Python 網路爬蟲](https://www.youtube.com/playlist?list=PLV4FeK54eNbwqSdrLfXitmfb4HhB51yOM "Python網路爬蟲")


## 延伸應用
- [Leaflet.js - Web 互動式地圖](https://www.youtube.com/playlist?list=PLV4FeK54eNbwNaCoJomI1jhvgm-A-vOsz)
- [GPT2-Chinese old branch 中文語言模型訓練與生成](https://youtu.be/c3fHRQonqlM)
- [臺大計中電子報 - 第0062期‧2022-09-20 發行 - 使用PyAutoGUI開發桌面自動化程式](https://www.cc.ntu.edu.tw/chinese/epaper/home/20220920_006203.html "臺大計中電子報 - 第0062期‧2022-09-20 發行 - 使用PyAutoGUI開發桌面自動化程式")
- [臺大計中電子報 - 第0059期‧2021.12.20 發行 - 使用GPT2-Chinese生成具有情感的中文對話文字](https://www.cc.ntu.edu.tw/chinese/epaper/0059/20211220_5908.html "臺大計中電子報 - 第0059期‧2021.12.20 發行 - 使用GPT2-Chinese生成具有情感的中文對話文字")
- [臺大計中電子報 - 第0058期‧2021.09.20 發行 - 使用GPT2-Chinese生成中文小說](https://www.cc.ntu.edu.tw/chinese/epaper/0058/20210920_5808.html "臺大計中電子報 - 第0058期‧2021.09.20 發行 - 使用GPT2-Chinese生成中文小說")