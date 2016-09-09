# coding:utf-8
' a company model '
__author__ = 'David West : admin@dxscx.com'

import position_model

class Company_Model:

    def __init__(self):
        #公司名
        self.name=""
        # 公司地址
        self.address =""
        # 公司网址
        self.website = ""
        # 公司介绍
        self.introduce =""
        #公司logo地址
        self.logourl =""
        #公司相关职位
        self.positions=set()

    def getPositions(self):
        return self.positions
    def getPosition(self):
        return self.positions.pop()
