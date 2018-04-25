
# バースマークの長さと検索結果に出てきた正解の数の関係を調べる

```
# 2件
長さは101
org.apache.activemq.protobuf.DeferredUnmarshal\$Bar2gram
25 183,183 177,177 25,183 58,58 25,25 176,176 25,183 25,25 182,182 25,182 177,177 187,187 89,89 183,182 176,182 153,153 25,25 25,182 182,182 87,87 25,87 167,167 25,25 180,180 198,198 25,180 180,180 172,172 25,180 2,2 159,159 25,172 3,3 54,54 25,153 21,21 4,4 25,182 184,184 96,96 54,21 5,5 25,21 6,6 25,25 21,21 181,181 21,21 172,182 54,54 21,21 16,16 126,126 7,7 160,160 25,176 21,21 171,171 25,176 167,25 187,182 192,192 182,180 199,199 25,21 182,182 181,181 1,1 58,89 21,21 188,188 183,183 181,181 25,58 187,89 25,180 183,25 4,25 5,25 6,25 198,180 182,182 167,176 187,192 176,183 18,18 182,182 18,25 18,25 166,166 4,4 172,18 165,165 3,3 172,25 192,182 172,172 18,18 25,182 130,130 172

# 38件
長さは101
protobuf_unittest.UnittestProto\$TestDupFieldNumber2gram
25 183,183 177,177 25,183 58,58 25,25 182,182 153,153 25,182 182,182 87,87 167,167 58,25 25,182 18,18 182,87 25,25 176,176 25,183 25,182 25,182 177,177 187,187 89,89 183,182 176,167 25,25 180,180 2,2 159,159 25,180 172,172 3,3 54,54 25,153 21,21 4,4 25,182 184,184 96,96 54,21 5,5 25,21 6,6 25,25 21,21 181,181 21,21 172,172 25,182 54,54 21,21 16,16 126,126 7,7 160,160 25,176 21,21 171,171 25,176 167,25 5,184 87,5 187,183 184,184 192,192 182,25 6,6 187,25 4,184 177,182 192,192 176,176 187,25 187,183 18,25 18,25 166,166 4,4 172,25 198,198 25,18 165,165 3,3 172,25 192,182 172,182 130,130 153,153 3,182 159,159 3,182 154,154 3,172 4,172 18,18 54,16 25,130 130,130 54,21 18,18 25
```

長さは一緒らしい、なるほど

## 結果のやつらが結果の上位何件に位置しているのかを調査

見たら全部上位勢だった

すなわち正解となっているのは，上位を全どりしている

36件正解が見つかったら，上から36件が正解集合だ

これを見るとどんな感じでpochiの類似度が下がっていっているのかきになる

image: ./pochi_sim_transition.png

### 考察

見る感じ順調に下がっているが，線形ではなく若干ブレている．
うーん

ズームして見た


use: protobuf_unittest.UnittestProto$TestRequired
image: ./pochi_sim_transition_zoom.png


75件ぐらいからほぼ横ばいでゆっくり下がって行く感じ

大体のpochiは0.2付近だと言える

こいつの正解は37件である

これはこれでいい結果