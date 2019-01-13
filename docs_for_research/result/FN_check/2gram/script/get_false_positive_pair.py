import sys
import csv

filename = sys.argv[1]

with open(filename, 'r') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if float(row[0]) <= 0.5:
            if float(row[1]) >= 0.75:
                print(row[0], row[1])
                print(i)
        i += 1
