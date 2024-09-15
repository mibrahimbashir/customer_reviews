import scrapy
from customer_reviews.items import ReviewItem

class TpSpider(scrapy.Spider):
    name = "tp"
    allowed_domains = ["www.trustpilot.com"]
    start_urls = ["https://www.trustpilot.com/"]

    def parse(self, response):
        category_page_url = response.xpath("//header/div/a[2]/@href").get()

        category_page_url = "https://www.trustpilot.com/" + category_page_url
        
        yield response.follow(category_page_url, callback=self.parse_all_categories_page)
    
    def parse_all_categories_page(self, response):

        categories_url = response.css("main li a::attr(href)").getall()

        for category_url in categories_url:
            category_url = "https://www.trustpilot.com/" + category_url

            yield response.follow(category_url, callback=self.parse_category_page)
    
    def parse_category_page(self, response):
        businesses_url = response.css('div.styles_wrapper__2JOo2 a::attr(href)').getall()

        for business_url in businesses_url:
            business_url = "https://www.trustpilot.com/" + business_url
            yield response.follow(business_url, callback=self.parse_business_page)
        
        next_page_url = response.xpath('//nav[last()]/a[last()]/@href').get(default='')

        if next_page_url:
            next_page_url = "https://www.trustpilot.com" + next_page_url
            yield response.follow(next_page_url, callback=self.parse_category_page)
    
    def parse_business_page(self, response):
        review_item = ReviewItem()

        business_unit = response.css("#business-unit-title")

        review_item["business_name"] = business_unit.css("h1 span::text").get()
        review_item["business_category"] = business_unit.xpath(".//a[last()]/text()").get(default='')

        customer_reviews = response.css("article section")

        for review in customer_reviews:
            review_item["rating"] = review.css('div.styles_reviewHeader__iU9Px::attr(data-service-review-rating)').get(default='0')
            review_item["review_date"] = review.xpath('.//time[1]/@datetime').get(default='')
            review_item["title"] = review.css('h2::text').get(default='')
            review_item["description"] = review.css('.typography_body-l__KUYFJ.typography_appearance-default__AAY17.typography_color-black__5LYEn::text').get(default='')
            review_item["date_experience"] = review.css('p.typography_body-m__xgxZ_.typography_appearance-default__AAY17::text').getall()[-1]
            
            yield review_item

        next_page_url = response.xpath('//nav[last()]/a[last()]/@href').get(default='')

        if next_page_url:
            next_page_url = "https://www.trustpilot.com" + next_page_url
            yield response.follow(next_page_url, callback=self.parse_business_page)