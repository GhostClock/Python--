# -*- coding=utf-8 -*-
__author__ = 'ghostclock'

from scrapy.cmdline import execute

import sys
import os

# print(os.path.dirname( os.path.abspath(__file__)))
sys.path.append(os.path.dirname( os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "jobbole"]) # 在终端启动想要运行的Spider命令 ->$:scrapy crawl xxxx
execute(['scrapy','crawl','mobile_zol'])