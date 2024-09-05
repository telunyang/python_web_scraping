'''
# 安裝 PyTorch - CPU only
pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cpu

# 安裝其它
pip install transformers accelerate numpy sentencepiece protobuf

# Flux GitHub
https://github.com/black-forest-labs/flux

# 安裝 diffusers
pip install git+https://github.com/huggingface/diffusers.git
'''

import torch
from diffusers import FluxPipeline
from time import time

t1 = time()

model_id = "black-forest-labs/FLUX.1-schnell" # you can also use `black-forest-labs/FLUX.1-dev`

pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell", torch_dtype=torch.bfloat16) # torch.bfloat16
pipe.enable_model_cpu_offload() # save some VRAM by offloading the model to CPU. Remove this if you have enough GPU power

prompt = "A cat holding a sign that says hello world"
seed = 42
image = pipe(
    prompt,
    output_type="pil",
    num_inference_steps=4, # use a larger number if you are using [dev]
    generator=torch.Generator("cpu").manual_seed(seed)
).images[0]
image.save("./flux-schnell.png")

t2 = time()

print(f"Time taken: {t2-t1:.4f} seconds")