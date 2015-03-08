  * [ Mind Hacks 的含义 ](http://mindhacks.cn/about/)
  * [ 前世档案 | C++的罗浮宫 ](http://mindhacks.cn/former-life-of-mindhacks/)
  * [ 所有文章 ](http://mindhacks.cn/archives/)
  * [ TopLanguage 讨论组 ](http://mindhacks.cn/about-toplanguage/)
  * [ 价值博客们 ](http://mindhacks.cn/friend-links/)

[ 刘未鹏 | Mind Hacks ](http://mindhacks.cn) 思维改变生活

  * [ 学习方法 ](http://mindhacks.cn/topics/learning-method/)
  * [ 思维改变生活 ](http://mindhacks.cn/topics/mind/)
  * [ 算法 ](http://mindhacks.cn/topics/algorithms/)
  * [ 计算机科学 ](http://mindhacks.cn/topics/computer-science/)
  * [ 数学 ](http://mindhacks.cn/topics/math/)
  * [ 机器学习与人工智能 ](http://mindhacks.cn/topics/machine-learning/)
  * [ 编程 ](http://mindhacks.cn/topics/programming/)

  * [ RSS Feed ](http://mindhacks.cn/feed/)

#  [ 编程的首要原则(s)是什么？ ](http://mindhacks.cn/2009/03/09/first-principles-of-
programming/)

By  [ 刘未鹏 ](http://mindhacks.cn/author/pongba/)

–  March 9, 2009  ** Posted in: ** [ 编程
](http://mindhacks.cn/topics/programming/)

半年前，JoelOnSoftware和CodingHorror合搞的stackoverflow.com刚上线不久，我兴冲冲地跑过去扔了一个问题：

** 你们认为编程的首要原则是什么？ **

作为我的 [ 学习原则 ](http://mindhacks.cn/2008/07/08/learning-habits-part1/) 的一个实践： [
![important](http://mindhacks.cn/wp-content/uploads/2009/03/important-
thumb.png) ](http://mindhacks.cn/wp-content/uploads/2009/03/important.png)

> 8\. 学习一项知识，必须问自己三个重要问题：1. 它的本质是什么。2. 它的第一原则是什么。3. 它的知识结构是怎样的。

5个月过去了，这个问题到现在还有人回复，我得到了一大堆有意思的答案，忍不住翻译过来与大家分享：

1\. 获得 ** 最多认同的答案 ** ：

> ** KISS – Keep It Simple Stupid **

>

> ** DRY – Don’t Repeat Yourself **

一点不感到意外吧？

注：DRY原则倒是比较好理解和实践的。但KISS原则则是看上去直白，其实实践起来不那么容易的一个原则，因为simple和stupid的定义并不是每个人、在每
个场景下都是一致且明显的，一个人的simple可能是另一个人的stupid，一个人的stupid可能是另一个人的unnecessary。一旦一个标准取决于具
体场景，事情就不那么简单了。所以我们经常要说“ [ It depends ](http://c2.com/cgi/wiki?ItDepends) ”。

2\. 获得 ** 第二认同的答案 ** ：

> ** 写代码时时刻设想你就是将来要来维护这坨代码的人。 **

在这个答案后面有人添加到：

> 最好设想你的代码会被一个挥着斧头的精神病来维护。

有人接着又YY道：

> 而且这个挥着斧头的精神病还知道你住在哪儿。 (( 事实上后面有人指出这是 Martin Golding 的一句名言 ))

注：其实这个原则在设计API时也有用：

> ** 写API时时刻设想你就是要去使用这坨API的人。 **

3\. ** 一些众所不一定周知的答案 ** ：

> ** 先弄清你的问题是什么！ **

[ 弄清问题 ](http://www.douban.com/subject/1135754/) 永远是问题解决过程中的第一步和最重要的一步。

> ** 代码只是工具，不是手段。 **

不知道怎么最好地解决你手头的问题（注：需求、架构、算法，技术选型，etc..），写上一万坨代码也是浪费比特。

> ** 知道什么时候不该编码 ** 。

（类似条目：YAGNI——“你并不需要编写这坨代码！”，针对你的需求编码，“写你所需”，别做“聪明事”，为一个不确定的未来编码。同时也注意模块化设计，以便能
在未来新增需求时无痛扩充系统）

> ** 永远不要假定你已经了解一切了！ **

> ** 不作没有证据的推论。 **

> ** 想清楚了再编写 ** 。类似条目： ** 如果方案在你脑子里面或者纸上不能工作，写成代码还是不能工作。 **

4\. 一些众所很可能周知的答案：

> 越懒越好。

>

> 过早优化是一切罪恶的根源。

>

> 不要重新发明轮子。

>

> 测试通过前说什么“它可以工作”都是纯扯淡。

>

> 了解你的工具。

>

> 一切以用户需求为导向。

>

> 利用分治、抽象，解开子问题之间的耦合。

5\. ** 最幽默的答案 ** ：

> ** 咖啡进，代码出 ** 。（Coffee in, Code out） (( 参见 [ Garbage in, Garbage out
](http://en.wikipedia.org/wiki/Garbage_in,_garbage_out) . ))

最后，整个问题的 thread 在 [ 这里 ](http://stackoverflow.com/questions/159176) 。

** Tags: ** [ 编程 ](http://mindhacks.cn/tags/%e7%bc%96%e7%a8%8b/)

[ ](http://mindhacks.cn/author/pongba/)

####  About 刘未鹏

  1. rurulikecc  on [ March 9, 2009 at 7:09 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-152) said: 

你喜欢怎样编程你的原则就是什么

  2. netawater  on [ March 9, 2009 at 8:33 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-154) said: 

脚注的返回链接怎么弄的啊？大侠是用muse吗？

    * [ 刘未鹏 ](http://mindhacks.cn) on [ March 9, 2009 at 8:54 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-155) said: 

我是先看到李笑来老师用的，注意到他每篇文章的 footnotes 都是标准格式，想必用了插件，于是 Google 了一把 “wordpress
footnotes” ，就找到了 wp-footnotes 插件。

      * netawater  on [ March 10, 2009 at 9:17 am  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-160) said: 

哦，了解，谢谢！那你文章中的超链接也是wordpress插件生成的咯？

        * [ 刘未鹏 ](http://mindhacks.cn) on [ March 10, 2009 at 11:04 am  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-161) said: 

指向脚注和脚注中回指的超链接是wp-footnotes生成的。

          * netawater  on [ March 10, 2009 at 9:43 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-166) said: 

不好意思，我是想指“It depends”这种超链接，文中很多，怎么生成的了？谢谢啦。

        * [ 刘未鹏 ](http://mindhacks.cn) on [ March 10, 2009 at 10:22 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-167) said: 

it depends的链接是手动加的，机器还没聪明到这个程度:D

          * netawater  on [ March 11, 2009 at 9:18 am  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-169) said: 

呵呵，辛苦了，我本以为是机器会去查预设的表，然后自动生成这些超链接。

  3. [ iamsujie ](http://iamsujie.com) on [ March 9, 2009 at 9:14 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-156) said: 

哇你站已经备案好了呀，好快，我常看到几个blog已经有不幸中招的了。。。  
技术由思想驱动，真是威力无穷～～～

    * [ 刘未鹏 ](http://mindhacks.cn) on [ March 9, 2009 at 9:31 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-157) said: 

我申请空间之后立即就备案了，反正填个表的事，几分钟 ![:\)](http://mindhacks.cn/wp-
includes/images/smilies/icon_smile.gif)

  4. xiaobo  on [ March 9, 2009 at 11:46 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-158) said: 

编程的首要原则是：这个问题是需要编程解决的吗，或者说编程能够解决的吗？ 思考到这一点才能真正了解编程（或者说工具）在问题解决过程中的所起的地位，他应该如何和
人，和人们做事的过程相匹配，能够调动人，调整人们做事的方法，过程，起到更好的作用。

    * [ ant ](http://an.haokanbu.com) on [ March 11, 2009 at 1:32 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-171) said: 

赞，编程的首要原则就是想办法不编程。

  5. [ Mark.long ](http://longlinfeng.blogspot.com) on [ March 10, 2009 at 8:35 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-164) said: 

呵呵，这个探讨有些意思。从小工到专家一定得仔细思考的两个原则

  6. [ vdust.leo ](http://blog.csdn.net/vdust) on [ March 10, 2009 at 8:55 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-165) said: 

K.I.S.S & D.R.Y， 我有钱的话，准备说说这个故事。

  7. [ sun ](http://www.osun.net) on [ March 12, 2009 at 2:40 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-172) said: 

看你在编程过程中扮演什么角色

  8. EMCToo  on [ March 12, 2009 at 9:18 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-173) said: 

内容我没有什么说的，很好、很强大。  
——我只是特别反感题目中的那个（s）。

  9. kevin  on [ March 13, 2009 at 4:06 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-175) said: 

写代码时时刻设想你就是将来要来维护这坨代码的人。

这句话里的“坨”字用的很传神～！

  10. joseph  on [ March 15, 2009 at 5:59 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-182) said: 

er..Could you use some e.g s to explain what is the first principle? Plus,
there may be several main principles of one discipline.

    * [ 刘未鹏 ](http://mindhacks.cn) on [ March 17, 2009 at 1:01 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-247) said: 

Yeah, I will, sometime.  
Collecting good examples and introspecting on the rationales are no easy
thing. I’m working on it ![:\)](http://mindhacks.cn/wp-
includes/images/smilies/icon_smile.gif)

  11. Tom Lau  on [ March 17, 2009 at 10:49 am  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-245) said: 

Here just brief a lot of principals/conclusions without challenging reasoning.
I think it is acceptable if you are an agile guy in software development
field. The article is something like a note of tips.

However, to those who are not very experienced, I would prefer “Clarify/Define
the questions/problems.’ As it is shown that a lot of people just get used to
zip-zap way to resolve the problem. Get to the points & don’t get side-track.

I would thank Mr. Liu (bartender) for incurring a lot of hints to our brains!
![:\)](http://mindhacks.cn/wp-includes/images/smilies/icon_smile.gif)

    * [ 刘未鹏 ](http://mindhacks.cn) on [ March 17, 2009 at 12:59 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-246) said: 

> Here just brief a lot of principals/conclusions without challenging
reasoning. However, to those who are not very experienced, I would prefer
“Clarify/Define the questions/problems.

I totally agree. This article is more of a reminder or memo for experienced
guys.

  12. victor  on [ March 22, 2009 at 8:24 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-286) said: 

你提出：学习一项知识，必须问自己三个重要问题：1. 它的本质是什么。2. 它的第一原则是什么。3. 它的知识结构是怎样的。  
请问，你所说的本质和第一原则到底是什么。

  13. [ Waternie ](http://www.51dida.net) on [ March 24, 2009 at 7:38 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-295) said: 

这些都是“Unix编程艺术”一书里说的原则。。。

  14. 宁静  on [ June 18, 2009 at 9:58 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-508) said: 

不要只低头的使你的代码完善，而要抬头看看他现在的样子

  15. [ Zianed ](http://my.unix-center.net/~Zianed/) on [ September 10, 2009 at 10:45 am  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-578) said: 

Make it Simple,Stupid  
我是很崇尚这句话，可是实施起来实在是难。

  16. [ vêtements femmes ](http://www.yaamaa.com) on [ October 12, 2009 at 2:18 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-607) said: 

编程以前我读书的时候学过,现在忘了,呵呵,

  17. [ gros vêtements ](http://www.yaakii.com) on [ January 13, 2010 at 2:26 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-742) said: 

, I would prefer “Clarify/Define the questions/problems

  18. [ Chaussures femmes ](http://www.kkily.com) on [ January 13, 2010 at 2:26 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-743) said: 

I would prefer “Clarify/Define the questions/problems.’ As it is shown that a
lot of people just get used to zip-zap way to resolve the problem

  19. [ 胡鹏飞 ](http://www.renren.com) on [ March 26, 2010 at 10:57 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-854) said: 

这个网站的文章挺好的

  20. joey  on [ July 19, 2010 at 11:28 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-993) said: 

对不起，不知道您的联系方式只有发送到这些文章的回复中了，期望您能够看得到。老师，求求您了，您多一点耐心把这里的看完吧，我真的不知道该怎么办。我的情况是这样的
，现在刚满17岁，因为之前读初中的时候一些其他因素没有上普通高中，而是去了一所职业高中，但是在高二的时候跑到了一个培训班去，培训的同时是在接受成人教育，毕业
有个成教专科毕业证。现在上到CSDN的一些论坛上发现文凭的重要性质，如果是专科文凭的话工作不仅不好找，而且没有系统的学习过计算机知识（数学也不好）也不会有太
大的发展潜力。  
现在有两条路可以走，一重新回去读普通高中，因为才17岁。  
二 继续读成教，在以后工作中花费更多的努力去参加自考（也不确信能够坚持下来。），来弥补自己的文凭上的欠缺，可以系统学习与计算机相关的知识为今后的发展打下更好
的基础。  
大概就是这样了，请老师指点一下吧，或者您有更好的办法。我真的感到无所适从，没有办法了才来打搅老师您的。  
因为不知道如何得知老师您的回复，可不可以将回复发送到wangyuTAT@163.com。感谢老师。

  21. [ C瓜哥 ](http://www.cguage.com) on [ December 7, 2010 at 12:10 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-11043) said: 

哈哈，我要把第5条修改成：“Headphones on, Code out”

  22. [ abercrombie and fitch uk ](http://www.abercrombiefitchhotsale.com) on [ December 8, 2010 at 4:12 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-11100) said: 

编程好难吖。。学不会。

  23. [ deepdiscuz ](http://deepdiscuz.com) on [ December 18, 2010 at 11:16 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-11231) said: 

very nice!

  24. [ deepdiscuz ](http://deepdiscuz.com) on [ December 18, 2010 at 11:19 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-11232) said: 

似乎好久没更新了,期待新文章

  25. Pingback: [ 代码质量系列之五：利用CodePro Analytic工具检测和删除重复代码——Don’t Repeat Yourself | 渔夫的网络日志 ](http://www.hackfisher.info/blog/?p=61)

  26. Pingback: [ a new beginning | Dream illuminates Reality ](http://letdreamfly.wordpress.com/2011/01/30/a-new-beginning/)

  27. Azuki  on [ February 1, 2011 at 11:39 am  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-12000) said: 

哈哈, 我就是咖啡进, 代码出. 我一个朋友是啤酒进, 文档出, 详细设计之前先灌瓶啤酒再说

  28. Cooker  on [ March 24, 2011 at 7:41 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-13203) said: 

有时候我真的很希望自己就是那个精神病，这样我就不用负法律责任去砍死那个写出如此混蛋代码的混蛋

  29. Pingback: [ 编程的首要原则是什么？ | Farewell ](http://aivboh.wordpress.com/2011/03/31/%e7%bc%96%e7%a8%8b%e7%9a%84%e9%a6%96%e8%a6%81%e5%8e%9f%e5%88%99%e6%98%af%e4%bb%80%e4%b9%88%ef%bc%9f/)

  30. [ coach bags outlet ](http://www.coachhandbagsoutletonline.com) on [ April 13, 2011 at 3:25 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-13801) said: 

来看看，楼主，支持了。。。

  31. zpp  on [ May 31, 2011 at 5:52 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-14280) said: 

你的灯亮着吗？

  32. Michael  on [ June 15, 2011 at 12:20 am  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-14457) said: 

注册stackoverflow.com时，在设置密码时，抛出一句”Must contain at least 7 more unique
characters”，无法注册。我尝试了’Mi@23com‘这样的密码都不行，请问你是怎么做到的？

  33. [ clarkok ](http://www.clarkok.com/) on [ July 30, 2011 at 1:33 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-15396) said: 

在中国，应该是＂酒进，码出＂吧

  34. daniel  on [ August 8, 2011 at 12:20 am  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-15726) said: 

您好，您这个Wordpress的主题(ARRAR Theme)很漂亮，请问是免费使用的吗？  
我再wordpress的主题里搜索，怎么没有找到呢？  
多谢！

  35. Pingback: [ 罗青-技术博客 | 编程的首要原则(s)是什么？ ](http://tsingroo.sinaapp.com/?p=91)

  36. Pingback: [ 罗青-技术博客 | 编程的首要原则(s)是什么？ ](http://tsingroo.sinaapp.com/?p=12)

  37. JJLiu天姿  on [ October 27, 2011 at 9:44 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-17499) said: 

越懒越好。  
过早优化是一切罪恶的根源。

这两条我没明白。是因为过早陷入细节，当迭代开发或重构时，那些过早的优化都将变成一坨吗？

  38. Martin  on [ November 23, 2011 at 3:31 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-18200) said: 

应该是酒进，钱出，代码只是手段，不是目的：）

  39. [ Business Directory ](http://www.gbizdir.com/) on [ December 7, 2011 at 11:46 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-18508) said: 

哈哈哈。Coffee in, Code out. 牛人就是这样的。

  40. Pingback: [ brainwave entrainment ](http://www.neuralsync.org/faq/)

  41. Pingback: [ Learn more about Lucas ](http://www.eltrimarket.com/bakeriosos/snack-cakes-es-page-full_list.html?sort_by=price&sort_order=desc)

  42. Pingback: [ website design ](http://apocalypticwebdesign.com/websitedesign/websiteredesign.html)

  43. Pingback: [ sim ](http://zlapdoladowanie.pl)

  44. Pingback: [ C++11（及现代C++风格）和快速迭代式开发 | 吃杂烩 ](http://blog.chiapp.com/html/2012-08-27/16598.html)

  45. [ icrt_ ](http://weibo.com/2177249280) on [ October 6, 2012 at 3:36 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-31914) said: 

不错的博文，真心喜欢这系列博文。

  46. [ 静水流深78 ](http://weibo.com/yjwei78) on [ November 24, 2012 at 8:50 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-32045) said: 

Coffee in, Code out. 看来公司里放台免费的咖啡机是必要的。

  47. [ CodeCore ](http://weibo.com/monkerman) on [ October 24, 2013 at 10:30 am  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-32850) said: 

好像在<Unix 编程艺术> 里见过几条. 不过, 这里有趣精彩多了.  
Coffee in, Code out.

  48. pikaia  on [ November 11, 2013 at 2:07 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-32886) said: 

编程的本质是什么？让机器为人做事  
编程的首要原则？让机器正确有效地做事

  49. [ 2012创业家 ](http://weibo.com/3230498441) on [ January 21, 2014 at 4:00 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-33038) said: 

写代码时时刻设想你就是将来要来维护这坨代码的人,说的好

  50. 琳小呆。  on [ February 2, 2014 at 8:47 pm  ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/comment-page-1/#comment-33074) said: 

怎么样才能学进去编程啊，作为计算机系的学生我对编程很捉急啊老师

  * #####  关于 

如果你对我的文章感兴趣，那么 ** 很可能你也对我平时的阅读感兴趣 ** ，以下是一些你可以参考或订阅的资源：

    1. [ 我在豆瓣 ](http://www.douban.com/people/pongba/) 上的豆列列举了一些看过的好书： [ [只读经典]思维改变生活 ](http://www.douban.com/doulist/46003/) | [ [只读经典]思考的技术与艺术 ](http://www.douban.com/doulist/127649/) | [ 决策与判断 ](http://www.douban.com/doulist/197706/) | [ 机器学习与人工智能书籍资源导引 ](http://www.douban.com/doulist/176513/)
我翻译的书：

    1. [ 《Imperfect C++ 中文版》 ](http://book.douban.com/subject/1470838/)
    2. [ 《Exceptional C++ Style 中文版》 ](http://book.douban.com/subject/1470842/)
    3. [ 《修改代码的艺术》 ](http://book.douban.com/subject/2248759/)
我写的书：

    1. [ ![](http://img3.douban.com/mpic/s6586365.jpg) ](http://book.douban.com/subject/6709809/)

  * #####  被阅读得最多的 

    * [ 怎样花两年时间去面试一个人 ](http://mindhacks.cn/2011/11/04/how-to-interview-a-person-for-two-years/) \- 282,579 views 
    * [ 数学之美番外篇：平凡而又神奇的贝叶斯方法 ](http://mindhacks.cn/2008/09/21/the-magical-bayesian-method/) \- 272,693 views 
    * [ [BetterExplained]为什么你应该（从现在开始就）写博客 ](http://mindhacks.cn/2009/02/15/why-you-should-start-blogging-now/) \- 244,807 views 
    * [ 暗时间 ](http://mindhacks.cn/2009/12/20/dark-time/) \- 225,722 views 
    * [ 逃出你的肖申克（二）：仁者见仁智者见智？从视觉错觉到偏见 ](http://mindhacks.cn/2009/03/15/preconception-explained/) \- 212,330 views 
    * [ 我在南大的七年 ](http://mindhacks.cn/2009/05/17/seven-years-in-nju/) \- 206,471 views 
    * [ [BetterExplained]如何有效地记忆与学习 ](http://mindhacks.cn/2009/03/28/effective-learning-and-memorization/) \- 202,213 views 
    * [ 逃出你的肖申克（一）：为什么一定要亲身经历了之后才能明白？ ](http://mindhacks.cn/2009/01/18/escape-from-your-shawshank-part1/) \- 172,290 views 
    * [ 逃出你的肖申克（三）：遇见20万年前的自己 ](http://mindhacks.cn/2010/03/18/escape-from-your-shawshank-part3/) \- 148,821 views 
    * [ [BetterExplained]书写是为了更好的思考 ](http://mindhacks.cn/2009/02/09/writing-is-better-thinking/) \- 137,125 views 
  * #####  我的微博 

  * #####  你可能也会喜欢以下文章 

    * [ C++11（及现代C++风格）和快速迭代式开发 ](http://mindhacks.cn/2012/08/27/modern-cpp-practices/) (138) 
    * [ 方法论、方法论——程序员的阿喀琉斯之踵 ](http://mindhacks.cn/2008/10/29/methodology-for-programmers/) (32) 
    * [ Failing To See the Big Picture – Mistakes we make when learning programming ](http://mindhacks.cn/2008/03/03/failing-to-see-the-big-picture/) (3) 

  *   * [ ** About Arras WordPress Theme ** ](http://www.arrastheme.com/)

Copyright 刘未鹏 | Mind Hacks. All Rights Reserved. [ 苏ICP备09004067号
](http://www.miibeian.gov.cn/) . Powered by [ Wordpress
](http://wordpress.org/) . Using [ Arras Theme ](http://www.arrastheme.com/) .

  *[
         March 9, 2009
        ]: 2009-03-09T15:12:00+00:00

