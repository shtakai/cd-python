def varargs(arg1, *rest):
    print "Got", arg1, ' and '.join(rest)

varargs("one")
varargs("one", "two")
varargs("one", "two", "three")

