# coding:utf-8
from bs4 import BeautifulSoup
import re
import urlparse

class CompanyUrl_Parser:
    def parse(self,url,cont):
        if url is None or cont is None:
            return
        soup = BeautifulSoup(cont,'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_url(url,soup)
        return new_urls

    def _get_new_url(self,url,soup):
        new_urls = set()
        links = soup.find_all('a', class_="e3 cutWord")
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url,new_url)
            new_urls.add(new_full_url)
        return new_urls
