import requests
from bs4 import BeautifulSoup
base_surl="http://en.muzmo.ru/search?q="
choices=["Look+what+you+made+me+do","havana","complicated","sorry","despacito"]
base_url="http://en.muzmo.ru"

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
    with open(fname+".mp3",'wb') as k:
        k.write(r2.content)
def get_link(choice):
    links=[]
    req_url=base_surl+choice
    r=requests.get(req_url)
    soup=BeautifulSoup(r.content,'html.parser')
    temp=soup.findAll(class_="block")
    for _ in temp:
        _=str(_)
        if "info" in _:
            _=_.split('href="')[1]
            _=_.split('&')[0]
            links.append(base_url+_)    
            req_link=links[0]

    return req_link
for i in choices:
    print get_link(i)  
    try:
        download(get_link(i),i)
        print "Done with "+i
    except:
        print "Couldnt do" + i
