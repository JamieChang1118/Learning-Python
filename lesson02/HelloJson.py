import json

# Json 資料
x = '{"name":"john" , "age":18}'
person = json.loads(x)  # Json 字串轉 Json 物件
print(type(person))
print(person['name'])

print('\n-------------------------------')

# 巢狀 Json 資料
x = '{"name":"john" , "age":18 , "profile":{"w":60.0 , "h":170.0}}'
person = json.loads(x)
print(type(person))
print(person['profile']['w'])

print('\n-------------------------------')
# 陣列 Json 資料
x = '[{"name":"john" , "age":18 , "profile":{"w":60.0 , "h":170.0}},' \
    '{"name":"john" , "age":18 , "profile":{"w":60.0 , "h":170.0}}]'

person = json.loads(x)
print(type(person))
for p in person:
    w = float(p['profile']['w'])
    h = float(p['profile']['h'])
    bmi = w / pow(h/100 , 2)
    print("%.2f" %(bmi))


print('\n--------------練習-----------------')

x = '[{"name":"john" , "age":18 , "profile":{"w":60.0 , "h":170.0}},' \
    '{"name":"jim" , "age":18 , "profile":{"w":60.0 , "h":180.0}}]'

data = json.loads(x)
person1 = data[0]['name']
person2 = data[1]['name']

print(person1 + '\n' + person2)