import sys
import csv

filename = sys.argv[1]
greater_than_count = 0
greater_than_count_075 = 0
greater_than_count_05 = 0
greater_than_count_025 = 0
seach_sim = [0, 0, 0]
other = 0

with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if float(row[0]) > float(row[1]):
            if float(row[1]) >= 0.75:
                greater_than_count_075 += 1
            if float(row[1]) >= 0.5:
                greater_than_count_05 += 1
            if float(row[1]) >= 0.25:
                greater_than_count_025 += 1

            if float(row[0]) >= 0.75:
                seach_sim[0] += 1
            if float(row[0]) >= 0.5:
                seach_sim[1] += 1
            if float(row[0]) >= 0.25:
                seach_sim[2] += 1

            greater_than_count += 1
        else:
            other += 1

print('greater_than_count: {0}, 0.75: {1}, 0.5: {2}, 0.25: {3}, 0.75: {4}, 0.5: {5}, 0.25: {6}, other: {7}'.format(
    greater_than_count, greater_than_count_075, greater_than_count_05, greater_than_count_025, seach_sim[0], seach_sim[1], seach_sim[2], other))
