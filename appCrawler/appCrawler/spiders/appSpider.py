from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from appCrawler.items import AppcrawlerItem


class appSpider(CrawlSpider):
    name = "app_spider"
    redis_key = 'app_spider:start_urls'
    start_urls = ['https://itunes.apple.com/us/genre/ios/id36?mt=8']

    def parse(self,response):
        selector = Selector(response)
        for href in selector.xpath('//*[@id="genre-nav"]/div/ul/li/a/@href').extract():
            yield Request(href, callback=self.parse_category)

    def parse_category(self,response):
        selector = Selector(response)
        for href in selector.xpath('//*[@id="selectedcontent"]/div/ul/li/a/@href').extract():
            yield Request(href, callback=self.parse_letter)

    def parse_letter(self,response):
        selector = Selector(response)
        for href in selector.xpath('//*[@id="selectedgenre"]/ul/li/a/@href').extract():
            yield Request(href, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        selector = Selector(response)
        item = AppcrawlerItem()
        item['name'] = response.xpath('//*[@id="title"]/div[1]/h1/text()').extract()[0]
        item['category'] = response.xpath('//*[@id="left-stack"]/div[1]/ul/li[2]/a/span/text()').extract()[0]
        item['updated'] = response.xpath('//*[@id="left-stack"]/div[1]/ul/li[3]/span[2]/text()').extract()[0]
        item['size'] = response.xpath('//*[@id="left-stack"]/div[1]/ul/li[5]/text()').extract()[0]
        item['languages'] = response.xpath('//*[@id="left-stack"]/div[1]/ul/li[6]/text()').extract()[0]
        item['seller'] = response.xpath('//*[@id="title"]/div[1]/h2/text()').extract()[0]
        item['rating'] = response.xpath('//*[@id="left-stack"]/div[2]/div[2]/@aria-label').extract()[0]
        item['compatibility'] = response.xpath('//*[@id="left-stack"]/div[1]/p/span[2]/text()').extract()[0]
        item['price'] = response.xpath('//*[@id="left-stack"]/div[1]/ul/li[1]/span/div/text()').extract()[0]
        item['description'] = response.xpath('//*[@id="content"]/div/div[2]/div[1]/p/text()').extract()[0]
        yield item
        nextLink = selector.xpath('//*[@id="selectedgenre"]/ul[2]/li[19]/a/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            print nextLink
            yield Request(nextLink, callback=self.parse)



