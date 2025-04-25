import scrapy

class newspaper(scrapy.Spider):
    name = "news"
    allowed_domains = ["edition.cnn.com"]
    
    def start_requests(self):
        yield scrapy.Request(
            url='https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html',
            callback=self.parse,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5756.197 Safari/537.36"
            }
        )

    def parse(self, response):
        title = response.css('h1.headline__text::text').get()
        article_paragraphs = response.css('div.article__content p::text').getall()
        
        with open("news.json", "w", encoding='utf-8') as f:
            f.write(f"Title: {title}\n\n")
            for para in article_paragraphs:
                f.write(para + "\n")

        
      #'article': response.xpath('//p[@class = "paragraph inline-placeholder vossi-paragraph"]/text()').getall(),
                

        #"title": response.css('h1.headline__text.inline-placeholder.vossi-headline-text::text').getall()
        #"article": response.css('paragraph inline-placeholder vossi-paragraph').getall()
        #'article': response.xpath('//p[@class = "paragraph inline-placeholder vossi-paragraph"]/text()').getall(),

            #for i in response.css('div'):
            #        yield {
            #            'title': response.css('h1.headline__text.inline-placeholder.vossi-headline-text::text').get(),
            #            'article': response.css('paragraph inline-placeholder vossi-paragraph').get(),
            #        }


    #def start_requests(self):
    #        urls = [
    #            "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html",
    #        ]
    #        for url in urls:
    #            yield scrapy.Request(url=url, callback=self.parse)

    