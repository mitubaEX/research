p=8980
for num in $(seq 100 100 1000)
do
  cd ./"$num"-jars-server/ToolForResearch
  sh row_search_get_only_last_result_script.sh $p &
  p=$(expr $p + 1)
  cd ../..
done

