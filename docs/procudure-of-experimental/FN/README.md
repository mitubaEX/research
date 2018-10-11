# FN 実験手順

## サーバー構築まで

```sh
git clone https://github.com/mitubaEX/birthmark_server.git
```

あとはREADME.mdのUsageに沿ってサーバーを立てる

## 相互比較

script: extract_and_compare_*.js

```sh
git clone https://github.com/tamada/pochi.git

cd pochi && mvn package

# mkdir
for i in 2gram 3gram 4gram 5gram 6gram uc ;do mkdir birthmark/"$i" ;done

# cp birthmark file
for i in 2gram 3gram 4gram 5gram 6gram uc ;do find birthmark_server/data/birthmark -name "$i" | xargs -I@ cp @ birthmark/"$i"/.;done

# pochi
for i in 2gram 3gram 4gram 5gram 6gram uc ; do java -jar target/pochi-runner-1.0-SNAPSHOT.jar ../pochi_script/extract_and_compare_"$i".js > "$i".csv;done
```

### 重複削除

script: remove_files.py

```sh
mkdir remove_files

# thresholdを適宜変更
paste <(for i in 2gram 3gram 4gram 5gram 6gram uc;do echo $i ;done) <(for j in 15 24 31 37 41 2; do echo $j ;done) | while read birth length ;do python3 remove_files.py $birth $length ;done
```

### 比較結果を得る

script: pre_remove.py

```sh
mkdir pre_result_remove

for i in 2gram 3gram 4gram 5gram 6gram uc ;do python3 pre_remove.py pochi/"$i".csv "$i";done
```

## 検索

script: row_search_once.py

```sh
mkdir search_result

# run
# thresholdを適宜変更
paste <(for i in 2gram 3gram 4gram 5gram 6gram uc;do echo $i ;done) <(for j in 15 24 31 37 41 2; do echo $j ;done) | while read birth threshold ; do for i in birthmark_server/data/birthmark/*"$birth"* ; do python3 row_search_once.py $i $threshold "$birth"; done;done
```

### parse result

```sh
mkdir pro_result

for birth in 2gram 3gram 4gram 5gram 6gram uc ;do (for i in search_result/*"$birth"*  ; do awk -v filename=`basename "$i"` -F '[/,]' '{printf("%s,%s,%s\n",filename,$1,$2)}' "$i" ;done)> ./pro_result/"$birth".csv;done
```

## 検出漏れをチェック

script: intersection.go

```sh
for i in 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 ; do for birth in 2gram 3gram 4gram 5gram 6gram uc ; do go run intersection.go ./pro_result/"birth".csv ./pre_result_remove/"birth".csv "$i";done;done
```
