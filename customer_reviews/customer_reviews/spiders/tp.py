import scrapy


class TpSpider(scrapy.Spider):
    name = "tp"
    allowed_domains = ["www.trustpilot.com"]
    start_urls = ["https://www.trustpilot.com/"]

    def parse(self, response):
        pass
