import torch
from diffusers.schedulers import EulerDiscreteScheduler
from diffusers.pipelines import StableDiffusionPipeline
from translate import Translator

translator = Translator(from_lang="ko",to_lang="en")

model_id = "stabilityai/stable-diffusion-2"

def generate_images(text):
  scheduler = EulerDiscreteScheduler.from_pretrained(model_id,subfolder="scheduler")
  pipe=StableDiffusionPipeline.from_pretrained(model_id,scheduler=scheduler,revision="fp16",torch_dtype=torch.float16)
  pipe = pipe.to("cuda")
  print(text)
  translation = translator.translate(text)
  print(translation)

  image = pipe(translation, height=768,width=768).images[0]

  return image

text = input("한글 텍스트를 입력하세요.")
generate_images(text)