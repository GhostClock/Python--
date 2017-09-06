# -*- coding=utf-8 -*-
__author__ = 'ghostclock'

from ArticleSpider.utils.zheye import zheye

z = zheye()
positions = z.Recognize('../../cn.gif')
print(positions)