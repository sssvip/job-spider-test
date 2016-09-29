# coding:utf-8
' a main module '
__author__ = 'David West : admin@dxscx.com'
from bs4 import BeautifulSoup
import position_model, html_downloader, re, datetime, sys


class PositionInfo_Parser:
    # 传入职位url，公司uuid,返回封装数据后的职位类
    def parse(self, position_url, company_uuid):
        if position_url is None:
            return
        position = self._get_position_info(position_url, company_uuid)
        return position

    # 进行职位信息封装
    def _get_position_info(self, position_url, uuid):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        position_cont = html_downloader.HtmlDownloader().download(position_url)
        if position_cont is None:
            return None
        soup = BeautifulSoup(position_cont, 'html.parser', from_encoding='utf-8')
        # 初始化职位信息
        position = position_model.Position_Model()
        # 职位信息解析
        position.company_uuid = uuid
        position.url = position_url
        # 名称
        position.name = soup.find("div", class_="internship-tille").find("h1").get_text().strip()
        # 职位类别
        position.requirement = soup.find("div", class_="internship-tille").find("p").get_text().strip();
        # 职位部门
        position.department = ""
        # 工作地区
        position.city = soup.find("ul", class_="list-mes").find("li", class_="city").get_text().strip()
        # 招聘人数
        personNumTemp = soup.find("ul", class_="list-mes").find("li",
                                                                class_="city").next_sibling.next_sibling.get_text().strip()
        position.personNum = personNumTemp.strip()[2:len(personNumTemp) - 1]
        # 有效期起始点----如果发布日期包含中文（一般是今天），则这里取当前日期，如果不包含中文，则去显示日期
        position.validStartDate = soup.find("div", class_="message").find("span").get_text().strip()[:-2]  # 去掉了发布2个字
        # zhPattern = re.compile('[\u4e00-\u9fa5]+')
        # 一个小应用，判断一段文本中是否包含简体中：
        # match = zhPattern.search(position.validStartDate)
        now = datetime.date.today()
        if position.validStartDate == '今天':  # 这里没采用match去判断有无中文，直接是否是今天（发布）
            position.validStartDate = str(now.strftime("%Y-%m-%d"))
        # 截止日期-默认发布日期后一个月
        position.validEndDate = str(now + datetime.timedelta(30))
        # 发布日期
        position.publish_time = position.validStartDate
        # 薪水
        position.salary = soup.find("div", class_="internship-tille").find_next_sibling().get_text()[:-2]
        # 职位描述
        desc = str(soup.find("dl", class_="detial").find('dd', class_="detial-line").prettify().strip())
        # 重新构造String,去掉不需要的空格，换行什么的
        temp_desc = []
        for temp_str in desc.replace("<br/>", "").split("\n"):
            # 去掉不需要的<dd></dd>
            if (temp_str.startswith("<dd")):
                continue
            if (len(temp_str) > 1):
                temp_desc.append(temp_str.strip())
                temp_desc.append("<br/>")
        position.desc = ''.join(temp_desc)
        # 解析部门-工作地点等
        dls = soup.find_all('dl', class_="detial")
        index = 0;
        for dl in dls:
            index = index + 1
            temp_soup = BeautifulSoup(str(dl), 'html.parser', from_encoding='utf-8');
            if (index == 1):  # ==1时解析职位描述--上面解析过了这里不再解析，跳过
                pass
            else:
                temp_content = temp_soup.find('dt').get_text().encode("utf-8")
                if (temp_content == "所属部门："):
                    position.department = temp_soup.find('dd').get_text().strip()
                if (temp_content == "工作地点："):
                    position.detailPosition = temp_soup.find('dd').get_text().strip()
        position.degree = soup.find("i", class_="school").find_parent().get_text().strip()[:-3]

        return position
