#  Flexbox的奇怪历史

[ Yuguo ](http://yuguo.us) 2013年 01月 16日

其实现在很多前端同学都知道flexbox这个CSS3布局属性了，它可以方便地让我们做出水平和垂直的布局，而不是依赖于浮动。

我最近在翻译《众妙之门3》的时候，原书关于Flexbox的代码就已经过时了，这里是 [ 他们的demo ](http://www.smashing-
links.com/smashing-book-3/demos/flexbox/flexsizeposition.html)
，但在我的Chrome和FF下均无效。但是如果Google一下Flexbox关键词，会发现很多过时的信息。

调研一下就发现这个属性的历史非常奇怪，也不怪Smashing Book的信息过时：

  * 如果你看的博客/书中关于Flexbox的代码是： ` display:box; ` 或者属性是 ` box-{*} ` ，那你看的是2009年以前的版本； 
  * 如果你看的博客/书中关于Flexbox的代码是： ` display:flexbox; ` 或者 ` flex() ` 函数，那你看到的是2011年的青涩少年； 
  * 如果你看的博客/书中关于Flexbox的代码是： ` display:flex; ` 并且属性是 ` flex-{*} ` 那你看到的是现在（2012-2013年）的版本。 

这些语法的兼容性各不一致，短期来看可能老版本的兼容性还好一点，但长远看来用老式语法是不明智的。至少新语法更简单易懂。还不支持新语法的浏览器以后会逐渐支持。

[ Example of OLD syntax ](http://codepen.io/chriscoyier/pen/DLikE)

[ Example of NEW syntax ](http://codepen.io/chriscoyier/pen/qazmI)

《众妙之门3》中的问题已经反馈给出版社了，看看怎么解决。

参考资料：

> [ “Old” Flexbox and “New” Flexbox ](http://css-tricks.com/old-flexbox-and-
new-flexbox/)

[ LESS in Action → ](/weblog/less/) [ ← 听Nico讲故事 ](/weblog/nico-story/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

