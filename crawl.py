import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://khanh-devos.github.io/MyPortfolio/']

    def parse(self, response):
        
        for title in response.css('.oxy-post-title'):
            print(title)
            yield {'title': title.css('::text').get()}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)