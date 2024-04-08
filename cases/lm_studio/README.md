# lm studio
- 在 localhost 安裝 large language model (LLM) 伺服器，並使用 OpenAI 的 API 來進行對話、圖片描述等應用。
  - [首頁](https://lmstudio.ai/)
    - 請依作業系統下載適合的版本
  - [使用說明](https://lmstudio.ai/docs/welcome)
- 可以參考 [The Walking Fish的程式小站](https://the-walking-fish.com/p/lmstudio/) 有關 LM Studio 的介紹
- 下載的 LLM 是 [量化](https://towardsdatascience.com/introduction-to-weight-quantization-2494701b9c0c) 後的版本
  - GGUF (GPT-Generated Unified Format) 的相關說明：
    - [GGUF](https://huggingface.co/docs/hub/en/gguf)
    - [TheBloke/Llama-2-13B-GGML](https://huggingface.co/TheBloke/Llama-2-13B-GGML)
	- [[Day 15] - 鋼鐵草泥馬 🦙 LLM chatbot 🤖 (6/10)｜GGML 量化 LLaMa](https://ithelp.ithome.com.tw/articles/10331431)
- index.html 和 web_api.py 是測試文字串流效果的範例，參考連結如下：
  - [YouTube video](https://www.youtube.com/watch?v=z6iYcqNECwA)
  - [Source code](https://github.com/PrettyPrinted/youtube_video_code/tree/master/2024/03/28/How%20to%20Stream%20OpenAI%20API%20Responses%20in%20a%20Flask%20App/flask_openai_streaming)


## 套件安裝
```bash
pip install openai requests flask
```

## 模型使用範例
- 英文
  - 程式碼生成
    - TheBloke/CodeLlama-7B-Instruct-GGUF/codellama-7b-instruct.Q8_0.gguf
  - 對話生成
    - lmstudio-ai/gemma-2b-it-GGUF/gemma-2b-it-q8_0.gguf
- 繁體中文 (Optional)
  - 對話生成
    - audreyt/Taiwan-LLM-7B-v2.0.1-chat-GGUF/Taiwan-LLM-7B-v2.0.1-chat-Q5_K_M.gguf
    - audreyt/Taiwan-LLM-7B-v2.0.1-chat-GGUF/Taiwan-LLM-7B-v2.0.1-chat-Q8_0.gguf

## 下載模型流程
- 選擇模型，最後按下 Download
![](https://i.imgur.com/PlDyc8s.png)
- 觀看模型下載進度
![](https://i.imgur.com/g9QEea6.png)
- 模型驗證中
![](https://i.imgur.com/xN5yyyI.png)
- 驗證完成
![](https://i.imgur.com/vqBxafd.png)
- 與 AI 對話 (需要先選擇模型，讀取需要一段時間)
![](https://i.imgur.com/fWTnQxz.png)

## 提示字
系統提示 (system prompt)
```log
A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.
```

使用者提示 (user prompt) 註: 使用 CodeLlama-7B-Instruct-GGUF 模型
```bash
請幫我撰寫一段 9x9 乘法表的程式碼，使用 python 來撰寫，只要程式碼範例就好，不用額外說明。
```
![](https://i.imgur.com/bIz47ui.png)

## 使用者提示字範例
- 一般使用者提示
```
問題：是位於臺灣臺北市中山區劍潭山的旅館，成立於第二次世界大戰後，早年為臺灣首屈一指的大型國際性飯店。目前所見的中國宮殿風格建築於1973年落成，是臺北地標之一。飯店屋顶使用歇山式。飯店的建築上採用相當多的龍形雕刻，故有人稱此飯店為「龍宮」； 除採用龍形之外，亦有石獅、梅花等中國建築常用的圖案。該建築的名稱是：(A)帝后大飯店(B)台北城大飯店(C)圓山大飯店(D)天成文旅華山町

注意：不用過多的說明，只要正確地回答 (A),(B),(C),(D) 其中一個就可以了。

答案是：
```
![](https://i.imgur.com/bLoK8sP.png)


- 一般使用者提示：加入問題相關的背景知識，幫助 LLM 回答問題，例如透過網路爬蟲、網頁搜尋、資料庫查詢等方式取得背景知識
```log
背景知識如下：
圓山大飯店，是一座位於臺灣臺北市中山區劍潭山的旅館，成立於第二次世界大戰後。酒店始建於1952年5月，主樓落成於1973年10月10日。曾為20世紀後期臺灣首屈一指的大型國際性飯店，並自啟用後曾接待過許多來臺北訪問的外國政要。當前臺北圓山大飯店已晉升為交通部觀光局評鑑之五星級飯店。

問題：是位於臺灣臺北市中山區劍潭山的旅館，成立於第二次世界大戰後，早年為臺灣首屈一指的大型國際性飯店。目前所見的中國宮殿風格建築於1973年落成，是臺北地標之一。飯店屋顶使用歇山式。飯店的建築上採用相當多的龍形雕刻，故有人稱此飯店為「龍宮」； 除採用龍形之外，亦有石獅、梅花等中國建築常用的圖案。該建築的名稱是：(A)帝后大飯店(B)台北城大飯店(C)圓山大飯店(D)天成文旅華山町

請從以上選項中選擇並回答。
注意：
1. 答案只能是選項 (A), (B), (C), (D) 其中 1 個，必須在回答的開頭顯示答案，而且答案左邊、右邊都要有括號(Parentheses)。
2. 回答的內容只能是一句話，不能有換行符號(\n)。

答案是：
```
![](https://i.imgur.com/pl8EhvL.png)


- 一般使用者提示：多一點背景知識的使用者提示 - 要注意支援 最大序列長度 (max_seq_length) 或 上下文長度 (context length) 是多少
```log
背景知識如下：
林懷民（），是一名臺灣編舞家及作家，為現代舞團雲門舞集創辦人與藝術總監。林懷民為國立政治大學新聞學士、愛荷華大學藝術碩士。2006年獲選為Discovery頻道《臺灣人物誌》的6名主角之1。
雲門舞集，是一個臺灣的現代舞蹈表演團體，於1973年由林懷民創辦，是臺灣的第一個現代舞職業舞團。雲門之名來自《呂氏春秋》中的一句話：「黃帝時，大容作雲門，大卷……」，也就是傳說中黃帝時代舞蹈的名稱。雲門舞集曾推出多個舞蹈作品，當中包括有薪傳，九歌，家族合唱，流浪者之歌，水月，竹夢，行草等等。

問題：臺灣第一個現代舞劇團「雲門舞集」的創辦人與藝術總監。2006年獲選為Discovery頻道《台灣人物誌》的6名主角之1。他的名字是：(A)林懷民(B)羅文裕(C)李國修(D)林怡君

請從以上選項中選擇並回答。
注意：
1. 答案只能是選項 (A), (B), (C), (D) 其中 1 個，必須在回答的開頭顯示答案，而且答案左邊、右邊都要有括號(Parentheses)。
2. 回答的內容只能是一句話，不能有換行符號(\n)。

答案是：
```
![](https://i.imgur.com/uCsXoCP.png)


## 在 localhost 建立 server
- 開啟 Local Inference Server (它會額外提供 Web API 服務)
![](https://i.imgur.com/KAzGvMN.png)
- 執行 web_api.py: `python web_api.py` (它會串接 Local Inference Server 的 Web API)
- 進入 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- 互動後，檢視 Local Inference Server 與瀏覽器頁面
![](https://i.imgur.com/257lhXU.png)


## 範例程式
**使用 CURL 來對 local server 進行聊天對話**
```bash
curl http://localhost:1234/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{ 
  "model": "TheBloke/CodeLlama-7B-Instruct-GGUF/codellama-7b-instruct.Q8_0.gguf",
  "messages": [ 
    { "role": "system", "content": "Always answer in rhymes." },
    { "role": "user", "content": "Introduce yourself." }
  ], 
  "temperature": 0.7, 
  "max_tokens": -1,
  "stream": true
}'
```

**使用 python 來對 local server 進行聊天對話**
```python
# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="TheBloke/CodeLlama-7B-Instruct-GGUF/codellama-7b-instruct.Q8_0.gguf",
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)
```

**在終端機與 AI 進行對話**
```python
# Chat with an intelligent assistant in your terminal
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

history = [
    {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
]

while True:
    completion = client.chat.completions.create(
        model="TheBloke/CodeLlama-7B-Instruct-GGUF/codellama-7b-instruct.Q8_0.gguf",
        messages=history,
        temperature=0.7,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)
    
    # # Uncomment to see chat history
    # import json
    # gray_color = "\033[90m"
    # reset_color = "\033[0m"
    # print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
    # print(json.dumps(history, indent=2))
    # print(f"\n{'-'*55}\n{reset_color}")

    print()
    history.append({"role": "user", "content": input("> ")})
```

**讀取圖片並進行描述**
```python
# Adapted from OpenAI's Vision example 
from openai import OpenAI
import base64
import requests

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Ask the user for a path on the filesystem:
path = input("Enter a local filepath to an image: ")

# Read the image and encode it to base64:
base64_image = ""
try:
  image = open(path.replace("'", ""), "rb").read()
  base64_image = base64.b64encode(image).decode("utf-8")
except:
  print("Couldn't read the image. Make sure the path is correct and the file exists.")
  exit()

completion = client.chat.completions.create(
  model="TheBloke/CodeLlama-7B-Instruct-GGUF/codellama-7b-instruct.Q8_0.gguf",
  messages=[
    {
      "role": "system",
      "content": "This is a chat between a user and an assistant. The assistant is helping the user to describe an image.",
    },
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          },
        },
      ],
    }
  ],
  max_tokens=1000,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content:
    print(chunk.choices[0].delta.content, end="", flush=True)
```

## 替選方案
- [GPT4All](https://gpt4all.io/index.html)
- [ollama](https://github.com/ollama/ollama)
- [llamafile](https://github.com/Mozilla-Ocho/llamafile)
