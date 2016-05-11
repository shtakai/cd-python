def x():
    print "-" * 50

n1 = [3,2,4,6,5]
print sorted(n1)
x()

an = ["monkey", "emu", "giraffe", "monkey", "seal"]
print sorted(an)
x()

print sorted( an, key=lambda x: x.find("e") )

x()
f = lambda num: num*2
print f(2)
f = lambda a,b: a*a + b*b
print f(3,4)
x()

# callback
print sorted(an, key=lambda x: x.find("e"))

# by length
print sorted(an, key=lambda x: len(x))
# by 3rd letter
print sorted(an, key=lambda x: x[2])
# sin
import math
print sorted(an, key=lambda x: math.sin(ord(x[-1])))
x()

# key parameter on dictionary
data = {
        'alpha'   : 4,
        'bravo'   : 2,
        'charie'  : 7,
        'delta'   : 1,
        'echo'    : 5,
        'foxtrot' : 3
        }
print min(data, key=lambda x: data[x])
print max(data, key=lambda x: data[x])
x()

# other uses
print list(map(lambda x: x*(x+1), n1))
print list(filter(lambda x: x%2==0, n1))
# print list(reject(lambda x: x%2==0, n1))

x()
# reduce
print reduce(lambda a,b: a+b, n1)
print reduce(lambda a,b: a*b, n1)
print reduce(lambda a,b: b**(a%b), n1)
x()

# implemented way
print [i**i for i in n1]
print [i for i in n1 if i%2==0]
print [i for i in n1 if i%2!=0]
print [i for i in n1 if not i%2==0]

print sum(n1)
print sum(i for i in n1)



