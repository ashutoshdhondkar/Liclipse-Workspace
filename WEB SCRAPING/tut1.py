import bs4 as bs
# https://pythonprogramming.net/parsememcparseface/
import urllib.request

url = "https://pythonprogramming.net/parsememcparseface/"

req = urllib.request.Request(url, data=None, 
             headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' } 
                                      )
f = urllib.request.urlopen(req)

#print(f.read().decode("utf-8"))
soup = bs.BeautifulSoup(f,'lxml')
#print(soup)

# to remove all the styling and scripting tags
for x in soup(['script','style']):
        x.extract()
    
print(soup.get_text())

#print(soup.title.string) #prints the title of the page
#print(soup.p.string)

# now to print all the paragraph tags
#print(soup.find_all('p'))

#for paragraph in soup.find_all('p'):
#    print(paragraph.text)


#print(soup.get_text())
List = []
for x in soup.get_text().splitlines():
    if(len(x)>0):
        List.append(x.strip())
        
#for x in List:
#    print(x)

#for x in soup.find_all('a'):
    #print(x.get('href'))

