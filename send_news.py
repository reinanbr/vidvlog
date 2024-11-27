from make_news import create_news as cn
from dotenv import load_dotenv
import os

load_dotenv()

api_eleven = os.getenv("api_eleven")
voice_id = os.getenv("voice_id")

json_eleven = {"api_eleven":api_eleven,"voice_id":voice_id}

cn('/sdcard/work/news/public/news.mp4','urgente!!',
   "O presidente da Câmara, Arthur Lira (PP-AL),\n vai se reunir com deputados da Frente \nParlamentar da Agropecuária (FPA) nesta terça-feira (26).\nO encontro ocorre em meio à crise envolvendo \na rede de supermercados francesa Carrefour e a compra de \ncarnes produzidas por países do Mercosul.",
   "/sdcard/work/news/news_bg.jpg","/sdcard/work/news/public/news.jpeg","/sdcard/work/news/news_song.m4a",json_eleven)
