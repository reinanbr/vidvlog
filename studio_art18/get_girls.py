from vidvlog.art18.make_video_actress import create_video
import random

all_actriz = []
with open('list_actriz.txt','r') as text:
    actress = text.read()

with open('past_actriz.txt','r') as text_pst:
    actriz_past = text_pst.read()

all_actriz = actress.split('\n')[:-1]


'''
actriz_pst = actriz_past.split('\n')[:-1]
with open('past_actriz.txt','r') as text_pst:
    actriz_past = text_pst.read()
actriz_now = []
for i in range(5):
    name = random.choice(all_actriz)
    if name in actriz_now or name in actriz_pst:
        all_actriz.remove(name)
        name = random.choice(all_actriz)
    actriz_now.append(name)

with open('past_actriz.txt','a+') as text_past:
    for actriz in actriz_now:
        text_past.writelines(actriz+'\n')

'''

create_video(all_actriz[:10],'now_video.mp4')
