# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime


class CustomerReviewsPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        field_names = adapter.field_names()

        # remove trailing whitespaces from all fields
        for field in field_names:
            value = adapter.get(field)

            adapter[field] = value.strip()

        # convert rating into integer
        rating = adapter.get("rating")
        adapter["rating"] = int(rating)

        # convert date fields to datetime format
        date_experience = adapter.get("date_experience")
        adapter["date_experience"] = datetime.strptime(date_experience, "%B %d, %Y").date()

        review_date = adapter.get("review_date")
        adapter["review_date"] = datetime.strptime(review_date, "%Y-%m-%dT%H:%M:%S.%fz").date()

        return item
