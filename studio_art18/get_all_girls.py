import requests as req
from bs4 import BeautifulSoup
from tqdm import tqdm


for i in tqdm(range(690)):
    page = req.get(f'https://www.xvideos.com/porn-actresses-index/from/worldwide/ever/{0}')
    soup = BeautifulSoup(page.text,features="html.parser")

    p_list_actriz = []
    for p in soup.findAll('p'):
        class_p = p.get('class',None)
        if class_p:
            if 'profile-name' in class_p:
                name = p.find('a').text
                #print(name)
                p_list_actriz.append(name)

    with open('list_actriz.txt','a+') as text:
        for actriz in p_list_actriz:
            text.writelines(actriz+'\n')

#print(page.text)
