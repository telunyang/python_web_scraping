'''
執行環境: Windows 10

套件安裝
$ pip install wget

參考網頁
[1] How to download portion of video with youtube-dl command?
https://unix.stackexchange.com/questions/230481/how-to-download-portion-of-video-with-youtube-dl-command
[2] FFmpeg: Seeking
https://trac.ffmpeg.org/wiki/Seeking
[3] Python 使用 zipfile 模組壓縮、解壓縮 ZIP 檔案教學與範例
https://officeguide.cc/python-zipfile-module-compression-decompression-tutorial-examples/



下載 yt-dlp (Linux 和 MacOS 版本，要設定「chmod +x yt-dlp」，MacOS 也要改成 yt-dlp)
- Windows: https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe
- Linux: https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp
- MacOS: https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos

下載 ffmpeg
- Windows: https://www.gyan.dev/ffmpeg/builds/
- Linux: https://ffmpeg.org/download.html#build-linux
- MacOS: https://ffmpeg.org/download.html#build-mac
'''

import subprocess, os, wget, zipfile
from pprint import pprint



# 是否已經下載工具 (True 代表已經下載過，跳過工具下載，直接剪輯片，反正則加入下載工具流程)
has_tools = False

# 工具下載路徑 (建議放在帳號權限最大的地方，同時確認是否有該路徑)
path_tmp_files = r'C:/Users/Owner/Desktop'

# 影片存放路徑 (建議放在帳號權限最大的地方，同時確認是否有該路徑)
path_save_output_video_to = r'C:/Users/Owner/Desktop'




# 建立 yt-dlp 資料夾存放路徑
path_tools_yt = 'yt'
if not os.path.exists(f'{path_tmp_files}/{path_tools_yt}'):
    os.makedirs(f'{path_tmp_files}/{path_tools_yt}')

# 若 has_tools 為 False，代表沒有工具，則自動下載
if not has_tools:
    # 下載 yt-dlp
    download_url = 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe'
    path_yt_dlp = f'{path_tmp_files}/{path_tools_yt}/yt-dlp.exe'
    if not os.path.exists(path_yt_dlp):
        wget.download(download_url, path_yt_dlp)

    # 下載 ffmpeg
    download_url = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip'
    path_ffmpeg_zip = f'{path_tmp_files}/ffmpeg.zip'
    if not os.path.exists(path_ffmpeg_zip):
        wget.download(download_url, f'{path_tmp_files}/ffmpeg.zip')

    # 對 ffmpeg 解壓縮 至 指定路徑
    if not os.path.exists(f'{path_tmp_files}/ffmpeg'):
        with zipfile.ZipFile(path_ffmpeg_zip, 'r') as zf:
            # 解壓縮
            zf.extractall(path=f'{path_tmp_files}')

            # 取得解壓縮後的資料夾名稱
            path_source_folder_name = f'{path_tmp_files}/{zf.namelist()[0].split("/")[0]}'
            path_destination_folder_name = f'{path_tmp_files}/ffmpeg'

            # 更改資料夾名稱
            os.rename(path_source_folder_name, path_destination_folder_name)

    # 刪除檔案
    os.remove(f'{path_tmp_files}/ffmpeg.zip')





# 設定影片 id
# video_id = '493899461941993'
video_id = 'xwEzl1X_LNE'

# yt-dlp 和 ffmpeg 執行檔存放路徑
yt_path = rf'{path_tmp_files}/{path_tools_yt}/yt-dlp.exe'
ffmpeg_path = rf'{path_tmp_files}/ffmpeg/bin/ffmpeg.exe'

# 設定 video 下載連結
# video_url = f'https://www.facebook.com/ithomeonline/videos/{video_id}'
video_url = f'https://www.youtube.com/watch?v={video_id}'

# 執行下載影片指令
cmd = [
    yt_path,
    video_url,
    '-f', 'b[ext=mp4]', 
    '-o', f'{path_save_output_video_to}/%(id)s.%(ext)s'
]
output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
pprint(output.stdout.decode('utf-8'))

# 自訂設定
file_name = 'output'
ss = '00:03:30.00'

# 切割影片 (設定持續時間，意思是從 ss 開始往後多少時間，速度快)
# duration = '00:00:29.00'
# cmd = [
#     ffmpeg_path,
#     '-ss', ss, 
#     '-i', f'{path_save_to}/{video_id}.mp4', 
#     '-t', duration,
#     '-y', 
#     '-c', 'copy', 
#     rf'{path_save_output_video_to}/{file_name}.mp4'
# ]

# 切割影片 (準確指定結束時間，速度慢)
to = '00:04:00.00'
cmd = [
    ffmpeg_path, 
    '-i', f'{path_save_output_video_to}/{video_id}.mp4', 
    '-ss', ss, 
    '-to', to,
    '-y', 
    '-c', 'copy', 
    rf'{path_save_output_video_to}/{file_name}.mp4'
]
output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
pprint(output.stdout.decode('utf-8'))

# 刪除檔案
os.remove(f'{path_save_output_video_to}/{video_id}.mp4')