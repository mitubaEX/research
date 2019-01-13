import sys


class Row:
    row1 = ''
    row2 = ''
    sim = 0.0

    def __init__(self, row1, row2, sim):
        self.row1 = row1
        self.row2 = row2
        self.sim = sim


def changeOrderOfRow(a, b):
    if a > b:
        return b + ',' + a
    return a + ',' + b


gre = open("pre_result_remove/" + sys.argv[2] + 'pre_0.75_greater.csv', 'w')
sma = open("pre_result_remove/" + sys.argv[2] + 'pre_0.75_smaller.csv', 'w')

# print(sys.argv[1].split('.')[0].split('_')[0])
remove_files = open("./remove_files/" +
                    sys.argv[2] + ".csv")
dic = {}

import csv
tmp_remove_list = list(csv.reader(remove_files, delimiter='\n'))
removed_list = []
for i in tmp_remove_list:
    # removed_list.append(i[0].split('.')[-1])
    removed_list.append(i[0])

# print(removed_list)
# removed_list = sum(removed_list, [])
# print(removed_list)
row_list = []

with open(sys.argv[1], 'r') as f:
    for row in csv.reader(f):
        if len(row) >= 2:
            if row[0] not in removed_list:
                continue
            if row[1] not in removed_list:
                continue
            # dic key contain and dic values contain
            elm = changeOrderOfRow(row[0], row[1])
            if elm not in list(dic.keys()):
                dic[elm] = float(row[2])
                if float(row[2]) >= 0.75:
                    gre.writelines('{0},{1}\n'.format(row[0], row[1]))
                # else:
                #     sma.writelines('{0},{1}\n'.format(row[0], row[1]))
                # row_list.append(Row(row[0], row[1], float(row[2])))

            # if row[0] not in list(dic.keys()):
            #     if row[1] not in list(dic.values()):
            #         if row[1] not in list(dic.keys()):
            #             if row[0] not in list(dic.values()):
            #                 dic[row[0]] = row[1]
            #                 row_list.append(Row(row[0], row[1], float(row[2])))

            # if float(row[2]) >= 0.75:
            #     gre.writelines('{0},{1}\n'.format(row[0], row[1]))
            # else:
            #     sma.writelines('{0},{1}\n'.format(row[0], row[1]))

# for row in row_list:
#     if float(row.sim) >= 0.75:
#         gre.writelines('{0},{1}\n'.format(row.row1, row.row2))
#     else:
#         sma.writelines('{0},{1}\n'.format(row.row1, row.row2))
