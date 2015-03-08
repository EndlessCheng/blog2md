#  修改hosts使用谷歌服务 

[ Find ](http://www.findspace.name/author/find) |  2014年6月22日  |  [ 推荐阅读 ](http://www.findspace.name/category/recommend) , [ 网络文摘 ](http://www.findspace.name/category/res/fromweb) , [ 资源 ](http://www.findspace.name/category/res) |  [ 101条评论  ](http://www.findspace.name/res/72#comments)

##  修改hosts方法的好处 

比用代理更加简单方便，而且不用开别的软件。 

习惯用vpn的可以看下 这个脚本（Win平台） ，这篇文章里的应该有Google的推荐的VPN广告。 

> hosts说明：来自百度百科 
> 
> 让我们来看看Hosts在Windows中是怎么工作的。 
> 
> 我们知道在网络上访问网站，要首先通过DNS服务器把要访问的网络域名解析成XXX.XXX.XXX.XXX的IP地址后，计算机才能对这个网络域名作访问。 
> 
> 要是对于每个域名请求我们都要等待域名服务器解析后返回IP信息，这样访问网络的效率就会降低，因为DNS做域名解析和返回IP都需要时间。 
> 
> 为了提高对经常访问的网络域名的解析效率，可以通过利用Hosts文件中建立域名和IP的映射关系来达到目的。根据Windows系统规定，在进行DNS请求以前，Windows系统会先检查自己的Hosts文件中是否有这个网络域名映射关系。如果有，则调用这个IP地址映射，如果没有，再向已知的DNS服务器提出域名解析。也就是说Hosts的请求级别比DNS高。 

##  修改方法： 

如果之前你有自定义的hosts条目，可以在原hosts文件后面粘贴，如果没有，直接覆盖即可 

> win用户覆盖 C:\windows\system32\drivers\etc 下面的hosts 
> 
> MAC&&linux用户覆盖 /etc/hosts 

##  Hosts 

###  [ http://www.findspace.name/adds/hosts ](http://www.findspace.name/adds/hosts)

打开这个链接，然后复制内容保存成hosts文件并覆盖 

（Ctrl+A全选，Ctrl+C复制，Ctrl+V粘贴） 

###  安卓端 

安卓用户可以用我写的app： ** [ CoolHosts ](http://www.findspace.name/easycoding/503) **

##  PS: 

如果linux出现了不能解析主机XXX的问题，比如不能解析Find-Ubuntu，那么在hosts中手动加上 

127.0.0.1 Find-Ubuntu 

如果不行的话，记得看下下面的回复。刷新dns，清除浏览器缓存。 

请不要翻墙发表不当言论，这里提供的主要是学术功能 

[ 动手能力强的可以参看这篇文章在自己的vps上搭建自己的shadowsocks ](http://www.findspace.name/res/956)

##  最后 

如果这篇文章对你管用，<请对本站关闭广告屏蔽功能，戳几个支持下>，你的支持，是我维护更新的最大动力！ 

* * *

2015.1.28 

某墙越来越厉害了，修改hosts的方法越来越不靠谱，如果有能力，请参考上面那个连接，自己搭建shadowsocks或者买vpn。 

Tags:  [ google ](http://www.findspace.name/tag/google) , [ hosts ](http://www.findspace.name/tag/hosts) , [ win8.1 ](http://www.findspace.name/tag/win8-1) , [ 网络资源 ](http://www.findspace.name/tag/websource)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/res/72](http://www.findspace.name/res/72)