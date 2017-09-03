# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from scrapy.http import Request
from scrapy.loader import ItemLoader    # ItemLoader来生成Item
from urllib import parse

from ArticleSpider.items import JobboleArticleItem, ArticleItemLoader

from ArticleSpider.utils.common import get_md5


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
        post_nodes = response.css('#archive div.floated-thumb div.post-thumb a')
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")   # 为了获取标题图片
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url),meta={"front_image_url": image_url}, callback=self.parse_detail)

        # 提取下一页并提交给scrapy进行下载
        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        article_item = JobboleArticleItem()

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

        """
        # 通过css选择器提取字段
        front_image_url = response.meta.get("front_image_url", "")  # 文章封面图

        title = response.css(".entry-header h1::text").extract_first()

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
            comment_nums = 0 # 没有评论

        content = response.css("div.entry").extract()[0]

        tags = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        tag_list = [elment for elment in tags if not elment.strip().endswith("评论")]
        tags = ",".join(tag_list)

        print(title, create_date, praise_nums, comment_nums, tags)


        
        #   给Item填充值
        article_item["title"] = title
        try:
            create_date = datetime.datetime.strptime(create_date, "%Y/%m/%d").date()
        except Exception as error:
            create_date = datetime.datetime.now().date()
        article_item["create_date"] = create_date
        article_item["url"] = response.url
        article_item["url_object_id"] = get_md5(response.url)
        article_item["front_image_url"] = [front_image_url]  # 改为数组
        article_item["praise_nums"] = praise_nums
        article_item["comment_nums"] = comment_nums
        article_item["fav_nums"] = fav_nums
        article_item["tags"] = tags
        article_item["content"] = content
        """


        """
        通过item Loader来加载Item  ----> 在以后的开发中都是用ItemLoader来解析值
        """
        front_image_url = response.meta.get("front_image_url", "")  # 文章封面图
        item_loader = ArticleItemLoader(item=JobboleArticleItem(), response=response)

        item_loader.add_css("title", ".entry-header h1::text")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
        item_loader.add_value("front_image_url", [front_image_url])
        item_loader.add_css("praise_nums", ".vote-post-up h10::text")
        item_loader.add_css("comment_nums", "a[href='#article-comment'] span::text")
        item_loader.add_css("fav_nums", "span.bookmark-btn::text")
        item_loader.add_css("tags", "p.entry-meta-hide-on-mobile a::text")
        item_loader.add_css("content", "div.entry")

        article_item = item_loader.load_item()

        """
        传递到pipeline类里面去
        """
        yield article_item
