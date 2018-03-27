import sys
import csv

filename = sys.argv[1]
each_threshold_rows_count = [0, 0, 0, 0, 0]

with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if float(row[0]) < 0.5:
            if float(row[1]) >= 0.75:
                each_threshold_rows_count[1] += 1
            else:
                each_threshold_rows_count[2] += 1


print(each_threshold_rows_count)
