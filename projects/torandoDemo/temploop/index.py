#!/usr/bin/env python
# coding:utf-8

import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


from tornado.options import define,options
define("port",default=8000,help="run on the give port",type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        lst = ["google","www.google.com","baidu","www.baidu.com"] #定义一个list
        self.render("index.html",info=lst)  # 讲定义的list传递给模板


handlers = [
    (r'/',IndexHandler),
]

template_path = os.path.join(os.path.dirname(__file__),"temploop") #模板路径
static_path = os.path.join(os.path.dirname(__file__),"stitic") #这里增加设置了静态路径


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers,template_path,static_path,debug=True) # 这里也增加了static 这里的debug=true的目的是为了让torando不重启也能够体现已经修改的代码功能
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()









