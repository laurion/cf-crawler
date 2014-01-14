from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.item import Item, Field
from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule

class UserItem(Item):
    id = Field()
    score = Field()

class CfSpider(BaseSpider):
    name = "cf_spider"
    allowed_domains = ["codeforces.com"]
    # login_page = 'http://codeforces.com/enter'
    start_urls = [
        "http://codeforces.com/contests"
    ]

    FIRST_CONTEST = 352
    LAST_CONTEST = 381

    user_page = 'http://codeforces.com/contests/with/'
    # theUser = ''
    # score = 0
    scores = {}
    def parse(self, response):
        self.fout = open("scores.txt", "w")
        for user in open("users.txt").readlines():
            yield Request(url=self.user_page + user, callback=self.parse_user)

    def parse_user(self, response):
        sel = Selector(response)
        base = '//table[@class="tablesorter user-contests-table"]//tr//a[2]/'
        ranks = sel.xpath(base+'text()').extract()
        hrefs = sel.xpath(base+'@href').extract()
        scores = []
        nr = 0
        for rank, href in zip(ranks, hrefs):
            if self.FIRST_CONTEST <= int(href[9:-10]) <= self.LAST_CONTEST:
                scores.append(int(rank))
                nr += 1

        scores = sorted(scores)
        print scores
        score = 0
        user = response.url.split('/')[-1][:-3]
        if(scores):
            if(len(scores) == 1):
                score = scores[0] * 52/10
            elif(len(scores) == 2):
                score = sum(scores) * 18/10
            elif(len(scores) >= 3):
                score = sum(scores[:3])
            self.fout.write(user+','+str(score)+','+str(nr)+'\n')
            print user, score, nr

        # print score
    
    # def get_score(self, rank, href):
    #     r = Request(url="http://codeforces.com" + href, callback=self.parse_contest)
    #     r.meta['rank'] = rank
    #     return r

    # def parse_contest(self, response):
    #     rank = response.meta['rank']
    #     page = int(rank)//100
    #     if page * 100 != rank:
    #         page += 1
    #     return Request(url=response.url + '/page/%d' % page, callback=self.parse_contest_page)

    # def parse_contest_page(self, response):
    #     sel = Selector(response)
    #     # import pdb;pdb.set_trace()
    #     print sel.xpath('//tr//text()[contains(.,"%s")/..]' % self.theUser).extract()

