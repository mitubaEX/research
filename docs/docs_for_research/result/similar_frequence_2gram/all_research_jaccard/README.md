## jaccard係数でやり直してみるよ


```
greater_than_count: 6026008, pochi::0.75: 124, pochi::0.5: 3283, pochi::0.25: 27412, pochi::0.25_under: 50940, search_sim::0.75: 78352, search_sim::0.5: 607906, search_sim::0.25: 3053401, other: 1784891, other_poshi::0.75: 120
```

### 検出漏れ


```
all: 7810899

# 0.25
[0, 4726751, 0, 0, 0]

# 0.5
[0, 7202678, 0, 0, 0]

# 0.75
[9, 7732418, 0, 0, 0]

# 0.8
[52, 7748909, 0, 0, 0]

# 0.85
[57, 7783062, 0, 0, 0]

# 0.9
[62, 7805086, 0, 0, 0]

# 0.95
[95, 7809329, 0, 0, 0]

# 1.0
[253, 7810646, 0, 0, 0]
```

## 正解が253個しかないのでそれを見てみる


## ミスったのでやり直し

```
greater_than_count: 5951912, pochi::0.75: 24, pochi::0.5: 2919, pochi::0.25: 27473, pochi::0.25_under: 76609, search_sim::0.75: 104082, search_sim::0.5: 628714, search_sim::0.25: 3037601, other: 1714121, other_poshi::0.75: 0
```

特に変化は見られない

そもそも0.75になったペアの長さが15以下である
だめじゃん・・・

正解0

### 長さの内訳
```
{5: 2, 8: 93, 11: 10, 10: 120, 14: 28}
```

6gramでやったら変わるかなぁ？

## 6gramをやった後の考察

6gramはクラス名が同じだったのに対して，2gramはクラス名が違っていた
でも長さで弾くので，まぁ何も見なかったことにしたらいい

ここでいいたいのは短い文字だったら余り効果が発揮できない
