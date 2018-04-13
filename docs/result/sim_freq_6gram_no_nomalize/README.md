# 6gramでやってみた

## 正解検索件数と検索バースマークの長さの関係
excel: ./sim_freq_6gram_no_nomalize.xlsx

これを見ると59件の検索バースマークで正解を見つけたが、3つの検索バースマークは正解が一つもでないという結果になった

調べたら59件の中にちゃんと検索結果のやつが入っている

## スコアと長さの関係

class: protobuf_unittest.UnittestProto$TestAllTypes
length: 664
image: ./score_length-664_relational.png

class: com.google.protobuf.test.UnittestImport$ImportMessage
length: 190
image: ./score_length-190_relational.png

class: protobuf_unittest.MessageWithNoOuter$NestedMessage
length: 190
image: ./score_length-190-2_relational.png

***そもそも正解が出てくると想定されているのにでてこないのはなんでだという疑問***

org.apache.activemq.protobuf.DeferredUnmarshal$FooBase
protobuf_unittest.MessageWithNoOuter$NestedEnum
protobuf_unittest.UnittestMset$RawMessageSet$ItemBase

なんで出てこないのかようわからんのでもういい


## 正解集合が検索結果の難易ぐらいに出てくるかの調査

意味不明な三件を除いて，全て上位に位置している

親和性はたかそう

image: ./pochi_sim_transition_6gram.png, ./pochi_sim_transition_6gram_zoom.png

これもいい感じに線形的に落ちている

親和性高そう
