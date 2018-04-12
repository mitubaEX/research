# 検索結果の長さとスコアの遷移が見たい

一つの検索結果を見て、検索バースマークの長さと検索結果の遷移を折れ線グラフで書く

仕様クラス：com.google.protobuf.test.UnittestImport\$ImportEnum2gram
image: ./score_length_relation_100.png (赤：スコア, 青：長さ)

検索したバースマークの長さは54である


## 前に気になって長さ101で正解ヒット数が変わったやつについて調べる

最高スコア：164.36046
使用クラス：org.apache.activemq.protobuf.DeferredUnmarshal\$Bar2gram
image: ./score_length_relational_100_2.png


最高スコア：184.71094
使用クラス：protobuf_unittest.UnittestProto$TestDupFieldNumber
image: ./score_length_relational_100_38.png


最高スコア：188.04883
使用クラス：protobuf_unittest.UnittestProto$TestRequired
image: ./score_length_relational_100_37.png

特徴としては、あるスコアより下になると結構長さが大きくなっている
これは類似度計算が、検索バースマークと検索結果バースマークの積集合をとることが関係していると思われる

6gramでやったらいいのかな
