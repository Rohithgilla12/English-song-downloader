import requests
import re
from bs4 import BeautifulSoup
def get_top():
    top=[]
    lang="english"
    url="https://www.saavn.com/play/featured/"+str(lang)+"/Weekly+Top+Songs/1"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    songs=soup.find_all(class_=re.compile("song-name"))
    for song in songs:
        req_song=str(song)
        req_song=req_song.split('>')
        req_song=req_song[1].split('<')[0]
        top.append(req_song)
    return top


base_surl="http://en.muzmo.ru/search?q="
choices=["Look+what+you+made+me+do","havana","complicated","sorry","despacito"]
base_url="http://en.muzmo.ru"
def get_filename(choice):
    choice=choice.replace('+',' ')
    choice=choice.capitalize()
    return choice+".mp3"
def download(link,fname):
    temp=[]
    r1=requests.get(link)
    soup1=BeautifulSoup(r1.content,'html.parser')
    blocks=soup1.findAll(class_="block")
    for _ in blocks:
        _=str(_)
        if "mp3" in _:
            _=_.split('href="')[1]
            _=_.split('"')[0]
            temp.append(_)
    print "Otta for loop"

    r2=requests.get(temp[3])
    print"Done"
    with open(get_filename(fname),'wb') as k:
        k.write(r2.content)
# def get_link(choice):
#     links=[]
#     req_url=base_surl+choice
#     r=requests.get(req_url)
#     soup=BeautifulSoup(r.content,'html.parser')
#     temp=soup.findAll(class_="block")
#     for _ in temp:
#         _=str(_)
#         if "info" in _:
#             _=_.split('href="')[1]
#             _=_.split('&')[0]
#             links.append(base_url+_)    
#             req_link=links[0]
#     return req_link

def get_link(choice):
    links=[]
    req_url=base_surl+choice
    r=requests.get(req_url)
    soup=BeautifulSoup(r.content,'html.parser')
    temp=soup.findAll(class_="block")
    for _ in temp:
        _=str(_)
        if "get" in _:
            _=_.split('href="')[1]
            _=_.split('&')[0]
            links.append(base_url+_)    
            req_link=links[0]
           # print links
    return links[0]
for i in get_top():
    print get_link(i)  
    try:
        download(get_link(i),i)
        print "Done with "+i
    except:
        print "Couldnt do" + i
