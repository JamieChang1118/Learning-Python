
exam = {'國文':80 , '數學':100 , '英文':90}
print(exam)
print(len(exam))
exam['英文'] = 85
print(exam)
exam['地理'] = 90
print(exam)

exam2 = exam.copy()
print(exam2)
print(exam2.get('地理'))
print('地理成績 = {}'.format(exam2.get('地理')))

if '英文' in exam:
    print('英文成績 = {}'.format(exam2.get('英文')))
else:
    print('沒有此成績')

print('\n--------------------------')

sum = 0
for key in exam:
    print('{}分數 = {}'.format(key , exam.get(key)))
    sum += exam.get(key)
print('總分 = {}'.format(sum))
print('平均 = {}'.format(sum/len(exam)))

print('\n--------------------------')

subjects = exam.keys()
print(subjects)

scores = exam.values()
print(scores)

print('\n--------------------------')

for s in subjects:
    print(s)

for sc in scores:
    print(sc)

print('\n--------------------------')

for k , v in exam.items():
    print('key = {} , value = {}'.format(k , v))

print('\n--------------------------')

print(exam)
print(exam.get('國文'))
print(exam.setdefault('國文' , 0))
print(exam.get('體育'))
print(exam.setdefault('體育' , 60))
print(exam)

print('\n--------------------------')

print(exam)
exam_add = {'自然':95 , '地科':85}
exam.update(exam_add)
print(exam)
exam.clear()
print(exam)


