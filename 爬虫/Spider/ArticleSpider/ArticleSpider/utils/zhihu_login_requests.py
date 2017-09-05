# -*- coding=utf-8 -*-
__author__ = 'ghostclock'

"""
模拟知乎登录
"""
import requests
import re
import json
import time
import os.path
from ArticleSpider.utils.zheye import zheye
try:
    import cookielib
except:
    import http.cookiejar as cookielib
try:
    from PIL import Image
except:
    pass

user_agent = 'Mozilla/5.0 (Linux; Android 7.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
header = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    "User-Agent": user_agent
}


session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies.txt')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")

#
def get_index():
    response = session.get("https://www.zhihu.com/", headers=header)
    with open("index_page.html", 'wb') as f:
        f.write(response.text.encode("utf-8"))
    print("OK")

#   获取xsrf
def get_xsrf():
    """
    获取_xsrf
    :return: _xsrf value
    """
    response = session.get("https://www.zhihu.com/", headers=header)
    # print(response.text)
    match_obj = re.match('.*name="_xsrf" value="(.*?)"', response.text)
    if match_obj:
        _xsrf = match_obj.group(1)
        print("_xsrf: %s", _xsrf)
        return _xsrf
    else:
        return ""


# 获取验证码
def get_ver_code():
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=header)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()

    # 用pillow 的 Image 显示验证码
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha


def zhihu_login(account, password):
    def post_request(post_url, login_key):
        post_data = {
            "_xsrf":  get_xsrf(),
            login_key: account,
            "password": password
        }
        # 不需要验证码直接登录成功
        login_page = session.post(post_url, data=post_data, headers=header)
        code = login_page.status_code
        if code == 200:
            login_code = login_page.json()
            if login_code.get('r') == 1:
                # 不输入验证码登录失败
                # 使用需要输入验证码的方式登录
                post_data["captcha"] = get_ver_code()
                login_page = session.post(post_url, data=post_data, headers=header)
                login_code = login_page.json()
                print(login_code['msg'])
        else:
            print(login_page.content)
        # 保存 cookies 到文件，
        # 下次可以使用 cookie 直接登录，不需要输入账号和密码
        session.cookies.save()

    #   知乎登录
    if re.match("^1\d{10}", account):
        print("手机号码登录")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_request(post_url, "phone_num")

    else:
        if "@" in account:
            print("邮件登录")
            post_url = "https://www.zhihu.com/login/email"
            post_request(post_url, "email")

def is_login():
    # 通过个人中心页面返回状态码来判断是否为登录状态
    inbox_url = "https://www.zhihu.com/inbox"
    response = session.get(inbox_url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True


zhihu_login("", "")
get_index()
# is_login()