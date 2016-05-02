def add(a,b):
    x = a + b
    return x

sum1 = add(4, 6)
sum2 = add(1, 4)
sum3 = sum1 + sum2
print sum1
print sum2
print sum3
# another way
print add(sum1, sum2)

#not work
print add(1,"sashimi")
