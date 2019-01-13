# 目的

バースマーク処理に検索エンジンの処理を追加する


## 弁別性

盗用のものを盗用とみなし，それ以外は盗用と見なさない

- 検索エンジンに入っているバースマークで検索して，ちゃんと同一のクラスが出てくるか（検出漏れを抑える）
- 検索エンジンに入ってないバースマークで検索して，きちんと関係ないとみなせるか（誤検出を抑える）

## 保存性

難読化したバースマークを検索エンジンに投げてもちゃんと難読化前のものが返ってくるか

## 検索エンジンの精度調査

precisionとかそこら周り


# 検証過程

## 無理やり正規化の類似度調査

- [similar_frequence_2gram](./docs/result/similar_frequence_2gram)
- [similar_frequence_6gram](./docs/result/similar_frequence_6gram)

## 500個のjarファイルを適当に選んで調査した

- [500_random_jar](./docs/result/500_random_jar)


## 検索エンジンのスコアに関していろいろ考えた

- [sim_freq_2gram_no_nomalize](./docs/result/sim_freq_2gram_no_nomalize)
- [sim_freq_6gram_no_nomalize](./docs/result/sim_freq_6gram_no_nomalize)

## スコア * 2 / 3くらいのところを閾値にすればいいのでは？という検証

- [score_2-3_threshold](./docs/result/score_2-3_threshold)

## 実験の戦略を考えていった

結果をここに入れていく
- [paper_experiment](./docs/docs/paper_experiment/)


## Deploy

```
# test
mkdocs serve

# deploy
mkdocs gh-deploy
```
