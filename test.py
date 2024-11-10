from moviepy.editor import *
import moviepy.editor as mp
import os

from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": "/usr/bin/convert"})
os.environ["IMAGEMAGICK_BINARY"] = "/usr/bin/convert"  # Adjust path if needed

#mp.config.change_settings({"IMAGEMAGICK_BINARY": "/usr/bin/convert"})  # Adjust the path accordingly



# Definir os arquivos
fundo_imagem = 'bg.jpg'
foto_pessoa = 'image.jpg'
musica = 'music.mp3'
nome_pessoa = 'Jo da Silva'
caminho_fonte = 'buller.otf'  # Caminho para a fonte no diretório

# Criar o clip de fundo
fundo = ImageClip(fundo_imagem)
fundo = fundo.resize((800, 900))  # Ajusta para resolução de vídeo

# Criar o clip da foto da pessoa
foto = ImageClip(foto_pessoa)
foto = foto.resize((600, 600)).set_position(('center', 'center')).set_duration(5)

# Criar o texto com o nome da pessoa e fundo branco
texto_nome = TextClip(nome_pessoa, fontsize=70, font=caminho_fonte, color='black', bg_color='white', size=(800, 90))
texto_nome = texto_nome.set_position(('right', 'top'), relative=True).set_duration(5)

# Carregar a música de fundo
musica_bkg = AudioFileClip(musica).subclip(0, 5)  # Ajuste para a duração do vídeo

# Juntar tudo em um único clipe
video = CompositeVideoClip([fundo, foto, texto_nome])

# Definir a música de fundo
video = video.set_audio(musica_bkg)

# Definir a duração total do vídeo
video = video.set_duration(5)

# Salvar o vídeo final
video.write_videofile('video_final.mp4', fps=24)

