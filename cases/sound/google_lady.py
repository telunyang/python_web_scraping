'''
下載 google 小姐的聲音

Web API 網址:
https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q=你的自訂文字

將文字進行 url encode 網頁:
https://www.onlinewebtoolkit.com/url-encode-decode

在 Terminal 使用 curl 指令下載 mp3:
curl -X GET "https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q=%E4%BD%A0%E7%9A%84%E8%87%AA%E8%A8%82%E6%96%87%E5%AD%97" -o ./test.mp3

tl=zh-TW 的其它設定:
[1] Understanding the Significance of Query Parameters in Google Translate
https://copyprogramming.com/howto/what-is-the-meaning-of-google-translate-query-params
[2] Google translate language codes
https://gist.github.com/JT5D/a2fdfefa80124a06f5a9
'''
import subprocess
from urllib.parse import quote
import os


'''
測試單句下載 mp3
'''
# 設定給 google 小姐發音的文字
q = '我的優點就是帥，缺點就是帥得不明顯'

# 轉成符合 url 格式的文字
encoded_sentence = quote(q)

# 定義指令
cmd = [
    'curl', 
    '-X', 
    'GET', 
    f'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q={encoded_sentence}',
    '-o',
    f'./{q}.mp3'
]

# 執行指令，回傳 Process 物件，其中的屬性 returncode == 0 代表成功
std_output = subprocess.run(cmd)
if std_output.returncode == 0:
    print(f'[{q}] 下載成功')
else:
    print(f'[{q}] 下載失敗')



'''
將 google 小姐的聲音加速 - 使用 ffmpeg

參考網頁:
https://ffmpeg.org/download.html

下載工具: 
- Windows 10: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
- MacOS: https://evermeet.cx/ffmpeg/ffmpeg-112875-g47e214245b.zip

Windows 說明:
1. 下載 zip 檔，解壓縮到專案目錄 (python_basics) 底下。
2. 如果解壓縮的目錄叫作「ffmpeg-6.1-essentials_build」，請改成「ffmpeg」。
3. ffmpeg 資料夾裡面有個 bin 資料夾，裡面的 ffmpeg.exe 是主要的轉檔程式。

MacOS 說明: 
1. 下載 zip 檔，解壓縮後，會直接看到 ffmpeg 這個檔案。
2. 給它可以執行的權限，例如在 Terminal 裡面對它輸入「chmod +x ffmpeg」。

參考指令: 
- Windows 10: .\ffmpeg\bin\ffmpeg.exe -i test.mp3 -filter:a "atempo=1.5" test_atempo.mp3
- MacOS: ./ffmpeg -i test.mp3 -filter:a "atempo=1.5" test_atempo.mp3
'''
cmd = [
    './ffmpeg/bin/ffmpeg.exe', # 左邊是 Windows 指令。MacOS: ./ffmpeg
    '-i',
    f'./{q}.mp3',
    '-filter:a',
    'atempo=1.5', # 'asetrate=44100*0.4,atempo=1.5'
    f'./{q}_atempo.mp3'
]
std_output = subprocess.run(cmd)
if std_output.returncode == 0:
    print(f'[{q}_atempo] 轉換成功')
else:
    print(f'[{q}_atempo] 轉換失敗')





'''
多句下載
'''
# 如果沒有自訂的資料夾，則自動新增
if not os.path.exists('mp3'):
    os.makedirs('mp3')

# 設定多個給 google 小姐發音的句子
list_words = [
    '人生短短幾個秋啊',
    '不醉不罷休',
    '東邊我的美人哪',
    '西邊黃河流'
]

# 把每一句都下載成 mp3
for index, q in enumerate(list_words):
    # 轉成符合 url 格式的文字
    encoded_sentence = quote(q)

    # 定義指令
    cmd = [
        'curl', 
        '-X', 
        'GET', 
        f'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q={encoded_sentence}',
        '-o',
        f'./mp3/{index}.mp3'
    ]

    # 執行指令，回傳 Process 物件，其中的屬性 returncode == 0 代表成功
    std_output = subprocess.run(cmd)
    if std_output.returncode == 0:
        print(f'[{index}] 下載成功')
    else:
        print(f'[{index}] 下載失敗')

    cmd = [
        './ffmpeg/bin/ffmpeg.exe',
        '-i',
        f'./mp3/{index}.mp3',
        '-filter:a',
        'atempo=1.5', # 'asetrate=44100*0.4,atempo=1.5'
        f'./mp3/{index}_atempo.mp3'
    ]
    std_output = subprocess.run(cmd)
    if std_output.returncode == 0:
        print(f'[{index}] 轉換成功')
    else:
        print(f'[{index}] 轉換失敗')