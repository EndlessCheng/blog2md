#  bugfix+newfeature

[ Yuguo ](http://yuguo.us) 2010年 09月 14日

发现两个臭虫，解决之。

1.RSS 输出自从第四周流水记就停止了，这真是一个严重的问题，幸亏某热心读者 [ Moon.Wong
](http://21haolou.tk/blogs/read) 评论指出来，我才发现这个bug，原来是上上周学习Google Date API的时候，WP
输出的Feed不能通过API抓取到，我就试着改了下核心代码中的RSS，当时没有发现问题。大学的时候就听从了前辈的建议，订阅自己的博客，能检查自己的博客是否出
了问题。现在懒了，都没注意自己博客feed了。

2.嵌套评论的JS出错了，我用Chrome都没发觉这个问题。偶尔用FF，发现Firebug提示JS错误，一看，漏掉了comment-
reply这个JS，无法动态嵌套了，已经修复。

这么多年，最在乎的就是博客的订阅者，无论是域名变更，还是服务器搬家，RSS总是用Feedburner烧录的这一个：http://feeds.feedburn
er.com/yuguo 可能有一些读者都订阅我好几年了吧，希望你能来这里冒个泡留言一下~我在边栏放了一个可爱的订阅图标~

新的读者可能会发现这个链接（也就是旁边那只僵尸）是打不开的，那是因为伟大的郭嘉的缘故，实际上你不需要访问这个链接，只要在你的RSS阅读器（Google
Reader或者QQ Reader或者xxx）里粘贴这个链接地址，就可以订阅到我的博客，第一时间收到文章的更新。

有任何bug，欢迎反馈~

[ 14条关于jQuery的知识【上】 → ](/weblog/14-jquery-notes-1/) [ ← 第八周流水记
](/weblog/week-8/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

