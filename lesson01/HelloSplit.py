# split 字串切割

str = '60.0,170.0'
data = str.split(',')
print(type(data))

w = float(data[0])
h = float(data[1])
bmi = w / pow(h/100 , 2)
print('w = %.1f h = %.1f bmi = %.2f' %(w , h , bmi))


print('\n------------練習------------------')

str = '160.0,70.0'

h , w = str.split(',')
print(h)
print(w)