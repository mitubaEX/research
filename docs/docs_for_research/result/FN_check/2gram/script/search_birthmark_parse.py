import csv
import sys
import collections

dic = collections.defaultdict(lambda: 0)

with open(sys.argv[1], 'r') as f:
    res = csv.reader(f, delimiter='=')
    for row in res:
        dic[len(row[0].split(',')[3:])] += 1
for i in dic.keys():
    print('{0},{1}'.format(i, dic[i]))
