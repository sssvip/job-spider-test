# coding:utf-8
' a company outputer '
__author__ = 'David West : admin@dxscx.com'
import os
class Company_Outputer:
    def __init__(self):
        self.datas = list()

    def collect_data(self, company):
        if company is None:
            return
        self.datas.append(company)
    def clear_data(self):
        del self.datas[:]
    def output_html(self):
        fout = open('companyDetails.html', 'w')
        fout.write("<html>")
        fout.write("<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<tr>")
        fout.write("<td>%s</td>" %"name")
        fout.write("<td>%s</td>" %"short_name")
        fout.write("<td>%s</td>" %"property")
        fout.write("<td>%s</td>" %"staff_nums")
        fout.write("<td>%s</td>" %"business_type1")
        fout.write("<td>%s</td>" %"business_type2")
        fout.write("<td>%s</td>" %"province_city")
        fout.write("<td>%s</td>" %"tags")
        fout.write("<td>%s</td>" %"address")
        fout.write("<td>%s</td>" %"website")
        fout.write("<td>%s</td>" %"mail_code")
        fout.write("<td>%s</td>" %"introduce_one_sentence")
        fout.write("<td>%s</td>" %"introduce")
        fout.write("<td>%s</td>" %"logourl")
        fout.write("<td>%s</td>" %"position number")
        fout.write("</tr>")
        for company in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" %company.name.encode('utf-8'))
            fout.write("<td>%s</td>" %company.short_name.encode('utf-8'))
            fout.write("<td>%s</td>" %company.property.encode('utf-8'))
            fout.write("<td>%s</td>" %company.staff_nums.encode('utf-8'))
            fout.write("<td>%s</td>" %company.business_type1.encode('utf-8'))
            fout.write("<td>%s</td>" %company.business_type2.encode('utf-8'))
            fout.write("<td>%s</td>" %company.province_city.encode('utf-8'))
            #tags拼串
            tags_String=""
            for tag in company.tags:
                tags_String=tags_String+","+tag
            tags_String = tags_String[1:len(tags_String) - 5]
            #注意去掉“,查看更多”(暂未实现)
            fout.write("<td>%s</td>" %tags_String.encode('utf-8'))
            fout.write("<td>%s</td>" %company.address.encode('utf-8'))
            fout.write("<td>%s</td>" %company.website.encode('utf-8'))
            fout.write("<td>%s</td>" %company.mail_code.encode('utf-8'))
            fout.write("<td>%s</td>" %company.introduce_one_sentence.encode('utf-8'))
            fout.write("<td>%s</td>" %company.introduce.encode('utf-8'))
            fout.write("<td>%s</td>" %company.logourl.encode('utf-8'))
            fout.write("<td>%s</td>" %str(len(company.positions)).encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()


    def output_txt(self):
        file_name='companyDetails.txt'
        #如果文件存在了，不输出表头
        if(os.path.exists(file_name)):
            fout = open(file_name, 'a')
        else:
            fout = open(file_name, 'w')
            fout.write("%s\t" % "公司UUID")
            fout.write("%s\t" % "公司URL")
            fout.write("%s\t" % "公司名")
            fout.write("%s\t" % "公司简称")
            fout.write("%s\t" % "公司性质")
            fout.write("%s\t" % "公司规模")
            fout.write("%s\t" % "行业性质1")
            fout.write("%s\t" % "行业性质2")
            fout.write("%s\t" % "公司省市")
            fout.write("%s\t" % "公司标签")
            fout.write("%s\t" % "公司地址")
            fout.write("%s\t" % "公司官网")
            fout.write("%s\t" % "公司邮编")
            fout.write("%s\t" % "一句话介绍")
            fout.write("%s\t" % "公司介绍")
            fout.write("%s\t" % "公司Logo_Url")
            fout.write("%s\t" % "公司发布职位数量")
            fout.write("\n")
        for company in self.datas:
            fout.write("%s\t" % company.uuid.encode('utf-8'))
            fout.write("%s\t" % company.url.encode('utf-8'))
            fout.write("%s\t" % company.name.encode('utf-8'))
            fout.write("%s\t" % company.short_name.encode('utf-8'))
            fout.write("%s\t" % company.property.encode('utf-8'))
            fout.write("%s\t" % company.staff_nums.encode('utf-8'))
            fout.write("%s\t" % company.business_type1.encode('utf-8'))
            fout.write("%s\t" % company.business_type2.encode('utf-8'))
            fout.write("%s\t" % company.province_city.encode('utf-8'))
            # tags拼串
            tags_String = ""
            for tag in company.tags:
                tags_String = tags_String + "," + tag
            tags_String = tags_String[1:len(tags_String) - 5]
            # 注意去掉“,查看更多”(暂未实现)
            fout.write("%s\t" % tags_String.encode('utf-8'))
            fout.write("%s\t" % company.address.encode('utf-8'))
            fout.write("%s\t" % company.website.encode('utf-8'))
            fout.write("%s\t" % company.mail_code.encode('utf-8'))
            fout.write("%s\t" % company.introduce_one_sentence.encode('utf-8'))
            fout.write("%s\t" % company.introduce.encode('utf-8'))
            fout.write("%s\t" % company.logourl.encode('utf-8'))
            fout.write("%s\t" % str(len(company.positions)).encode('utf-8'))
            fout.write("\n")
        fout.close()
