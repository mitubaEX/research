import requests
import time
import sys


def convertHexData(row_birthmark):
    hex_row = ""
    for j in row_birthmark:
        for i in j.split(' '):
            try:
                hex_row += hex(int(i)).replace('0x', '')
            except:
                return row_birthmark
        hex_row += ','
    return hex_row


import os
os.makedirs('search_result', exist_ok=True)
postFile = sys.argv[1]
with open(postFile, 'r') as f:
    import csv
    for row in csv.reader(f):
        if len(row[3:]) <= int(sys.argv[2]):
            break
        postData = convertHexData(row[3:])
        print(postData)

        payload = {'indent': 'on', 'q': 'encode_data:'+postData, 'sort': 'score desc',
                   'wt': 'json', 'rows': '1000', 'fl': '*,score'}

        start = time.time()
        sumQtime = 0

        r = requests.get(
            'http://localhost:8983/solr/2gram/select', params=payload)
        maxScore = float(r.json()['response']['maxScore'])
        print(maxScore)
        print(float(r.json()['response']['docs'][-1]['score']))
        starts = 1000
        while True:
            with open('search_result/'+row[0]+'2gram', 'w') as write_file:
                write_file.write(','.join(row) + '\n')
                for result in r.json()['response']['docs']:
                    if float(result['score']) < maxScore * (2 / 3):
                        break
                    write_file.write('{0},{1},{2},{3}\n'.format(
                        result['filename'], result['score'], result['barthmark'], result['data'].replace('quot;', '')))
            if float(r.json()['response']['docs'][-1]['score']) < maxScore * (2 / 3):
                break
            payload = {'indent': 'on', 'q': 'encode_data:'+postData,
                       'wt': 'json', 'rows': '1000', 'fl': '*,score', 'start': starts}
            r = requests.get(
                'http://localhost:8983/solr/2gram/select', params=payload)
            starts += 1000
            # qtime
            sumQtime += r.json()['responseHeader']['QTime']
            print('{0}, {1}'.format(maxScore, float(
                r.json()['response']['docs'][-1]['score'])))
            print(sumQtime)
            elapsed_time = time.time() - start
            print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

        elapsed_time = time.time() - start
        print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
