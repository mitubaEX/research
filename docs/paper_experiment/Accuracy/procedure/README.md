# 保存性評価

## 難読化

### donquixote

```sh
mkdir jar

# jarディレクトリに任意のjarファイルを置く

git clone https://github.com/tamadalab/donquixote.git

cd donquixote && mvn package

cd ..

mkdir DNR

# run
for i in ./jar/*.jar ;do java -jar ./donquixote/target/donquixote-3.0.1.jar --processor apiblinder --destination des1 --summary report1.txt "$i" && jar cvf DNR/`basename "$i"` des1/* && rm dest1;done
```

### sandmark

```sh
# Please install sandomark
# http://cgi.cs.arizona.edu/~sandmark/download.html

mkdir DNR DR IOP MLI IR

# run
for i in ./jar/*.jar ; do java -cp sandmark.jar sandmark.smash.SandmarkCLI -O -A "Insert Opaque Predicates" -i $i -o ./IOP/`basename "$i"`-IOP.jar ;done

for i in ./jar/*.jar ; do java -cp sandmark.jar sandmark.smash.SandmarkCLI -O -A "Irreducibility" -i $i -o ./IR/`basename "$i"`-IR.jar ;done

for i in ./jar/*.jar ; do java -cp sandmark.jar sandmark.smash.SandmarkCLI -O -A "Duplicate Registers" -i $i -o ./DR/`basename "$i"`-DR.jar ;done

for i in ./jar/*.jar ; do java -cp sandmark.jar sandmark.smash.SandmarkCLI -O -A "Merge Local Integers" -i $i -o ./MLI/`basename "$i"`-MLI.jar ;done
```

### extract

```sh
git clone https://github.com/tamada/stigmata.git

cd stigmata && mvn package

cd ..

for obf in DNR DR IOP MLI IR ; do find ./"$obf" -name "*.jar" | while read file ; do for i in 2gram 3gram 4gram 5gram 6gram uc ; do java -jar ./stigmata/target/stigmata-5.0-SNAPSHOT.jar extract -b $i "$file" > ./"$obf"/`basename "$file"`-"$i".csv;done;done;done
```

## 検索

```sh
mkdir search_result

for i in DNR DR IOP MLI IR ; do mkdir search_result/"$i";done

# thresholdは適宜変更
for obfu in DNR DR IOP IR MLI ;do paste <(for i in 2gram 3gram 4gram 5gram 6gram uc;do echo $i ;done) <(for j in 15 24 31 37 41 2; do echo $j ;done) | while read birth threshold ; do for i in ./extract_obfu/"$obfu"/*"$birth"*.csv ; do python3 row_search.py $i $threshold "$birth" "$obfu"; done;done;done
```

## 結果を整理

```sh
mkdir pro_result

for i in DNR DR IOP MLI IR ; do mkdir pro_result/"$i";done

for obfu in DNR DR IOP MLI IR ; do for birth in 2gram 3gram 4gram 5gram 6gram uc;do for i in search_result/"$obfu"/*"$birth"*  ; do awk -v filename=`basename "$i"` -F '[/,]' '{printf("%s,%s,%s\n",filename,$1,$2)}' "$i";done > pro_result/"$obfu"/"$birth".csv;done;done

# 保存割合を求めるスクリプト忘れた
for obfu in DNR DR IOP MLI IR ; do for birth in 2gram 3gram 4gram 5gram 6gram uc;do <何かしらのscript> pro_result/"$obfu"/"$birth".csv ;done;done
```
