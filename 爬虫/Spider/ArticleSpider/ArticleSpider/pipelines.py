# -*- coding: utf-8 -*-


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import codecs   # 避免文件编码的繁杂工作
import json

from scrapy.exporters import JsonItemExporter

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


"""
自定义Pipeline图片下载
"""
class ArticleImagePipeline(ImagesPipeline):
    """
    重写item_completed
    """
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_file_path = value['path']
        item['front_image_path'] = image_file_path

        return item
