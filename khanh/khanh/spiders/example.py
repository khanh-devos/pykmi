import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["khanh-devos.github.io"]
    start_urls = ["https://khanh-devos.github.io/MyPortfolio/"]

    def parse(self, response):
        pass
