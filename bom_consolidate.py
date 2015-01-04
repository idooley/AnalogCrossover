#!/opt/local/bin/python3.4

import csv
import sys

counts = {}
description = {}

qty = 3

with open(sys.argv[1], newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        digikeypart = row[2].strip()
        part = row[0].strip()
        if digikeypart != "ResDef" :
            if digikeypart in counts:
                counts[digikeypart] = counts[digikeypart] + 1
                description[digikeypart] = description[digikeypart] + " " + part
            else:
                counts[digikeypart] = 1
                description[digikeypart] = part

for digikeypart in counts:
    print (digikeypart + "," + str(counts[digikeypart] * 3) + "," + description[digikeypart])
