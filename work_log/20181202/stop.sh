p=8980
for num in $(seq 100 100 1000)
do
  cd ./"$num"-jars-server/solr-6.4.1
  bin/solr stop -p $p
  # for i in 2gram 3gram 4gram 5gram 6gram uc ; do bin/solr create -c "$i" -p $p ;done
  # for i in 2gram 3gram 4gram 5gram 6gram uc ; do rm server/solr/"$i"/conf/managed-schema && wget -O  server/solr/"$i"/conf/managed-schema 'https://raw.githubusercontent.com/mitubaEX/birthmark_server/master/managed-schema';done
  # bin/solr restart -p $p
  # for i in 2gram 3gram 4gram 5gram 6gram uc ; do find ../birthmark_server/data/birth_xml -name "*$i*" | xargs -I% bin/post -c "$i" -p $p  % ;done
  cd ../../
  p=$(expr $p + 1)
done



