#!/usr/bin/env python
# coding=utf-8

# 这是项目的入口文件,里面包含 if __name__ == '__main__' ，从这里启动项目和服务

import tornado.ioloop
import tornado.options
import tornado.httpserver

import sys

from application import application

from tornado.options import define,options
define('port',default=8000,help="run on the given port",type=int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print "Development server is runing at http://127.0.0.1:%s/" % options.port
    print "Quit the server with Ctrl-C"
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()

