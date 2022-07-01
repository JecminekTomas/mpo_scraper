import scrapy


class MpoSpider(scrapy.Spider):
    name = 'mpo'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
