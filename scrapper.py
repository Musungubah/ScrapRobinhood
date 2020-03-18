import scrapy

class QuoteMyPage(scrapy.Spider):
    name = 'title'
    start_urls = [
        'https://www.goal.com/en-us'
    ]

    def parse(self, response):
        for quote in response.xpath('//h1[@class="page-header"]').get():
            yield {"title": quote}
            

