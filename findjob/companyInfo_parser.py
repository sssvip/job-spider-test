# coding:utf-8
from bs4 import BeautifulSoup
import company_model, position_model, re, uuid_Utils


class CompanyInfo_Parser:
    def parse(self, root_url, url, cont):
        if url is None or cont is None:
            return
        soup = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8')
        company = self._get_company_info(root_url, url, soup)
        return company

    # 进行公司信息封装
    def _get_company_info(self, root_url, url, soup):
        # 初始化公司对象
        company = company_model.Company_Model()
        # 公司信息解析
        # 一边解析，一边提取数据装载到公司对象
        # 公司唯一编号
        company.uuid = uuid_Utils.getUuid(url)
        # 公司来源url
        company.url = url
        # 公司名解析
        name = soup.find('h1', class_="com-name")
        company.name = name.get_text().strip()
        company.short_name = company.name
        # 公司性质解析
        property = soup.find('ul', class_="other-com")
        company.property = property.get_text().split("|")[1][4:].strip()  # [0] 切分后的第一个 [3:]从字符串第三个字符开始，去掉“行业：”
        # 公司一级行业
        company.business_type1 = property.get_text().split("|")[0][4:].split("/")[
            0].strip()  # [0] 切分后的第一个 [3:]从字符串第三个字符开始，去掉“行业：”
        # 公司二级行业
        # 判断为防止公司网址没有二级行业
        if len(property.get_text().split("|")[0][3:].split("/")) > 1:
            company.business_type2 = property.get_text().split("|")[0][3:].split("/")[
                1].strip()  # [0] 切分后的第一个 [3:]从字符串第三个字符开始，去掉“行业：”
        # 省市解析--放在公司地址解析后了
        # 公司规模解析
        company.staff_nums = property.get_text().split("|")[2][4:].strip()  # [0] 切分后的第一个 [3:]从字符串第三个字符开始，去掉“行业：”
        # 公司标签解析
        tags = soup.find('ul', id="compBenefits");
        tags = soup.find_all('li', class_="cutWord");
        for tag in tags:
            company.tags.append(tag.get_text().strip())
        # 公司地址解析
        try:
            address = soup.find('i', class_="address").find_parent()
            if (address is not None):
                # 去掉前面的“公司地址：”
                company.address = address.get_text()[5:].strip()
        except:
            pass
        citys = company.address.split(" ")
        if (len(citys) > 2):
            company.province_city = citys[0].strip() + citys[1].strip()
        # 公司官网解析
        # 防止公司网址为空
        if soup.find('i', class_="web-address") is not None:
            website = soup.find('i', class_="web-address").find_parent().find('a')
            if (website is not None):
                company.website = website.get_text().strip()
        # 公司介绍解析
        company.introduce = soup.find('dd', id="detail-text").get_text().strip()
        logourl = soup.find('img', class_="img-attr")  # 公司名解析
        # 职位解析 -此处缩小了解析范围
        positions = soup.find_all('a', href=re.compile(r"/job/\d+\.html"))
        # 单独进行公司职位信息封装
        position = None;
        for temp_position in positions:
            position = position_model.Position_Model();
            temp_position_soup = BeautifulSoup(str(temp_position), 'html.parser', from_encoding='utf-8')
            # 此处只搜集职位URL，便于后期爬职位相关信息
            position.url = root_url + str(temp_position_soup.find('a')['href'])  # 添加公司网址集合
            position.url = position.url.strip()
            # 最后进行职位信息封装
            company.positions.add(position)
        # 存在公司没有LOGO情况
        if (logourl is None):
            company.logourl = "no.jpg"
        else:
            company.logourl = logourl['src']
        #
        return company
