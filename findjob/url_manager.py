# coding:utf-8


class UrlManager:
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
#添加新URL
    def add_new_url(self,new_url):
        if new_url is None:
            return
        if new_url not in self.new_urls and new_url not in self.old_urls:
            self.new_urls.add(new_url)

# 添加新URLS
    def add_new_urls(self,new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for new_url in new_urls:
            self.add_new_url(new_url)
#出栈一个
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
#是否还有待爬的url
    def has_new_url(self):
        return len(self.new_urls) != 0