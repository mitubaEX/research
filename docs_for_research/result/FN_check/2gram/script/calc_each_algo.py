def jaccard(x, y):
    """
    Jaccard index
    Jaccard similarity coefficient
    https://en.wikipedia.org/wiki/Jaccard_index
    """
    x = frozenset(x)
    y = frozenset(y)
    return len(x & y) / float(len(x | y))


def overlap(x, y):
    """
    overlap coefficient
    Szymkiewicz-Simpson coefficient)
    https://en.wikipedia.org/wiki/Overlap_coefficient
    """
    x = frozenset(x)
    y = frozenset(y)
    return len(x & y) / float(min(map(len, (x, y))))


def dice(x, y):
    """
    Dice's coefficient
    Sørensen-Dice coefficient
    https://en.wikipedia.org/wiki/Dice%27s_coefficient
    """
    x = frozenset(x)
    y = frozenset(y)
    return 2 * len(x & y) / float(sum(map(len, (x, y))))


import sys
import csv
import Levenshtein

with open(sys.argv[1]) as f:
    reader = csv.reader(f, delimiter='-')
    next(reader)
    for row in reader:
        print(row[0] + '-------' + row[1])
        print(jaccard(row[0].split(','), row[1].split(',')))
        print(overlap(row[0].split(','), row[1].split(',')))
        print(dice(row[0].split(','), row[1].split(',')))
        print(Levenshtein.distance(row[0], row[1]))
