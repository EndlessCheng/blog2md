#  Instapaper Friendly -- dos and don'ts

[ Yuguo ](http://yuguo.us) 2011年 09月 26日

##  什么是Instapaper

[ Instapaper ](http://www.instapaper.com/) 是一个提供Read
Later服务的跨平台解决方案。在任何地方（比如浏览器中，或者Google Reader中，邮件等）选择Read
Later之后，还能在任何地方（iPad，iPhone，kindle）阅读。

##  什么是Instapaper Friendly？

当读者访问你的网站，而且你的网站是阅读性质的（比如博客、相册），而不是社交性质的（比如SNS，Twitter），那么你的读者很有可能会使用Instapape
r来Read Later。如果读者保存下来的内容乱七八糟，要么没有保存到正文，要么保存了广告，或者评论，那就不是友好的。反之则是友好的。

Read Later之后的text文件拥有以下特性的页面是友好的：

  * 有且只有一个标题 
  * 无广告 
  * 无交互链接或者交互按钮（比如评论、赞等） 
  * 无评论（除非评论是页面的重要内容） 
  * 像一篇文章 
  * 文章内容顺序正确 
  * 有内容图片（注意是img而不是background-image） 
  * 无装饰图片（比如list前面的小星星图片在text中用·来表示就好） 
  * 有版权信息 
  * …… 

##  为什么我要关心Instapaper？

Instapaper使用一些内部的算法来获取文章中的标题信息、正文信息，并且把它们和广告、评论区分开来。这些算法不得而知，但一定是一种聪明的算法，根据htm
l标签等前端代码来读取内容，这跟Google的爬虫非常类似。被Instapaper抓取得乱七八糟的页面一定是语义化或者结构有问题的页面，基于此，我认为对In
stapaper友好不仅仅是对Instapaper用户友好，更加重要的目标是对所有的机器人友好。

举一个简单的例子， [ Daily Tip: How to Make Your WordPress Blog Instapaper Friendly
](http://wpmu.org/daily-tip-how-to-make-your-wordpress-blog-instapaper-
friendly/) WPMU的一个错误之处就是在文章页里有两个h1，一个是网站logo“ [ WPMU.org
](http://www.wpmu.org/) ”，另一个就是本文标题。这就导致在Read Later中会出现两个标题。

##  如何做到Instapaper Friendly？

Instapaper虽然对网站主隐藏了其获取正文信息的算法，但它也给网站主一些 [ 公开的建议
](http://www.instapaper.com/publishers)
。从编程思想上来看，这是很好的：没有必要展现出复杂的实现，而仅仅给出简单的接口，保证谁所有人会使用、所有人都有权限使用。

###  公开的建议

Instapaper给网站开发者一些公开的建议，包括对正文文本解析的控制、对Instapaper的拒绝（就好像通过robots.txt来拒绝google一样
）、在站点添加Read Later按钮等。我只分析对正文文本解析的控制（Control text parsing for your site with
HTML）。

  * ` instapaper_title ` : The first element with this class will be used as the title. If omitted, the HTML ` <title> ` element is used and Instapaper will try to remove common prefixes (such as “Archive”). 
  * ` instapaper_body ` : The first element with this class will be used as the body container. All text outside of this element will be removed from the text output. If omitted, Instapaper will try to locate a suitable body container that includes all article text with minimal clutter. If such a container cannot be found with confidence, the HTML ` <body> ` element will be used. 
  * ` instapaper_ignore ` : Any elements with this class, and their contents, will be removed from the text output. It’s not necessary to specify this on anything outside of the ` instapaper_body ` element, if present. 

也就是说，通过3个class名，可以显式地告诉Instapaper如何读取内容。instapaper_title这个class里的元素会作为标题，如果没有这
个class，那么会获取页面的<title>标签。

###  前端代码的最佳实践

####  使用语义化的html标签，不使用inline style

比如<h2>、<h3>作为段落标题，使用<strong>而不是<span style=”font-
weight:bold”>加粗，使用<code>来输出代码，使用<li>输出代码，使用<p>而不是<br/>来区分段落……因为当Read
Later之后，站点样式就失效了。

####  <h1>标签

页面中不要用两个<h1>标签，只需要一个作为最重要的标题就好了，比如新闻标题，博客标题……而不是网站标题。

也不要把<h1>标签放在<li>等其他标签中，从语义化来讲这是不对的。比如 [ 大猫 ](http://ooxx.me) 的日志页： [
![错误地使用h1标签](http://yuguo.us/files/2011/09/instapaper-2.png) ](http://ooxx.me
/mybloglog-farewell.orz) 那么在Instapaper的text中显示如下：
![错误地使用h1，导致在Instapaper中显示错误](http://yuguo.us/files/2011/09/instapaper-3.png)
<h4><h1>标签要带链接并指向本页url</h4> 帮助text来找到原文页面。不是必须的，但是会更友好。

####  不要错误地使用<section>标签

检查自己博客的read
later情况的时候，发现顶部导航条那里的个人信息也出现在了text中。调试过后发现使用了<section>标签，改为div就好了。查阅了这么一篇文章 [
《<section>不仅仅是“语义化的<div>”》 ](http://csspod.com/archives/section-is-not-just-a
-semantic-div) 之后，觉得自己之前对section的理解确实是错了。

> HTML 5中有一个构造文档大纲的算法，可以被诸如AT（不知何意，屏幕阅读器一类？）用来帮助用户通览文档。<section>及其他的新元素是这个算法的重
要组成部分。每嵌套一个<section>，大纲的深度就增加一级（如果你想把这种模型的优势和传统的<h1>-<h6>模型比较，想象一下一个基于Web的Feed
阅读器通过组合在一起的内容整合网站的页面结构，在HTML 4中，这意味要解析所有的内容并重新把所有的标题重新编号；HTML
5则可以在恰当的文档层级结束标题。）

所以其实<section>与<h1>-<h6>构建大纲有点类似，滥用的话，会让read later读取到错误的文章大纲。

####  注意标签顺序

即时在设计上是发表日期在前，标题在后，而在html代码中也应该是h1在前，这也是保证盲人读屏器第一次读到的是标题而不是不重要的时间。

####  对文章的操作，比如评论、编辑等不要放在<article>标签中。

##  最终优化结果

下面的截图是优化之后的结果，就像一篇文章一样，阅读体验很好。
![](http://yuguo.us/files/2011/09/instapaper-5.png) 相关资料：

[ Instapaper Friendly ](http://wordpress.org/extend/plugins/instapaper-
friendly/) [ Daily Tip: How to Make Your WordPress Blog Instapaper Friendly
](http://wpmu.org/daily-tip-how-to-make-your-wordpress-blog-instapaper-
friendly/) [ Information for publishers
](http://www.instapaper.com/publishers)

[ CMS的能力和责任 → ](/weblog/cms-power-and-responsibility/) [ ← 郁闷的开发环境
](/weblog/fml/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

