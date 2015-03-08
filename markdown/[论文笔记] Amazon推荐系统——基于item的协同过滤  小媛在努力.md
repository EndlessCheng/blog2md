#  [论文笔记] Amazon推荐系统——基于item的协同过滤 

_ _ [ zxy_snow ](http://www.xysay.com/author/zxy_snow) _ _ [ 推荐系统 ](http://www.xysay.com/category/%e6%8e%a8%e8%8d%90%e7%b3%bb%e7%bb%9f) , [ 论文笔记 ](http://www.xysay.com/category/%e8%ae%ba%e6%96%87%e7%ac%94%e8%ae%b0) _ _ 围观 _ 270 _ 次  _ _ [ 18 条评论 ](http://www.xysay.com/amazon-item-to-item-collaborative-filtering-207.html#comments) _ _ 编辑日期：  2014-07-01  _ _ 字体： [ 大 ](javascript:;) [ 中 ](javascript:;) [ 小 ](javascript:;)

#  Amazon.com Recommendations Item-to-Item Collaborative Filtering 

[   
点此下载论文：Amazon.com Recommendations Item-to-Item Collaborative Filtering ](http://www.cs.umd.edu/~samir/498/Amazon-Recommendations.pdf)   


** 内容概要：文章大致介绍了一下基于物品的协同过滤。并和基于用户的协同过滤、聚类方法以及基于搜索的方法进行了对比。 **   
  
评价邮件和web广告效果两个重要的指标：点击数，转化率。   
推荐系统的一些挑战： 

  1. 数据量大 

  2. 要求速度快，最好可以达到实时的效果 

  3. 冷启动问题 

  4. 老用户信息太多，如何筛选 

  5. 用户信息不稳定，可能随时更新<\--more-->

** 推荐的一般方法： **   
聚集一批相似的用户，根据他们共同购买或者评分过的商品估计未购买过的商品评分从而推荐。这个算法的实现就是传统的协同过滤和聚类模型。 

  1. 传统协同过滤（基于用户的协同过滤 ** User-based Collaborative Filtering ** ）：将用户表示成一个N维的物品的向量。多个用户表示成一个稀疏的矩阵。然后根据相似度（比如余弦相似度）计算出来用户的距离，用最相似用户的评分来替代未知的评分。 _ 本文指的是最近邻的协同过滤。 _
  * 复杂度：M个用户，N个物品，需要计算的用户跟每个用户进行相似度计算，每次为O(N)，所以总的复杂度为O(MN)。因为很稀疏所以总的复杂度大概在O(M+N)。  _ 因为矩阵非常非常稀疏，所以可以看做每个用户有常数个购买，假设计算次数为 _ _ aM+b _ _ （假设用邻接表或者 _ _ hash _ _ 表存储），则  扫描所有的用户复杂度为 _ _ O(M) _ _ 。筛掉一些购买量很大或者购买量非常小的商品，需要的复杂度为 _ _ O(N) _ _ 。 _
  2. 聚类的方法( ** Cluster Models ** )：将其看做分类的问题，使用无监督的聚类方法。聚类模型比基于用户的协同过滤在线上表现好。 _ 线下计算分类，线上直接使用线下的结果，找到需要的相似用户。 _
  3. 基于搜索的方法( ** Search-Based Methods ** )：根据相似的关键词，作者等来搜索相似物品。  _ 这个跟之前两种方法的不同之处是找的是相似的商品而不是用户，这个和下面的新方法有相同之处。 _
  * 缺点：范围太窄或者太宽泛。  _ 如果搜索的过程这么推荐感觉还可以，虽然窄或者宽泛，但都是在用户可以承受的范围内。如果用户买过这个物品再推荐同一类别的话，就不太合适了。 _

  
** 本文提出的新方法：基于物品的协同过滤 ** ** ( ** ** Item-to-Item Collaborative Filtering ** ** ) ** ** ： **

特点：实时推荐、大规模数据   
找到用户倾向一起购买的物品，然后建立一个商品对商品的相似矩阵。复杂度在O(N  2  M)，  _ 扫一遍商品N，扫每个商品的购买者M _ _ ，对于每个购买者扫他购买的其他商品 _ _ N _ _ ，故复杂度为 _ _ O(N  2  M) _ _ 。 _ 实现中接近O(MN)。 _ 最内层的扫描由于矩阵很稀疏，所以可以看做常数（邻接表或者 _ _ hash表实现），故可以减少个N。 _

> For each item in product catalog, I1 
> 
> For each customer C who purchased I1 
> 
> For each item I2 purchased by customer C 
> 
> Record that a customer purchased I1 and I2 
> 
> For each item I2 
> 
> Compute the similarity between I1 and I2 

![](file:///C:\\Users\\zxy\\AppData\\Local\\Temp\\msohtmlclip1\\01\\clip_image001.png)   
基于物品的协同过滤的关键是创建线下的物品相似矩阵。线上算法作为补充，计算量独立于总的物品个数和总的用户个数。它仅仅依赖于用户购买量和评分量。因此这个算法即使在大数据上也会很快。 

  
** 四种方法的对比 ** ： 

  1. 传统协同过滤几乎没有线下计算，而线上如果不减小维度的话的计算量太大。 
  2. 聚类模型线下计算要好一点，但是推荐质量低。为了提升推荐质量，分类的个数要增加，但是这样的话会使得线上分类代价高。 
  3. 基于搜索的模型不能给用户推荐比较有兴趣的物品，推荐的域太窄。 

[   
看完了发现本论文的全文翻译一篇>< ](http://blog.sina.com.cn/s/blog_586631940100pduh.html)

  * 本文固定链接: [ http://www.xysay.com/amazon-item-to-item-collaborative-filtering-207.html ](http://www.xysay.com/amazon-item-to-item-collaborative-filtering-207.html)
  * 转载请注明: [ zxy_snow ](http://www.xysay.com/author/zxy_snow) 2014年06月23日  于 [ 小媛在努力 ](http://www.xysay.com/) 发表 

_ _ [ item-based ](http://www.xysay.com/tag/item-based) ， [ 亚马逊 ](http://www.xysay.com/tag/%e4%ba%9a%e9%a9%ac%e9%80%8a) ， [ 协同过滤 ](http://www.xysay.com/tag/%e5%8d%8f%e5%90%8c%e8%bf%87%e6%bb%a4) ， [ 推荐系统 ](http://www.xysay.com/tag/%e6%8e%a8%e8%8d%90%e7%b3%bb%e7%bb%9f)

  

#### 原文：[http://www.xysay.com/amazon-item-to-item-collaborative-filtering-207.html](http://www.xysay.com/amazon-item-to-item-collaborative-filtering-207.html)