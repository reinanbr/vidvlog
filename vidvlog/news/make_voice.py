import requests

def create_audio_voice(text,file_audio,
                       api_key,
                       voice_id,
                       similarity_boost=0.7,
                       style=0.7):
   text = ' '.join(text.split("\n"))
    # Configurações
   CHUNK_SIZE = 1024
   api_key = 'sk_6d223452ee732508dd444cf2c32f556164ea5fa7422605fd'
   voice_id = 'bIHbv24MWmeRgasZH58o'
   #text = "Tipo, é louco saber que as coisas que constituem a matéria, são tão, foluvéis.."
   
   # Endpoint da API para geração de voz
   url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
   
   # Cabeçalho e dados da requisição
   headers = {
       'xi-api-key': api_key,
       'Content-Type': 'application/json',
       'Accept': 'audio/mpeg',
   }
   
   data = {
       "text": text,
       "model_id": "eleven_multilingual_v2",
       "voice_settings": {
           "stability": 0.8,
           "similarity_boost": 0.7,
           "style": 0.7,
           "use_speaker_boost": True
       },
       "language_id": "pt-br"
   }
   
   # Solicitação de geração de áudio
   response = requests.post(url, headers=headers, json=data)
   
   # Salvar o áudio gerado
   if response.status_code == 200:
       with open(file_audio, "wb") as f:
           #f.write(response.content)
           for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
               if chunk:
                   f.write(chunk)
       print("Áudio gerado com sucesso!")
       return file_audio
   else:
       print(f"Erro ao gerar áudio: {response.status_code} - {response.text}")
       return 0
   
