# coding:utf-8

class PositionOutputer:
    def __init__(self):
        self.datas = list()

    def collect_data(self, position):
        if position is None:
            return
        self.datas.append(position)

    def output_html(self):
        fout = open('positionDetails.html', 'w')
        fout.write("<html>")
        fout.write("<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data.company_name.encode('utf-8'))
            fout.write("<td>%s</td>"%data.name.encode('utf-8'))
            fout.write("<td>%s</td>"%data.salary.encode('utf-8'))
            fout.write("<td>%s</td>" % data.requirement.encode('utf-8'))
            fout.write("<td>%s</td>" % data.url.encode('utf-8'))
            fout.write("<td>%s</td>" % data.city.encode('utf-8'))
            fout.write("<td>%s</td>" % data.personNum.encode('utf-8'))
            fout.write("<td>%s</td>" % data.degree.encode('utf-8'))
            fout.write("<td>%s</td>" % data.desc.encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
