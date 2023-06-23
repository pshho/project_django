import requests

url1 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail?'
page = 'page=1&'
perPage = 'perPage=100000&'
serviceKey = 'serviceKey=ibEJT6J0bl9WzpzbwJVPg9on2aBStbXKZnT8a7sLOTuEi5LMGvjsPAufQYld%2Br%2FvL6B4VhxXZ5EnI7j1GO%2B8uQ%3D%3D'

url2 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getUrbtyOfctlLttotPblancDetail?'
url3 = 'https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getRemndrLttotPblancDetail?'

reqUrl1 = url1 + page + perPage + serviceKey
reqUrl2 = url2 + page + perPage + serviceKey
reqUrl3 = url3 + page + perPage + serviceKey
result1 = requests.get(reqUrl1)
json_data1 = result1.json()

count = 0

data_list = []
# APT 분양정보 청약 접수 시작일
for data in json_data1['data']:
    if '보은 대신 센텀캐슬 아파트' == data['HOUSE_NM']:
        if '2023-06' in data['RCEPT_BGNDE']:
            data_list.append(data)
            count += 1
        elif '2023-07' in data['RCEPT_BGNDE']:
            data_list.append(data)
            count += 1
            # print(data)

print(data_list)

'''
# 오피스텔/도시형/민간임대 분양정보 청약 접수 시작일
result2 = requests.get(reqUrl2)
json_data2 = result2.json()

for data in json_data2['data']:
    if '2023-06' in data['SUBSCRPT_RCEPT_BGNDE']:
        data_list.append(data)
        count += 1
    elif '2023-07' in data['SUBSCRPT_RCEPT_BGNDE']:
        data_list.append(data)
        count += 1
        # print(data)

# APT 무순위/잔여세대 일반 공급 접수 시작일
result3 = requests.get(reqUrl3)
json_data3 = result3.json()

for data in json_data3['data']:
    if '2023-06' in data['SUBSCRPT_RCEPT_BGNDE']:
        data_list.append(data)
        count += 1
    elif '2023-07' in data['SUBSCRPT_RCEPT_BGNDE']:
        data_list.append(data)
        count += 1
        # print(data)

print(data_list)
print(count)


for data in data_list:
    if '평택현덕지역주택조합' in data['BSNS_MBY_NM']:
        print(data)

results = []
# count = 0

for data in data_list:
    if 'RCEPT_BGNDE' in data:
        result = {
            'title': data['HOUSE_NM'],
            'start': data['RCEPT_BGNDE']
        }
        # count += 1
        results.append(result)
    elif 'SUBSCRPT_RCEPT_BGNDE' in data:
        result = {
            'title': data['HOUSE_NM'],
            'start': data['SUBSCRPT_RCEPT_BGNDE']
        }
        # count += 1
        results.append(result)

print(results)
print(count)
'''