# coding:utf-8
import html_downloader,position_outputer,positionInfo_parser

position = positionInfo_parser.PositionInfo_Parser().parse("http://campus.chinahr.com/job/133727.html","company_test_uuid")
#职位所属公司uuid
print "company_uuid:"+position.company_uuid
#职位url
print "url:"+position.url
#职位名称
print "name:"+position.name
# 职位类别（全职/实习）
print "requirement:"+position.requirement
#职位部门
print "department:"+position.department
# 工作地区（确定到市级）
print "city:"+position.city
#工作详细地点
print "detailPosition:"+position.detailPosition
#招聘人数
print "personNum:"+position.personNum
# 职位发布时间
print "publish_time:"+position.publish_time
#职位有效日期（起始日期）
print "validStartDate:"+position.validStartDate
#职位有效日期（截止日期）
print "validEndDate:"+position.validEndDate
# 职位薪资
print "salary:"+position.salary
#职位学历要求
print "degree:"+position.degree
#职位英语等级要求
print "english_require:"+position.english_require
#职位性别要求
print "sex:"+position.sex
#职位最小年纪要求
print "startAge:"+position.startAge
#职位最大年纪要求
print "endAge:"+position.endAge
#职位描述
print "desc:"+position.desc


outer = position_outputer.PositionOutputer()
outer.collect_data(position)
outer.output_txt()