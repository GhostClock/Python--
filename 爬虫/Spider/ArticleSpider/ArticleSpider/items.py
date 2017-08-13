# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#   item的设计

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobboleArticleItem(scrapy.Item):
    title = scrapy.Field()  # 文章标题

    create_date = scrapy.Field()    # 创建时间

    url = scrapy.Field()    # 文章URL

    url_object_id = scrapy.Field()

    front_image_url = scrapy.Field()    # 封面图

    front_image_path = scrapy.Field()   # 封面图本地存放路径

    praise_nums = scrapy.Field()    # 点赞数

    comment_nums = scrapy.Field()   # 评论数

    fav_nums = scrapy.Field()  # 收藏数

    tags = scrapy.Field()   # 标签

    content = scrapy.Field()    # 文章



