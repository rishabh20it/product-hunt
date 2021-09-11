from bs4 import BeautifulSoup
import requests
from  lxml import etree

url=('https://www.producthunt.com/')
r=requests.get(url)
htmlContent=r.content


#print(htmlcontent)

soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify())

links=soup.find_all('div',class_='styles_postContent__3Sqgf' )
print(links)
#for link in links:
    #if 'href'in link.attrs:
        #print(str(link.attrs['href'])+'\n')
