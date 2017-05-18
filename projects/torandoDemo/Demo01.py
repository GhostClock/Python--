#!/usr/bin/env python
# coding:utf-8

import tornado.httpserver  # 是用来解决web服务器的http协议问题,提供了不少属性和方法,实现客户端和服务端的互通,tornado的非阻塞和单线程的特点就在这个模型中体现出来
import tornado.ioloop  # 能够实现非阻塞socket循环,不能互通一次就结束了
import tornado.options  # 命令行解析模块
import tornado.web  # 必不可少的模块,它提供了一个简单的Web框架与异步功能,从而使其扩展到大量打开的连接,使其成为理想的长轮询


# 这两行显示了所谓的『命令行解析模块』的用途
# 在这里通过tornado.options.define()定义了访问本服务器的端口
from tornado.options import define,options
define("port",default=8000,help="run on the give port",type=int)

# 定义请求 - 处理程序类
# 所谓处理程序类,就是定义一个类,专门应付客户端向服务器提出的请求(这个请求也许是要读取某个页面，也许是要将某些消息存到服务器上)，服务器要有相应的程序来接受并处理这个请求，并且反馈某些消息
# (或者针对请求反馈所要的消息，或者返回其他的错误消息等)
# 类的名称首字母要大写,如果这个类是请求处理程序类,最好用Handler结尾,这样在名称上就很明确,是干什么的
# tornado.web.RequestHandler 这个参数很重要，是专门用于完成请求处理程序的,通过它定义get(),post()两个在web中应用最多的两个方法内容,
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting',"Hello") # 在这句中，当实例化后,self对应的就是tornado.web.RequestHandler,而get_argument就是tornado.web.RequestHandler的一个方法
        self.write(greeting + ', welcom you to read:www.mysite.com')# write也是tornado.web.RequestHandler的一个方法,这个方法的主要功能是向客户端反馈参数中的消息



if __name__ == '__main__':
    tornado.options.parse_command_line()  # 这是在执行tornado的解析命令行，在tornado的程序中，只要import这个模块之后,就会在运行的时候自动加载
    app = tornado.web.Application(handlers=[(r"/",IndexHandler)]) # 将tornado.web.Application实例化,这个实例化，本质上是建立了整个网站程序的请求处理集合,然后它可以被Httpserver做为参数调用,实现http协议服务器访问
    http_server = tornado.httpserver.HTTPServer(app) # HTTPServer是tornado.options里面定义的类,HTTPServer是一个单线程非阻塞HTTP服务器，
    http_server.listen(options.port) # 执行HTTPServer一般要回调Application对象,并提供发送响应的接口
    tornado.ioloop.IOLoop.instance().start() # 表示可以接受来自HTTP的请求了


