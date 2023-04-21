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
[4] 下載 yt-dlp (Linux 和 MacOS 版本，要設定「chmod +x yt-dlp」，MacOS 也要改成 yt-dlp)
- GitHub: https://github.com/yt-dlp/yt-dlp
  - Windows: https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe
  - Linux: https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp
  - MacOS: https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos
[5] 下載 ffmpeg binary
- 網站: https://ffmpeg.org/download.html
  - Windows: https://www.gyan.dev/ffmpeg/builds/
  - Linux: https://ffmpeg.org/download.html#build-linux
  - MacOS: https://ffmpeg.org/download.html#build-mac



測試指令:

- 下載影片
  - Windows 10: ./yt-dlp.exe https://www.youtube.com/watch?v=zU93rvXBMOY -f "b[ext=mp4]" -o "%(id)s.%(ext)s"
  - MacOS: ./yt-dlp "https://www.youtube.com/watch?v=zU93rvXBMOY" -f "b[ext=mp4]" -o "%(id)s.%(ext)s"

- 切割影片 方式1 (設定持續時間，意思是從 ss 開始往後多少時間，速度快)
  - Windows 10: ./ffmpeg/bin/ffmpeg.exe -ss 00:00:02.00 -i =zU93rvXBMOY.mp4 -t 00:00:34.00 -y -c copy output.mp4
  - MacOS: ./ffmpeg -ss 00:00:02.00 -i =zU93rvXBMOY.mp4 -t 00:00:34.00 -y -c copy output.mp4

- 切割影片 方式2 (準確指定結束時間，就是真的從 ss 看到 to，速度慢)
  - Windows 10:./ffmpeg/bin/ffmpeg.exe -i =zU93rvXBMOY.mp4 -ss 00:00:02.00 -to 00:00:36.00 -y -c copy output.mp4
  - MacOS: ./ffmpeg -i =zU93rvXBMOY.mp4 -ss 00:00:02.00 -to 00:00:36.00 -y -c copy output.mp4

可能延伸應用:
[1] [nodejs] Youtube Video Downloader, Splitter and Converter (ubuntu, nodejs, socketio, ffmpeg)
https://youtu.be/2whO3-DBXkw
'''

import subprocess, os, wget, zipfile

'''
路徑設定
'''
# 工具下載路徑 (建議放在帳號權限最大的地方，同時確認是否有該路徑)
path_download = '.'

# 影片存放路徑 (建議放在帳號權限最大的地方，同時確認是否有該路徑)
path_output = '.'

'''
下載路徑相關設定
'''
# 工具下載路徑
download_url_yt_dlp = 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe'
download_url_ffmpeg_zip = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip'

# ffmpeg 工具資料夾存放路徑
path_ffmpeg_zip = f'{path_download}/ffmpeg.zip'
path_ffmpeg_folder = f'{path_download}/ffmpeg'

# ffmpeg 執行檔存放路徑
path_ffmpeg_exe = f'{path_download}/ffmpeg/bin/ffmpeg.exe'

# yt-dlp 存放路徑 (預設放在 ffmpeg/bin 底下)
path_yt_dlp_exe = f'{path_download}/ffmpeg/bin/yt-dlp.exe' 
# 註: MacOS: yt-dlp (可能需要給它可執行權限，例如用 subprocess 額外下指令) 

'''
手動設定
'''
# True 代表程式整體執行結束後，要刪除影音檔原始檔；反之則保留下來
delete_video = False

# 輸出切割後的影片檔案名稱
file_name = 'output'

# 副檔名
ext = 'mp4'

# 設定影片切割的開始時間 (一定要有) (記得自己先看過)
ss = '00:00:04.00'

'''
指令選擇方式
'''
# 選擇方式 1 或 2 (會影響執行程式的指令選擇)
choice = 1 

# 選擇方式 1: 連續播放時間
duration = '00:00:32.00' # 或是直接寫秒數，例如 29

# 選擇方式 2: 預期結束時間 (時間軸實際時間)
to = '00:00:36.00' 

# 設定 YouTube 影片 id 和 video 連結
video_id = 'zU93rvXBMOY'
video_url = f'https://www.youtube.com/watch?v={video_id}'

# Facebook 的 video 也可以用
# video_id = '493899461941993'
# video_url = f'https://www.facebook.com/ithomeonline/videos/{video_id}'

'''
下載工具
'''
# 確認 ffmpeg 資料夾是否存在，不存在就下載，並解壓縮
if not os.path.exists(path_ffmpeg_folder):
    # 下載 ffmpeg
    if not os.path.exists(path_ffmpeg_zip):
        print('[下載 ffmpeg]')
        wget.download(download_url_ffmpeg_zip, path_ffmpeg_zip)

    # 對 ffmpeg 解壓縮 至 指定路徑
    with zipfile.ZipFile(path_ffmpeg_zip, 'r') as zf:
        # 解壓縮
        print('[解壓縮 zip]')
        zf.extractall(path=f'{path_download}')

        # 取得解壓縮後的資料夾名稱
        path_source_folder_name = f'{path_download}/{zf.namelist()[0]}'

        # 更改資料夾名稱
        os.rename(path_source_folder_name, path_ffmpeg_folder)

# 下載 yt-dlp
if not os.path.exists(path_yt_dlp_exe):
    print('[下載 yt-dlp]')
    wget.download(download_url_yt_dlp, path_yt_dlp_exe)

'''
下載影片
'''
# 判斷影片是否已經下載
if not os.path.exists(f'{path_output}/{video_id}.mp4'):
    # 設定下載影片指令
    cmd = [
        path_yt_dlp_exe,
        video_url,
        '-f', f'w[ext={ext}]', 
        '-o', f'{path_output}/%(id)s.%(ext)s'
    ]

    # 執行指令，並取得輸出訊息
    print("[下載影片]")
    std_output = subprocess.run(cmd)
    if std_output.returncode == 0:
        print(f'成功')
    else:
        print(f'失敗')

'''
影像剪輯
'''
# 定義剪輯指令
if choice == 1: # 切割影片 方式1 (設定持續時間，意思是從 ss 開始往後多少時間，速度快)
    cmd = [
        path_ffmpeg_exe,
        '-ss', ss, '-i', f'{path_output}/{video_id}.{ext}', '-t', duration, 
        '-y', '-c', 'copy', 
        f'{path_output}/{file_name}.{ext}'
    ]
elif choice == 2: # 切割影片 方式2 (準確指定結束時間，就是真的從 ss 看到 to，速度慢)
    cmd = [
        path_ffmpeg_exe, '-i', f'{path_output}/{video_id}.{ext}', 
        '-ss', ss, '-to', to,'-y', '-c', 'copy', f'{path_output}/{file_name}.{ext}'
    ]

# 執行指令
print("[切割影片]")
std_output = subprocess.run(cmd)
if std_output.returncode == 0:
    print(f'成功')
else:
    print(f'失敗')

# 是否刪除原始影片檔案 (有些人只會留下剪完的影片，原始影片會刪掉)
if delete_video:
    print("[刪除來源影片]")
    os.remove(f'{path_output}/{video_id}.mp4')