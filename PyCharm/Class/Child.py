# coding:utf-8
import Parent

class Child(Parent.Parent): # 模块名.类名 才可以
    def __init__(self):
        print "子类的构造方法"

    def childMethod(self):
        print "子类的方法 childMethod"

    def parentMethod(self):
        print "重写后的父类方法"



c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

print c

if issubclass(Child,Parent.Parent) :
    print "YES"
if isinstance(c,Child) :
    print "YES"

cc = Parent.Parent()

print cc


