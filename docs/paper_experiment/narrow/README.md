# 絞り込みというやつ

検索結果を閾値で区切っていき，閾値ごとでどれくらい検索件数が減ったかを求める

## 戦略

- `ToolForResearch`の検索結果の閾値ごとの件数と全体の件数を持って来たら終わり


## 20180626での最新


### 検索件数
```
# 2gram
817256

# 3gram
266095

# 4gram
64522

# 5gram
27939

# 6gram
14533

```

### 全体

```
/Volumes/mituba_20180425/restart/2gram/search_result ❯❯❯ find . -name "*2gram*" | wc -l                                                                          master ✱
      79 * 131476 -> 10386604

/Volumes/mituba_20180425/restart/2gram/search_result ❮❮❮ find . -name "*3gram*" | wc -l                                                                          master ✱
      68 * 353292 -> 24023856

/Volumes/mituba_20180425/restart/2gram/search_result ❮❮❮ find . -name "*4gram*" | wc -l                                                                          master ✱
      67 * 308614 -> 20677138

/Volumes/mituba_20180425/restart/2gram/search_result ❮❮❮ find . -name "*5gram*" | wc -l                                                                          master ✱
      62 * 438772 -> 27203864

/Volumes/mituba_20180425/restart/2gram/search_result ❮❮❮ find . -name "*6gram*" | wc -l                                                                          master ✱
      62 * 382350 -> 23705700
```

### ***誤検出***

