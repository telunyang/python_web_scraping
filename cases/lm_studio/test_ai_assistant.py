'''
在 Terminal 中執行以下指令，啟動 AI assistant 服務，實現多輪對話功能
'''

# 匯入套件
from openai import OpenAI

# 指向 localhost 伺服器
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# 設定對話紀錄
history = [
    {"role": "system", "content": "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions."},
    {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
]

# 進入對話迴圈
while True:
    # 透過 Chat Completions API 來取得 ai assistant 的回應
    completion = client.chat.completions.create(
        model="TheBloke/CodeLlama-7B-Instruct-GGUF/codellama-7b-instruct.Q8_0.gguf",
        messages=history,
        temperature=0.7,
        stream=True,
    )

    # 取得 ai assistant 的回應
    new_message = {"role": "assistant", "content": ""}
    
    # 透過 stream 方式，將 ai assistant 生成的文字一個一個輸出
    for chunk in completion:
        if chunk.choices[0].delta.content:
            # 以 stream 方式，將 ai assistant 生成文字一個一個輸出的方法
            print(chunk.choices[0].delta.content, end="", flush=True)

            # 將 ai assistant 輸出的文字串接起來
            new_message["content"] += chunk.choices[0].delta.content

    # 將 ai assistant 生成的文字加入到對話紀錄中
    history.append(new_message)
    
    '''
    # 取消註解，來觀看對話紀錄
    import json
    gray_color = "\033[90m"
    reset_color = "\033[0m"
    print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
    print(json.dumps(history, indent=2))
    print(f"\n{'-'*55}\n{reset_color}")
    '''
    
    # 換行
    print()

    # 使用者輸入 (請在 Terminal 中輸入文字，並按下 Enter 鍵，以繼續對話)
    history.append({"role": "user", "content": input("> ")})


'''
覺得純英文的模型，看得懂中文嗎？

請嘗試使用以下這段話來提問：
請幫我撰寫一個 9 9 乘法表的程式，程式使用 python 來撰寫。
'''

'''
可能的輸出結果如下：


sure, here is a program to print the multiplication table of 9 using Python:
```
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print()
```
This program uses nested loops to iterate over the rows and columns of the multiplication table. The `range` function is used to generate a sequence of numbers from 1 to 9, which are then multiplied together to get the product for each cell in the table. Finally, the `print` function is used to print the resulting products on separate lines.

You can run this program by saving it to a file with a `.py` extension and running it using the Python interpreter. For example:
```
$ python multiplication_table.py
```
This will output the multiplication table of 9 to the console.
'''
