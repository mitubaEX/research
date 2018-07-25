import sys

with open(sys.argv[1], 'r') as f:
    import csv
    reader = csv.reader(f)
    for row in reader:
        for i in row[0].split('\t'):
            li = list(map(float, i.split(':')))
            if (len(li) == 3):
                sum = 0
                sum += li[0]*3600.0
                sum += li[1]*60.0
                sum += li[2]
                print(sum, end=" ")
            else:
                sum = 0
                sum += li[0]*60.0
                sum += li[1]
                print(sum, end=" ")
        print()
