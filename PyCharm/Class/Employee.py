# coding: UTF-8
class Employee :
    '==我是文档=='
    empCount = 0 #类变量 只可以在类的所有实例之间共享

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name :",self.name,", Salary:",self.salary



em = Employee("Ghost","123")
em.displayEmployee()

# em.age = 7
# del  em.age

print getattr(em,'name')
print hasattr(em,'age')
setattr(em,'one',10000)
print em.one

delattr(em,"one")

print Employee.__doc__ #文档
print Employee.__name__ #获取类名
print Employee.__module__ #类定义所在的模块
print Employee.__bases__ #类的所有父类构成的元素
print Employee.__dict__ #类的属性