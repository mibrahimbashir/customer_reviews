# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CustomerReviewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ReviewItem(scrapy.Item):
    business_name = scrapy.Field()
    business_category = scrapy.Field()
    rating = scrapy.Field()
    review_date = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    date_experience = scrapy.Field()