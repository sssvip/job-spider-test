# coding:utf-8
import  companyInfo_parser,html_downloader,company_outputer

compayinfo_paraser=companyInfo_parser.CompanyInfo_Parser()
#url="http://campus.chinahr.com/company/e23dae840dc05e5646baab19j.html"
url="http://campus.chinahr.com/company/09bbb0e4370a4857a4329bacj.html"
root_url="http://campus.chinahr.com"
cont=html_downloader.HtmlDownloader().download(url)
company=compayinfo_paraser.parse(root_url,url,cont);
#打印输出
print "company name:"+company.name
print "company short_name:"+company.short_name
print "company property:"+company.property
print "company staff_nums:"+company.staff_nums
print "company business_type1:"+company.business_type1
print "company business_type2:"+company.business_type2
print "company province_city:"+company.province_city
#tags拼串
tags_String=""
for tag in company.tags:
	tags_String=tags_String+","+tag
# 注意去掉“,查看更多”
tags_String=tags_String[1:len(tags_String)-5]

print "company tags:"+tags_String
print "company address:"+company.address
print "company website:"+company.website
print "company mail_code:"+company.mail_code
print "company introduce_one_sentence:"+company.introduce_one_sentence
print "company introduce:"+company.introduce
print "company logourl:"+company.logourl
print "company position number:"+str(len(company.positions))

outer=company_outputer.Company_Outputer()
outer.collect_data(company)
outer.output_txt()
