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
