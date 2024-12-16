from vidvlog.news.make_news import create_news as cn
from dotenv import load_dotenv
import os

load_dotenv()

api_eleven = os.getenv("api_key1")
voice_id = "Xb7hH8MSUJpSbSDYk0k2" #laura #os.getenv("voice_id")

json_eleven = {"api_eleven":api_eleven,"voice_id":voice_id}




text_news = str(open("/sdcard/work/fofoca/public/fofoca.txt","r").read())



cn(file_news="/sdcard/work/fofoca/public/fofoca.mp4",
   title="Urgente!!",
   text=text_news,
   font="/sdcard/work/news/quiva.ttf",  
   path_bg="/sdcard/work/fofoca/fofoca_bg.jpg",
   path_img="/sdcard/work/fofoca/public/fofoca.jpg",
   path_song="/sdcard/work/fofoca/fofoca_song.m4a",
   json_eleven=json_eleven)





'''

cn(,'/sdcard/work/news/dist/news.mp4',
   'urgente!!',
   news_text,
   "/sdcard/work/news/news_bg.jpg","/sdcard/work/news/public/news.jpeg","/sdcard/work/news/news_song.m4a",json_eleven)
'''
