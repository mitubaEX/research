# distributed

分散インデックスについてのメモ

## example

今回は5このノードで分散して検索を行ってみる．

```
mkdir example/nodes

# 5件のノードを作成
for i in $(seq 1 5); do mkdir "example/nodes/node$i" && cp server/solr/solr.xml "example/nodes/node$i/." ; done
for i in $(seq 1 5); do mkdir "example/nodes/node$i" ; done


bin/solr start -s example/nodes/node1 -p 8983
bin/solr start -s example/nodes/node2 -p 8984
bin/solr start -s example/nodes/node3 -p 8985
bin/solr start -s example/nodes/node4 -p 8986
bin/solr start -s example/nodes/node5 -p 8987


bin/solr restart -s example/nodes/node1 -p 8983 -m 24g
bin/solr restart -s example/nodes/node2 -p 8984 -m 24g
bin/solr restart -s example/nodes/node3 -p 8985 -m 24g
bin/solr restart -s example/nodes/node4 -p 8986 -m 24g
bin/solr restart -s example/nodes/node5 -p 8987 -m 24g


bin/solr create_core -c core1 -p 8983
bin/solr create_core -c core1 -p 8984
bin/solr create_core -c core1 -p 8985
bin/solr create_core -c core1 -p 8986
bin/solr create_core -c core1 -p 8987


find /Volumes/mituba_server/birthmark_server_encoded/data/birth_xml -name "birth_uc*.xml" | head -n 40 | xargs -I% bin/post -c core1 % -port 8983
find /Volumes/mituba_server/birthmark_server_encoded/data/birth_xml -name "birth_uc*.xml" | head -n 80 | tail -n 40 | xargs -I% bin/post -c core1 % -port 8984
find /Volumes/mituba_server/birthmark_server_encoded/data/birth_xml -name "birth_uc*.xml" | head -n 120 | tail -n 40 | xargs -I% bin/post -c core1 % -port 8985
find /Volumes/mituba_server/birthmark_server_encoded/data/birth_xml -name "birth_uc*.xml" | head -n 160 | tail -n 40 | xargs -I% bin/post -c core1 % -port 8986
find /Volumes/mituba_server/birthmark_server_encoded/data/birth_xml -name "birth_uc*.xml" | tail -n 40 | xargs -I% bin/post -c core1 % -port 8987


curl "http://localhost:8983/solr/core1/select?q=*:*&indent=true&shards=localhost:8983/solr/core1,localhost:8984/solr/core1,localhost:8985/solr/core1,localhost:8986/solr/core1,localhost:8987/solr/core1&fl=id,name"

# クエリ
curl "http://localhost:8983/solr/core1/select?q=*:*&indent=true&shards=localhost:8983/solr/core1,localhost:8984/solr/core1,localhost:8985/solr/core1,localhost:8986/solr/core1,localhost:8987/solr/core1&rows=398201&fl=filename&wt=json" > tmp.json

# solrconfig いじり
find . -type f -name "solrconfig.xml" | xargs -J% sed -i -e 's/<str name="content-type">text\/plain; charset=UTF-8<\/str>/<str name="content-type">application\/json; charset=UTF-8<\/str>/g' %

type="string" multiValued="false" indexed="true" required="true" stored="true"
```

クエリを投げたらエラーが出る．
どうやらmime typeが違うらしい

```json
    "msg":"Error from server at http://localhost:8987/solr/core1: Expected mime type application/octet-stream but got application/xml. <?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<response>\n<lst name=\"error\"><lst name=\"metadata\"><str name=\"error-class\">org.apache.solr.common.SolrException</str><str name=\"root-error-class\">org.apache.solr.common.SolrException</str></lst><str name=\"msg\">application/x-www-form-urlencoded content length (3121735 bytes) exceeds upload limit of 2048 KB</str><int name=\"code\">400</int></lst>\n</response>\n",
```

## 対処

managed-schemaをいじっていく

```
# 失敗
find "$i" -name "managed-schema" | xargs -J% sed -i -e 's/multiValued="true"/multiValued="false"/g' %

find . -name "managed-schema" | xargs -J% sed -i -e 's/type=\"strings\"/type=\"string\" multiValued=\"false\" indexed=\"true\" required=\"true\" stored=\"true\"/g' %


find . -name "managed-schema" | xargs -J% sed -i -e 's/<dynamicField name="*_ss" type="string" multiValued="false" required="true" stored="true" indexed="true"\/>/<dynamicField name="*_ss" type="strings" indexed="true" stored="true"\/>/g' %
  <dynamicField name="*_ss" type="strings" indexed="true" stored="true"/>


# データが変だったのでちょっと変えた
find . -name "birth_uc*" | xargs -J% sed -i -e 's/&amp;quot;//g' %
```

stop
```
bin/solr stop -s example/nodes/node1 -p 8983
bin/solr stop -s example/nodes/node2 -p 8984
bin/solr stop -s example/nodes/node3 -p 8985
bin/solr stop -s example/nodes/node4 -p 8986
bin/solr stop -s example/nodes/node5 -p 8987
```

## わかったこと
件数が多すぎるとタイムアウトしているのかわからないがエラーを吐く
逆に件数が少ないとエラーは吐かない
タイムアウト設定いじってみる
CursorMarkを使おう

```
# クエリ
curl "http://localhost:8983/solr/core1/select?q=*:*&indent=true&shards=localhost:8983/solr/core1,localhost:8984/solr/core1,localhost:8985/solr/core1,localhost:8986/solr/core1,localhost:8987/solr/core1&rows=100000&fl=filename,data,score&wt=json&sort=id%20desc&cursorMark=*" > tmp.json
```

送信データ量の限界に達していたらしい
変更する
CursorMark使うと遅すぎる

```
# 変更
find . -type f -name "solrconfig.xml" | xargs -J% sed -i -e 's/multipartUploadLimitInKB="2048000"/multipartUploadLimitInKB="204800000"/g' %

find . -type f -name "solrconfig.xml" | xargs -J% sed -i -e 's/formdataUploadLimitInKB="2048"/formdataUploadLimitInKB="20480000"/g' %
```

変更したけど特に改善されなかった・・・

100万件検索した結果 -> 4:16
遅い

10万件 -> 1:21

無理
