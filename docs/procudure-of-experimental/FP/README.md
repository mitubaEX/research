# FP 実験手順

## サーバ構築

FNとほぼ同様

## 検索

`<(for j in 15 24 31 37 41 2; do echo $j ;done)`の部分は適宜サーバを作成した時の値を利用する

```
paste <(for i in 2gram 3gram 4gram 5gram 6gram uc;do echo $i ;done) <(for j in 15 24 31 37 41 2; do echo $j ;done) | while read birth threshold ; do for i in dir/*"$birth".csv; do python3 row_search.py $i $threshold "$birth" ; done > time_"$birth".csv;done
```

## FP check

※ToolForResearchで比較するときにtimeコマンドで比較時間を出力するのを忘れずに

- 効率悪いが，search_result直下の結果を各閾値ごとのディレクトリに分ける (search_result_0.9とか)
- 後はToolForResearchのinput optionにそのディレクトリを指定する
- 比較結果ディレクトリでどれだけ0.75があったのかを確認して，その割合がFP

## 検索時間について

検索時間は，time_"$birth".csv内の時間の合計を求めたら良い
比較時間はtimeコマンドで

従来手法の時間は，普通に相互比較で (FN参照)


## 11/14追記

ToolForResearch/row_search_get_only_last_result.pyを作成した

これをparseするためのスクリプトを記述しておく．

```
find . -name "*-898*.csv" | while read file
do
  grep 'narrow_count' $file | sed 's/narrow_count: //g' | gowk sum -c 0
  grep 'elapsed_time:' $file | sed 's/elapsed_time://g' | sed 's/\[sec\]//g' | gowk sum -c 0
  grep 'comparison: ' $file | sed 's/comparison: //g' | sed 's/ ns//g' | gowk sum -c 0
  grep 'correct_count: ' $file | sed 's/correct_count: //g' | sed 's/count: //g' | gowk sum -c '0,1'
done
```

これじゃダメっぽい
これを使う

```
python3 ./parse.py <file>
```

