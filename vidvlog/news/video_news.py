from moviepy.editor import ImageClip, AudioFileClip, CompositeAudioClip

def create_video_news(file_video,
                      image_path = "sua_imagem.jpg",
                      voice_audio_path = "voz.mp3",
                      music_audio_path = "trilha_sonora.mp3",
                      time_add=5,
                      volumex=0.2
                      ):
    voice_audio = AudioFileClip(voice_audio_path)
    duration = voice_audio.duration
    video = ImageClip(image_path, duration=duration)
    music_audio = AudioFileClip(music_audio_path).subclip(0, duration+time_add).volumex(volumex)
    final_audio = CompositeAudioClip([voice_audio, music_audio])
    
    video = video.set_audio(final_audio)
    video.write_videofile(file_video,fps=24)
    return file_video
