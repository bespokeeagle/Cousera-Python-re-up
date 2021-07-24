#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to
#The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

# import statements to enable GET requests 
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen

g = []
# import statements for Beautiful soup
from bs4 import BeautifulSoup
import ssl

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
tags = s("span")
# loop through said lines
for tag in tags:
    print (tag)
    for t in tag:
# a second loop to get the numbers out
        g.append(int (t))


    

print (sum(g))


