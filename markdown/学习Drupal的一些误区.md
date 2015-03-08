#  学习Drupal的一些误区

[ Yuguo ](http://yuguo.us) 2011年 05月 19日

翻译自 [ Stackoverflow ](http://stackoverflow.com/questions/1791553/what-are-the-
most-common-pitfalls-for-a-beginner-drupal-user) 上面的一个问答。

##  问

我刚开始学习 [ Drupal ](http://en.wikipedia.org/wiki/Drupal)
，并且我真的很喜欢它！那么初学者最常见的陷阱是什么呢？如何避免？

##  回答

首先你要知道你到底是想要学什么？

  * 主题定制？ 
  * 建站？ 
  * 开发新的模块/功能？ 

当然它们并不是完全分离开的，但如果能决定学哪一个方向的话，会有一些稍各不不同的模式。这是我的观点：

###  通常的陷阱（适用于所有领域）

初学者最常犯的错误就是太着急。这个世界上有很多《24小时学会C++》这样的书，这样初学者往往试图在研究了几天别人的代码之后就能玩转Drupal。如果它们没有
一开始就明白Drupal是如何工作的，它们就会进入狂暴模式，在所有的论坛大放厥词说Drupal是多么该死地复杂难用。

所以：准备好投入时间和精力来迎接Drupal的复杂性（复杂性不等同于复杂化）。真的准备好 ** 学习 **
它是如何工作的，而不是初略浏览问题列表或者邮件列表。如果你对这一条仍然怀疑，这里有一篇 [ 很好的文章
](http://norvig.com/21-days.html) 。

###  如果你在学习主题制作

陷进：从hack前人的主题开始学习制作

更好的方法：首先，好好看看Drupal [ 主题手册 ](http://drupal.org/theme-guide)
。它枯燥无味但能给你一个很好的概要，告诉你主题引擎是如何工作的。然后下载安装 [ zen theme
](http://drupal.org/project/zen) 然后从里面包含的初学者包（starter kit）开始编码。

###  如果你在学习建站

陷阱：可用的模块如此多，有可能让你不知所措而错过一些重要的

更好的方法：学习一些已经在drupal.org上经过几年历练筛选的 [ 案例研究 ](http://drupal.org/cases) ，你会得到一些很好的
模式，他们结合一些特定的模块能完成各种各样的需求。然后理解Drupal的核心组件。它们是其余一切的基础，所以你绝对有必要知道nodes和revision的工
作原理，taxonomy的功能，权限/角色是如何工作的，nodes和blocks的区别等等……不要错过 [ CCK
](http://drupal.org/project/cck) 和 [ Views ](http://drupal.org/project/views)
，99%的网站都用到他们。

###  如果你在学习写模块

陷阱：通过把网上搜索来的PHP代码和jQuery片段来组成自己需要的功能

更好的方法： _ _ if you want to be good at drupal you can’t afford to go by the _
just in time _ learning paradigma, you have to go for the old-school _ just in
case _ one. You really need to have a general overall understanding of all the
components of the system (amongst others: form API, menu system, hook logic,
js in Drupal, node processing, theming engine, localisation, caching…). Drupal
is somehow a framework, and if you do not know well the ecosystem in which you
are planting your code, chances are you will spent lot of time in producing an
horrible code that will soon or later fail in doing what it is supposed to.
Above all you will take a lot of time to code something that possibly would
have taken a fraction of the time to be realised “the drupal way”.

###  如果要学好Drupal，我认为有用的工具

[ http://drupal.org ](http://drupal.org)
这里打包了很多有用的信息，但是缺点是有点杂乱而且信噪比如此低，很难把它作为主要的信息来源。

书籍：我的观点是，如果你初学Drupal，有必要投资几本书。书籍提供了一个很好的逻辑结构，这个逻辑结构是你从一个站点跳到另一个站点的过程中无法领略到的。

[ 要帅到什么程度才能找到女朋友？ → ](/weblog/handsome-enough-to-get-a-girl/) [ ←
上海、杭州、西塘、南京旅游小攻略 ](/weblog/travel/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

