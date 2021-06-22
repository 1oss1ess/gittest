import scrapy


class ImotItem(scrapy.Item):
    location = scrapy.Field()
    one_bedroom_price = scrapy.Field()
    one_bedroom_price_for_one_meter = scrapy.Field()
    two_bedroom_price = scrapy.Field()
    two_bedroom_price_for_one_meter = scrapy.Field()
    three_bedroom_price = scrapy.Field()
    three_bedroom_price_for_one_meter = scrapy.Field()
    all_price_for_one_meter = scrapy.Field()
