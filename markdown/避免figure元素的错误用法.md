#  避免figure元素的错误用法

[ Yuguo ](http://yuguo.us) 2011年 08月 22日

新的html5标签<figure>和<figcaption>有一些常用的错误用法。

###  不是所有的图片都是<figure>

写html代码的时候一个重要原则就是“如非必要，不要写额外的代码”。有的人给整个网站所有的img都加上<figure>，这给自己增加了额外的不必要工作量。规
范说<figure>是：  some flow content, optionally with a caption, that is self-
contained and is typically referenced as a single unit from the main flow of
the document.（一些文本流，可能包含标题——它们通常是作为文档的主要内容流中的一个自我包含的独立单元。）  如何判断图片是不是需要用<figur
e>包括起来？这样判断吧：图片是不是与上下文有关的？如果是，那么再回答：把图片移到附录中，而不影响读者对全文的理解吗？如果回答再次是肯定的，那么就可以用<f
igure>。

###  logo不是<figure>

它被滥用了。

[ ![](http://yuguo.us/files/2011/08/taobao-logo.png)
](http://yuguo.us/files/2011/08/taobao-logo.png) 淘宝的logo错误地使用的figure标签

###  <figure>不只是图片

<figure>可以是视频、音频、表单（比如SVG）、引用、表格、代、一段散文或者……任何这些元素的集合。

参考资料： [ http://html5doctor.com/the-figure-figcaption-elements/
](http://html5doctor.com/the-figure-figcaption-elements/)

[ 自定义wordpress翻页 → ](/weblog/custom-wordpress-pagenav/) [ ← Custom Post Types
](/weblog/custom-post-types/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

