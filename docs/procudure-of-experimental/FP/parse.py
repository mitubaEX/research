import re

# s = '''
# 0.0--------------
# aaaaaa
# bbbbb
# 0.1--------------
# aaaaaa
# bbbbb
# 0.2--------------
# 0.3--------------
# 0.4--------------
# 0.5--------------
# 0.6--------------
# 0.7--------------
# 0.8--------------
# 0.9--------------
# 0.0--------------
# 0.1--------------
# 0.2--------------
# 0.3--------------
# 0.4--------------
# 0.5--------------
# 0.6--------------
# 0.7--------------
# 0.8--------------
# 0.9--------------
# '''
#
# count = 0
# l = re.split("[0-1]\.[0-9]--------------", s)
# print(l)
# for i in l[1:]:
#     if count == 10:
#         count = 0
#     print(count)
#     for m in i.split('\n'):
#         if m == '':
#             continue
#         print(m)
#     count += 1

import sys

file1 = sys.argv[1]

c = 0
print('{0},{1},{2},{3},{4}'.format('narrow_count', 'elapsed_time', 'comparison', 'correct_count', 'count'))
with open(file1) as f:
    s = f.read()
    l = re.split("[0-1]\.[0-9]--------------", s)
    for i in l[1:]:
        if c == 10:
            c = 0
        print('%d,' % c, end='')
        narrow_count = 0
        elapsed_time = 0
        comparison = 0
        correct_count = 0
        count = 0
        for m in i.split('\n'):
            if m == '':
                continue
            # print(m)
            if 'narrow_count' in m:
                narrow_count += float(m.replace('narrow_count: ', ''))
            elif 'elapsed_time:' in m:
                elapsed_time += float(m.replace('elapsed_time:', '').replace('[sec]', ''))
            elif 'comparison: ' in m:
                comparison += float(m.replace('comparison: ', '').replace(' ns', ''))
            elif 'correct_count: ' in m:
                spl = m.split(',')
                correct_count += float(spl[0].replace('correct_count: ', ''))
                count += float(spl[1].replace('count: ', ''))
        print('{0},{1},{2},{3},{4}'.format(narrow_count, elapsed_time, comparison, correct_count, count))
        c += 1
