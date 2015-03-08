[ ![小媛在努力](https://farm4.staticflickr.com/3878/14293872807_5d75ce918e_o.png)
](http://www.xysay.com/) _ hi hi bye bye~ _ SEARCH

![小媛在努力](https://farm3.staticflickr.com/2923/14479005692_29a98a69a0_o.jpg)

网站导航

  * [ Home ](http://xysay.com)
  * [ About Me ](http://www.xysay.com/about-me)

_ _ [ 首页 ](http://www.xysay.com) > [ 推荐系统
](http://www.xysay.com/category/%e6%8e%a8%e8%8d%90%e7%b3%bb%e7%bb%9f) > [论文笔记]
GroupLens: 一个基于协同过滤的新闻架构

2014  
07-01

#  [论文笔记] GroupLens: 一个基于协同过滤的新闻架构

_ _ [ zxy_snow ](http://www.xysay.com/author/zxy_snow) _ _ [ 推荐系统
](http://www.xysay.com/category/%e6%8e%a8%e8%8d%90%e7%b3%bb%e7%bb%9f) , [ 论文笔记
](http://www.xysay.com/category/%e8%ae%ba%e6%96%87%e7%ac%94%e8%ae%b0) _ _ 围观 _
121 _ 次  _ _ [ 3 条评论 ](http://www.xysay.com/grouplens-open-architecture-
collaborative-filtering.html#comments) _ _ 编辑日期：  2014-07-01  _ _ 字体： [ 大
](javascript:;) [ 中 ](javascript:;) [ 小 ](javascript:;)

#  GroupLens： An Open Architecture for Collaborative Filtering of Netnews  

[ 点此下载论文：  GroupLens：An Open Architecture for Collaborative Filtering of
Netnews  ](http://su-2010-projekt.googlecode.com/svn-
history/r202/trunk/literatura/resnick1994grouplens.pdf)

##  内容概要  

GroupLens[1]提出了一个新的基于协同过滤的架构。应该是最早的协同过滤的提出了。现在看来应该没啥内容，但是应该在当时是个很厉害的文章吧。

##  网络新闻  

两大机制：

  1. 根据话题内容将新闻分类 
  2. 有一些新闻组有审稿人，他们将投稿过来的新闻分类 

GroupLens提出了新的机制：用户评过分（高分）的话题以后关注的可能性会更大。

##  相关工作  

  1. content-based filtering techniques：根据文章的内容选择。比如根据关键词过滤；根据逻辑运算AND,OR,NOT进行操作；根据用户的选择来反馈，然后更新。 
  2. Social filtering techniques：根据人之间的关系和主观判断来选择文章。Collaborative filtering是根据其他读者的评价来推荐。是一种比较有前途的社会过滤。相当于原来只有一个评稿人（moderator），现在有很多个。 

类似于Tapestry，我们的不同之处在于：

  1. Tapestry只参考一个网站，而我们的评价是贯穿好几个网站的。 
  2. 我们根据一些评价者整合了评分，用户不需要知道这些评分是怎么来的。 

##  评分  

评分范围是1到5分，从兴趣、写作质量、作者的权威性等等来评分。用户会被问到别的用户怎么看而不是用户对这篇文章多喜欢。根据 ** 相关系数 **
来判断文章的相关度。评分后将这些评分展示出来让读者看。

##  思考  

这篇文章是1994年发表的，距今已经20年了，读起来很生硬，大概是因为很多专业术语现在都不用或者改名了吧，读着好困难，冗杂信息很多，更像科普类的文章。不过，
真难想象，那时候win98都没出来，都开始搞推荐了><，果然中国不是落后一点点。这篇文章应该是一篇引领性的文章，提出的方法还是很稚嫩的，但是却开辟了协同过滤
这片领域。读不下去了，呜呜。 ** 原谅我的粗读吧，实在是读不下去了。 **

[1] GroupLens: http://grouplens.org/

  * 本文固定链接: [ http://www.xysay.com/grouplens-open-architecture-collaborative-filtering.html ](http://www.xysay.com/grouplens-open-architecture-collaborative-filtering.html)
  * 转载请注明: [ zxy_snow ](http://www.xysay.com/author/zxy_snow) 2014年07月01日  于 [ 小媛在努力 ](http://www.xysay.com/) 发表 

最后编辑：  2014-07-01

** 作者：zxy_snow **

![](http://1.gravatar.com/avatar/390ba7fe743122e7d40c1b778d8777f1?s=96&d=ident
icon&r=G)

吃好，喝好，学习好！

[ _ _ 站内专栏 ](http://www.xysay.com?author=1) [ _ _ 站点 ](http://www.xysay.com)

_ _ [ GroupLens ](http://www.xysay.com/tag/grouplens) ， [ 协同过滤
](http://www.xysay.com/tag/%e5%8d%8f%e5%90%8c%e8%bf%87%e6%bb%a4) ， [ 推荐系统
](http://www.xysay.com/tag/%e6%8e%a8%e8%8d%90%e7%b3%bb%e7%bb%9f)

  

[ _ _ [读书笔记] sk_buff套接口缓存结构 ](http://www.xysay.com/sk-buff-struct.html)

[ [论文笔记] 基于物品的协同过滤算法 _ _ ](http://www.xysay.com/item-based-collaborative-
filtering-algorithms.html)

###  _ _ 您可能还会对这些文章感兴趣！

  * [ [论文笔记] 基于物品的协同过滤算法 ](http://www.xysay.com/item-based-collaborative-filtering-algorithms.html)
  * [ [论文笔记] Amazon推荐系统——基于item的协同过滤 ](http://www.xysay.com/amazon-item-to-item-collaborative-filtering-207.html)

  1. [ uidhfuaish ](http:zho) on [ 2014 年 7 月 17 日 at 11:00  ](http://www.xysay.com/grouplens-open-architecture-collaborative-filtering.html#comment-2383) said: 

admiration

  2. 剑洋侠客  on [ 2014 年 7 月 29 日 at 11:40  ](http://www.xysay.com/grouplens-open-architecture-collaborative-filtering.html#comment-2387) said: 

嗯，界面越来越漂亮了

  3. [ XxX_Stu ](http://www.3xstu.tk) on [ 2014 年 9 月 8 日 at 16:27  ](http://www.xysay.com/grouplens-open-architecture-collaborative-filtering.html#comment-2407) said: 

露个脸...

  *   * ###  分类 

    * [ Life ](http://www.xysay.com/category/life) (9) 
    * [ Linux ](http://www.xysay.com/category/linux%e5%ad%a6%e4%b9%a0) (2) 
    * [ 写代码玩儿 ](http://www.xysay.com/category/%e5%86%99%e4%bb%a3%e7%a0%81%e7%8e%a9%e5%84%bf) (1) 
    * [ 学习笔记 ](http://www.xysay.com/category/%e5%ad%a6%e4%b9%a0%e7%ac%94%e8%ae%b0) (3) 
    * [ 推荐系统 ](http://www.xysay.com/category/%e6%8e%a8%e8%8d%90%e7%b3%bb%e7%bb%9f) (3) 
    * [ 论文笔记 ](http://www.xysay.com/category/%e8%ae%ba%e6%96%87%e7%ac%94%e8%ae%b0) (3) 
    * [ 题解 ](http://www.xysay.com/category/%e9%a2%98%e8%a7%a3) (1) 
  * ###  最近评论 

  * ###  近期文章 

    * [ 14已过，15整装待发，准备启航 ](http://www.xysay.com/14-summary-15-outlook.html)
    * [ [读书笔记] 网络模块初始化 ](http://www.xysay.com/net-module-init.html)
    * [ [读书笔记] sk_buff套接口缓存结构 ](http://www.xysay.com/sk-buff-struct.html)
    * [ [论文笔记] GroupLens: 一个基于协同过滤的新闻架构 ](http://www.xysay.com/grouplens-open-architecture-collaborative-filtering.html)
    * [ [论文笔记] 基于物品的协同过滤算法 ](http://www.xysay.com/item-based-collaborative-filtering-algorithms.html)
  * ###  友情链接 

    * [ cgangee@ZZU ](http://www.cgangee.com)
    * [ FOOKWOOD@阿里 ](http://www.fookwood.com)
    * [ IdleMind ](http://idlemind.sinaapp.com/)
    * [ LaiZhihua ](http://HelloACM.com)
    * [ Vgo@Darling ](http://zhangjixin.tk/)
    * [ 一起吧，GO! ](http://www.178-go.com/)
    * [ 刁瑞@Google ](http://diaorui.net/)
    * [ 我的CSDN博客 ](http://blog.csdn.net/zxy_snow)
    * [ 李奇@ZZU ](http://qilee.me/)
  * ###  文章归档 

    * [ 2015年一月 ](http://www.xysay.com/2015/01)
    * [ 2014年十月 ](http://www.xysay.com/2014/10)
    * [ 2014年七月 ](http://www.xysay.com/2014/07)
    * [ 2014年六月 ](http://www.xysay.com/2014/06)
    * [ 2013年四月 ](http://www.xysay.com/2013/04)
    * [ 2012年十一月 ](http://www.xysay.com/2012/11)
    * [ 2012年五月 ](http://www.xysay.com/2012/05)
    * [ 2012年三月 ](http://www.xysay.com/2012/03)
    * [ 2012年二月 ](http://www.xysay.com/2012/02)
    * [ 2012年一月 ](http://www.xysay.com/2012/01)
    * [ 2011年十二月 ](http://www.xysay.com/2011/12)
  * ###  Tags 

[ 碎碎念 (4) ](http://www.xysay.com/tag/%e7%a2%8e%e7%a2%8e%e5%bf%b5) [ linux (3)
](http://www.xysay.com/tag/linux) [ 计划 (3)
](http://www.xysay.com/tag/%e8%ae%a1%e5%88%92) [ 感想 (3)
](http://www.xysay.com/tag/%e6%84%9f%e6%83%b3) [ 协同过滤 (3)
](http://www.xysay.com/tag/%e5%8d%8f%e5%90%8c%e8%bf%87%e6%bb%a4) [ 推荐系统 (3)
](http://www.xysay.com/tag/%e6%8e%a8%e8%8d%90%e7%b3%bb%e7%bb%9f) [ 网络协议栈 (2)
](http://www.xysay.com/tag/%e7%bd%91%e7%bb%9c%e5%8d%8f%e8%ae%ae%e6%a0%88) [
item-based (2) ](http://www.xysay.com/tag/item-based) [ ACM (2)
](http://www.xysay.com/tag/acm) [ 校赛 (2)
](http://www.xysay.com/tag/%e6%a0%a1%e8%b5%9b) [ 郑州大学 (2)
](http://www.xysay.com/tag/%e9%83%91%e5%b7%9e%e5%a4%a7%e5%ad%a6) [ 内核 (2)
](http://www.xysay.com/tag/%e5%86%85%e6%a0%b8) [ 考研 (1)
](http://www.xysay.com/tag/%e8%80%83%e7%a0%94) [ algorithm (1)
](http://www.xysay.com/tag/algorithm) [ GroupLens (1)
](http://www.xysay.com/tag/grouplens) [ 2014总结 (1)
](http://www.xysay.com/tag/2014%e6%80%bb%e7%bb%93) [ 2015展望 (1)
](http://www.xysay.com/tag/2015%e5%b1%95%e6%9c%9b) [ 亚马逊 (1)
](http://www.xysay.com/tag/%e4%ba%9a%e9%a9%ac%e9%80%8a) [ C++ (1)
](http://www.xysay.com/tag/c) [ 408 (1) ](http://www.xysay.com/tag/408) [ 中科院
(1) ](http://www.xysay.com/tag/%e4%b8%ad%e7%a7%91%e9%99%a2) [ socket (1)
](http://www.xysay.com/tag/socket) [ 算法 (1)
](http://www.xysay.com/tag/%e7%ae%97%e6%b3%95) [ 数据库 (1)
](http://www.xysay.com/tag/%e6%95%b0%e6%8d%ae%e5%ba%93)

[ 返回顶部 ](javascript:void\(0\)) [ 网站地图 ]() [ ](http://www.miitbeian.gov.cn/) ©
| Theme  frontopen2

[ ](javascript:void\(\)) [ ](http://www.xysay.com/wp-admin/) [
](javascript:void\(\))

