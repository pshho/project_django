import csv
import pandas as pd

'''
with open('./polls/static/poll/resources/서울시부동산정보.csv', 'r') as r:
    data_list = csv.reader(r)
    ssg_list = []
    count = 0

    
    for data in data_list:
        print(data)
        break

    

    for data in data_list:
        if data[2] == '강남구':
            if data[7] != '' or data[8] != '' or data[15] != '':
                if data[8] != '0000':
                    result = [f"{data[2]}", f"{data[4]}", f"{data[7]}", f"{data[8]}"]
                    ssg_list.append(result)
                    count += 1
                elif data[8] == '0000':
                    result = [f"{data[2]}", f"{data[4]}", f"{data[7]}"]
                    ssg_list.append(result)
                    count += 1

        if len(ssg_list) > 999:
            break


print(ssg_list)
print(count)

with open('강남구.csv', 'w', newline='') as w:
    writer = csv.writer(w)
    writer.writerows(ssg_list)
'''

ssg_list = []
total_list = []
c1 = 0


for i in range(1, 26):
    with open(f'C:/Users/zptmz/OneDrive/바탕 화면/전월세,실거래가정보/서울시부동산전월세가{i}(위도,경도).csv', 'r') as r:
        data_list = csv.reader(r)

        for data in data_list:
            total_list.append(data)
            c1 += 1

'''
with open(f'C:/Users/zptmz/OneDrive/바탕 화면/전월세,실거래가정보/서울시부동산실거래가.csv', 'r') as r:
    data_list = csv.reader(r)

    for data in data_list:
        if '강서구' == data[2]:
            ssg_list.append(data)
            c1 += 1

            if c1 == 50:
                break
'''

with open('C:/Users/zptmz/OneDrive/바탕 화면/전월세,실거래가정보/서울시부동산전월세가(위도,경도).csv', 'w', newline='') as w:
    write = csv.writer(w)
    write.writerows(total_list)
    print('쓰기 성공')

print(c1)
# print(ssg_list)