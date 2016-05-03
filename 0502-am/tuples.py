tuple_data = ('tokyo', 'japan', 1999, 2000)
tuple_num = (1, 2, 3, 4, 5)
tuple_letter = "a", "b", "sashimi", "ramen"

# print tuple_data
# print tuple_num
# print tuple_letter

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# print julia[2]

for data in julia:
    print data

# not work
# julia[0] = "A"


julia += ("Eat Pray Love", 2010)
julia = julia[3:] + ("Eat Pray Love", 2010)

# print julia
# print len(julia)
# print min(julia)

# not work
# print sum(julia)

value =("Sashimi", "udon", "hell")
(name, position, company) = value
# print name, position, company

a = "x"
b = "y"

# tmp = a
# a = b
# b = tmp
(a, b) = (b, a)

# print a, b
# print sum( (1, 2, 5))
# print all((1, 2, 5))
# print  any((0,1))

for index, item in enumerate(julia):
    pass
    # print(str(index), str(item))

# print sorted(("ss",2,3,5,3))
num = (1,5,"aaa",3,4,2,333)
# print tuple(reversed(num))
# print tuple(sorted(num))
# print list(reversed(num))
# print reversed(num)

import math

def get_circle_area(r):
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)

print get_circle_area(20)
