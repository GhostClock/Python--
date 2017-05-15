#!/usr/bin/python
# coding:utf-8

import xml.sax

class MovieHanderler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData    =   ""
        self.type           =   ""
        self.format         =   ""
        self.year           =   ""
        self.rating         =   ""
        self.stars          =   ""
        self.description    =   ""

    # 元素开始事件
    def startElement(self, name, attrs):
        self.CurrentData = name
        if name == "movie" :
            print "** Movie **"
            title = attrs['title']
            print "title: " , title

    # 元素结束事件
    def endElement(self, name):
        if self.CurrentData == "type":
            print "Type: " , self.type
        elif self.CurrentData == "format":
            print "format: ", self.format
        elif self.CurrentData == "year":
            print "year: ", self.year
        elif self.CurrentData == "rating":
            print "rating: ",self.rating
        elif self.CurrentData == "stars":
            print "stars: ",self.stars
        elif self.CurrentData == "description":
            print "description: ",self.description
        self.CurrentData == ""


    # 内容处理事件
    def characters(self,content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if (__name__ == "__main__"):

    # 创建一个xmlRander
    parser = xml.sax.make_parser()

    parser.setFeature(xml.sax.handler.feature_namespaces,0)

    # 重写ContextHander
    Handler = MovieHanderler()
    parser.setContentHandler(Handler)

    parser.parse("movies.xml")













