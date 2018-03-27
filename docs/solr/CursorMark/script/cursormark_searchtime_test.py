import requests
import time

payload = {'indent': 'on', 'q': '*:*', 'sort': 'id desc',
           'wt': 'json', 'rows': '1000', 'cursorMark': '*'}

start = time.time()
sumQtime = 0

r = requests.get(
    'http://localhost:8983/solr/uc/select', params=payload)
# print(r.json()['response']['docs'])
nextCursorMark = r.json()['nextCursorMark']
beforeCursorMark = ''

while True:
    payload = {'indent': 'on', 'q': '*:*', 'sort': 'id desc',
               'wt': 'json', 'rows': '1000', 'cursorMark': nextCursorMark}
    r = requests.get(
        'http://localhost:8983/solr/uc/select', params=payload)
    nextCursorMark = r.json()['nextCursorMark']
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
