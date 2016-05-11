class Underscore(object):
    def __init__(self):
        pass

    def map(self, obj, proc):
        return list(map(proc, obj))

    def reduce(self, obj, proc):
        return reduce(proc, obj)

    def find(self, obj, proc):
        return filter(proc, obj)[0] if filter(proc, obj) else None

    def filter(self, obj, proc):
        return filter(proc, obj)

    def reject(self, obj, proc):
        return list(set(obj) - set(self.filter(obj, proc)))

_ = Underscore()

print _.reduce([1, 2, 3, 4, 5, 6], lambda x,y: x+y )
print _.find([1, 2, 3, 4, 5, 6], lambda x: x==5 )
print _.map([1, 2, 3, 4, 5, 6], lambda x: x*2 )
print _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
