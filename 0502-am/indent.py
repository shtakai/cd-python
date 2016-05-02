

def say_hello(name):
    if name:
        print 'Hello, ' + name + ' from inside the function'
    else:
        print 'no name'

print 'outside of the function'


say_hello('sushi bento')
