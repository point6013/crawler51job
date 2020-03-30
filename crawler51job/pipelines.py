# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pandas import DataFrame


class Crawler51JobPipeline(object):
    def process_item(self, item, spider):
        # 将取出的信息放到数据框
        jobInfo = DataFrame([item['position'], item['company'], item['place'], item['salary']]).T
        # 设置列名
        jobInfo.columns = ['职位名', '公司名', '工作地点', '薪资']
        # 将数据保存到本地
        jobInfo.to_csv('jobInfo.csv', encoding='gbk')  # 设置编码格式，防止乱码
        return item
