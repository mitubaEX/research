import sys
import csv

filename = sys.argv[1]
fp_075 = 0
fp_05 = 0
fp_025 = 0
other = 0

with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if float(row[1]) < 0.75:
            break
        if float(row[0]) >= 0.75:
            fp_075 += 1
        elif float(row[0]) >= 0.5:
            fp_05 += 1
        elif float(row[0]) >= 0.25:
            fp_025 += 1
        else:
            other += 1


print('0.75: {0}, 0.5: {1}, 0.25: {2}, other: {3}'.format(
    fp_075, fp_05, fp_025, other))
