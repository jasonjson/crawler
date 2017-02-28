# import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from my_crawler.items import MyCrawlerItem

class MyCrawlSpider(CrawlSpider):
    name = 'my_crawler'
    allowed_domains = ['mickeyliu5.github.io']
    start_urls = [
            "https://mickeyliu5.github.io/blog"
            ]

    rules = (Rule(LinkExtractor(allow=r'/page[0-9]*'),callback='parse_item', follow=True),)

    def parse_item(self, response):
        articles = response.xpath('//ul[@class="post-list"]/*')

        for article in articles:
            item = MyCrawlerItem()
            try:
                item['title'] = article.xpath('h2/a/text()').extract()[0]
                item['url'] = "mickeyliu5.github.io/{0}".format(article.xpath('h2/a/@href').extract()[0])
                item['summary'] = article.xpath('div[@class="post-excerpt"]/p/strong/em/text()').extract()[0]
                yield item
            except:
                pass
