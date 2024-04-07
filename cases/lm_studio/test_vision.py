# Adapted from OpenAI's Vision example 
from openai import OpenAI
import base64
import requests

# 指向 localhost 伺服器
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# 輸入圖片路徑
path = input("輸入本機的圖片路徑 (可用相對路徑): ")

# 以 base64 格式讀取圖片
base64_image = ""
try:
  image = open(path.replace("'", ""), "rb").read()
  base64_image = base64.b64encode(image).decode("utf-8")
except:
  print("無法讀取圖片，請確認路徑上的圖片檔案是否存在。")
  exit()

# 生成文字
completion = client.chat.completions.create(
  model="TheBloke/CodeLlama-7B-Instruct-GGUF/codellama-7b-instruct.Q8_0.gguf",
  messages=[
    {
      "role": "system",
      "content": "This is a chat between a user and an assistant. The assistant is helping the user to describe an image.",
    },
    {
      "role": "user",
      "content": [ # 使用者對話內容，可以是一個 list
        { # 使用者提示
          "type": "text", 
          "text": "What’s in this image?"
        }, 
        { # 使用者提供的圖片
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

# 以 stream 方式，將 ai assistant 生成文字一個一個輸出的方法
for chunk in completion:
  if chunk.choices[0].delta.content:
    print(chunk.choices[0].delta.content, end="", flush=True)