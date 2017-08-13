# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse


class CocoachinaSpider(scrapy.Spider):
    name = 'cocoachina'
    allowed_domains = ['http://www.cocoachina.com/']
    start_urls = ['http://www.cocoachina.com/ios/']
    first_request = True    # 判断是不是第一次请求
    def parse(self, response):

        # 解析列表中所有的url
        post_urls = response.css("#list_holder .clearfix.newstitle a::attr(href)").extract()
        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail, dont_filter=True)

        # 获取.下一页
        if self.first_request:
            next_pages = response.css("#page a::attr(href)").extract()[0:-1]
            for next_page in next_pages:
                if next_page:
                    self.first_request = False
                    yield Request(url=parse.urljoin(response.url, next_page), callback=self.parse, dont_filter=True)
        else:
            next_pages = response.css("#page a::attr(href)").extract()[7:-1]
            if len(next_pages) == 2:
                return None
            for next_page in next_pages:
                if next_page:
                    yield Request(url=parse.urljoin(response.url, next_page), callback=self.parse, dont_filter=True)


    def parse_detail(self, response):

        title = response.css("div.detail-main h2::text").extract()[0]   # 标题

        create_date = response.css("div.detail-main span.ml0::text").extract()[0]   # 创建时间

        author = response.css("div.detail-main #field_author::text").extract()[0]   #编辑

        category = response.css("div.detail-main div.p-ico.clearfix div span a::text").extract()[1] #分类

        source = response.css("div.detail-main div.p-ico.clearfix div span a::text").extract()[2]   # 来源

        comments = response.css("span#artical_comment_cnt::text").extract_first()    # 评论数

        views = response.css("div.float-r span:nth-child(2)::text").extract_first()     # 查看量

        content = response.css("#detailbody").extract_first()   # 内容

        print(title, create_date, author, category, source, comments, views)

        pass
