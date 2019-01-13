
# BM25

### 0.75

```
/Volumes/HD/false_negative_50_jar/false_negative ❯❯❯ for i in compare_result/* ;do awk -F ',' '{a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

17287
/Volumes/HD/false_negative_50_jar/false_negative ❯❯❯ for i in compare_result/* ;do awk -F ',' '{if($3 >= 0.75) a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

7717
```

### 0.5

```
/Volumes/HD/false_negative_50_jar/false_negative ❯❯❯ for i in compare_result/* ;do awk -F ',' '{if($3 >= 0.75) a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

10366
/Volumes/HD/false_negative_50_jar/false_negative ❮❮❮ for i in compare_result/* ;do awk -F ',' '{a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

92648
```

### 0.25

```
/Volumes/HD/false_negative_50_jar/false_negative ❯❯❯ for i in compare_result/* ;do awk -F ',' '{if($3 >= 0.75) a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

12501
/Volumes/HD/false_negative_50_jar/false_negative ❯❯❯ for i in compare_result/* ;do awk -F ',' '{a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

2064436
```

# edit

### 0.75

```
/Volumes/HD/false_negative_50_jar/false_negative_edit ❯❯❯ for i in compare_result/* ;do awk -F ',' '{if($3 >= 0.75) a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

4853
/Volumes/HD/false_negative_50_jar/false_negative_edit ❮❮❮ for i in compare_result/* ;do awk -F ',' '{a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

10304
```

### 0.5

```
/Volumes/HD/false_negative_50_jar/false_negative_edit ❯❯❯ for i in compare_result/* ;do awk -F ',' '{if($3 >= 0.75) a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'
8107
/Volumes/HD/false_negative_50_jar/false_negative_edit ❮❮❮ for i in compare_result/* ;do awk -F ',' '{a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'
178692
```

### 0.25

```
/Volumes/HD/false_negative_50_jar/false_negative_edit ❯❯❯ for i in compare_result/* ;do awk -F ',' '{if($3 >= 0.75) a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'
17840

/Volumes/HD/false_negative_50_jar/false_negative_edit ❯❯❯ for i in compare_result/* ;do awk -F ',' '{a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'
12758770
```

# jw

### 0.75

```
/Volumes/HD/false_negative_50_jar/false_negative_jw ❯❯❯ for i in compare_result/* ;do awk -F ',' '{if($3 >= 0.75) a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

16296
/Volumes/HD/false_negative_50_jar/false_negative_jw ❮❮❮ for i in compare_result/* ;do awk -F ',' '{a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

3476875
```

### 0.5

```
/Volumes/HD/false_negative_50_jar/false_negative_jw ❯❯❯ for i in compare_result/* ;do awk -F ',' '{if($3 >= 0.75) a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

16296
/Volumes/HD/false_negative_50_jar/false_negative_jw ❮❮❮ for i in compare_result/* ;do awk -F ',' '{a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

20339657
```

### 0.25

```
/Volumes/HD/false_negative_50_jar/false_negative_jw ❯❯❯ for i in compare_result/* ;do awk -F ',' '{if($3 >= 0.75) a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

16296
/Volumes/HD/false_negative_50_jar/false_negative_jw ❮❮❮ for i in compare_result/* ;do awk -F ',' '{a+=1} END {print a}' $i ;done | awk '{b+=$1} END {print b}'

20340099
```
