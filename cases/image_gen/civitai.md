# Civitai
- [連結](https://civitai.com/)
  - 選擇 Featured Models，最右有 Explore all models 的連結。
  - 在預覽圖上，右上角有類似一支筆 (Create 按鈕)，就可以點進去看。
  - 進入內頁後，可以看到預覽器的右上角有一個 Create 按鈕，點下去就會在左側出現設定的地方。
  - 生成圖片前，參考以下範例的 Prompt 與 Negative Prompt，將它們貼到左側的設定區域。
  - 也可以在網頁最上方的搜尋欄，選擇 Models，輸入 CN，可以找到東方臉孔的模型輸出結果。

## Stable Diffusion 提示詞 (prompt) 參考資料
- [PormptHero](https://prompthero.com/)
  - 選上方連結 [Stable Diffusion](https://prompthero.com/stable-diffusion-prompts)，尋找偏好的圖片，點進去參考它們的設定
  - [Prompt 與 Negative prompt](https://prompthero.com/prompt/7fc0b9928fb-stable-diffusion-xl-base-0-9-playtime-s-over)

## 範例
Prompt:
```
(masterpiece, best quality:1.2<),highly detailed,extremely detailed,real photo,
fullbody,1girl,solo,asian,looking at viewer,(body facing viewer:1.2)(relax sitting),knees separation,
red lips,brown long hair,
collared shirt and dress shirt,long sleeves,(knees length dress:1.1),
(wrap hip very thick pantyhose:1.1),color high heels,
nice figure,good anatomy,good proportions,nice pose,(2shoes,2legs:1.2)(perfect legs:1.1),nice hand,
outdoors,buildings,photorealistic,realistic,<lora:more_details:0.4>,
<lora:yuzuv10:0.5>,<lora:sit_cross_leg_v2:0.6>,<lora:control_skin_exposure:-1.0>
```
```
a chinese young lady lying of a pink wall with a bow tie on it's chest and a pink and white top, white shorts, sunny, a screenshot, aestheticism, movie style, studio lighting, movie cinematic,  horizon,
1girl, solo, ,masterpiece, high quality, highres, absurdres, high details,8k,HDR,raw photo,realistic, bokeh, shallow depth of field, beautiful eyes, high detail eyes, beautiful face, high detail face, high detail skin, beautiful hands, beautiful fingers, beautiful eyelashes, fingernails,(above the thigh:1.6), pixie curly cut hair, lying down, hand reaching towards viewer,  big pink towel, white simple background
```

Negative Prompt:
```
bad anatomy, lowres, normal quality, grayscale, worstquality, watermark, bad proportions, out of focus, long neck, deformed, mutated, mutation, disfigured, poorly drawn face, skin blemishes, skin spots, acnes, missing limb, malformed limbs, floating limbs, disconnected limbs, extra limb, extra arms, mutated hands, poorly drawn hands, malformed hands, mutated hands and fingers, bad hands, missing fingers, fused fingers, too many fingers, extra legs, bad feet, cross-eyed, (distorted, :1.3) , (:1.4) , low quality, camera, BadDream, UnrealisticDream, bad-hands-5, BadNegAnatomyV1-neg, EasyNegative, FastNegativeV2, bad-picture-chill-75v
```

其它設定:
```
Steps: 30
Sampler: DPM++ 2M SDE Karras, 
CFG scale: 5
Seed: 2451060841
Size: 512x768
Model hash: e4a30e4607
Model: 麦橘写实_MajicMIX_Realistic_v6
Denoising strength: 0.35
Clip skip: 2
ADetailer model: face_yolov8n.pt
ADetailer prompt: asian girl, make up, beautiful face
ADetailer confidence: 0.3
ADetailer dilate/erode: 4
ADetailer mask blur: 4
ADetailer denoising strength: 0.4
ADetailer inpaint only masked: True
ADetailer inpaint padding: 0
ADetailer ControlNet model: control_v11p_sd15_inpaint [ebff9138]
ADetailer ControlNet module: inpaint_global_harmonious
ADetailer version: 23.7.6, 
Hires upscale: 2
Hires steps: 5
Hires upscaler: 4x-UltraSharp
Lora hashes:more_details: 3b8aa1d351ef, yuzuv10: b1464588227a, sit_cross_leg_v2: cb80e9bce437, control_skin_exposure: 58bbb7a04626
TI hashes: ng_deepnegative_v1_75t: 54e7e4826d53, negative_hand: 73b524a2da12, badhandv4: 5e40d722fc3d, negative_feet_v2: df90b1ff666d, EasyNegative: 66a7279a88dd
ControlNet 0: preprocessor: inpaint_global_harmonious, model: control_v11p_sd15_inpaint [ebff9138], weight: 1.0, starting/ending: (0.0, 1.0), resize mode: ResizeMode.INNER_FIT, pixel perfect: True, control mode: ControlMode.BALANCED, preprocessor params: (-1, -1, -1)
Version: v1.5.1
```