#  我对SASS的看法

[ Yuguo ](http://yuguo.us) 2012年 08月 07日

在阮一峰的 [ 《SASS用法指南》 ](http://www.ruanyifeng.com/blog/2012/06/sass.html) 中写到：

> 你可以用它开发网页样式，但是没法用它编程。也就是说，CSS基本上是设计师的工具，不是程序员的工具。在程序员眼里，CSS是一件很麻烦的东西。它没有变量，也
没有条件语句，只是一行行单纯的描述，写起来相当费事。

这篇文章写的很好，介绍了SASS很强大的功能，我亲身使用了一段时间的SASS之后，却觉得它相当难用，有以下几个原因：

  * 编辑器不支持对SASS格式的支持，所以没有代码高亮 
  * 没有办法直接编辑SASS代码之后，刷新页面就看到结果，而需要用ruby跑一个sass命令（相当于“编译”），有点复杂。我觉得CSS更需要即时的反馈，而不像c++，写一大堆之后编译下看看逻辑对不对。更何况sass的命令无法检测出错误代码。 
  * debug困难，我在浏览器中看到错误需要修改的时候，回到编辑器中搜索class或者代码相对困难，因为是编译过的，行数和代码都不一样了。 
  * 同样是合并代码和图片的cssgaga就相当友好了，我们还是在写css代码，可以本地刷新看到效果，多组件@import，图片放在slice里会自动合并，还特别照顾我们这些需要兼容IE6的苦逼国内前端。 
  * CSS3的多样化前缀可能是需要SASS的一个理由，但这个理由是暂时并且畸形的，也可以用cssgaga来解决。 

总体来说，sass提供了另一种可能性，但这种可能性是否适合所有人、所有场景？我十分怀疑。

[ 如何正确设置缓存 → ](/weblog/send-the-correct-headers-to-leverage-browser-caching/)
[ ← 使用git部署站点 ](/weblog/push-git-repository-to-server/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

