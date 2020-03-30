# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Crawler51JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position = scrapy.Field()  # 职位
    company = scrapy.Field()  # 公司名
    place = scrapy.Field()  # 工作地点
    salary = scrapy.Field()  # 薪资
