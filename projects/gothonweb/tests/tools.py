from nose.tools import *

import re

def assert_response(resp, contains = None,metches = None,headers = None,status = "200"):
    assert status in resp.status, "Excepted response %r not in %r" % (status,resp.status)

    if status == "200" :
        assert resp.data, "Respone data is empty"

    if contains :
        assert contains in resp.data, "Respone does not contain %r" % contains

    if metches :
        reg = re.compile(metches)
        assert reg.matches(resp.data), "Respone does not match %r" % matches

    if headers :
        assert_equal(resp.headers,headers)