import scrapy 
from ..items  import QuotetutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        all_div_quotes = response.css('div.quote')
        
        items = QuotetutorialItem()
        
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('small.author::text').extract()
            tag = quote.css('.tag::text').extract()
            
            items['title']= title
            items['author']=author
            items['tag'] = tag
            yield items

