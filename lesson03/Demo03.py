
f = lambda : print('Lambda OK')
f()


f2 = lambda x , y : x if x > y else y
print(f2(10,20))


def max(x , y):
    return x if x > y else y

f3 = lambda x , y : max(x , y)
print(f3(50,40))

print('\n--------------------------')

print({'A':100 , 'B':80}.get('C', None))    # 沒有 C 所以印出 None

{'1': lambda : print('男') , '2': lambda : print('女')}.get('3' , lambda : print('Error'))()

