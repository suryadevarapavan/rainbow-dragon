import urllib3 as url
from lxml import html
import requests as r 
print(r"""
             __.-/|
             \`o_O'
              =( )=  +----------------+
                U|   | RAINBOW DRAGON |
      /\  /\   / |   +----------------+
     ) /^\) ^\/ _)\     |
     )   /^\/   _) \    |
     )   _ /  / _)  \___|_
 /\  )/\/ ||  | )_)\___,|))
<  >      |(,,) )__)    |
 ||      /    \)___)\
 | \____(      )___) )____
  \______(_______;;;)__;;;)
""")
c=0
ip=str(input("PLEASE ENTER LINK!!!"))
path=str(input("ENTER PATH:"))
#this function saved gifs
def save(link,path):
    global c 
    c+=1
    response = r.get(link)
    with open(f'{path}/{c}.gif','wb') as file:
       file.write(response.content) 

#for http request 
intial = url.PoolManager()
response = intial.request('GET',ip)


#for finding specific links 
base = response.data.decode('utf-8', errors='ignore')
parse=html.fromstring(base)
links = parse.xpath('//img')
for link in links:
    t=link.get('src')
    if '.gif' in t:
        save(t,path)
        print(t)
