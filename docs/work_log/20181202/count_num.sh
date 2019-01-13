for num in $(seq 100 100 1000)
do
  cd ./"$num"-jars-server
  for birth in {2..6}gram uc
  do
    echo "$birth-$num"
    TMP=$(find birthmark_server/data/birth_xml -name "*$birth*" | while read file ; do grep 'output' $file | wc -l ;done | gowk sum -c 0 -d ' ')
    searched=$(find birthmark_server/data/search_birthmark -name "*$birth*" | while read file ; do wc -l $file ;done | gowk sum -c 0 -d ' ')
    for num_i in $(seq 1 1 10)
    do
      echo $(($TMP * $searched))
    done
    echo
    echo
  done
  echo
  cd ..
done



