'''
測試對話生成
'''

# 匯入套件
from openai import OpenAI

# 指向 localhost 伺服器
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# 生成對話
completion = client.chat.completions.create(
  model="TheBloke/CodeLlama-7B-Instruct-GGUF/codellama-7b-instruct.Q8_0.gguf",
  messages=[
    {"role": "system", "content": "Always answer in rhymes."}, # 設定對話的風格或是要求 AI 扮演某些角色
    {"role": "user", "content": "Introduce yourself."},
    # ...
    # 想要一直聊下去，可以繼續加入對話：
    # {"role": "assistant", "content": ""},
    # {"role": "user", "content": ""},
    # {"role": "assistant", "content": ""},
    # {"role": "user", "content": ""},
    # ...
  ],
  temperature=0.7
)

# 輸出結果
print(completion.choices[0].message)
'''
輸出結果：
ChatCompletionMessage(
    content='Hello there! I am LLaMA, an AI assistant developed by Meta AI that can understand and respond to human input in a conversational manner. I am capable of answering questions, providing information, and even generating creative content such as stories or poems. I am constantly learning and improving my responses based on the interactions I have with users like you. Please feel free to ask me anything!', 
    role='assistant', 
    function_call=None, 
    tool_calls=None
)
'''

# # 若只想取得回覆內容的文字部分，可以使用 completion.choices[0].message.content
# print(completion.choices[0].message.content)