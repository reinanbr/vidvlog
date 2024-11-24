from vidvlog.art18.make_video_actress import create_video
import random
from datetime import datetime as dt




def make_video():
    all_actriz = []
    with open('list_actriz.txt','r') as text:
        actress = text.read()

    all_actriz = actress.split('\n')

    with open('past_actriz.txt','r') as text_past:
        actriz_past = text_past.read()

    actriz_pst = actriz_past.split('\n')[:2000]
    for actrizp in actriz_pst:
#        all_actriz.remove('Siri')
#        all_actriz.remove('Natalia')
        all_actriz.remove(actrizp)
    #print(actriz_pst[0])
    actriz_now = []

    #print(len(all_actriz))
    #print(actriz_pst)
    actriz_now = []
    for i in range(5):
    #    print(name)
        name = random.choice(all_actriz)
        print(i,name)
        if (name in actriz_now) or (name in actriz_pst):
            print(f"'{name}' jah foi! Escolhendo outra...")
            all_actriz.remove(name)
            name = random.choice(all_actriz)
            print(f"a escolhida foi '{name}'")
        print(f"'{name}' estah sendo adicionado...")
        actriz_now.append(name)

    with open('past_actriz.txt','a+') as text_past:
        for actriz in actriz_now:
            text_past.writelines(actriz+'\n')


    dir = "/sdcard/Download/"
    now = dt.now()
    name_video = now.strftime("video_%m_%d_%Y__%H_%M_%S_.mp4")
    print(name_video)
    create_video(actriz_now,dir+name_video,image_time=2.5)
#create_video(all_actriz[10:20],'now_video.mp4',image_time=2.5)
    return dir+name_video

for i in range(10):
    print("=+="*10,f"[making video {i}]","=+="*10)
    
    make_video()

