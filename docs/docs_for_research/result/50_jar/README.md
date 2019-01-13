# 50個のjarファイルでpochiの比較時間がどうなるかを確かめる


## 比較時間

### 50この場合


class file数 => 149634
1131090481581 ns => 1131.090481581 s => 18 m

実際の時間
01:29 s
## 30この場合

class file 数 => 100112
337057583177 ns => 337.057583177 s => 5.61762638628333 m

## 10万個くらい


2390067969474 ns => 39.8344661579 m

実際のpochiの実行時間
01:44:22 s

## 30個のjarファイルの平均/3


 N   ../birthmark_server/data     master    python3 calc_birthmark_length_ave.py 2gram
13.49104510451045

 N   ../birthmark_server/data     master    python3 calc_birthmark_length_ave.py 3gram
20.567040704070408

 N   ../birthmark_server/data     master    python3 calc_birthmark_length_ave.py 4gram
25.39137513751375

 N   ../birthmark_server/data     master    python3 calc_birthmark_length_ave.py 5gram
28.54257425742574

 N   ../birthmark_server/data     master    python3 calc_birthmark_length_ave.py 6gram
30.701298129812983

 I   ../birthmark_server/data     master    python3 calc_birthmark_length_ave.py uc
1.629086908690869


## 50個のjarファイルの平均/3

 I   ../birthmark_server/data     master    python3 calc_birthmark_length_ave.py 2gram
14.171505889844
 N   ../birthmark_server/data     master    python3 calc_birthmark_length_ave.py 3gram
22.00541228907991
 N   ../birthmark_server/data     master    python3 calc_birthmark_length_ave.py 4gram
27.55772047118752
 N   ../birthmark_server/data     master    python3 calc_birthmark_length_ave.py 5gram
31.13476599808978
 N   ../birthmark_server/data     master    python3 calc_birthmark_length_ave.py 6gram
33.526361031518626
 I   ../birthmark_server/data     master    python3 calc_birthmark_length_ave.py uc
2.1663482967207894


