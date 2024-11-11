from vidvlog.art18.create_img import create_image
from bing_image_downloader import downloader
import glob, os


def create_painel_actriz(actriz_name,path_img='.data/img.png',limit=1,dir_dataset='dataset'):
    dir = f"{dir_dataset}/{actriz_name}/"
    if not os.path.isdir(dir):
        downloader.download(actriz_name, limit=limit,  output_dir=dir_dataset, adult_filter_off=False, force_replace=False, timeout=60, verbose=True)

    pattern = os.path.join(dir,"Image_1.*")
    if limit>1:
        pattern = os.path.join(dir,"Image_*")
    imgs = glob.glob(pattern)
    #print(dir)
  #  print(imgs)
    background_path = 'bg3.jpg'
    overlay_image_path = imgs[0] if type(imgs)==list else imgs

    font_path = 'buller.otf'
    if not type(imgs)==list:
        print('retornando este ..')
        return create_image(background_path, overlay_image_path, actriz_name,path_img, font_path)
    img_path_list = []
    i = 0
    for img in imgs:
        img_path_list.append(create_image(background_path, img, actriz_name,path_img%{'i':i}, font_path))
        i+=1
    return img_path_list


#create_painel_actriz('Mia Khalifa','mia.jpg')
