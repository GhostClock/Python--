# coding:utf-8

class Parent:
    parenAttr = 100

    def __init__(self):
        print "父类的构造方法"

    def parentMethod(self):
        print "父类的方法"

    def setAttr(self,attr):
        Parent.parenAttr = attr

    def getAttr(self):
        print "父类属性",Parent.parenAttr

