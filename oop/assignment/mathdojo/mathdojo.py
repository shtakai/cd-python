class Mathdojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *args):
        for i in args:
            self.result += i
        return self

    def subtract(self, *args):
        for i in args:
            self.result -= i
        return self

    def result(self):
        return result


# part 1
print Mathdojo().add(2).add(2, 5).subtract(3, 2).result
# print Mathdojo().add(2).add(2, 5).result



class Mathdojo2(object):
    def __init__(self):
        self.result = 0

    def add(self, *args):
        for i in args:
            if self.is_tuple_or_list(i):
                for j in i:
                    self.result += j
            else:
                self.result += i
        return self

    def subtract(self, *args):
        total = 0
        for i in args:
            if self.is_tuple_or_list(i):
                for j in i:
                    total += j
            else:
                total += i
        self.result -= total
        return self

    def result(self):
        return result

    def is_tuple_or_list(self,obj):
        return isinstance(obj,list) or isinstance(obj,tuple)


# Part 2
print Mathdojo2().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result

# Part 3
print Mathdojo2().add(( 1 ),3,4).add([3, 5, 7, 8], ( 2, 4.3, 1.25 )).subtract(2, ( 2,3 ), [1.1, 2.3]).result

