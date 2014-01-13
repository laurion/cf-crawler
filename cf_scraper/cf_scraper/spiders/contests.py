from scrapy.spider import BaseSpider
from scrapy.selector import Selector

class UsersSpider(BaseSpider):
    name = "users"
    allowed_domains = ["codeforces.com"]
    start_urls = [
        "http://codeforces.com/contest"
    ]
    # rules = [Rule(SgmlLinkExtractor(allow=['/\d+']), 'parse')]

    def parse(self, response):
        sel = Selector(response)
