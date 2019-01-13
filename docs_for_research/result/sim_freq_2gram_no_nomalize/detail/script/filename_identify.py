import sys
import csv
import collections

count = 0
other = 0

with open(sys.argv[1], 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if float(row[3]) >= 0.75:
            # if row[0] == row[2]:
                # count += 1
            # else:
            other += 1
print(count, other)
