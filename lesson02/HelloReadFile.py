file = open('demo.txt','r', encoding='utf-8')
data = file.read()
print(data)

# 逐行讀取
file = open('demo.txt','r', encoding='utf-8')
row1 = file.readline()
row2 = file.readline()
print(row1.strip('\n'))
print(row2)

print('\n--------------------------------------')

file = open('demo.txt','r', encoding='utf-8')
for row in file.readlines():
    print(row.strip(' \n0'))     # 濾掉斷行和空白

print('\n----------------練習----------------------')

