import math

def calcArea(r):
    pi = math.pi
    area = pow(r,2) * pi
    return area

print(calcArea(10) , calcArea(20))


print('\n----------------------------------')

# 有無預設值
def calcArea2(r=10):
    if (r == None):
        print('請輸入半徑')
        return 0

    pi = math.pi
    area = pow(r, 2) * pi
    return area

print(calcArea2())


print('\n---------------練習-------------------')

def calc2(r):
    area2 = pow(r , 2) * math.pi
    return area2

print(calc2(5))