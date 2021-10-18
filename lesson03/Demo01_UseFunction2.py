# 不定數量的參數 *args

def getSum(*score):
    return sum(score)

print(getSum(100,90) , getSum(100,90,80))


print('\n----------------------------------')

# 帶名字的參數

def printExamInfo(no , *score , **info):
    print('座號:' , no)
    print('總分:' , sum(score))
    print('學生資料:', info)

printExamInfo(2 , 100 , 80 , 90 , 姓名='John' , 年齡='18')


print('\n----------------------------------')

# 函數的參考作用域

def changeScore(s , i , score):
    s[i] = score

scores = [100,90,80]
print(scores)
changeScore(scores , 1 , 100)
print(scores)


print('\n----------------------------------')

# 區域變數與全域變數

score = 90

def updateScore():
    global score
    score = 100

print(score)
updateScore()
print(score)


print('\n-------------練習---------------------')