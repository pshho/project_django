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

with open('./polls/static/poll/resources/강남구.csv', 'r') as r:
    data_list = csv.reader(r)
    ssg_list = []
    count = 0

    for item in data_list:
        if len(item) >= 4:
            result = item[0] + ' ' + item[1] + ' ' + item[2] + ' ' + item[3]
            ssg_list.append(result)
            count += 1
        else:
            result = item[0] + ' ' + item[1] + ' ' + item[2]
            ssg_list.append(result)
            count += 1

print(ssg_list)
print(count)