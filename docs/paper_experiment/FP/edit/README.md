# edit distanceの評価

## editの検索時間

```
/Volumes/mituba_20180425/restart/edit_restart ❯❯❯ sed 's/elapsed_time://g' 2gram_time.csv | sed 's/\[sec\]//g' | gowk sum
7118.484686374664 sec
```

## editの比較時間

```
./Tool -m compare -b "$i" -f row_search_script.sh -i ../search_result_"$thre"  734.54s user 135.46s system 125% cpu 11:35.21 total
./Tool -m compare -b "$i" -f row_search_script.sh -i ../search_result_"$thre"  723.79s user 135.62s system 117% cpu 12:10.57 total
./Tool -m compare -b "$i" -f row_search_script.sh -i ../search_result_"$thre"  689.97s user 122.70s system 121% cpu 11:07.76 total
./Tool -m compare -b "$i" -f row_search_script.sh -i ../search_result_"$thre"  615.15s user 100.25s system 128% cpu 9:17.42 total
./Tool -m compare -b "$i" -f row_search_script.sh -i ../search_result_"$thre"  518.22s user 72.22s system 143% cpu 6:52.01 total
./Tool -m compare -b "$i" -f row_search_script.sh -i ../search_result_"$thre"  240.84s user 20.59s system 193% cpu 2:14.78 total
./Tool -m compare -b "$i" -f row_search_script.sh -i ../search_result_"$thre"  153.81s user 15.26s system 165% cpu 1:42.02 total
./Tool -m compare -b "$i" -f row_search_script.sh -i ../search_result_"$thre"  143.23s user 14.91s system 161% cpu 1:37.97 total
./Tool -m compare -b "$i" -f row_search_script.sh -i ../search_result_"$thre"  140.82s user 14.44s system 161% cpu 1:36.42 total
./Tool -m compare -b "$i" -f row_search_script.sh -i ../search_result_"$thre"  140.08s user 14.30s system 160% cpu 1:35.95 total
```

```
11:35.21 sec
12:10.57
11:07.76
9:17.42
6:52.01
2:14.78
1:42.02
1:37.97
1:36.42
1:35.95

## 秒に直した
695.21
730.57
667.76
557.42
412.01
134.78
102.02
97.97
96.42
95.95

## 逆にした
95.95
96.42
97.97
102.02
134.78
412.01
557.42
667.76
730.57
695.21
```


## 速度比

```
0.9	489.37%
0.8	489.40%
0.7	489.51%
0.6	489.78%
0.5	492.01%
0.4	510.81%
0.3	520.68%
0.2	528.16%
0.1	532.42%
0	530.02%
```

速度が半端なく遅いのでもうだめ
