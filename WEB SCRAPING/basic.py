# web scraping tutorial 1
# using beautiful soup 4

import bs4 as bs
import urllib.request
import re
 
source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# gives the source code

soup = bs.BeautifulSoup(source,'lxml')

print(soup.title)
print(soup.title.string)

#print(soup.find_all('p'))

#for para in soup.find_all('p'):
#    print(para.string)  # string will work if you don't have child tags under it

#print(soup.get_text())

pattern = re.compile('https:\W\W | http:\W\W')
urlList = []
for url in soup.find_all('a'):
    match = pattern.match(str(url))
    if(match):
        url.group()
    
print(urlList)