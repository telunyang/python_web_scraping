'''
執行環境: Windows 10
python 版本: 3.6+


套件安裝
$ pip install wget

執行指令 (請先確認「下載路徑相關設定」後，再執行)
$ python video_cutter.py


參考網頁
[1] How to download portion of video with youtube-dl command?
https://unix.stackexchange.com/questions/230481/how-to-download-portion-of-video-with-youtube-dl-command
[2] FFmpeg: Seeking
https://trac.ffmpeg.org/wiki/Seeking
[3] Python 使用 zipfile 模組壓縮、解壓縮 ZIP 檔案教學與範例
https://officeguide.cc/python-zipfile-module-compression-decompression-tutorial-examples/
[4] yt-dlp (Linux 和 MacOS 版本，要設定「chmod +x yt-dlp」，MacOS 也要改成 yt-dlp)
- Windows: https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe
- Linux: https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp
- MacOS: https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos
[5] ffmpeg
- Windows: https://www.gyan.dev/ffmpeg/builds/
- Linux: https://ffmpeg.org/download.html#build-linux
- MacOS: https://ffmpeg.org/download.html#build-mac
'''

import subprocess, os, wget, zipfile
from pprint import pprint





'''
下載路徑相關設定 (本案例為 Windows 10 環境，作業系統不同的話，設定也要不同)
'''
# 工具下載路徑 (建議放在帳號權限最大的地方，同時確認是否有該路徑)
path_tools_download = r'C:/Users/Owner/Desktop'

# 影片存放路徑 (建議放在帳號權限最大的地方，同時確認是否有該路徑)
path_save_output_video_to = r'C:/Users/Owner/Desktop'

# 建立 yt-dlp 資料夾存放路徑
path_tools_yt = f'{path_tools_download}/yt'
if not os.path.exists(path_tools_yt):
    os.makedirs(path_tools_yt)

# 工具下載路徑
download_url_yt_dlp = 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe'
download_url_ffmpeg_zip = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip'

# yt-dlp 存放路徑
path_yt_dlp = f'{path_tools_yt}/yt-dlp.exe'

# ffmpeg 存放路徑
path_ffmpeg_folder = f'{path_tools_download}/ffmpeg'
path_ffmpeg_zip = f'{path_tools_download}/ffmpeg.zip'
path_ffmpeg = rf'{path_ffmpeg_folder}/bin/ffmpeg.exe'





'''
判斷工具是否已經下載
'''
# True 代表已經下載過，跳過工具下載，直接剪輯影片，沒有工具會報錯；反之則加入下載工具流程
has_tools = False

# 若 has_tools 為 False，代表沒有工具，則自動下載
if not has_tools:
    # 下載 yt-dlp
    if not os.path.exists(path_yt_dlp):
        wget.download(download_url_yt_dlp, path_yt_dlp)

    # 下載 ffmpeg
    if not os.path.exists(path_ffmpeg_zip):
        wget.download(download_url_ffmpeg_zip, path_ffmpeg_zip)

    # 對 ffmpeg 解壓縮 至 指定路徑
    if not os.path.exists(path_ffmpeg_folder):
        with zipfile.ZipFile(path_ffmpeg_zip, 'r') as zf:
            # 解壓縮
            zf.extractall(path=f'{path_tools_download}')

            # 取得解壓縮後的資料夾名稱
            path_source_folder_name = f'{path_tools_download}/{zf.namelist()[0].split("/")[0]}'

            # 更改資料夾名稱
            os.rename(path_source_folder_name, path_ffmpeg_folder)





'''
影片下載
'''
# 設定 YouTube 影片 id 和 video 連結
video_id = 'xwEzl1X_LNE'
video_url = f'https://www.youtube.com/watch?v={video_id}'
'''
備註:
Facebook 的 video 也可以用

例如:
video_id = '493899461941993'
video_url = f'https://www.facebook.com/ithomeonline/videos/{video_id}'
'''
# 設定下載影片指令
cmd = [
    path_yt_dlp,
    video_url,
    '-f', 'b[ext=mp4]', 
    '-o', f'{path_save_output_video_to}/%(id)s.%(ext)s'
]

# 執行指令，並取得輸出訊息
output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print("下載影片的輸出訊息:")
pprint(output.stdout.decode('utf-8'))
print()





'''
影像處理
'''
# 輸出切割後的影片檔案名稱
file_name = 'output'

# 設定影片切割的開始時間 (記得自己先看過)
ss = '00:03:30.00'


# # 切割影片 方式1 (設定持續時間，意思是從 ss 開始往後多少時間，速度快)
# duration = '00:00:29.00' # 或是直接寫秒數，例如 29
# cmd = [
#     path_ffmpeg,
#     '-ss', ss, 
#     '-i', f'{path_save_output_video_to}/{video_id}.mp4', 
#     '-t', duration,
#     '-y', 
#     '-c', 'copy', 
#     rf'{path_save_output_video_to}/{file_name}.mp4'
# ]

# 切割影片 方式2 (準確指定結束時間，就是真的從 ss 看到 to，速度慢)
to = '00:04:00.00' 
cmd = [
    path_ffmpeg, 
    '-i', f'{path_save_output_video_to}/{video_id}.mp4', 
    '-ss', ss, 
    '-to', to,
    '-y', 
    '-c', 'copy', 
    rf'{path_save_output_video_to}/{file_name}.mp4'
]

# 執行指令
output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print("切割影片的輸出訊息:")
pprint(output.stdout.decode('utf-8'))
print()

# 刪除原始影片檔案
os.remove(f'{path_save_output_video_to}/{video_id}.mp4')