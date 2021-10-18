import random

poker1 = ['♠A','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K']
poker2 = ['♥A','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥J','♥Q','♥K']
poker3 = ['♦A','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦J','♦Q','♦K']
poker4 = ['♣A','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K']

poker = poker1 + poker2 + poker3 + poker4

# 洗牌
random.shuffle(poker)
#print(poker)

sum = 0.0
# for item in poker[:2]:   # 取牌取幾張
#     num = item[1:2]
#     print(num)
#     # 判斷取到的牌的點數
#     if num.isdigit() :   # 2-10點
#         sum += int(num)
#     elif num == 'A':
#         sum += 1
#     else:
#         sum += 0.5
# print(sum)   # 計算點數總和

# for item in poker[:5]:
#     play = input('是否要牌 ? y=要 n=不要 ?')
#     if play == 'n':
#         break
#     num = item[1:2]
#     if num.isdigit():
#         sum += int(num)
#     elif num == 'A':
#         sum += 1
#     else:
#         sum += 0.5
#
#     print('抽到 %s 總點數 %.1f' %(num , sum))
#
#     if sum == 10.5:
#         print('厲害唷!!!')
#         break
#     elif sum > 10.5:
#         print('爆了喔...')
#         break
#
# print(sum)

print('\n----------------------------------')

p1 = ['♠A','♠2','♠3']
p2 = ['♦A','♦2','♦3']
p3 = p1 + p2

random.shuffle(p3)
print(p3)

sum = 0.0
for item in p3[:5]:
    ask = input('要取牌嗎? y or n ?')

    if ask == 'n':
        break

    num = item[1:2]
    if num.isdigit():
        sum += int(num)
    elif num == 'A':
        sum += 1
    else:
        sum += 0.5

    print('拿到 %s  目前總點數 %.1f' %(num , sum))

    if sum > 8:
        print('掛了喔')
        break
    elif sum == 8:
        print('不錯喔')
        break

print(sum)