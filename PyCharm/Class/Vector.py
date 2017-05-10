class Vector:
    __private = 0
    public = 0
    def __init__(self,a,b):
        self.a = a
        self.b = b

        self.__private += 1
        self.public += 1

    def __str__(self):
        return "Vector (%d %d)" % (self.a,self.b)

    def __add__(self, other):
        return Vector(self.a + other.a,self.b + other.b)

    def __privateMethod(self):
        print ""
    def publicMethod(self):
        print "public"


v1 = Vector(a = 2,b = 5)
v2 = Vector(a = 5,b = -1)

v1.publicMethod()


import re

line = "Cat are smarter \\\\\\ than dogs"
obj = re.match(r'(.*) are (.*?) .*',line,re.M | re.I)
if obj :
    print obj.group()
    print obj.group(1)
    print obj.group(2)
else:
    print "No Match"
