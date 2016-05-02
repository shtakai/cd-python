for count in range(0, 5):
    pass
    # print "looping -", count

my_list = [4, 'dog', 99, ['list', 'inside', 'another'], 'hello world']
for element in my_list:
    # print element
    pass

count = 0
while count < 5:
    # print "looping = ", count
    count += 1

for value in "string":
    if value == 'i':
        continue
    # print value

class EmptyClass:
    pass

for val in "sashimi":
    pass


x = 3
y = x
while y > 0:
    print y
    y = y - 1
else:
    print "final else statement"

print 
x = 3
y = x
while y > 0:
    print y
    y = y - 1
    if y == 1:
        break
else:
    print "final else statement"
