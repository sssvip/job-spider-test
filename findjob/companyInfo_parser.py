# coding:utf-8
from bs4 import BeautifulSoup
import company_model, position_model,re

class CompanyInfo_Parser:
    def parse(self,root_url,url, cont):
        if url is None or cont is None:
            return
        soup = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8')
        company = self._get_company_info(root_url,url, soup)
        return company

    # 进行公司信息封装
    def _get_company_info(self,root_url, url, soup):
        # 初始化公司对象
        company = company_model.Company_Model()
        # 公司信息解析
        name = soup.find('h1', class_="com-name")  # 公司名解析
        address = soup.find('h4', class_="address-com")  # 公司名解析
        introduce = soup.find('dd', id="detail-text")  # 公司介绍解析
        logourl = soup.find('img', class_="img-attr")  # 公司名解析
        # 职位解析 -此处缩小了解析范围
        positions = soup.find_all('a', href=re.compile(r"/job/\d+\.html"))
        # 单独进行公司职位信息封装
        position = None;
        for temp_position in positions:
            position = position_model.Position_Model();
            temp_position_soup = BeautifulSoup(str(temp_position), 'html.parser', from_encoding='utf-8')
            #此处只搜集职位URL，便于后期爬职位相关信息
            position.url=root_url+str(temp_position_soup.find('a')['href'])  # 添加公司网址集合
            #最后进行职位信息封装
            company.positions.add(position)
        # 提取数据装载到公司对象
        company.name=name.get_text()
        if(address is not None):
            company.address=address.get_text()
        company.introduce = introduce.get_text().strip()
        # 存在公司没有LOGO情况
        if (logourl is None):
            company.logourl="no.jpg"
        else:
            company.logourl = logourl['src']
        #
        return company
