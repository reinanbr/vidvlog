from create_img import create_image
from bing_image_downloader import downloader
import glob, os


def create_painel_actriz(actriz_name,path_img):
    dir = f"dataset/{actriz_name}/"
    if not os.path.isdir(dir):
        downloader.download(actriz_name, limit=1,  output_dir='dataset', adult_filter_off=False, force_replace=False, timeout=60, verbose=True)

    pattern = os.path.join(dir, f"Image_1.*")
    imgs = glob.glob(pattern)

    background_path = 'bg3.jpg'
    overlay_image_path = imgs[0] if type(imgs)==list else imgs

    font_path = 'buller.otf'
    return create_image(background_path, overlay_image_path, actriz_name,path_img, font_path)


create_painel_actriz('Mia Khalifa','mia.jpg')
