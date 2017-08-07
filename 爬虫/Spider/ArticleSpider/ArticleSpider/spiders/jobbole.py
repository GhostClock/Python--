# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        1. 获取文章列表页中的文章url,并交给scrapy下载后并进行解析
        2. 获取下一页url并交给scrapy进行下载，下载完成后交给parse
        """

        # 解析列表页中所有文章url,并交给scrapy下载后并进行解析
        post_urls = response.css('#archive div.floated-thumb div.post-thumb a::attr(href)').extract()
        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

        # 提取下一页并提交给scrapy进行下载
        next_urls = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_urls :
            yield Request(url=parse.urljoin(response.url, next_urls), callback=self.parse)


    def parse_detail(self, response):
        # 提取文章的具体字段

        # 通过xpath提取文章具体字段
        """
        title = response.xpath('//*[@id="post-112051"]/div[1]/h1/text()').extract_first("") #extract_first("")提取不到，返回为空

        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace(" ·","")

        praise_nums = response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0]

        fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        match_re = re.match(r".*?(\d+).*", fav_nums)
        if match_re :
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0

        comment_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract_first("")
        match_re = re.match(r".*?(\d+).*", comment_nums)
        if match_re:
            comment_nums = int(match_re.group(1))
        else:
            comment_nums = 0 #没有评论

        content = response.xpath("//div[@class='entry']").extract()[0]

        tags = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        tag_list = [elment for elment in tags if not elment.strip().endswith("评论")]
        tags = ",".join(tag_list)

        print(title, create_date, praise_nums, comment_nums, tags)
        """

        # 通过css选择器提取字段
        title = response.css(".entry-header h1::text").extract()

        create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace(" ·","")

        praise_nums = response.css(".vote-post-up h10::text").extract()[0]

        fav_nums = response.css("span.bookmark-btn::text").extract()[0]
        match_re = re.match(r".*?(\d+).*", fav_nums)

        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0

        comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        match_re = re.match(r".*?(\d+).*", comment_nums)
        if match_re:
            comment_nums = int(match_re.group(1))
        else:
            comment_nums = 0 #没有评论

        content = response.css("div.entry").extract()[0]

        tags = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        tag_list = [elment for elment in tags if not elment.strip().endswith("评论")]
        tags = ",".join(tag_list)

        pass
