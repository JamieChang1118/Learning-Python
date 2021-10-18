# split 字串切割

str = 'w=60.0,h=170.0'

w , h = (item.split('=')[1] for item in str.split(','))
print(w)
print(h)


print('\n--------------練習----------------')

str2 = '身高=160.0,體重=70.0'


h , w = (item.split('=')[1] for item in str2.split(','))
print(h)
print(type(w))



