
from urllib.parse import urlparse, urljoin
import requests as r
import os
from bs4 import BeautifulSoup

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

ip = str(input("PLEASE ENTER LINK!!! "))
path = str(input("ENTER PATH: "))
tp = str(input("ENTER FILE TYPE (like .gif, .jpg, .pdf): ")).strip().lower()

# this function saves files
def save(link, path):
    os.makedirs(path, exist_ok=True)
    response = r.get(link, stream=True)
    t = os.path.basename(urlparse(link).path)
    if not t:  # handle URLs with no filename
        t = "downloaded_file" + tp
    with open(f'{path}/{t}', 'wb') as file:
        for i in response.iter_content(1024):
            file.write(i)

# for http request 
response = r.get(ip)

# for finding specific links
try:
    base = response.text
    soup = BeautifulSoup(base, 'html.parser')
    for tag in soup.find_all(['img', 'a', 'source']):
        link = tag.get('src') or tag.get('href')
        if link and tp in link.lower():  # filter by file type
            flink = urljoin(ip, link)  # make absolute URL
            save(flink, path)
            print(f"Downloaded: {flink}")

except r.exceptions.HTTPError as eh:
    print(f"Error:{eh}")
except r.exceptions.ConnectionError as ec:
    print(f"Error:{ec}")
except r.exceptions.Timeout as et:
    print(f"Error:{et}")
except r.exceptions.RequestException as ee:
    print(f"Error:{ee}")
