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

def parsePostData(postData):
    return convertHexData(postData.split(',', 3)[3])

postFile = sys.argv[1]
with open(postFile, 'r') as f:
    import csv
    for row in csv.reader(f):
        postData = convertHexData(row[3:])
        print(postData)

        payload = {'indent': 'on', 'q': 'encode_data:'+postData, 'sort': 'score desc',
                'wt': 'json', 'rows': '100', 'cursorMark': '*', 'fl': '*,score'}

        start = time.time()
        sumQtime = 0

        r = requests.get(
            'http://localhost:8983/solr/2gram/select', params=payload)
        print(r.json())
        nextCursorMark = r.json()['nextCursorMark']
        maxScore = r.json()['response']['maxScore']
        print(maxScore)
        print(float(r.json()['response']['docs'][-1]['score']))
        if float(r.json()['response']['docs'][-1]['score']) < maxScore * (2 / 3):
            break
        # print(r.json()['response']['docs'][-1]['score'])
        beforeCursorMark = ''

        while True:
            payload = {'indent': 'on', 'q': 'encode_data:'+postData, 'sort': 'id desc',
                       'wt': 'json', 'rows': '100', 'cursorMark': nextCursorMark, 'fl': '*,score'}
            r = requests.get(
                'http://localhost:8983/solr/2gram/select', params=payload)
            nextCursorMark = r.json()['nextCursorMark']
            # print(r.json()['response']['maxScore'])
            if float(r.json()['response']['docs'][-1]['score']) < maxScore * (2 / 3):
                break
            if nextCursorMark == beforeCursorMark:
                break
            beforeCursorMark = nextCursorMark

            # qtime
            sumQtime += r.json()['responseHeader']['QTime']
            print(sumQtime)

            elapsed_time = time.time() - start
            print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

        elapsed_time = time.time() - start
        print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
