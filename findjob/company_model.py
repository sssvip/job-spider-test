# coding:utf-8
' a company model '
__author__ = 'David West : admin@dxscx.com'

import position_model

class Company_Model:
    def __init__(self):
        #公司uuid
        self.uuid=""
        # 公司信息来源url
        self.url = ""
        # 公司名
        self.name = ""
        # 公司简称
        self.short_name = ""
        # 公司性质(所有权)
        self.property = ""
        # 公司规模
        self.staff_nums = ""
        # 公司行业类别1
        self.business_type1 = ""
        # 公司行业类别2
        self.business_type2 = ""
        # 公司省市
        self.province_city = ""
        # 公司标签
        self.tags = list()
        # 公司地址
        self.address = ""
        # 公司官网
        self.website = ""
        # 公司邮编
        self.mail_code = ""
        # 公司一句话介绍
        self.introduce_one_sentence = ""
        # 公司介绍
        self.introduce = ""
        # 公司logo地址
        self.logourl = ""

        # 公司相关职位
        self.positions = set()

    def getPositions(self):
        return self.positions

    def getPosition(self):
        return self.positions.pop()
