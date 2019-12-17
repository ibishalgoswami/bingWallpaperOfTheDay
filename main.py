#Bing wallpaper of the day.
import requests
from bs4 import BeautifulSoup
import urllib.request
url="https://bing.wallpaper.pics/"
r=requests.get(url)
html_content=r.content
soup=BeautifulSoup(html_content,'html.parser')

all_images=soup.find_all('img')
images_con=[]
for i in all_images:
    if i['src']!='/images/logo.gif' and i['src']!='/images/amazon.png':
        images_con.append(i['src'])
remove_duplicate_from_lis=set(images_con)

for j,k in enumerate(remove_duplicate_from_lis):
    urllib.request.urlretrieve(k,str(j)+'.jpg')#Downloading the images
    print(j,k)#Printing the iamges link with the index no.






