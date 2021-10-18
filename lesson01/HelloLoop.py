
import random

for x in [1,2,8,9,10]:
    print(x , end=",")
print('\n------------------------')


for x in range(1,11):
    print(x , end=" , ")
print('\n------------------------')

for x in range(10):
    print(x,end=" , ")
print('\n------------------------')

for x in range(1,11,2):
    print(x , end=" , ")
print('\n------------------------')

for x in range(1 , 11):
    if x % 3 == 0:
        continue
    if x % 8 == 0:
        break
    print(x , end=" , ")
print('\n------------------------')


while True:
    x = random.randint(1 , 10)
    if x % 2 == 0:
        print(x , end=" , ")
    else:
        break
print('\n------------------------')

n = 5
while n > 0:
    print("Python" , end=" , ")
    n -= 1

print('\n--------練習----------------')

while True:
    aa = random.randint(1,11)
    print('{}是偶數喔'.format(aa) if aa % 2 == 0 else '{}是奇數喔'.format(aa))
    break

