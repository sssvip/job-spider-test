# coding:utf-8
import url_manager,html_downloader,companyUrl_parser,html_outputer,positionInfo_parser

position_cont = html_downloader.HtmlDownloader().download("http://campus.chinahr.com/job/120567.html".encode("utf-8"))
position = positionInfo_parser.PositionInfo_Parser().parse(position_cont)

root="http://campus.chinahr.com/qz/p2"
url="http://campus.chinahr.com"

outer = html_outputer.HtmlOutputer()
outer.collect_data(position)
outer.output_html()