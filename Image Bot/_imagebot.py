import torch
from diffusers import StableDiffusionPipeline
from datetime import datetime
import os

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")
pipe = pipe.to(device)


now = datetime.now()
current_time = now.strftime("%H.%M.%S")

chars = set('#%&\{\}\\<>*?/$!\'\":@+`|=')

while True:
    
    prompt = input("Enter Prompt: ")
    
    if any((c in chars) for c in prompt):
        
        print('Error, please avoid using these characters in your prompt:\n # % & \{ \} \\ < > * ? / $ ! \' \" : @ + ` | =')
    else:
        
        image = pipe(prompt).images[0]  
            
        image.save(str(prompt) + " - " + str(current_time) + ".png")
        image.save("_recent.png")

        now = datetime.now()
        current_time = now.strftime("%H.%M.%S")
