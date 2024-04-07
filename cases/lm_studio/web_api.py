from flask import Flask, request
from flask_cors import CORS
from openai import OpenAI

'''
Flask 初始化
'''
app = Flask(__name__)
app.json.ensure_ascii = False # 防止中文變成 unicode 編碼
CORS(app) # 設定全域 CORS

'''
OpenAI 設定初始化
'''
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


# 使用字典來保存每個會話的對話歷史
sessions_history = {}

# 自訂路由
@app.route("/chat", methods=["POST"])
def chat():
    # 取得前端傳來的 JSON 格式資料
    data = request.json

    # 取得 session id 和 使用者的訊息
    session_id = data.get("session_id")
    user_message = data.get("message")

    # 如果 session id 不存在於對話記錄中，針對這個 session id 建立一個新的會話記錄
    if session_id not in sessions_history:
        sessions_history[session_id] = [
            {"role": "system", "content": "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions."}
        ]

    # 將使用者的訊息，加入到會話記錄中
    sessions_history[session_id].append({"role": "user", "content": user_message})

    # 生成回應
    def generate_responses():
        # 透過 Chat Completions API 來取得 ai assistant 的回應
        completion = client.chat.completions.create(
            model="audreyt/Taiwan-LLM-7B-v2.0.1-chat-GGUF/Taiwan-LLM-7B-v2.0.1-chat-Q5_K_M.gguf",
            messages=sessions_history[session_id],
            temperature=0.7,
            stream=True,
        )

        # 透過 stream 方式，將 ai assistant 生成的文字一個一個輸出
        content = ''
        for chunk in completion:
            if chunk.choices[0].delta.content:
                content += chunk.choices[0].delta.content
                yield chunk.choices[0].delta.content

        # 將生成的回應加入到會話歷史中
        sessions_history[session_id].append({"role": "assistant", "content": content})

    # 回傳 ai assistant 生成的回應
    return generate_responses(), {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(
        # 除錯模式為 True，服務執行期間有錯誤，會將 Traceback 顯示在網頁上，
        # 反之則顯示一般的 Internal Server Error
        debug=True,

        # 127.0.0.1 或 localhost 限定本機使用服務，
        # 0.0.0.0 代表所有知道主機實際 IP 的人都能存取 
        host='127.0.0.1',

        # 網址或 IP 後面附加的 Port 號，代表服務由該 Port 號提供
        port=5000 
    )
