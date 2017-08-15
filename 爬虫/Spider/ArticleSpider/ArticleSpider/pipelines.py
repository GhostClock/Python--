# -*- coding: utf-8 -*-


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import codecs   # 避免文件编码的繁杂工作
import json
import pymysql
import pymysql.cursors

from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi   # adbapi 可以把M数据库操作变成异步化的操作

# 需要打开setting.py 里面的ITEM_PIPELINES

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

"""
以Json文件保存
"""
class JsonWithEncodeingPipeline(object):
    """
    自定义Json文件的导出
    """
    def __init__(self):
        self.file = codecs.open("article.json", 'w', encoding="utf-8")

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"  # ensure_ascii=False 放置写入中文出错
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


class JsonItemExporterPipeline(object):
    """
    调用scrapy提供的json exporter导出json文件
    """

    def __init__(self):
        self.file = open("articleExporter.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item



class MysqlPipleline(object):
    """
    把数据插入到Mysql数据库中 -> 当插入数据库的速度比解析速度慢很多时，就会阻塞 同步操作
    """
    def __init__(self):
        self.conn = pymysql.connect('192.168.0.100', 'root', 'admin123', 'article_spider', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into jobbole_article(
            title, create_date, url, url_object_id, front_image_url, front_image_path,
            praise_nums, comment_nums, fav_nums, tags, content
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        self.cursor.execute(insert_sql,
                            (item["title"], item["create_date"], item["url"], item["url_object_id"],
                             item["front_image_url"], item.get('front_image_url', "")[0], item["praise_nums"], item["comment_nums"],
                             item["fav_nums"], item["tags"], item["content"]))
        self.conn.commit()


class MysqlTwistedPiplines(object):
    """
    用Twisted框架来异步插入数据库 -> 异步 Twisted提供的是异步的容器
    """
    def __init__(self, dbpool):
        self.dbpool = dbpool

    #   会把setting传进来，可以任意读取
    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBANAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparms)  # 连接池 可变参数 面试可能会问到

        return cls(dbpool)

    def process_item(self, item, spider):
        #   使用Twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)     # 处理异常

    def handle_error(self, failuer, item, spider):
        #   处理异步插入的异常
        print(failuer)

    def do_insert(self, cursor, item):
        #   执行具体的插入
        insert_sql = """
                    insert into jobbole_article(
                    title, create_date, url, url_object_id, front_image_url, front_image_path,
                    praise_nums, comment_nums, fav_nums, tags, content
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

        cursor.execute(insert_sql,
                        (item["title"], item["create_date"], item["url"], item["url_object_id"],
                        item["front_image_url"], item.get('front_image_url', "")[0], item["praise_nums"],
                        item["comment_nums"], item["fav_nums"], item["tags"], item["content"])
                       )



"""
自定义Pipeline图片下载
"""
class ArticleImagePipeline(ImagesPipeline):
    """
    重写item_completed
    """
    def item_completed(self, results, item, info):
        if "front_image_url" in item:
            for ok, value in results:
                image_file_path = value['path']
            item['front_image_path'] = image_file_path

        return item
