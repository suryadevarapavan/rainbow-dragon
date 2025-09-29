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
response = r.request('GET',ip)

#for finding specific links
try:
    response=r.get(ip)
    base=response.text 
    response=r.get(ip)
    parse=html.fromstring(base)
    links = parse.xpath('//img')
    for link in links:
        t=link.get('src')
        if '.gif' in t:
            save(t,path)
            print(t)
except requests.exceptions.HTTPError as eh:
    print(f"Error:{eh}")
except requests.exceptions.ConnectionError as ec:
    print(f"Error:{ec}")
except requests.exceptions.Timeout as et:
    print(f"Error:{et}")
except requests.exceptions.RequestException as ee:
    print(f"Error:{ee}")
    
