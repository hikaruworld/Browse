sublime-browse
==============

Sublime text2 plugin. Dump the browser output.

このプラグインは、 [w3m](http://w3m.sourceforge.net/index.ja.html "w3m") ないしは [Pandoc](http://johnmacfarlane.net/pandoc/ 'Pandoc') 
を利用して新規View上に出力を行います。

出力される内容は、利用するツールによって出力が異なります。

プラグインとして提供しているのは、引数で渡されたURL情報を上記ツールに渡し、
その結果をView上に出力するのみです。

Bookmarks
---------

設定ファイルに定義した任意のURLの内容を新規view上にdumpします。

Bookmarks With...
-----------------

設定ファイルに定義した任意のURLにGETパラメーターを付与してアクセスを行い、
HTMLの内容をDumpします。


 
GoTo
----

任意に入力したURLの内容を新規view上にdumpします。


