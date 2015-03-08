#  [论文笔记] GroupLens: 一个基于协同过滤的新闻架构 

_ _ [ zxy_snow ](http://www.xysay.com/author/zxy_snow) _ _ [ 推荐系统 ](http://www.xysay.com/category/%e6%8e%a8%e8%8d%90%e7%b3%bb%e7%bb%9f) , [ 论文笔记 ](http://www.xysay.com/category/%e8%ae%ba%e6%96%87%e7%ac%94%e8%ae%b0) _ _ 围观 _ 121 _ 次  _ _ [ 3 条评论 ](http://www.xysay.com/grouplens-open-architecture-collaborative-filtering.html#comments) _ _ 编辑日期：  2014-07-01  _ _ 字体： [ 大 ](javascript:;) [ 中 ](javascript:;) [ 小 ](javascript:;)

#  GroupLens： An Open Architecture for Collaborative Filtering of Netnews   


[ 点此下载论文：  GroupLens：An Open Architecture for Collaborative Filtering of Netnews  ](http://su-2010-projekt.googlecode.com/svn-history/r202/trunk/literatura/resnick1994grouplens.pdf)

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


评分范围是1到5分，从兴趣、写作质量、作者的权威性等等来评分。用户会被问到别的用户怎么看而不是用户对这篇文章多喜欢。根据 ** 相关系数 ** 来判断文章的相关度。评分后将这些评分展示出来让读者看。 

##  思考   


这篇文章是1994年发表的，距今已经20年了，读起来很生硬，大概是因为很多专业术语现在都不用或者改名了吧，读着好困难，冗杂信息很多，更像科普类的文章。不过，真难想象，那时候win98都没出来，都开始搞推荐了><，果然中国不是落后一点点。这篇文章应该是一篇引领性的文章，提出的方法还是很稚嫩的，但是却开辟了协同过滤这片领域。读不下去了，呜呜。 ** 原谅我的粗读吧，实在是读不下去了。 **

[1] GroupLens: http://grouplens.org/ 

  * 本文固定链接: [ http://www.xysay.com/grouplens-open-architecture-collaborative-filtering.html ](http://www.xysay.com/grouplens-open-architecture-collaborative-filtering.html)
  * 转载请注明: [ zxy_snow ](http://www.xysay.com/author/zxy_snow) 2014年07月01日  于 [ 小媛在努力 ](http://www.xysay.com/) 发表 

_ _ [ GroupLens ](http://www.xysay.com/tag/grouplens) ， [ 协同过滤 ](http://www.xysay.com/tag/%e5%8d%8f%e5%90%8c%e8%bf%87%e6%bb%a4) ， [ 推荐系统 ](http://www.xysay.com/tag/%e6%8e%a8%e8%8d%90%e7%b3%bb%e7%bb%9f)

  

#### 原文：[http://www.xysay.com/grouplens-open-architecture-collaborative-filtering.html](http://www.xysay.com/grouplens-open-architecture-collaborative-filtering.html)