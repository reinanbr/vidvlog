from PIL import Image, ImageDraw, ImageFont

# Função para criar a imagem
def create_image(background_path, overlay_image_path, name,path_img, font_path):
    # Carregar a imagem de fundo
    background = Image.open(background_path)
    background = background.resize((800, 900))  # Redimensiona a imagem de fundo

    # Carregar a imagem que vai sobrepor
    overlay_image = Image.open(overlay_image_path)
    overlay_image = overlay_image.resize((600, 700))  # Redimensiona a imagem de sobreposição

    # Posição para colocar a imagem sobreposta
    position = (100, 150)  # Você pode ajustar a posição conforme necessário
    background.paste(overlay_image, position)

    # Adicionar o nome no canto superior da imagem sobreposta
    draw = ImageDraw.Draw(background)

    # Carregar a fonte
    font = ImageFont.truetype(font_path, 80)  # Ajuste o tamanho da fonte conforme necessário

    # Usar textbbox para calcular o tamanho do texto
    text_bbox = draw.textbbox((0, 0), name, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Posição do texto
    #text_position = (0, 0)
    text_position = (
        (background.width - text_width) // 2,  # Centraliza horizontalmente no background
        5  # Alinha ao topo do background (ajuste conforme necessário)
    )

    # Criar fundo branco para o texto
#    draw.rectangle([text_position, (text_position[0] + text_width, text_position[1] + text_height)], fill="white")
    draw.rectangle([0, 0, background.width, 20 + text_height], fill="white")
    # Adicionar o texto
    draw.text(text_position, name, font=font, fill="black")

    # Salvar a imagem final
    background.save(path_img)
    return path_img
