import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://howtofashion.in/']

    def parse(self, response):
        title = response.css('title::text').extract()
        yield{'titletext':title}

