
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://web.archive.org/web/20150314214039/http://everythingessential.me/oils-and-blends-2/"
html = urlopen(url)

soup = BeautifulSoup(html,features = "html.parser" )
type(soup)


info = soup.find_all('h5')

oils = list(info)


print((type(oils[0])))


for i in oils:
    i = str(i)

print((type(oils[0])))


#for each_oil in info:
    #oils.append(each_oil.get('href'))





print('')
print('')


#all_links = soup.find_all('a')  #this prints a list of all the hyperlinks on the website


##for link in all_links:
   # print(link.get('href'))


#('div', class_='one_third') this returns all the div class's