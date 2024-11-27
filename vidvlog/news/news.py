from PIL import Image, ImageDraw, ImageFont

def criar_imagem_noticia(titulo, noticia, caminho_fundo, caminho_imagem, saida):
    # Abrir a imagem de fundo
    imagem_final = Image.open(caminho_fundo).convert("RGB")
    imagem_final = imagem_final.resize((900,1600))
    largura, altura = imagem_final.size

    # Configurações de texto
    cor_texto = (0, 0, 0)  # Preto
    cor_fundo_caixa = (255, 255, 255)  # Branco
    draw = ImageDraw.Draw(imagem_final)

    # Fonte para o título e notícia
    try:
        print('peguei aqui')
        fonte_titulo = ImageFont.truetype("quiva.ttf", 60)
        fonte_noticia = ImageFont.truetype("quiva.ttf", 30)
    except:
        fonte_titulo = ImageFont.load_default()
        fonte_noticia = ImageFont.load_default()

    # Adicionar caixa e título
    largura_texto, altura_texto = draw.textbbox((0, 0), titulo, font=fonte_titulo)[2:]
    posicao_titulo = ((largura - largura_texto) // 2, altura // 14)
    caixa_titulo = [
        posicao_titulo[0] - 10, posicao_titulo[1] - 5,
        posicao_titulo[0] + largura_texto + 10, posicao_titulo[1] + altura_texto + 5
    ]
    draw.rectangle(caixa_titulo, fill=cor_fundo_caixa)
    draw.text(posicao_titulo, titulo, fill=cor_texto, font=fonte_titulo)

    # Adicionar caixa e notícia abaixo do título
    largura_noticia, altura_noticia = draw.textbbox((0, 0), noticia, font=fonte_noticia)[2:]
    posicao_noticia = ((largura - largura_noticia) // 2, altura // 10 + altura_texto + 20)
    caixa_noticia = [
        posicao_noticia[0] - 10, posicao_noticia[1] - 5,
        posicao_noticia[0] + largura_noticia + 10, posicao_noticia[1] + altura_noticia + 5
    ]
    draw.rectangle(caixa_noticia, fill=cor_fundo_caixa)
    draw.text(posicao_noticia, noticia, fill=cor_texto, font=fonte_noticia)

    # Abrir a imagem central
    imagem_central = Image.open(caminho_imagem).convert("RGBA")

    # Redimensionar a imagem central proporcionalmente
    proporcao = min((largura - 100) / imagem_central.width, (altura // 2) / imagem_central.height)
    nova_largura = int(imagem_central.width * proporcao)
    nova_altura = int(imagem_central.height * proporcao)
    imagem_central = imagem_central.resize((nova_largura, nova_altura), Image.LANCZOS)

    # Criar máscara para preservar transparência
    if imagem_central.mode != "RGBA":
        imagem_central = imagem_central.convert("RGBA")
    
    mascara = imagem_central.split()[3]  # Canal alpha

    # Posicionar a imagem central
    posicao_central = ((largura - nova_largura) // 2, (altura - nova_altura) // 2)
    imagem_final.paste(imagem_central, posicao_central, mask=mascara)

    # Salvar a imagem final
    imagem_final.save(saida)
    return saida



# Exemplo de uso
'''criar_imagem_noticia(
    titulo="Notícia de Última Hora",
    noticia="Esta é a descrição da notícia que será exibida abaixo do título.\nentão vamos ver se vai assim..",
    caminho_fundo="/sdcard/bg/bg2_philo.jpg",
    caminho_imagem="bg3.jpg",
    saida="/sdcard/noticia.png"
)'''

