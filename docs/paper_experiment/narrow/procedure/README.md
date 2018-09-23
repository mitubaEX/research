# narrow 手順

FPを調査後，その結果からどれくらいクラス数が減ったかを求めればいい

全体のクラス数は，`find . -name "*.jar" | xargs -I@ jar tf @ | grep ".class" | wc -l`でおそらくいける
