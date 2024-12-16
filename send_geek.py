from vidvlog.news.make_news import create_news as cn
from dotenv import load_dotenv
import os

load_dotenv()

api_eleven = os.getenv("api_key1")
voice_id = "IKne3meq5aSn9XLyUdCD" #os.getenv("voice_id")

json_eleven = {"api_eleven":api_eleven,"voice_id":voice_id}




text_news = str(open("/sdcard/work/geek/public/news.txt","r").read())



cn(file_news="/sdcard/work/geek/public/news.mp4",
   title="Urgente!!",
   text=text_news,
   font="/sdcard/work/geek/geek.ttf",  
   path_bg="/sdcard/work/geek/geek_bg.jpg",
   path_img="/sdcard/work/geek/public/geek.jpg",
   path_song="/sdcard/work/geek/geek_song.m4a",
   json_eleven=json_eleven,
   time_add=2,
   volumex=0.1)





'''

cn(,'/sdcard/work/news/dist/news.mp4',
   'urgente!!',
   news_text,
   "/sdcard/work/news/news_bg.jpg","/sdcard/work/news/public/news.jpeg","/sdcard/work/news/news_song.m4a",json_eleven)'''
