from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
import torch
import string
import random
from datetime import datetime


def generate512x512(prompt):
    pipe = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-base",
        torch_dtype=torch.float16,
        revision="fp16"
    )
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(
        pipe.scheduler.config)
    pipe = pipe.to("cuda")

    image = pipe(prompt, num_inference_steps=50,
                 negative_prompt="blurry, bad, deformed, bad anatomy, ugly").images[0]

    dt = datetime.now()
    ts = datetime.timestamp(dt)
    randomString = ''.join(random.choices(string.ascii_lowercase, k=8))
    print("images/" + randomString + str(int(ts)) + '.png')
    image.save("images/" + randomString + str(int(ts)) + '.png')


def generate768x768(prompt):
    pipe = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2",
        torch_dtype=torch.float16,
        revision="fp16"
    )
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(
        pipe.scheduler.config)
    pipe = pipe.to("cuda")

    image = pipe(prompt, guidance_scale=9, num_inference_steps=50,
                 negative_prompt="blurry, bad, deformed, bad anatomy, ugly").images[0]

    dt = datetime.now()
    ts = datetime.timestamp(dt)
    randomString = ''.join(random.choices(string.ascii_lowercase, k=8))

    image.save("images/" + randomString + str(int(ts)) + '.png')


if __name__ == "__main__":
    # generate512x512('cat playing with a ball')
    generate512x512(
        'Music single cover image for a song called "we all make mistakes" that talks about love and pain')
