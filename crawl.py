import requests
from bs4 import BeautifulSoup
url='http://indiatoday.intoday.in/'
plain_text=requests.get(url).text
soup=BeautifulSoup(plain_text)
for link in soup.findAll('div',{'class':'newsimg'},recursive=True):
	for l in link.findAll('a'):
		print(l.get('title')+"\n")

