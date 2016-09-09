# coding:utf-8

from bs4 import BeautifulSoup
import position_model

class PositionInfo_Parser:
    def parse(self,cont):
        if cont is None:
            return
        soup = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8')
        position = self._get_position_info(soup)
        return position

    # 进行职位信息封装
    def _get_position_info(self,soup):
        #初始化职位信息
        position = position_model.Position_Model()
        #职位信息解析
        position.name = soup.find("div",class_="internship-tille").find("h1").get_text().strip()
        position.city = soup.find("ul",class_="list-mes").find("li",class_="city").get_text().strip()
        position.degree = soup.find("i",class_="school").find_parent().get_text()
        position.desc = soup.find("dl",class_="detial").find('dd',class_="detial-line").get_text().strip()
        position.detailPosition = soup.find("dl",class_="detial").find_next_sibling().find("dd").get_text()
        position.personNum = soup.find("ul",class_="list-mes").find("li",class_="city").next_sibling.next_sibling.get_text().strip()
        position.publish_time = soup.find("div",class_="message").find("span").get_text().strip()
        position.requirement =soup.find("div",class_="internship-tille").find("p").get_text().strip();
        position.salary =soup.find("div",class_="internship-tille").find_next_sibling().get_text()
        return position
