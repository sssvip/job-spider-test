# coding:utf-8
from bs4 import BeautifulSoup
import urllib2


url="http://www.baidu.com"
rs=urllib2.urlopen(url); 

soup=BeautifulSoup(rs,'html.parser',from_encoding='utf-8');

links=soup.find_all('a')

for link in links:
	print link.name,link['href'],link.get_text()