import scrapy
from ..items import ImotItem


class ImotBase(scrapy.Spider):
    name = 'imotbg'

    def start_requests(self):
        urls = [
            'https://www.imot.bg/pcgi/imot.cgi?act=14'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_list_response)

    def parse_list_response(self, response):
        towns = response.css('select[name=town] option::text').extract()
        pns = response.css('select[name=pn] option::text').extract()
        years = response.css('select[name=year] option::text').extract()
        dates = response.css('select[name=date] option::text').extract()
        url = 'https://www.imot.bg/pcgi/imot.cgi?act=14&pn={}&town={}&year={}&date={}'
        for town in towns:
            for pn in pns:
                for year in years:
                    for date in dates:
                        yield scrapy.Request(url=url.format(pn, town, year, date), callback=self.parse)

    def parse(self, response):
        items = ImotItem()

        location = response.css('.tabStatList b::text').extract()
        one_bedroom_price = response.css('td:nth-child(3) b::text').extract()
        one_bedroom_price_for_one_meter = response.css(
            'tr~ tr+ tr td:nth-child(4)::text').extract()

        two_bedroom_price = response.css('td:nth-child(6) b::text').extract()
        two_bedroom_price_for_one_meter = response.css(
            'tr~ tr+ tr td:nth-child(7)::text').extract()

        three_bedroom_price = response.css(
            'td:nth-child(9) b::text').extract()
        three_bedroom_price_for_one_meter = response.css(
            'tr~ tr+ tr td:nth-child(10)::text').extract()

        all_price_for_one_meter = response.css(
            'table.tabStat tr~ tr+ tr td[style="width:60px; text-align:center;"] b::text').extract()

        items['location'] = location
        items['one_bedroom_price'] = one_bedroom_price
        items['one_bedroom_price_for_one_meter'] = one_bedroom_price_for_one_meter
        items['two_bedroom_price'] = two_bedroom_price
        items['two_bedroom_price_for_one_meter'] = two_bedroom_price_for_one_meter
        items['three_bedroom_price'] = three_bedroom_price
        items['three_bedroom_price_for_one_meter'] = three_bedroom_price_for_one_meter
        items['all_price_for_one_meter'] = all_price_for_one_meter

        yield items
