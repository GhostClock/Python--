### 需要在命令行下执行
from sys import argv

script,user_name = argv

prompt = '---->'

print "Hi %s, Im the %s script" % (user_name,script)
print "Id like to ask you a faw questions"
print "Do you link me %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s"% user_name
lives = raw_input(prompt)

print "What Kind of computer do you have ?"
computer = raw_input(prompt)

print """
Alrght ,so you said %r about linking me,
You live in %r ,Not sure Where that is,
And you hava a %r computer, Nice
"""  % (likes,lives,computer)


