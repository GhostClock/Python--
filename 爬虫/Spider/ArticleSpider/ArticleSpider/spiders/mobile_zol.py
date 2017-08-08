# -*- coding: utf-8 -*-
import scrapy


class MobileZolSpider(scrapy.Spider):
    name = 'mobile_zol'
    allowed_domains = ['mobile.zol.com.cn']
    start_urls = ['http://mobile.zol.com.cn/650/6503851.html'] #http://mobile.zol.com.cn/

    def parse(self, response):

        title = response.css('.article-header.clearfix h1::text').extract()[0]  # 标题

        create_date = response.css('.article-aboute #pubtime_baidu::text').extract()[0]   # 创建日期

        tags = response.css('.article-aboute #source_baidu::text').extract()[0] #标签



        pass




