# -*- coding: utf-8 -*-
import scrapy

from crawler51job.items import Crawler51JobItem


class Spider51jobSpider(scrapy.Spider):
    name = 'spider51job'
    allowed_domains = ['51job.com']
    start_urls = [
        'https://search.51job.com/list/010000,000000,0000,32,9,99,Java%25E5%25BC%2580%25E5%258F%2591,2,1.html']

    def parse(self, response):
        item = Crawler51JobItem()
        item['position'] = response.xpath('//div[@class="el"]/p[@class="t1 "]/span/a/@title').extract()
        item['company'] = response.xpath('//div[@class="el"]/span[@class="t2"]/a/@title').extract()
        item['place'] = response.xpath('//div[@class="el"]/span[@class="t3"]/text()').extract()
        item['salary'] = response.xpath('//div[@class="el"]/span[@class="t4"]/text()').extract()
        yield item
