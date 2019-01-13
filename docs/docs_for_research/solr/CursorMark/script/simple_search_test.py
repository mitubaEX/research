import requests
import time

payload = {'indent': 'on', 'q': '*:*', 'sort': 'id desc',
           'wt': 'json', 'rows': '3982010'}

start = time.time()
sumQtime = 0

r = requests.get(
    'http://localhost:8983/solr/uc/select', params=payload)


# qtime
sumQtime += r.json()['responseHeader']['QTime']
print(sumQtime)

elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
