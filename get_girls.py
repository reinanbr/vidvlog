from vidvlog.art18.make_video_actress import create_video
import random

all_actriz = []
with open('list_actriz.txt','r') as text:
    actress = text.read()

all_actriz = actress.split('\n')[:-1]


'''
actriz_pst = actriz_past.split('\n')[:-1]
with open('past_actriz.txt','r') as text_pst:
    actriz_past = text_pst.read()
actriz_now = []

'''

actriz_now = []
for i in range(10):
    name = random.choice(all_actriz[:100])
    if name in actriz_now:
        all_actriz.remove(name)
        name = random.choice(all_actriz[:200])
    actriz_now.append(name)

'''
with open('past_actriz.txt','a+') as text_past:
    for actriz in actriz_now:
        text_past.writelines(actriz+'\n')
'''


create_video(actriz_now,'rand.mp4',image_time=2.5)
#create_video(all_actriz[10:20],'now_video.mp4',image_time=2.5)
