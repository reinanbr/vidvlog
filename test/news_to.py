from make_news import create_news as cn
from dotenv import load_dotenv
import os

load_dotenv()

api_eleven = os.getenv("api_eleven")
voice_id = os.getenv("voice_id")

json_eleven = {"api_eleven":api_eleven,"voice_id":voice_id}

cn('/sdcard/news.mp4','urgente!!',
   "fulano, irmão de ciclano,\nmorreu com um pirulito","bg3.jpg","news.png","push_me.m4a",json_eleven)
