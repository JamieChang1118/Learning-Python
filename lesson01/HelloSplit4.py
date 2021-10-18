# split 字串切割

str = '體重=60.0,身高=170.0'


x = dict(item.split('=') for item in str.split(','))
print(type(x))
print(x)

print(x.get('體重'))
print(x.get('身高'))

