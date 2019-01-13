import sys
import csv

filename = sys.argv[1]
each_threshold_rows_count = [0, 0, 0, 0, 0]

with open(filename, 'r') as f:
    reader = list(csv.reader(f))
    for index, row in enumerate(reader):
        if float(row[0]) <= 1.0:
            if float(row[1]) >= 0.75:
                each_threshold_rows_count[0] += 1
                # print(index)
            else:
                each_threshold_rows_count[1] += 1
                # pass

print(each_threshold_rows_count)
