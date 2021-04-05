# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country']

    def parse(self, response):
        countries = response.xpath('//td/a')
        link = countries.xpath('.//@href')

        for country in countries:
            country_name = countries
            country_link = link.get()


        yield {
            'country_name' : country_name,
            'country_link' : country_link
        }
