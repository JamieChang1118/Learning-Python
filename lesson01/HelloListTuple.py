
a = [20 , 30 , 10]
print(a)
print(len(a))
print("最大值: " + format(max(a)))
print("最小值: " + format(min(a)))

a.append(90)
print(a)

a.append([40,80])
print(a)

a.extend([60,50])
print(a)

a.insert(0 , 100)
print(a)

a = [100,90,80,70,60]
print(a[0])

print(a.index(90))

value = a.pop(0)
print("a.pop(0) = " , format(value))


a = [20,30,50,80,40,70,90]
a.sort()
print(a)

a.reverse()
print(a)

print('\n------------練習--------------')


