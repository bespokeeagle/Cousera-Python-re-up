import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen

from bs4 import BeautifulSoup
import ssl

k = []

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# enter url
url = input ("enter: ")
# open url and read it
x = urlopen(url,context=ctx).read()
# parse url url using beautiful soup
s = BeautifulSoup(x,'html.parser')
# search for and give me lines with span
tags = s("a")
# loop through said lines
#print(tags[2]) 
f = tags[2]
#print (f)
for t in tags :
#   print('URL:', t.get('href', None))
   k.append(t.get('href', None))
#print (k[:4])
print (k[17])
r = 0 
url = k[17]
while r < 6 :
    
    o = urlopen(url,context=ctx).read()
    b = BeautifulSoup(o,'html.parser')
    tagsh = b("a")
#    print (tagsh[2])
    for v in tagsh:
        position = tagsh.index(v)
        if position == 17:
    #    k.append(v.get('href',None))
            url = (v.get('href',None))
            print (url)
        
    r = int(r) + 1
















#for l in k:
#    if l is k[0]:
 #       url = l
  #      x = urlopen(url,context=ctx).read()
# parse url url using beautiful soup
   #     s = BeautifulSoup(x,'html.parser')
# search for and give me lines with span
    #    tags = s("a")
# loop through said lines
#print(tags) 
     #   for t in tags :
      #      print('URL:', t.get('href', None))



    

    


