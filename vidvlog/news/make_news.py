from news import criar_imagem_noticia as cin
from video_news import create_video_news as cvn
from make_voice import create_audio_voice as cav 
#from dotenv import load_dotenv
#import os


def create_news(file_news,
                title,
                text,
                path_bg,
                path_img,
                path_song,
                json_eleven
                ):

    api_key, voice_id = json_eleven['api_eleven'],json_eleven['voice_id']
    
    voice_path = cav(title+" "+text,'voice.mp3',
                     api_key=api_key,
                     voice_id=voice_id)
    
    img_news = cin(title,text,path_bg,path_img,'news.png')
    video_news = cvn(file_news,img_news,voice_path,path_song)
    
    return video_news


'''
create_news('/sdcard/news.mp4','testando',
    'eu estou testando essa catapimba,\n que estou fazendo no colegio',
            'news.png',
            'bg2_philo.jpg',
            'push_me.m4a',json_eleven)
'''
