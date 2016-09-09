# coding:utf-8
' a company outputer '
__author__ = 'David West : admin@dxscx.com'
class Company_Outputer:
    def __init__(self):
        self.datas = set()

    def collect_data(self, company):
        if company is None:
            return
        self.datas.add(company)

    def output_html(self):
        fout = open('companyDetails.html', 'w')
        fout.write("<html>")
        fout.write("<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<tr>")
        fout.write("<td>%s</td>" %"公司名")
        fout.write("<td>%s</td>" %"公司地址")
        fout.write("<td>%s</td>" %"网址")
        fout.write("<td>%s</td>" %"介绍")
        fout.write("<td>%s</td>" %"LogoUrl")
        fout.write("<td>%s</td>" %"城市")
        fout.write("</tr>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data.name.encode('utf-8'))
            fout.write("<td>%s</td>"%data.address.encode('utf-8'))
            fout.write("<td>%s</td>"%data.website.encode('utf-8'))
            fout.write("<td>%s</td>" % data.introduce.encode('utf-8'))
            fout.write("<td>%s</td>" % data.logourl.encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
