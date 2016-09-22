# coding:utf-8
from bs4 import BeautifulSoup
import urllib2

url = "http://campus.chinahr.com/job/127489.html"
rs = urllib2.urlopen(url);

soup = BeautifulSoup(rs, 'html.parser', from_encoding='utf-8');

dls = soup.find_all('dl', class_="detial")
index = 0;
for dl in dls:
    index = index + 1
    temp_soup = BeautifulSoup(str(dl), 'html.parser', from_encoding='utf-8')
    if (temp_soup.find('dt').get_text().encode("utf-8") == "职位描述："):
        print temp_soup.find('dd').get_text().strip()
    if (temp_soup.find('dt').get_text().encode("utf-8") == "所属部门："):
        print temp_soup.find('dd').get_text().strip()
