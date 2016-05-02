
def multiply(array, times):
    result = []
    for value in array:
        result.append(value * times)
    return result

a = [2, 4, 10, 16]
b = multiply(a, 5)
print b
