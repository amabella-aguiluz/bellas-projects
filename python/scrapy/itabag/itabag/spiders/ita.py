import scrapy

class scraperSpider(scrapy.Spider):
    name = 'scraper'
    start_urls = ['https://www.aliexpress.com/w/wholesale-itabag.html']

    def parse(self, response):
        for products in response.css('div.l5_ju.card-out-wrapper'):
            yield {
                'name': products.css('h3.l5_kr::text').get(),
                'link': products.css('a.l5_b.h7_ic.search-card-item').attrib['href'],
            }

