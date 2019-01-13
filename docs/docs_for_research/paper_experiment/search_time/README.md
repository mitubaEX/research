## 0.25

### 検索時間

```
/Volumes/mituba_20180425/restart/2gram ❯❯❯ cat time_2gram.csv | sed 's/elapsed_time://g' | sed 's/\[sec\]//g' | awk '{a+=$1} END {print a }'                     master ✱
551.455 sec

## 3gram
295.639

## 4gram
102.067

## 5gram
72.807

## 6gram
64.3604

## uc
/Volumes/mituba_20180425/restart/sim_0.25 ❯❯❯ cat time_uc.csv | sed 's/elapsed_time://g' | sed 's/\[sec\]//g' | awk '{a+=$1} END {print a }'                   master ✱ ◼
179.524
```
### 比較時間

```
/Volumes/mituba_20180425/restart/sim_0.25 ❮❮❮ for i in 2gram 3gram 4gram 5gram 6gram ; do time ./sim_0.25 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i" -r 231476 -l 15;done
../../activemq-protobuf-test-1.1.jar-2gram.csv
./sim_0.25 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i  509.12s user 65.59s system 143% cpu 6:40.54 total
../../activemq-protobuf-test-1.1.jar-3gram.csv
./sim_0.25 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i  352.15s user 44.80s system 133% cpu 4:56.87 total
../../activemq-protobuf-test-1.1.jar-4gram.csv
./sim_0.25 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i  289.56s user 34.64s system 134% cpu 4:00.42 total
../../activemq-protobuf-test-1.1.jar-5gram.csv
./sim_0.25 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i  200.24s user 22.61s system 151% cpu 2:27.37 total
../../activemq-protobuf-test-1.1.jar-6gram.csv
./sim_0.25 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i  156.07s user 16.10s system 166% cpu 1:43.28 total

/Volumes/mituba_20180425/restart/sim_0.25 ❯❯❯ for i in uc ; do time ./sim_0.25 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i" -r 231476 -l 15;done
../../activemq-protobuf-test-1.1.jar-uc.csv
./sim_0.25 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i  222.68s user 22.16s system 188% cpu 2:10.05 total
```

## 0.5


```

## 検索時間
/Volumes/mituba_20180425/restart/sim_0.5 ❯❯❯ for i in 2gram 3gram 4gram 5gram 6gram uc ; do cat time_"$i".csv | sed 's/elapsed_time://g' | sed 's/\[sec\]//g' | awk '{a+=$1} END {print a }';done
372.692
448.015
496.216
494.379
721.027
139.361

## 比較時間
/Volumes/mituba_20180425/restart/sim_0.5 ❯❯❯ for i in 2gram 3gram 4gram 5gram 6gram uc ; do time ./sim_0.5 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i" -r 231476 -l 15;done

../../activemq-protobuf-test-1.1.jar-2gram.csv
./sim_0.5 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i"  206.02s user 20.78s system 178% cpu 2:07.26 total
../../activemq-protobuf-test-1.1.jar-3gram.csv
./sim_0.5 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i"  168.07s user 18.10s system 171% cpu 1:48.83 total
../../activemq-protobuf-test-1.1.jar-4gram.csv
./sim_0.5 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i"  149.38s user 16.46s system 167% cpu 1:39.15 total
../../activemq-protobuf-test-1.1.jar-5gram.csv
./sim_0.5 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i"  120.47s user 13.18s system 163% cpu 1:21.57 total
../../activemq-protobuf-test-1.1.jar-6gram.csv
./sim_0.5 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i"  118.47s user 13.08s system 161% cpu 1:21.51 total
../../activemq-protobuf-test-1.1.jar-uc.csv
./sim_0.5 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i"  120.66s user 12.79s system 167% cpu 1:19.71 total
```

## 0.75

```
/Volumes/mituba_20180425/restart/sim_0.75 ❯❯❯ for i in 2gram 3gram 4gram 5gram 6gram uc ; do cat time_"$i".csv | sed 's/elapsed_time://g' | sed 's/\[sec\]//g' | awk '{a+=$1} END {print a }';done
78.6733
100.671
82.8259
73.2421
73.0622

/Volumes/mituba_20180425/restart/sim_0.75 ❯❯❯ cat time_uc.csv | sed 's/elapsed_time://g' | sed 's/\[sec\]//g' | awk '{a+=$1} END {print a }'                   master ✱ ◼
334.713
```

### 比較時間

```
/Volumes/mituba_20180425/restart/sim_0.75 ❯❯❯ for i in 2gram 3gram 4gram 5gram 6gram uc ; do time ./sim_0.75 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i" -r 231476 -l 15;done
../../activemq-protobuf-test-1.1.jar-2gram.csv
./sim_0.75 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i  161.36s user 17.69s system 162% cpu 1:50.22 total
../../activemq-protobuf-test-1.1.jar-3gram.csv
./sim_0.75 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i  145.83s user 15.90s system 165% cpu 1:37.78 total
../../activemq-protobuf-test-1.1.jar-4gram.csv
./sim_0.75 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i  143.03s user 15.61s system 165% cpu 1:36.03 total
../../activemq-protobuf-test-1.1.jar-5gram.csv
./sim_0.75 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i  133.10s user 14.69s system 166% cpu 1:28.97 total
../../activemq-protobuf-test-1.1.jar-6gram.csv
./sim_0.75 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i  132.02s user 14.54s system 165% cpu 1:28.69 total
../../activemq-protobuf-test-1.1.jar-uc.csv
./sim_0.75 -m compare -f ../../activemq-protobuf-test-1.1.jar-"$i".csv -b "$i  140.65s user 14.91s system 172% cpu 1:29.95 total
```
