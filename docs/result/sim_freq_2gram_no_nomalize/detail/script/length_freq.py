import sys
import csv
import collections

length_freq = collections.defaultdict(lambda: 0)

with open(sys.argv[1], 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if float(row[1]) >= 0.75:
            length_freq[row[0]] += 1

for i in length_freq.keys():
    print('{0},{1}'.format(i, length_freq[i]))
