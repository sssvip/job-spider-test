# coding:utf-8

from bs4 import BeautifulSoup
import position_model
import re
import datetime

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
        position.degree = soup.find("i",class_="school").find_parent().get_text().strip()[:-3]
        position.desc = soup.find("dl",class_="detial").find('dd',class_="detial-line").get_text().strip()
        #position.detailPosition = soup.find("dl",class_="detial").find_next_sibling().find("dd").get_text()
        personNumTemp = soup.find("ul",class_="list-mes").find("li",class_="city").next_sibling.next_sibling.get_text().strip()
        position.personNum = personNumTemp.strip()[2:len(personNumTemp)-1]
        position.validStartDate = soup.find("div",class_="message").find("span").get_text().strip()[:-2]
        zhPattern = re.compile('[\u4e00-\u9fa5]+')
        #一个小应用，判断一段文本中是否包含简体中：
        match = zhPattern.search(position.validStartDate)
        if match:
            now = datetime.datetime.now()
            position.validStartDate = now.strftime("%Y-%m-%d")
        position.requirement =soup.find("div",class_="internship-tille").find("p").get_text().strip();
        position.salary =soup.find("div",class_="internship-tille").find_next_sibling().get_text()[:-2]
        position.validEndDate = "2016/12/31"
        return position
  