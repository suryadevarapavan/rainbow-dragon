from lxml import html
import requests as r 
from urllib.parse import urlparse
import os
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
ip=str(input("PLEASE ENTER LINK!!!"))
path=str(input("ENTER PATH:"))

#this function saved gifs
def save(link,path):
os.makedirs(path, exist_ok=True)
    response = r.get(link)
    t=os.path.basename(urlparse(link).path)
    with open(f'{path}/{t}','wb') as file:
       file.write(response.content) 

#for http request 
response = r.request('GET',ip)

#for finding specific links
try:
    base=response.text 
    response=r.get(ip)
    parse=html.fromstring(base)
    links = parse.xpath('//img')
    for link in links:
        t=link.get('src')
        if '.gif' in t:
            save(t,path)
            print(t)
except r.exceptions.HTTPError as eh:
    print(f"Error:{eh}")
except r.exceptions.ConnectionError as ec:
    print(f"Error:{ec}")
except r.exceptions.Timeout as et:
    print(f"Error:{et}")
except r.exceptions.RequestException as ee:
    print(f"Error:{ee}")
    
