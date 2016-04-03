import scrapy
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from movieCrawler.items import MoviecrawlerItem

class Movie(CrawlSpider):
    name = "xijumovie"
    redis_key = 'xijumovie:start_urls'
    start_urls = ['http://www.loldytt.com/Anime/chart/1.html']

    def parse(self, response):
        selector = Selector(response)
        page = selector.xpath('//*[@id="classpage10"]/div/span[1]/text()').extract()[0]
        page = int(page[-3:-1])
        for i in range(0,page):
            print(i)
            yield Request("http://www.loldytt.com/Anime/chart/" + str(i) + ".html", callback=self.parse_page)

    def parse_page(self,response):
        selector = Selector(response)
        for eachMovie in selector.xpath('//li/a/@href').extract():
            yield Request(eachMovie, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        selector = Selector(response)
        for eachlink in selector.xpath('//*[starts-with(@id,"li1")]'):
            print(eachlink)
            item = MoviecrawlerItem()
            item['title'] = eachlink.xpath('a/text()').extract()[0]
            item['href'] = eachlink.xpath('a/@href').extract()[0]
            yield item
        for eachtorrent in selector.xpath('//*[@id="bt"]/ul/li/a'):
            item = MoviecrawlerItem()
            item['title'] = eachtorrent.xpath('text()').extract()[0]
            item['href'] = eachtorrent.xpath('@href').extract()[0]
            yield item

