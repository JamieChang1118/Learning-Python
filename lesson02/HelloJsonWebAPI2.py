import json
import requests

url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json&limit=1000'

youbike = requests.get(url).text
youbike = json.loads(youbike)
# print(youbike)

for item in youbike['result']['records']:
    sna = item['sna']
    bemp = int(item['bemp'])  # 還車
    sbi = int(item['sbi'])    # 借車
    if bemp >= 20 and sbi >= 20:
        print("%s bemp=%d sbi=%d" %(sna,bemp,sbi))


print('\n-------------------練習------------------------')