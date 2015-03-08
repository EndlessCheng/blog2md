#  介绍Drupal

[ Yuguo ](http://yuguo.us) 2011年 01月 26日

Drupal是一个相当不错的CMS。在这几年CMS的蓬勃发展中，他跟wordpress一起发展壮大起来，这说明在CMS业不会有一家独大的现象，每个站点都有适
合自己的系统。在认识Drupal之前我用过的几个CMS都是以博客为主的系统——比如wordpress，而如果希望用以博客为主的CMS来做新闻站点或者类目复杂
一点的信息发布站点就会比较麻烦。当然了，完全可以用不是那么适合的工具做出各种类型的站点，但那只能说明开发者牛叉并且很爱折腾。我觉得以显示自己技术的折腾都是耍
流氓，所以我开始使用Drupal。

因为我对wordpress更加熟悉，所以介绍Drupal的时候会作出对比，从一个熟悉的概念介绍一个陌生的概念往往是一种很有效的学习方法。

##  Drupal与wordpress的不同

这二个系统经常被拿来跟对方比较。 [ changingway.org ](http://changingway.org/2010/04/29/drupal-
and-wordpress-two-years-on/) 的结论是“wordpress更容易上手。而当页面开始复杂的时候，Drupal是更好的选择”。这些年
来两个系统互相从对方身上学习优点，都在变得更加易用、更易配置。

###  哪些人适合使用wordpress搭建站点

初学者；希望搭建一个类博客——发布时间敏感的内容（Time Senstive Content）的站点——的开发者；

###  哪些人适合使用Drupal搭建站点

搭建更复杂的站点；希望给客户制作站点的时候提供友好的后台界面和适当接口；希望后台模块可自定义，不加载不必要的影响速度的模块的开发人员；希望不用重复发明轮子的
开发人员；崇尚开源的开发人员。

##  基本概念

mode（模块）：Drupal有一个优秀的模块化结构，提供了许多模块，包括短消息、个性化书签、网站管理、Blog、日记、电子商务、电子出版、留言簿、Job、
网上电影院、论坛、投票等模块。有一些模块是必须开启的核心模块比如node，此外还有一些可选的模块比如vote。需要建立一个什么样的系统，就对应开启哪些可选模
块，这能有效提高网站速度。

node（节点）：Drupal中的node大致相当于wordpress中的post和page，但是在概念上更加直白。比如说如果为医院做一个网站系统，希望医生
登录后能发布处方。如果用wordpress实现，那么医生就会新建一个post，category设置为处方，然后在custom fields里填一些字段以完成
特殊的功能。如果用Drupal，医生就能直接选择新建一个“处方”。“处方”就是一个node，工程师设定了处方需要的字段——比如一段描述，n个药名，一张图片。
医生新建这个处方之后只需要填好这些字段，发布就好了。它会按照设定出现在该出现的地方，以预期的方式显示出来。

taxonomies（分类学）：Drupal的分类学比wordpress层次更深一些，也更有逻辑一些。在wordpress中类别是category，一篇po
st发出去之后能设定属于一个或者n个category，这些category的关系可能有层级，也可能没有层级。Drupal中是通过 **
vocabularies（类别） ** 和 ** terms（分类） ** 来管理内容的，一个类别下包含一个或多个分类。比如一个node叫做“相片”，那么新
建一个“相片”的时候能够输入的类别可能是两个“在哪儿”“主题是什么”，在每种类别中可以选择一个分类，比如上传一张表哥的照片的时候就在哪儿选择“纽约”，主题是
什么选择“人像”。而如果另一个node叫做“诗歌”，那么类别就不会有“在哪儿”，而是“诗歌类型”这样的，这个类别包含的分类可能包含十四行诗、现代诗等等。

分类方法：一个类别中有一些分类，那么这些分类是以何种类型来展示的呢，有三种类型：flat（平滑的）、tree（树）、free-
tagging（自由标记）。详见 [ Understanding taxonomies for new users
](http://drupal.org/node/46268) tag：在Drupal中，你可以自定义一个类别叫Keywords，把它设置为free-
tagging这种类型的类别——也就是说这个类别的分类是由用户自由输入的。

##  相关资料

###  英文

[ Content types ](http://drupal.org/node/21947) [ Vocabularies and terms
](http://drupal.org/node/22272) <h3>中文</h3> [ 适用于初学者的Drupal菜谱
](http://zhupou.cn/drupal-handbook/tutorials/beginners-cookbook)
接下来的几篇文章会介绍如何迁移到Drupal以及一些更高级的话题。

[ 从wordpress迁移到Drupal → ](/weblog/migrating-from-wordpress/) [ ← 关于云端书签的一个想法
](/weblog/one-idea-about-cloud-bookmark/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

