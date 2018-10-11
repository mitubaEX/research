import sys
import glob

# python3 remove_files.py 2gram <length>


remove_files = []

birthmark = sys.argv[1]
length = int(sys.argv[2])

gre = open("./remove_files/" + birthmark + ".csv", "w")

for i in glob.glob("./birthmark_server/data/birthmark/*" + birthmark + "*"):
    import csv
    with open(i, 'r') as f:
        for row in csv.reader(f):
            # over length
            if len(row[3:]) >= length:
                gre.write(row[0] + "\n")
                # remove_files.append(row[0])
