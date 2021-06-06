import csv

data1 = []
data2 = []

with open('dataset_1.csv','r',newline='')as f:
    csvreader = csv.reader(f)
    for rows in csvreader:
        data1.append(rows)

with open('planet.csv','r',newline='')as p:
    csvreader = csv.reader(p)
    for rows in csvreader:
        data2.append(rows)

header1 = data1[0]
header2 = data2[0]
planets1 = data1[1:]
planets2 = data2[1:]

headers = header1 + header2

planets = []

for i,data in enumerate(planets1):
    planets.append(planets1[i]+planets2[i])

with open('write.csv','a+',newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planets)
