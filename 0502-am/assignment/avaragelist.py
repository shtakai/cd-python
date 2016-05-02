a = [1, 2, 5, 10, 255, 3]

size = len(a)

a_sum = 0
for value in a:
    a_sum += value

# print 'manually', (1+2+5+10+255+3)/6
print a_sum / size
