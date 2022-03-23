# GPT2-Chinese

## 一、簡介
自然語言生成（natural language generation，NLG）是自然語言處理（natural language processing，NLP）重要的一部分。它可以降低人類與機器之間資訊交流的鴻溝，也試著將大量的非結構性資料，轉換成人類能夠理解的呈現方式。自然語言生成的系統，常用於協助人類作家撰寫日常的文件，包括商業書信、天氣報告，也被用作互動式解說工具，以易於理解的方式，與非專業使用者進行溝通交流；在進行決策時，儘管最常用的方法是以圖形方式顯示數據，但已證明文本摘要可以改善決策制定。
***
由於近年人工智慧（artificial intelligence，AI）議題的興起，透過 AI 即時處理並應用大量數據的特性，延伸出許多 NLG 的應用，例如聊天機器人（chatbot）、線上客戶（online customer service）等對話系統，其對話的內容與訊息，是透過 NLG 來產生。
***
在過去，對話生成通常使用循環神經網路（recurrent neural network）、長短期記憶（long-short term memory，LSTM）、閘道循環單位（gated recurrent unit，GRU）等來建立語言模型（language model），以考慮前一個文字，來對下一個可能生成的文字進行預測，然而 RNN 在長時間的記憶表現不好，LSTM 與 GRU 雖然改善了 RNN 架構，卻又有耗費系統資源的問題。在 2019 年，Open AI 推出了 GPT-2（generative pre-trained 2），在對話生成上，有著優異的表現。GPT-2 是一個大型、以 transformer 為基礎的語言模型，其語言建模對大約 40 GB 的超大語料庫進行了預訓練。GPT-2 的模型訓練效果不僅比 RNN、LSTM、GRU 好，且對上下文的文句預測精準度更佳，徹底改變了自然語言處理的生態；現今主流自然語言生成領域的機器學習模型基礎，大多建立在 transformer 之上。
***
近年 GPT-2 應用的範圍很多，例如透過生成專利範圍內容，用來協助發明人解決對於專利範圍無法掌握撰寫要領的問題；在收集多樣化的問題過後，透過人、事、時、地、物加以分類，再透過生成完整的問題句子，來解決將相同分類中相似的問題進行替換後，問句不完整的情形；給定風格、關鍵句子與隨機參數，進行歌詞生成，根據風格條件生成具有結構性、押韻性、原創性的歌詞等等。

## 二、本例練習目的
1. 透過 GPT2-Chinese 訓練自行整理的語料。
2. 套用訓練完成的語言模型，透過自訂的前導文字，來進行後續的文字生成。

## 三、說明
- 作業環境:
  - Windows 10 or Linux Ubuntu 18.04+
  - Anaconda (Python 3.7+)
- 專案連結:
  - [GPT2-Chinese 專案連結](https://github.com/Morizeyao/GPT2-Chinese/tree/old_gpt_2_chinese_before_2021_4_22 "GPT2-Chinese 專案連結")
- 下載方式:
  - Git 下載指令：```git clone https://github.com/Morizeyao/GPT2-Chinese.git```
  - 手動下載：專案連結頁面 -> Code -> Download ZIP
- 開始前的準備與流程
  - 說明:
    - 以 電腦 / 筆電 有 GPU 的 Windows 環境為例
    - 請注意 nvidia driver 與 CUDA、CUDA 與 CuDNN 之間的相依問題
  - 流程一: 先確認 nVIDIA driver 是否安裝，如果不是進階使用者，建議用最新版 [NVIDIA 驅動程式下載](https://www.nvidia.com.tw/Download/index.aspx?lang=tw "NVIDIA 驅動程式下載")
    - 下載方式分為「SD」與「GRD」
      - 如果你需要對最新遊戲、DLC 提供最即時支援的玩家，請選擇 Game Ready 驅動程式。
      - 如果你需要對影片編輯、動畫、攝影、繪圖設計和直播等創作流程提供穩定的品質，請選擇 Studio 驅動程式。
  - 流程二: 以 GPT-2 所使用的 Transformer 為例
    - 它使用 PyTorch 框架，所以要先了解 PyTorch 支援的 CUDA 版本: [INSTALL PYTORCH](https://pytorch.org/ "INSTALL PYTORCH")
    - 下載 CUDA 前，請先至 PyTorch 網站，了解目前支援 CUDA 的版本，下載 cuDNN 亦同。
    - ![INSTALL PYTORCH](https://i.imgur.com/xBctpZ0.png "INSTALL PYTORCH")
  - 流程三: 下載: [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive "CUDA Toolkit Archive")
  - 流程四: 下載: [NVIDIA cuDNN](https://developer.nvidia.com/cudnn "NVIDIA cuDNN")
    - 需要先申請帳號密碼，才能進入下載頁面
    - 中間可能會請你填寫問卷，依實際情況填寫即可
  - 目前個人電腦環境所配對的 CUDA / cuDNN 下載連結
    - CUDA: [CUDA Toolkit 11.1 Update 1 Downloads](https://developer.download.nvidia.com/compute/cuda/11.1.1/local_installers/cuda_11.1.1_456.81_win10.exe "cuda_11.1.1_456.81_win10.exe")
    - cuDNN: [cuDNN Library for Windows (x86)](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.0.5/11.1_20201106/cudnn-11.1-windows-x64-v8.0.5.39.zip "cudnn-11.1-windows-x64-v8.0.5.39.zip")
  - 安裝套件:
    - 進入專案資料夾後輸入 ```pip install -r requirements.txt```
  - 檢測目前電腦有沒有支援 CUDA 的程式碼
    ```
    import torch
    print(torch.cuda.is_available())
    print(torch.cuda.current_device())
    print(torch.cuda.device(0))
    ```
    ```
    若有支援，應該輸出類似下方的字樣:
    True
    0
    <torch.cuda.device object at 0x0000024A91A63130>   
    ```
- 安裝參考連結: 
  - [Table 3. CUDA Toolkit and Corresponding Driver Versions](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html "Table 3. CUDA Toolkit and Corresponding Driver Versions")
  - [CUDA 與 CuDNN 安裝及環境變數設定](https://qqmanlin.medium.com/cuda-%E8%88%87-cudnn-%E5%AE%89%E8%A3%9D-e982d92162af "CUDA 與 CuDNN 安裝及環境變數設定")
  - [Win10環境下配置CUDA與cuDNN](https://dotblogs.com.tw/CYLcode/2018/09/20/163005 "Win10環境下配置CUDA與cuDNN")
- 確認 CUDA 是否正確安裝的指令:
  - 安裝完 nVIDIA driver 後可用的指令（GPU 當前狀態）: ```nvidia-smi```
  - 安裝完 CUDA 後可用的指令（觀看目前安裝的 CUDA 版本）: ```nvcc -V```
- 訓練資料結構:
    - [連結](https://github.com/Morizeyao/GPT2-Chinese/blob/old_gpt_2_chinese_before_2021_4_22/train.json "連結")
	- ![訓練格式](https://i.imgur.com/Dab1QPY.png "訓練格式")
- 參考網頁:
  - [直觀理解 GPT-2 語言模型並生成金庸武俠小說](https://leemeng.tw/gpt2-language-model-generate-chinese-jing-yong-novels.html "直觀理解 GPT-2 語言模型並生成金庸武俠小說")
  - [使用GPT2-Chinese生成中文小說](https://www.cc.ntu.edu.tw/chinese/epaper/0058/20210920_5808.html "作者：楊德倫 / 資策會數位教育研究所數位人才培育中心講師")

- 金庸小說訓練資料的爬取教學
  - [selenium 取得金庸小說的內容，並存成txt與json檔](https://www.youtube.com/watch?v=jJzZcMjZsKM "[selenium]取得金庸小說的內容，並存成txt與json檔")
  - [requests 取得金庸小說的內容，並存成txt與json檔](https://www.youtube.com/watch?v=JsmLtMC43Lc "[requests]取得金庸小說的內容，並存成txt與json檔")

## 四、在 Windows 的基本使用方式

### （一）win10 安裝pytorch gpu 及 解決報錯“OSError: [WinError 126] 找不到指定的模組
[WinError 126 找不到指定的模組](https://www.mdeditor.tw/pl/pndo/zh-tw "WinError 126 找不到指定的模組")

### （二）[WinError 126] VC-redist 安裝檔
[WinError 126 VC-redist 安裝檔](https://download.visualstudio.microsoft.com/download/pr/89a3b9df-4a09-492e-8474-8f92c115c51d/B1A32C71A6B7D5978904FB223763263EA5A7EB23B2C44A0D60E90D234AD99178/VC_redist.x64.exe "WinError 126 VC-redist 安裝檔")

### （三）訓練文章的指令
```
python train.py --device=0 --epochs=1 --batch_size=1 --min_length=10 --raw_data_path=data/jinyong.json --output_dir=model/ --raw
```
| 參數 | 說明 |
| ------ | ------ |
| train.py | 訓練用主程式 |
| device | 指定用哪一個 GPU (沒 GPU，預設 CPU) |
| epochs | 訓練幾回 |
| batch_size | 每次拿幾個樣本進行訓練。常見的是 2 的 n 次方 |
| min_length | 每個樣本至少需要多少長度才拿來訓練 |
| raw_data_path | 訓練資料 JSON 檔案路徑 |
| output_dir | 訓練完的語言模型存放資料夾 |
| raw | 設定此參數，會將樣本進行 tokenize |

### （四）生成文章的指令
```
python generate.py --length=250 --nsamples=3 --prefix="張無忌見三名老僧在片刻間連斃崑崙派四位高手，" --temperature=0.7 --model_path=model/model_epoch100_jinyong/ --save_samples --save_samples_path=output/
```
| 參數 | 說明 |
| ------ | ------ |
| generate.py | 生成文字用主程式 |
| length | 生成文字的長度 |
| nsamples | 生成幾個文章範本 |
| prefix | 生成文章的前導文字，會影響生成的發展 |
| temperature | 生成溫度溫度越高，模型產生出來的結果越隨機、越不可預測；換言之，使得原先容易被選到的字，抽出的機會變小，平常較少出現的字，被選到的機會稍微增加 |
| model_path | 生成文字所使用的語言模型資料夾路徑 |
| save_samples | 有設定的話，會儲存生成文章的範本 |
| save_samples_path | 生成文章範本的儲存路徑 |

有關溫度（temperature）的參考資料
[Deep learning with Python 學習筆記（10）生成式深度學習](https://www.cnblogs.com/zhhfan/p/10335907.html "Deep learning with Python 學習筆記（10）生成式深度學習")
![更低的溫度= 更確定，更高的溫度= 更隨機](https://img2018.cnblogs.com/blog/1503464/201901/1503464-20190129211804100-1598676964.png "更高的溫度得到的是熵更大的採樣分佈，會生成更加出人意料、更加無結構的生成數據，而更低的溫度對應更小的隨機性，以及更加可預測的生成數據。對同一個概率分佈進行不同的重新加權。")

## 五、在 Linux、MacOS 的基本使用方式

### （一）訓練文章的指令
```
time python3.7 train.py \
--device=0 \
--epochs=1 \
--num_pieces=100 \
--batch_size=32 \
--min_length=10 \
--raw_data_path=data/jinyong.json \
--output_dir=model/ \
--raw 
```

### （二）生成文章的指令
```
time python3 generate.py \
--length=250 \
--nsamples=3 \
--prefix="張無忌見三名老僧在片刻間連斃崑崙派四位高手，" \
--temperature=0.7 \
--model_path=model/model_epoch100_jinyong/ \
--save_samples \
--save_samples_path=output/
```

## 六、擷圖
!["訓練過程中，每個 step 輸出 log 的畫面"](https://i.imgur.com/nIh2b7b.png "訓練過程中，每個 step 輸出 log 的畫面")

圖 1 訓練過程中，每個 step 輸出 log 的畫面

![每一回合訓練的 model，會各別輸出儲存](https://i.imgur.com/dUOe9ZI.png "每一回合訓練的 model，會各別輸出儲存")

圖 2 每一回合訓練的 model，會各別輸出儲存

![每訓練完 1 個 epoch，會計算與顯示當前回合的訓練時間長](https://i.imgur.com/apTVmn6.png "每訓練完 1 個 epoch，會計算與顯示當前回合的訓練時間長")

圖 3 每訓練完 1 個 epoch，會計算與顯示當前回合的訓練時間長(圖片以 epoch 1 為例)

![以訓練第 100 回合的 model 來進行生成測試](https://i.imgur.com/0Rq0oK5.png "以訓練第 100 回合的 model 來進行生成測試")

圖 4 以訓練第 100 回合的 model 來進行生成測試

![訓練 100 epochs 後的畫面，訓練程式結束的畫面](https://i.imgur.com/NEx0J0H.png "訓練 100 epochs 後的畫面，訓練程式結束的畫面")

圖 5 訓練 100 epochs 後，訓練程式結束的畫面

## 七、預訓練模型與相關檔案連結
[Google 雲端硬碟](https://drive.google.com/drive/folders/1EmqZsb3Lp_M7ftSiKVgHC6xIiWQVmDBe?usp=sharing "Google 雲端硬碟")