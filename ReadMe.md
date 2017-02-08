# このソフトウェアについて

ファイルサイズを[SI](https://ja.wikipedia.org/wiki/%E5%9B%BD%E9%9A%9B%E5%8D%98%E4%BD%8D%E7%B3%BB)や[2進接頭辞](https://ja.wikipedia.org/wiki/2%E9%80%B2%E6%8E%A5%E9%A0%AD%E8%BE%9E)で取得する(1KB,1KiB等)。

# 開発環境

* [Linux Mint 17.3 MATE](https://www.linuxmint.com/rel_rosa_mate.php)
* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)

# 実行

```sh
bash Test.sh
```

# 結果

`FileSize.py`のユニットテスト結果が出力される。

# 使い方

```python
import FileSize
f = FileSize.FileSize()
print(f.Get(9999))  # 9999 iB
print(f.Get(10000)) # 9.76 KiB
```

## 設定

コンストラクタに引数を与えることで表示形式などを変更できる。

設定|デフォルト|可能範囲|説明
----|---------|--------|----
byte_size_of_unit|1024|1000,1024|1000なら[SI](https://ja.wikipedia.org/wiki/%E5%9B%BD%E9%9A%9B%E5%8D%98%E4%BD%8D%E7%B3%BB),1024なら[2進接頭辞](https://ja.wikipedia.org/wiki/2%E9%80%B2%E6%8E%A5%E9%A0%AD%E8%BE%9E)として算出する
integral_figure_num|4|3,4|整数部の桁数
imaginary_figure_num|2|0,1,2,3|虚数部の桁数
rounding|decimal.ROUND_DOWN|decimal.rounding|算出時の丸め方式
is_hidden_imaginary_all_zero|True|False,True|虚数部がすべてゼロなら省略する

## 表示パターン

### 桁数

* 9999.999
* 9999.99
* 9999.9
* 9999
* 999
* 999.9
* 999.99
* 999.999

### 単位

10^n|SI|BinaryPrefix
----|--|------------
3|KB|KiB
6|MB|MiB
9|GB|GiB
12|TB|TiB
15|PB|PiB
18|EB|EiB
21|ZB|ZiB
24|YB|YiB

なお、`10^3`の表現について[SI](https://ja.wikipedia.org/wiki/%E5%9B%BD%E9%9A%9B%E5%8D%98%E4%BD%8D%E7%B3%BB)では`KB`でなく`kB`らしいが今回は`KB`にしてある。よって正確な[SI](https://ja.wikipedia.org/wiki/%E5%9B%BD%E9%9A%9B%E5%8D%98%E4%BD%8D%E7%B3%BB)ではない。

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
