from moviepy import *
import moviepy.editor as mpy
from vidvlog.art18.painel_actriz import create_painel_actriz as cpa
import numpy as np
import os
from PIL import Image


def create_video_actriz(actriz,path_video='actriz.mp4',limit_photos=10,image_time=2,dir='.data'):
    if not os.path.isdir(dir):
        os.mkdir(dir)
    dir_dataset = f"{dir}/dataset"
    if not os.path.isdir(dir_dataset):
        os.mkdir(dir_dataset)
    images_actress = []
    path_img_list = cpa(actriz,f'{dir}/actriz_{actriz}_%(i)d.jpg',limit=limit_photos,dir_dataset=dir_dataset)
    print(path_img_list)
    for path_img in path_img_list:
     #   print(path_img)
        img = Image.open(path_img)
        images_actress.append(img)
    clips = []
    for img in images_actress:
        clip = mpy.ImageClip(np.array(img))
        clip = clip.set_duration(image_time)  
        clips.append(clip)
    video = mpy.concatenate_videoclips(clips, method="compose")
    audio = mpy.AudioFileClip("push_me.m4a")
    audio_time = image_time*limit_photos
    print(audio_time)
    audio = audio.set_duration(audio_time)
    video = video.set_audio(audio)
    video.write_videofile(path_video, codec="libx264", fps=24)
    return path_video



