import glob
import sys

# python3 pro.py 2gram 0.25


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


gre = open('pro_result/' + sys.argv[1] +
           '.csv', 'w')
# sma = open('pro_result/' + sys.argv[1] +
#            'pre_' + sys.argv[2] + '_smaller.csv', 'w')

dic = {}
row_list = []
for filename in glob.glob("./false_negative/search_result/*" + sys.argv[1] + "*"):
    with open(filename, 'r') as f:
        import csv
        reader = csv.reader(f)
        header = next(reader)
        max_score = 0.0
        for row in reader:
            try:
                max_score = max(float(row[1]), max_score)
            except:
                continue
            elm = changeOrderOfRow(header[0], row[0])
            # print(len(row))
            # if len(row) >= 2:
            #     if row[0] not in list(dic.keys()):
            #         if row[1] not in list(dic.values()):
            #             if row[1] not in list(dic.keys()):
            #                 if row[0] not in list(dic.values()):
            #                     dic[row[0]] = row[1]
            #                     row_list.append(
            #                         Row(header[0], row[0], float(row[1]) / max_score))
            if len(row) >= 2:
                if elm not in row_list:
                    row_list.append(elm)
                    # if float(row[1]) / max_score >= float(sys.argv[2]):
                    gre.writelines('{0},{1}\n'.format(header[0], row[0]))
                    # else:
                    #     sma.writelines('{0},{1}\n'.format(header[0], row[0]))

# for row in row_list:
#     if float(row.sim) >= float(sys.argv[2]):
#         gre.writelines('{0},{1}\n'.format(row.row1, row.row2))
#     else:
#         sma.writelines('{0},{1}\n'.format(row.row1, row.row2))
