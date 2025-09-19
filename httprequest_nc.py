import urllib3 as url
from lxml import html

#for making http requests
http = url.PoolManager()
r = http.request('GET','http://www.google.com')
print(r.data)

