from sys import argv

script,fileName = argv

print "We will going to erase %r " % fileName
print "If you dont want that ,Hit CTRL-C"
print "If you do want that ,Hit RETURN"

raw_input("?")

print "Opening the file..."

target = open(fileName,'w')
print "Truncating the file ,Good Bye"
target.truncate()

print "Now Im going to ask you for three lines"

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "Im going to write there to the file"

target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")
print "And finally, we close it"
target.close()

try:
    pass
except :
    pass