import pandas as pd
import json, os
import random
import shutil
import torch

def sampleImage(df):
    prefix = '/home/data/aigc/images/'

    sample = df.sample(1)

    filename = sample.file_name.values[0]
    text = sample.texts.values[0]

    shutil.copy(prefix + filename, '/DATA/bvac/personal/competitions/aigc/0.png')
    print(text)
    
    
# df = pd.read_csv('/home/data/aigc/images/metadata.csv')

# sampleImage(df)


from diffusers import StableDiffusionPipeline
import torch

lora_model_path = "diffusers/examples/text_to_image/baseline_512-lora"
pipe = StableDiffusionPipeline.from_pretrained("/home/data/aigc/match-weight", torch_dtype=torch.float16, use_safetensors=True)
pipe.unet.load_attn_procs(lora_model_path)
pipe.to("cuda:3")


prompt = "比尔·佩恩(Bill Payne)在一辆福特Fusion的帽子下提供一张眼镜."
image = pipe(prompt, num_inference_steps=30, guidance_scale=7.5).images[0]
image.save("/DATA/bvac/personal/competitions/aigc/0.png")


import ipdb;ipdb.set_trace()