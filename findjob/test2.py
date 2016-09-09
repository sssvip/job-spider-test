import  company_model,companyInfo_parser,html_downloader

compayinfo_paraser=companyInfo_parser.CompanyInfo_Parser()
url="http://campus.chinahr.com/company/2ae9b0e4a298eb56d21cb363j.html"

cont=html_downloader.HtmlDownloader().download(url)

company=compayinfo_paraser.parse("url",cont);

print "company name:"+company.getName()
print "company address:"+company.getAddress()
print "company introduce:"+company.getIntroduce()
print "company logourl:"+company.getLogoUrl()
