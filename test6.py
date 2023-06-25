import csv

s1 = []
s2 = []
s3 = []
c1 = 0
c2 = 0
c3 = 0

with open('C:/Users/zptmz/OneDrive/바탕 화면/전월세,실거래가정보/서울시부동산전월세가.csv', 'r') as r:
    data_list = csv.reader(r)

    for data in data_list:
        s1.append(data)
        c1 += 1

with open('C:/Users/zptmz/OneDrive/바탕 화면/전월세,실거래가정보/서울시부동산전월세가(위도,경도).csv', 'r') as r:
    data_list2 = csv.reader(r)

    for data in data_list2:
        s2.append(data)
        c2 += 1

for item1 in s1:
    for item2 in s2:
        if item1[2] + ' ' + item1[4] + ' ' + item1[7].lstrip('0') + ' ' + item1[8].lstrip('0') == item2[0]:
            if item1 + [str(item2[1])] + [str(item2[2])] not in s3:  # 중복 추가 방지
                s3.append(item1 + [str(item2[1])] + [str(item2[2])])
                c3 += 1

with open('C:/Users/zptmz/OneDrive/바탕 화면/전월세,실거래가정보/서울시부동산전월세가,위도경도추가.csv', 'w', newline='') as w:
    write = csv.writer(w)
    write.writerows(s3)

print(f'{s3}\n')
print(c3)
print('쓰기 성공')