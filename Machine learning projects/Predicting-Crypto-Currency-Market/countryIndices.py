# -*- coding: utf-8 -*-
import scrapy


class CountryindicesSpider(scrapy.Spider):
    name = 'countryIndices'
    allowed_domains = ['https://www.finanzen.net/indizes/alle']
    start_urls = ['http://https://www.finanzen.net/indizes/alle/']

    def parse(self, response):
        pass
