from nose.tools import *

# 这一坨代码是为了消除 ImportError: No module named 错误
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import WWW


def setup():
    print "SETUP"

def teardown():
    print "TEAR DOWN"

def test_basice():
    print "I RAN"