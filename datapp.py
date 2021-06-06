import csv

dataset = []

with open('dataset_2.csv','r',newline='')as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset.append(row)

headers = dataset[0]
planets = dataset[1:]

for i in planets:
    i[2] = i[2].lower()
    
planets.sort(key = lambda planets:planets[0])

with open('planet.csv','a+',newline='')as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planets)