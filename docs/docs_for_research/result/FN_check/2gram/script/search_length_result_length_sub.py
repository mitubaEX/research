import csv
import sys
import collections

dic = collections.defaultdict(lambda: 0)

with open(sys.argv[1], 'r') as f:
    for row in csv.reader(f, delimiter='-'):
        if len(row[0].split(',')) - len(row[1].split(',')) <= -1:
            print(row[0] + '-' + row[1])
        # dic[len(row[0].split(',')) - len(row[1].split(','))] += 1

        # for i in dic.keys():
        #     print('{0},{1}'.format(i, dic[i]))
