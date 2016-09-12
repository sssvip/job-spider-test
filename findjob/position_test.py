# coding:utf-8
import html_downloader,position_outputer,positionInfo_parser

position_cont = html_downloader.HtmlDownloader().download("http://campus.chinahr.com/job/120567.html".encode("utf-8"))
position = positionInfo_parser.PositionInfo_Parser().parse(position_cont)
#职位名称
print "name:"+position.name
#职位部门
print "department:"+position.department
#工作有效日期（起始日期）
print "validStartDate:"+position.validStartDate
#工作有效日期（截止日期）
print "validEndDate:"+position.validEndDate
# 职位薪资
print "salary:"+position.salary
# 职位类别（全职/实习）
print "requirement:"+position.requirement
# 职位发布时间
print "publish_time:"+position.publish_time
# 职位链接
print "url:"+position.url
# 工作地区
print "city:"+position.city
#招聘人数
print "personNum"+position.personNum
#职位学历要求
print "degree:"+position.degree
#职位英语等级要求
print "degree:"+position.degree
#职位性别要求
print "sex:"+position.sex
#职位最小年纪要求
print "startAge:"+position.startAge
#职位最大年纪要求
print "endAge:"+position.endAge
#职位介绍
print "desc:"+position.desc
#工作详细地点
print "detailPosition:"+position.detailPosition

outer = position_outputer.PositionOutputer()
outer.collect_data(position)
outer.output_txt()