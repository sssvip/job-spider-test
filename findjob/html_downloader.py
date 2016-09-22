# coding:utf-8
import urllib2
class HtmlDownloader:
    def download(self,url):
        if url is None:
            return
        try:
            response = urllib2.urlopen(url)
            if response.code != 200:
                print str(url) + "url---download 状态码非200,请查看"
                return None
            return response.read()
        except:
            print str(url) + "url---download出错,请查看"
            return None
