def say_hi(name):
    print "Hi, " + name

say_hi("Michael")
say_hi("Andrew")
say_hi("jay")

def say_hi2():
    return "Hi"

greeting = say_hi2()
print greeting
print say_hi2()

greeting2 = say_hi
greeting2("tt")

greeting3 = say_hi("ss")
greeting3
