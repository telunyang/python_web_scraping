# GPT2-Chinese

## 一、說明
- 作業環境:
  - Windows 10 or Linux Ubuntu 18.04+
  - Anaconda (Python 3.7+)
- 專案連結:
  - [GPT2-Chinese 專案連結](https://github.com/Morizeyao/GPT2-Chinese "GPT2-Chinese 專案連結")
- 下載方式:
  - Git 下載指令：```git clone https://github.com/Morizeyao/GPT2-Chinese.git```
  - 手動下載：專案連結頁面 -> Code -> Download ZIP
- 安裝套件:
  - 進入專案資料夾後輸入 ```pip install -r requirements.txt```
- CUDA 下載與參考連結
  - 說明:
    - 以電腦有 GPU 的 Windows 環境為例
    - 請注意 nvidia driver 與 CUDA、CUDA 與 CuDNN 之間的相依問題
  - 下載: [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive "CUDA Toolkit Archive") 
  - 參考連結: 
    - [CUDA 與 CuDNN 安裝及環境變數設定](https://qqmanlin.medium.com/cuda-%E8%88%87-cudnn-%E5%AE%89%E8%A3%9D-e982d92162af "CUDA 與 CuDNN 安裝及環境變數設定")
    - [Win10環境下配置CUDA與cuDNN](https://dotblogs.com.tw/CYLcode/2018/09/20/163005 "Win10環境下配置CUDA與cuDNN")
  - 訓練資料結構:
    - [連結](https://github.com/Morizeyao/GPT2-Chinese/blob/master/train.json "連結")
- 參考網頁:
  - [直觀理解 GPT-2 語言模型並生成金庸武俠小說](https://leemeng.tw/gpt2-language-model-generate-chinese-jing-yong-novels.html "直觀理解 GPT-2 語言模型並生成金庸武俠小說")

## 二、在 Windows 的基本使用方式

### （一）win10 安裝pytorch gpu 及 解決報錯“OSError: [WinError 126] 找不到指定的模組
[WinError 126 找不到指定的模組](https://www.mdeditor.tw/pl/pndo/zh-tw "WinError 126 找不到指定的模組")

### （二）[WinError 126] VC-redist 安裝檔
[WinError 126 VC-redist 安裝檔](https://download.visualstudio.microsoft.com/download/pr/89a3b9df-4a09-492e-8474-8f92c115c51d/B1A32C71A6B7D5978904FB223763263EA5A7EB23B2C44A0D60E90D234AD99178/VC_redist.x64.exe "WinError 126 VC-redist 安裝檔")

### （三）訓練文章的指令
```
python train.py --device=0 --epochs=1 --num_pieces=100 --batch_size=1 --min_length=10 --raw_data_path=data/jinyong.json --output_dir=model/ --raw 
```
| 參數 | 說明 |
| ------ | ------ |
| train.py | 訓練用主程式 |
| device | 指定用哪一個 GPU |
| epochs | 訓練幾回 |
| num_pieces | 訓練資料分成幾份 |
| batch_size | 每次拿幾個樣本進行訓練。常見的是 2 的 n 次方 |
| min_length | 每個樣本至少需要多少長度才拿來訓練 |
| raw_data_path | 訓練資料 JSON 檔案路徑 |
| output_dir | 訓練完的語言模型存放資料夾 |
| raw | 設定此參數，會將樣本進行 tokenize |

### （四）生成文章的指令
```
python generate.py --topk=8 --length=250 --nsamples=3 --prefix="張無忌見三名老僧在片刻間連斃崑崙派四位高手，" --temperature=0.7 --model_path=model/model_epoch100_jinyong/ --save_samples --save_samples_path=output/
```
| 參數 | 說明 |
| ------ | ------ |
| generate.py | 生成文字用主程式 |
| topk | 前 k 個當中取 1 |
| length | 生成文字的長度 |
| nsamples | 生成幾個文章範本 |
| prefix | 生成文章的前導文字，會影響生成的發展 |
| temperature | 生成溫度溫度越高，模型產生出來的結果越隨機、越不可預測；換言之，使得原先容易被選到的字，抽出的機會變小，平常較少出現的字，被選到的機會稍微增加 |
| model_path | 生成文字所使用的語言模型資料夾路徑 |
| save_samples | 有設定的話，會儲存生成文章的範本 |
| save_samples_path | 生成文章範本的儲存路徑 |

## 三、在 Linux、MacOS 的基本使用方式

### （一）訓練文章的指令
```
time python3.7 train.py \
--device=0 \
--epochs=1 \
--num_pieces=100 \
--batch_size=2 \
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

## 四、擷圖
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

## 五、預訓練模型與相關檔案連結
[Google 雲端硬碟](https://drive.google.com/drive/folders/1EmqZsb3Lp_M7ftSiKVgHC6xIiWQVmDBe?usp=sharing "Google 雲端硬碟")