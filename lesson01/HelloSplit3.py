# split 字串切割

str = 'w=60.0,h=170.0'

w , h = (item.split('=')[1] for item in str.split(','))
print(w)
print(h)


