# coding:utf-8
' a main module '
__author__ = 'David West : admin@dxscx.com'

import url_manager, html_downloader, companyUrl_parser, companyInfo_parser, positionInfo_parser, position_outputer, \
    company_outputer, time, random


class Spider:
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = companyUrl_parser.CompanyUrl_Parser()
        self.sleep_time = 0;  # 爬取输出一个公司暂停几秒

    # 爬虫起始点
    # root_url起始页面
    # url
    def crawl(self, root_url, url):
        company_urls = self.getCompanyUrls(url, 1, 175)
        company_outer = company_outputer.Company_Outputer()
        position_outer = position_outputer.PositionOutputer()
        index = 0
        print len(company_urls)
        for link in company_urls:
            index = index + 1
            print index
            print "正在收集%s公司信息-准备打印" % link.encode("utf-8")
            company = self.getCompanyInfo(url, link)
            company_outer.collect_data(company)
            # 搜集一个公司信息，追加一个公司，以免后面出错一点也没有写入
            company_outer.output_txt()
            company_outer.clear_data()  # 输出后清空搜集的数据，以便下次使用此输出对象数据重复
            # 随机暂停休息几秒
            self.sleep_time = sleep_time = random.randint(3, 15);
            time.sleep(self.sleep_time)
            print "程序休息" + str(self.sleep_time) + "秒"
            for position in company.positions:
                print "正在收集公司职位信息-准备打印"
                position.company_name = company.name
                position_outer.collect_data(position)
            # 每个公司职位信息在搜集完后直接追加
            position_outer.output_txt()
            position_outer.clear_data()  # 输出后清空搜集的数据，以便下次使用此输出对象数据重复

    # 此方法存在特殊逻辑----只适用于url：http://campus.chinahr.com的情况
    # 返回start_page到end_page页面所有公司网址，便于后期通过公司网址爬取公司信息以及职位信息
    # 更新时间：20160907
    def getCompanyUrls(self, url, start_page, end_page):
        if start_page <= 0:
            print "Parameters can not be negative"
            start_page = 1
        temp_url = ""
        company_url_manager = url_manager.UrlManager();
        # 获取公司页面start_page-end_page页
        for x in range(start_page, end_page):
            # print "---------------------------------------------------page"+str(x)
            if x <= 1:
                temp_url = url + "/qz"
            else:
                temp_url = url + "/qz/p" + str(x)
            try:
                html_cont = self.downloader.download(temp_url)
                new_urls = self.parser.parse(url, html_cont)
                company_url_manager.add_new_urls(new_urls)
            except:
                print 'getCompanyUrls Failed. errer details:' + temp_url

        return company_url_manager.new_urls

    # 获取公司信息---
    # root_url 公司根url :类似 http://campus.chinahr.com
    # url 公司url访问地址 :类似 http://campus.chinahr.com/company/e782ae84cb8c8b56ba8e1a05j.html
    # 返回公司类
    def getCompanyInfo(self, root_url, url):
        # 公司信息解析器
        compayinfo_paraser = companyInfo_parser.CompanyInfo_Parser()
        # 获取到公司网页内容
        company_cont = html_downloader.HtmlDownloader().download(url)
        company = compayinfo_paraser.parse(root_url, url, company_cont);
        positioninfo_parser = positionInfo_parser.PositionInfo_Parser()
        # 解决公司职位信息封装
        temp_positions = list()  # 临时存放position集合
        size = len(company.positions)
        # 取出所有职位网址进行解析转换
        while size > 0:
            temp_positions.append(positioninfo_parser.parse(company.positions.pop().url.encode("utf-8"), company.uuid))
            size = size - 1
        company.positions = temp_positions
        return company


if __name__ == '__main__':
    root_url = "http://campus.chinahr.com"
    url = "http://campus.chinahr.com"
    obj_spider = Spider()
    obj_spider.crawl(root_url, url)
