# coding:utf-8
' a company model '
__author__ = 'David West : admin@dxscx.com'

class Position_Model:

    def __init__(self):
        #职位名称
        self.name=""
        #职位部门
        self.department=""
        #工作有效日期（起始日期）
        self.validStartDate=""
        #工作有效日期（截止日期）
        self.validEndDate=""
        # 职位薪资
        self.salary = ""
        # 职位类别（全职/实习）
        self.requirement = ""
        # 职位发布时间
        self.publish_time = ""
        # 职位链接
        self.url = ""
        # 工作地区
        self.city=""
        #招聘人数
        self.personNum=""
        #职位学历要求
        self.degree=""
        #职位英语等级要求
        self.degree=""
        #职位性别要求
        self.sex=""
        #职位最小年纪要求
        self.startAge=""
        #职位最大年纪要求
        self.endAge=""
        #职位介绍
        self.desc=""
        #工作详细地点
        self.detailPosition=""
