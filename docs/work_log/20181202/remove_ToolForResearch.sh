for num in $(seq 100 100 1000) ; do rm -rf "$num"-jars-server/ToolForResearch;done
for num in $(seq 100 100 1000) ; do git clone --recursive https://github.com/mitubaEX/ToolForResearch.git "$num"-jars-server/ToolForResearch;done
for num in $(seq 100 100 1000) ; do git clone https://github.com/tamada/pochi.git "$num"-jars-server/ToolForResearch/pochi_new;done
for num in $(seq 100 100 1000) ; do cd "$num"-jars-server/ToolForResearch/pochi_new && mvn package && cd ../../..;done

