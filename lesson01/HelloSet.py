
import random

x = {}
print(type(x))

x = set()
print(type(x))

x = {1 , 2 , 3 , 3}
print(x)
print(len(x))

x.add(4)
x.add(5)
print(x)

x.remove(3)
print(x)

print('\n----------------------------------')

# 電腦選號 1-46 不重複 選6個

lotto = set()

while len(lotto) < 6 :
    lotto.add(random.randint(1,46))
print(lotto)

