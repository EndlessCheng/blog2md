#  SVN添加新增加的文件 

[ Find ](http://www.findspace.name/author/find) |  2015年1月28日  |  [ Linux ](http://www.findspace.name/category/easycoding/linux) , [ 小工具 ](http://www.findspace.name/category/easycoding/tools) , [ 随意Coding ](http://www.findspace.name/category/easycoding) |  [ 没有评论  ](http://www.findspace.name/easycoding/1062#comments)

我经常会一次往Subversion里添加一批文件。在使用命令行做这件事时，你必须指定所有想要添加的文件名。   
如果文件不多的话这还不算太糟糕，但如果你要添加20个文件，那就费事了。当然你也可以用通配符，但这样一来就可能匹配到已经在版本控制之下的文件(这不会有什么损害，只不过会输出一堆错误信息，可能会跟别的错误信息混淆)。为了解决这个问题，我写了一行简单的bash命令： 
    
    
    svn st | grep '^\?' | tr '^\?' ' ' | sed 's/[ ]*//' | sed 's/[ ]/\\ /g' | xargs svn add

我大概花了15分钟写出这条命令，然后用了它成百上千次。 

* * *

这个自动化过程已经很完美了，一个“简单”的shell脚本，这是一个权威编写并使用了百上千次的脚本。 

然后我在一个博客中看到这样一个脚本： 
    
    
    svn st|awk '{print $2}'|xargs svn add。

乍看之下觉得更加精炼，仔细看下就会发现这个脚本没有区分文件状态。所以完善了以下这个脚本： 
    
    
    svn st | awk '{if ( $1 == "?") { print $2}}' | xargs svn add  

这样，以后我可能使用这个脚本成百上千次。(当然这个脚本也没有考虑过滤掉不要添加的文件） 

当你第三次做一件事情的时候，就应该考虑将其工具化，自动化！ 

* * *

本文系 [ 转载自CSDN ](http://blog.csdn.net/spare_h/article/details/6677435)

Tags:  [ Linux ](http://www.findspace.name/tag/linux)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/easycoding/1062](http://www.findspace.name/easycoding/1062)