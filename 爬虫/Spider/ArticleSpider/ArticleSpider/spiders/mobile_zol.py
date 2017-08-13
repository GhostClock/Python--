# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse

class MobileZolSpider(scrapy.Spider):
    name = 'mobile_zol'
    allowed_domains = ['mobile.zol.com.cn']
    # start_urls = ['http://mobile.zol.com.cn/650/6503851.html'] #http://mobile.zol.com.cn/
    start_urls = ['http://mobile.zol.com.cn/more/2_428.shtml']

    def parse(self, response):

        # 解析列表页中所有文章url, 并交给scrapy下载后并进行解析
        post_urls = response.css(".content-mod ul.content-list.imglazyload li div.info-mod.clearfix div.info-head a::attr(href)").extract()
        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

        # 提取下一页并提交给scrapy进行下载
        next_url = response.css(".page a.next::attr(href)").extract_first("")
        if next_url :
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)


    def parse_detail(self, response):

        title = response.css('.article-header.clearfix h1::text').extract()[0]  # 标题 ---> 疑问:为什么这里总是报 “IndexError: list index out of range”

        create_date = response.css('.article-aboute #pubtime_baidu::text').extract()[0]   # 创建日期

        tags = response.css('.article-aboute #source_baidu::text').extract()[0]     # 标签

        author = response.css('.article-aboute a::text').extract()[0]

        editor = response.css('.article-aboute #editor_baidu::text').extract()[0]

        content = response.css("#article-content").extract()[0]

        print(title, create_date, tags, author, editor)

        pass




