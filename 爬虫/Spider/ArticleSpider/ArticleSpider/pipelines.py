# -*- coding: utf-8 -*-


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline

# 需要打开setting.py 里面的ITEM_PIPELINES

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


"""
自定义Pipeline
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
