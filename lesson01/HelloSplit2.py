# split 字串切割

str = '60.0,170.0'
w , h = str.split(',')
print(w)
print(h)


print('\n-------------練習-----------------')

str2 = '160.0,70.0'
h , w = str2.split(',')
h = float(h)
w = float(w)
bmi = w / pow(h/100 , 2)
print(bmi)