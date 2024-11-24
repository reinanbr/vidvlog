import requests as req
from bs4 import BeautifulSoup
from tqdm import tqdm


for i in range(690):
    page = req.get(f'https://www.xvideos.com/porn-actresses-index/from/worldwide/ever/{i}')
 #   print(f"[it.{i}] - getting actriz from '{page.url}'...")
    soup = BeautifulSoup(page.text,features="html.parser")

    p_list_actriz = []
    u = 0
    for p in soup.findAll('p'):
        class_p = p.get('class',None)
        if class_p:
            if 'profile-name' in class_p:
                name = p.find('a').text
                #print(name)
                p_list_actriz.append(name)
        u+=1
    with open('all_actriz.txt','a+') as text:
        for actriz in p_list_actriz:
            text.writelines(actriz+'\n')
    print(f"[it.{i}] - getting '{u} actriz name', from '{page.url}'...")
 
#print(page.text)
