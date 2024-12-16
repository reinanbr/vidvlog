from vidvlog.news.make_news import create_news as cn
from dotenv import load_dotenv
import os

load_dotenv()

api_eleven = os.getenv("api_key1")
voice_id = "IKne3meq5aSn9XLyUdCD" #os.getenv("voice_id")

json_eleven = {"api_eleven":api_eleven,"voice_id":voice_id}




text_news = str(open("/sdcard/work/dev/public/news.txt","r").read())



cn(file_news="/sdcard/work/dev/public/news.mp4",
   title="Urgente!!",
   text=text_news,
   font="/sdcard/work/dev/dev.ttf",  
   path_bg="/sdcard/work/dev/dev_bg.jpg",
   path_img="/sdcard/work/dev/public/news.jpg",
   path_song="/sdcard/work/dev/dev_song.m4a",
   json_eleven=json_eleven,time_add=2)





'''

cn(,'/sdcard/work/news/dist/news.mp4',
   'urgente!!',
   news_text,
   "/sdcard/work/news/news_bg.jpg","/sdcard/work/news/public/news.jpeg","/sdcard/work/news/news_song.m4a",json_eleven)
'''
