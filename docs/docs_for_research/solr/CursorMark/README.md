## 調査

### 目的
大量検索する際のI/O負荷の分散

### 実験

#### 5件ずつ検索してみた

##### 検索クエリ
curl 'http://localhost:8983/solr/uc/select?indent=on&q=*:*&sort=id%20desc&wt=json&rows=5&cursorMark=*'

二回目以降はcursorMarkにnextCursorMarkの値を入れる
結果はsmallに入れておく

#### 1000件ずつ検索してみた

結構な速度感で取得できている気がする

### 結論

10000件だと取得はちょっと時間がかかるので，1000件を刻んでいく感じで行きたい

## 適当にScriptを組んでみる

#### 1000件ずつぶん投げていく

検索エンジンのメモリは24g

##### 結果

qtime: 55778
elapsed_time:69.0891661643982[sec]

速い気がする

#### 全件を一気に検索して何秒か確かめてみる

1596
elapsed_time:13.586029767990112[sec]

負けた

##### 二回め
0
elapsed_time:12.383924961090088[sec]

