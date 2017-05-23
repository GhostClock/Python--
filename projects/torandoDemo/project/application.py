#!/usr/bin/env python
# coding=utf-8

# 这个文件的核心任务是完成tornado.web.Application()的实例化

from url import url

import tornado.web
import os

setting = dict(
    template_path = os.path.join(os.path.dirname(__file__),"template"),
    static_path = os.path.join(os.path.dirname(__file__),"static"),
)

application = tornado.web.Application(
    handlers=url,
    **setting
)




