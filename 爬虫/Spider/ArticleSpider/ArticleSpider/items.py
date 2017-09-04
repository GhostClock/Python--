# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#   item的设计

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from ArticleSpider.utils.common import extract_num
import datetime
import re
from ArticleSpider.settings import SQL_DATETIME_FORMAT, SQL_DATE_FORMAT


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

    def get_insert_sql(self):
        insert_sql = """
                        insert into jobbole_article(
                        title, create_date, url, url_object_id, front_image_url, front_image_path,
                        praise_nums, comment_nums, fav_nums, tags, content
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                        fav_nums=VALUES (fav_nums),
                        
                    """

        params = (self["title"], self["create_date"], self["url"],
                  self["url_object_id"], self["front_image_url"],
                  self.get('front_image_url', "")[0], self["praise_nums"],
                  self["comment_nums"], self["fav_nums"],
                  self["tags"], self["content"])
        return insert_sql, params

#   中关村在线 - 手机频道
class mobile_colArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class mobile_zolArticleItem(scrapy.Item):
    title = scrapy.Field()

    url = scrapy.Field()

    url_object_id = scrapy.Field()

    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )

    create_date = scrapy.Field(
        input_processor=MapCompose(date_conver)
    )

    tags = scrapy.Field()

    author = scrapy.Field()

    editor = scrapy.Field()

    content = scrapy.Field()


class ZhihuQuestionItem(scrapy.Item):
    """
    知乎的问题Item
    """
    zhihu_id = scrapy.Field()

    topics = scrapy.Field()

    url = scrapy.Field()

    title = scrapy.Field()

    content = scrapy.Field()

    answer_num = scrapy.Field()

    comments_num = scrapy.Field()

    watch_num = scrapy.Field()

    click_num = scrapy.Field()

    crawl_num = scrapy.Field()

    def get_insert_sql(self):
        # 插入知乎question表的sql语句
        insert_sql = """
            insert into zhihu_question (
              zhihu_id, topics, url, title,
              content, answer_num, comments_num, 
              watch_user_num, click_num, crawl_time
            )VALUES (
              %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s
            )
            ON DUPLICATE KEY UPDATE
             topics=VALUES (topics), 
             title=VALUES (title),
             content=VALUES (content),
             answer_num=VALUES (answer_num),
             comments_num=VALUES (comments_num),
             watch_user_num=VALUES (watch_user_num),
             click_num=VALUES (click_num),
             crawl_time=VALUES (crawl_time)
        """
        zhihu_id = self["zhihu_id"][0]
        topics = ",".join(self["topics"])
        url = self["url"][0]
        title = "".join(self["title"])
        content = "".join(self["content"])
        answer_num = extract_num("".join(self["answer_num"]))
        comments_num = extract_num("".join(self["comments_num"]))

        if len(self["watch_num"]) == 2:
            watch_user_num = int(self["watch_num"][0])
            click_num = int(self["watch_num"][1])
        else:
            watch_user_num = int(self["watch_num"][0])
            click_num = 0

        crawl_time = datetime.datetime.now().strftime(SQL_DATETIME_FORMAT)

        params = (
            zhihu_id, topics, url, title,
            content, answer_num, comments_num,
            watch_user_num, click_num, crawl_time
        )

        return insert_sql, params


class ZhihuAnswerItem(scrapy.Item):
    """
    知乎的问题回答Item
    """
    zhihu_id = scrapy.Field()

    url = scrapy.Field()

    question_id = scrapy.Field()

    author_id = scrapy.Field()

    content = scrapy.Field()

    parise_num = scrapy.Field()

    comments_num = scrapy.Field()

    create_time = scrapy.Field()

    update_time = scrapy.Field()

    crawl_time = scrapy.Field()

    def get_insert_sql(self):
        # 插入知乎question表的sql语句
        insert_sql = """
            insert into zhihu_answer (
              zhihu_id, url, question_id, 
              author_id, content, comments_num, 
              praise_num, create_time, 
              update_time, crawl_time
            )
             VALUES (
              %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s
            )
            ON DUPLICATE KEY UPDATE
             content=VALUES (content), 
             comments_num=VALUES (comments_num),
             praise_num=VALUES (praise_num),
             update_time=VALUES (update_time)
        """
        create_time = datetime.datetime.fromtimestamp(self["create_time"]).strftime(SQL_DATETIME_FORMAT)
        update_time = datetime.datetime.fromtimestamp(self["update_time"]).strftime(SQL_DATETIME_FORMAT)
        params = (
            self["zhihu_id"], self["url"],
            self["question_id"], self["author_id"],
            self["content"], self["comments_num"],
            self["parise_num"], create_time, update_time,
            self["crawl_time"].strftime(SQL_DATETIME_FORMAT)
        )

        return insert_sql, params