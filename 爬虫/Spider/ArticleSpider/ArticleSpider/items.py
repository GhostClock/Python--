# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#   item的设计

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

import datetime
import re


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def add_jobbole(value):
    return value + "-jobbole"


#   处理日期
def date_conver(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as error:
        create_date = datetime.datetime.now().date()

    return create_date


#   获得数字
def get_nums(value):
    match_re = re.match(r".*?(\d+).*", value)

    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums


def remove_comment_tags(value):
    #   去掉tag提取的评论
    if "评论" in value:
        return ""
    else:
        return value


def return_value(value):
    #   这做起到了没有修改原来值的目的
    return value


class ArticleItemLoader(ItemLoader):
    #   自定义itemloader
    default_output_processor = TakeFirst()


class JobboleArticleItem(scrapy.Item):
    title = scrapy.Field()  # 文章标题

    create_date = scrapy.Field(
        input_processor=MapCompose(date_conver)
    )    # 创建时间

    url = scrapy.Field()    # 文章URL

    url_object_id = scrapy.Field()

    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)   # 还可以覆盖掉default_output_processor
    )    # 封面图 -----> 这里一定要是数组，否则会有异常

    front_image_path = scrapy.Field()   # 封面图本地存放路径

    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )    # 点赞数

    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )   # 评论数

    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )  # 收藏数

    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(",")
    )   # 标签

    content = scrapy.Field()    # 文章



