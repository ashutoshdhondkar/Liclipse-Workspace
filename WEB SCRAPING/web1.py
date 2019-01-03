import urllib.request
from bs4 import * 

url="https://www.youtube.com/watch?v=D34WjCuSBe4"#"http://www.thejakartapost.com/travel"

req = urllib.request.Request(url, data=None, 
             headers={ 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' } 
                                      )
f = urllib.request.urlopen(req) 
#print(f.read().decode('utf-8'))

soup = BeautifulSoup(f,'lxml')  # we can also use html.parser
#print(soup)

for x in soup(["script","style"]):
    x.extract()
    
text = soup.getText()
#print(text)
word = input("Enter a word : ")
List=[]
for line in text.splitlines(): # splitting each of lines
    if(len(line)>0):    # to overcome the blank spaces
        List.append(line.strip())
#print(List)

temp=[]
for x in List:
    temp.extend(x.split(' '))   # extend will add the elements of new list to temp whereas append would insert list inside list

print(temp)
print(temp.count(word))

