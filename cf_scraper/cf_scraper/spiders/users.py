from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.item import Item, Field

class UserItem(Item):
    id = Field()
    score = Field()
class UsersSpider(BaseSpider):
    name = "users"
    allowed_domains = ["codeforces.com"]
    start_urls = [
        "http://codeforces.com/ratings/organization/371"
    ]
    http_user = 'laurion'
    http_pass = 'B9u5qxYc'

    def parse(self, response):
        sel = Selector(response)
        users = []
        print sel.xpath('//div[contains(@class,"lang-chooser")]').extract()
        for name in sel.xpath('//table//a[contains(@class,"rated-user")]/text()').extract()[20:]:
        	userItem = UserItem()
        	userItem['id'] = name
        	userItem['score'] = 0
        	users.append(userItem)
        	print name
        return users
