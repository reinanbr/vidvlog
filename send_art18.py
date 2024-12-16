from vidvlog.art18.make_video_actress import create_video
from datetime import datetime as dt
    
atrizes = ["kesha ortega","ava adams","eva notty","alexis texas"]

dir = "/sdcard/Download/"
now = dt.now()
name_video = now.strftime("video_%m_%d_%Y__%H_%M_%S_.mp4")
print(name_video)
create_video(atrizes,dir+name_video,image_time=2.5)

