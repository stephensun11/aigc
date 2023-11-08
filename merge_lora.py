from diffusers import StableDiffusionPipeline
import torch

lora_model_path = "diffusers/examples/text_to_image/baseline_512-lora_epoch9"
pipe = StableDiffusionPipeline.from_pretrained("/home/data/aigc/baseline", use_safetensors=True)
pipe.unet.load_attn_procs(lora_model_path)

pipe.unet.fuse_lora()

state = pipe.unet.state_dict()

torch.save(state, '/home/data/aigc/baseline/unet/diffusion_pytorch_model2.bin')



state1 = torch.load('/home/data/aigc/baseline/unet/diffusion_pytorch_model.bin', map_location='cpu')
state2 = torch.load('/home/data/aigc/baseline/unet/diffusion_pytorch_model2.bin', map_location='cpu')

import ipdb;ipdb.set_trace()
