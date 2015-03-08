#  Git的优缺点

[ Yuguo ](http://yuguo.us) 2012年 08月 01日

前几天写了一篇 [ git基础 ](http://yuguo.us/weblog/git-base/)
，总结起来就是git是一种分布式版本管理工具，优点如下：

  * 比svn更快速的分支切换，因为分支都在本地。这使得git特别适合处理临时需求，或者小实验。 
  * 可以在星巴克写代码的时候随时提交，因为各版本快照（commit）都在本地 
  * 有一个全世界最大的开源社区——github，上面可以看到各种优秀的各语言代码，去官网语言列表看看才知道有那么多语言，就跟奥运会开幕式才知道世界上有那么多国家一样 

缺点：

  * 因为是分布式的，每台机器上都commit的时候，有的时候忘记了push到远程服务器（github），那就不同步了。不过常常status一下看看状态，问题不大 

不知道是优点还是缺点的：

  * 要使用命令行（我在windows下装的git bash），其实用gui也是可以的，但基本上还是命令行更灵活，而且有一本专业开源教程 [ 《Pro Git（中文）》 ](http://git-scm.com/2010/06/09/pro-git-zh.html) ，而且如果遇到问题可以在stackoverflow上去搜解决方案，答案都是命令行 

本来准备写一下常用命令，但是又觉得Pro Git已经又透彻又详细了，就没有必要重复劳动了。学好git只用读这一本书。

[ 使用git部署站点 → ](/weblog/push-git-repository-to-server/) [ ← CSS3字体的MIME TYPE
](/weblog/css3-font-mime-type/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

