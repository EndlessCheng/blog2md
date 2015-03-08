[ WDK.PW-DK博客 ](http://www.wdk.pw)

当代中国大学生的独立博客

  * [ 首页 ](http://www.wdk.pw)
  * [ 互联网 ](http://www.wdk.pw/category/uncategorized)
  * [ 随笔 ](http://www.wdk.pw/category/other)
  * [ 文字 ](http://www.wdk.pw/category/words)
  * [ 关于我 ](http://www.wdk.pw/sample-page)
  * [ 我的历程 ](http://www.wdk.pw/%e6%88%91%e7%9a%84%e5%8e%86%e7%a8%8b)
  * [ RSS订阅 ](http://www.wdk.pw/rss)
  * [ 我的简历 ](http://www.wdk.pw/me/#/resume)
  * [ 雇佣 ](https://jinshuju.net/f/3NPhAJ)

#  我为什么做了地震短信服务专页

2,556 views

  * 四月 24, 2013 
  * [ 3 条评论 ](http://www.wdk.pw/26.html#comments)

> 北京时间2013年4月20日8时02分四川省雅安市芦山县（北纬30.3,东经103.0）发生7.0级地震。震源深度13公里。震中距成都约100公里。成都
、重庆及陕西的宝鸡、汉中、安康等地均有较强震感。据雅安市政府应急办通报，震中芦山县龙门乡99%以上房屋垮塌，卫生院、住院部停止工作，停水停电。

那时我正在用电脑，突然发现桌子摇晃的厉害，我立即意识到地震来了，庆幸的是我的反应是逃生而非恐惧。我大叫，把一群室友叫起来，然后把门打开，飞奔了出去，到门外，
眼前已站了一群裸男，像晒咸鱼一般的密密麻麻。过了不久，大家又陆陆续续的回到了宿舍，事情总是这样，无论当时的事情多么危险紧急，但总要归于平静的。比如一开始所有
网站的灰色，比如百度的logo，这都是暂时的，你知道这暂时无可厚非，也只能如此，但是某天它突然换回来的时候，你还是会感到一阵触动。而死去的人们再也不会回来。  
  
中午我去吃了一顿饭，是个基友，这个是真的基友，基督教的朋友，过生日。吃完饭后我回到寝室，突然觉得应该做点什么，室友都在打游戏或者写作业，我楞在电脑前面。这时
候我想起来波士顿爆炸案之后美国互联网的反应，我有了一个主意。

我想到的是GooglePersonFinder和一个叫Twilio的东西

![](http://a.36krcnd.com/photo/41b7dfdee818787f5a189e9544c17d07.jpg)

> 没有信号，大灾之后很多人都没法同家人联系。 [ Twilio ](http://www.twilio.com/) 随后上线了一个页面，叫做 [
CallYourFamily ](http://callyourfamily.twilio.ly/)
，如果你人在波士顿又没有手机信号，可以通过这个网站给你的亲人打电话。不用注册，接打双方都免费，Twillio
称这项服务将会持续到波士顿的手机网络恢复正常。源代码已公布到 GitHub，遵从 MIT 许可协议。

我知道这就是我想做的，我首先做了一个寻人的页面，采用类似于留言本的PHP+MYSQL，实现了简单的记录和查询，然后我又开始做电话，可是我发现无论从技术还是资
源上我都难以实现Twilio的功能，于是我只能退而求其次，制作了短信的服务。正如你所看到的

![](http://a.36krcnd.com/photo/9e2eaf4a7090d945c37b1185c75802fd.png)

![](http://a.36krcnd.com/photo/6758eeb2b9d683e672de94a0ad7b4530.png)

如果叫我自己来评价我做的这个网站的话，我只能用简陋两个字来评价。我没有做任何的美化，优化，很多代码也极不规范，但是做的很快，下午就做出来了。

一开始的时候这的确是个Finder+Sender的网站，但Finder这个功能的前提是大量的用户，我没有用户基础，后来我又发现谷歌百度360也陆续推出了自己
的寻人平台，所以我干脆把自己的寻人功能删除了，只留下了短信发送的功能。也就是现在你看到的样子。同时也更名为 ** 四川地震短信服务.专页 **

感谢36kr的报道，让我的网站被更多的人知道，这意味着它更可能真正的帮到灾区的人们，这也是我最大的心愿了。

源码很简单，简单到我都很不好意思公布了。如果你有兴趣可以直接问我，当然，任何一个学过一点点html和php的都会鄙视我的简陋的。不过我还是很高兴它能提供一些
帮助。

雅安加油。

爱里没有惧怕——《圣经》

分享到：  [ ](http://www.jiathis.com/share?uid=1769785)

  1. Pingback: [ 这次灾难给我的感触 | 王登科的博客 ](http://test.wdk.pw/30.html)

  2. 牙刷  on [ 2013 年 4 月 24 日 at 下午 12:50  ](http://www.wdk.pw/26.html#comment-24) said: 

佩服

[ [ 回复 ](javascript:void\(0\)) ]

  3. 斌  on [ 2013 年 4 月 24 日 at 下午 5:02  ](http://www.wdk.pw/26.html#comment-19) said: 

兄弟你很棒。做得东西能帮到很多人。我也想做这些，只是技术太烂了哈！向你学习

[ [ 回复 ](javascript:void\(0\)) ]

搜索

###  我的微信公众号

![](http://susefood.u.qiniudn.com/dkw.jpg) 微信号：greatdk

###  支付宝扫描赞助，支持博主

![](http://susefood.u.qiniudn.com/zanzhu.png) 为有价值的文章付费是对博主的最大鼓励

###  近期文章

  * [ 微博情绪分析器开发过程 ](http://www.wdk.pw/909.html)
  * [ 朝三暮四的环境问题 ](http://www.wdk.pw/905.html)
  * [ 不折腾的四步备案攻略 ](http://www.wdk.pw/884.html)
  * [ 网赚，微商，以及更多 ](http://www.wdk.pw/885.html)
  * [ 冰天雪地奇妙夜 ](http://www.wdk.pw/895.html)

###  热评文章

###  分类目录

  * [ 互联网 ](http://www.wdk.pw/category/uncategorized)
  * [ 文字 ](http://www.wdk.pw/category/words)
  * [ 随笔 ](http://www.wdk.pw/category/other)
  * [ 音乐 ](http://www.wdk.pw/category/music)

###  文章归档

  * [ 2015年三月 ](http://www.wdk.pw/date/2015/03)
  * [ 2015年二月 ](http://www.wdk.pw/date/2015/02)
  * [ 2015年一月 ](http://www.wdk.pw/date/2015/01)
  * [ 2014年十二月 ](http://www.wdk.pw/date/2014/12)
  * [ 2014年十一月 ](http://www.wdk.pw/date/2014/11)
  * [ 2014年十月 ](http://www.wdk.pw/date/2014/10)
  * [ 2014年九月 ](http://www.wdk.pw/date/2014/09)
  * [ 2014年八月 ](http://www.wdk.pw/date/2014/08)
  * [ 2014年七月 ](http://www.wdk.pw/date/2014/07)
  * [ 2014年六月 ](http://www.wdk.pw/date/2014/06)
  * [ 2014年五月 ](http://www.wdk.pw/date/2014/05)
  * [ 2014年四月 ](http://www.wdk.pw/date/2014/04)
  * [ 2014年三月 ](http://www.wdk.pw/date/2014/03)
  * [ 2014年二月 ](http://www.wdk.pw/date/2014/02)
  * [ 2014年一月 ](http://www.wdk.pw/date/2014/01)
  * [ 2013年十二月 ](http://www.wdk.pw/date/2013/12)
  * [ 2013年十一月 ](http://www.wdk.pw/date/2013/11)
  * [ 2013年十月 ](http://www.wdk.pw/date/2013/10)
  * [ 2013年九月 ](http://www.wdk.pw/date/2013/09)
  * [ 2013年六月 ](http://www.wdk.pw/date/2013/06)
  * [ 2013年五月 ](http://www.wdk.pw/date/2013/05)
  * [ 2013年四月 ](http://www.wdk.pw/date/2013/04)

###  友情链接

[ 酷燃网 ](http://www.coolirand.com)

[ 左岸读书 ](http://www.zreading.cn)

[ 彩云之南 ](http://wendy.imsuse.de)

[ 华生的博客 ](http://www.johnwatsonblog.co.uk)

[ 福尔摩斯的博客 ](http://www.thescienceofdeduction.co.uk)

[ 叶科忠的博客 ](http://www.yekezhong.com)

[ 听风扯淡 ](http://www.windsays.com/)

[ 不给力的面条 ](http://miantiao.me)

[ 代码家 ](http://blog.daimajia.com/)

[ 博客大全 ](http://lusongsong.com/daohang)

[ Finle. ](http://finle.me/)

© 2015. | [ DK博客总访问量：1,288,966 次 ](http://www.wdk.pw/) | [ 酷燃网
](http://www.coolirand.com) | 主题作者: [ cho ](http://pagecho.com) | 本博客托管在 [
云左主机 ](http://www.cloudleft.com/aff.php?aff=086)

