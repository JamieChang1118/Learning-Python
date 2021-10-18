def add(x):
    return x + 1

def sub(x):
    return x - 1

def calc(func , x):
    r = func(x)
    return r

print(add(3))
print(sub(3))

print(calc(add , 3))
print(calc(sub , 3))

print(calc(add , 4))