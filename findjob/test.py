# coding:utf-8
import url_manager,html_downloader,companyUrl_parser,html_outputer

urls = url_manager.UrlManager()
downloader = html_downloader.HtmlDownloader()
parser = companyUrl_parser.CompanyUrl_Parser()

root="http://campus.chinahr.com/qz/p2"
url="http://campus.chinahr.com"
cont=url,downloader.download(root)

print cont;

