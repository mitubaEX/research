import csv
import sys
import collections

dic = collections.defaultdict(lambda: 0)

with open(sys.argv[1], 'r') as f:
    for row in csv.reader(f, delimiter='-'):
        dic[len(row[0].split(','))] += 1

for i in dic.keys():
    print('{0},{1}'.format(i, dic[i]))
