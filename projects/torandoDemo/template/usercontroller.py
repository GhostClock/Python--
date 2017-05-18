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
        self.render("index.html")


class UserHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        user_name = self.get_argument("username")
        user_email = self.get_argument("email")
        user_website = self.get_argument("website")
        user_language = self.get_argument("language")
        self.render("user.html",username = user_name,email = user_email,website = user_website,language = user_language) # 这里的参数必须和user.html的一直，否则会出现500错误


handlers = [
    (r'/',IndexHandler),
    (r'/user',UserHandler)
]

template_path = os.path.join(os.path.dirname(__file__),"template") #获取目录template的路径

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers,template_path)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()