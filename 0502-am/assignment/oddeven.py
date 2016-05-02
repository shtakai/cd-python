
def count2000():
    for value in range(1,2001):
        condition = ''
        if value % 2 == 0:
            condition = "an even"
        else:
            condition = "an odd"
        print "Number is {}.  This is {} number.".format(value, condition)

count2000()
