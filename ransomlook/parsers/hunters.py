import os
from bs4 import BeautifulSoup

def main():
    list_div=[]

    for filename in os.listdir('source'):
        if filename.startswith(__name__.split('.')[-1]+'-'):
            html_doc='source/'+filename
            file=open(html_doc,'r')
            soup=BeautifulSoup(file,'html.parser')
            divs_name=soup.find_all('div', {"class": "wrapper ng-star-inserted"})
            for div in divs_name:
                title = div.find('div', {"class": "title"}).text.strip()
                description = ''
                link = div.a['href']
                list_div.append({'title': title, 'description': description, 'link': link, 'slug': filename})
            file.close()
    print(list_div)
    return list_div