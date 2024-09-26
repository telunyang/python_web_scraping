# ComfyUI
[連結](https://github.com/comfyanonymous/ComfyUI)

## 安裝套件
- PyTorch - CPU only
  `pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cpu`

## 下載連結 for Windows
- 需要安裝 7zip 壓縮工具: [連結](https://www.7-zip.org/)
- [版本一覽](https://github.com/comfyanonymous/ComfyUI/releases)
  - [直接下載](https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI_windows_portable_nvidia.7z)

## 參考網頁
- [教你如何在 Windows 中安裝 Stable Diffusion，目前最簡單的運行方式](https://today.line.me/tw/v2/article/5yR9OBE)
- [Stable Diffusion 台灣社群v2](https://www.facebook.com/groups/sdaitw)

## 啟用服務
- 對 `ComfyUI_windows_portable\run_cpu.bat` 點兩下

## 基本設定與操作
- 下載模型
  - [Stable Diffusion XL Base 1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/tree/main)
    - 下載 `sd_xl_base_1.0.safetensors`
  - [Stable Diffusion XL Refiner 1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/tree/main)
    - 下載 `sd_xl_refiner_1.0.safetensors`
  - [SDXL-VAE](https://huggingface.co/stabilityai/sdxl-vae/tree/main)
    - 下載 `sdxl_vae.safetensors`
- 預設路徑
  - 下載 base 和 refiner 模型: `ComfyUI_windows_portable\ComfyUI\models\checkpoints`
    - 裡面會有 `sd_xl_base_1.0.safetensors` 和 `sd_xl_refiner_1.0.safetensors`
  - 下載 VAE 模型權重: `ComfyUI_windows_portable\ComfyUI\models\vae`
    - 裡面會有 `sdxl_vae.safetensors`
  - 如果有其它種類的模型，請依種類來放置模型: `ComfyUI_windows_portable\ComfyUI\models\*`
- 生成圖片

## 從 civitai 尋找合適的模型來下載
  - 按下選單上的 `Model` 連結
  - 選擇 `BASE MODEL` (其它的也可以)
  - 在顯示的列表中，選擇圖卡左上方有寫 `Checkpoint` 字眼，例如 [Speciosa Realistica](https://civitai.com/models/488361/speciosa-realistica)
  - 在頁面右側，有個 `Download (6.46 GB)`，按下即可下載 `safetensors` 檔案
  - 將 `safetensors` 檔案，放到 `ComfyUI_windows_portable\ComfyUI\models\checkpoints` 當中
  - 刷新 ComfyUI 畫面，就可以在 `Load Checkpoint` 底下的 `ckpt_name` 選單中看到新的模型了
  - 點一下範例圖片後，可以看到生成圖片的 prompt 或 negative prompt，還有一些參數可以調整