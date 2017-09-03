# -*- coding: utf-8 -*-
import scrapy
import re
import time
import os.path
import json
from scrapy.http import FormRequest,Request
try:
    from PIL import Image
except:
    pass


"""
用scrapy模拟登录知乎
"""
class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    _xsrf = ""

    user_agent_Android = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
    user_agent_FireFox = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
    headers = {
        "Host": "www.zhihu.com",
        "Referer": "https://www.zhihu.com/",
        "User-Agent": user_agent_FireFox
    }

    def parse(self, response):
        #   深度优先
        pass

    def parse_detail(self, response):
        pass

    def start_requests(self):
        """
        第一次请求
        :return:
        """
        return [FormRequest(url="https://www.zhihu.com/#signin",
                            headers=self.headers,
                            callback=self.init)]

    def init(self, response):
        match_obj = re.match(b'.*name="_xsrf" value="(.*?)"',
                             response.body, re.DOTALL)  # 匹配全局，换行
        if match_obj:
            self._xsrf = match_obj.group(1)

        t = str(int(time.time() * 1000))
        captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
        return Request(captcha_url,
                       headers=self.headers,
                       callback=self.login)

    def get_ver_code(self, response):
        with open('captcha.jpg', 'wb') as f:
            f.write(response.body)
            f.close()
        # 用pillow 的 Image 显示验证码
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except IOError as e:
            print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
        captcha = input("输入验证码\n>")
        return captcha

    def login(self, response):
        post_url = "https://www.zhihu.com/login/email"
        post_data = {
            "_xsrf": self._xsrf,
            "email": "",
            "password": "",
            "captcha": self.get_ver_code(response)
        }
        return [FormRequest(
            url=post_url,
            formdata=post_data,
            headers=self.headers,
            callback=self.check_login
        )]

    def check_login(self, response):
        # 验证服务器的返回判断是否成功
        text_json = json.loads(response.text)
        print(text_json["msg"])

        if "msg" in text_json and "登录成功" == text_json["msg"]:
            for url in self.start_urls:
                yield Request(url, dont_filter=True, headers=self.headers)


