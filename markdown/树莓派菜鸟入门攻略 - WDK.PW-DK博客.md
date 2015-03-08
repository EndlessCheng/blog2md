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

#  树莓派菜鸟入门攻略

10,143 views

  * 一月 9, 2015 
  * [ 21 条评论 ](http://www.wdk.pw/845.html#comments)

首先来看看树莓派是什么：

> ** 树莓派 ** （  [ 英语 ](http://zh.wikipedia.org/wiki/%E8%8B%B1%E8%AF%AD) ：  **
Raspberry Pi ** ），是一款基于 [ Linux ](http://zh.wikipedia.org/wiki/Linux) 系统的只有一张
[ 信用卡 ](http://zh.wikipedia.org/wiki/%E4%BF%A1%E7%94%A8%E5%8D%A1) 大小的 [ 单板机
](http://zh.wikipedia.org/wiki/%E5%8D%95%E6%9D%BF%E6%9C%BA) 电脑。它由 [ 英国
](http://zh.wikipedia.org/wiki/%E8%8B%B1%E5%9C%8B) 的树莓派基金会所开发，目的是以低价 [ 硬件
](http://zh.wikipedia.org/wiki/%E7%A1%AC%E4%BB%B6) 及 [ 自由软件
](http://zh.wikipedia.org/wiki/%E8%87%AA%E7%94%B1%E8%BB%9F%E9%AB%94) 刺激在学校的基本的
[ 电脑科学 ](http://zh.wikipedia.org/wiki/%E7%94%B5%E8%84%91%E7%A7%91%E5%AD%A6)
教育。

>

> ![](http://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/RaspberryPi.jpg
/1024px-RaspberryPi.jpg)

这学期即将结束的时候，我因为机缘巧合，拿到了一块树莓派。

我的这块树莓派型号是B+，拥有512M的RAM和四个USB接口，理论上，把它接入电源，再连上网络，就可以作为一个独立的主机来工作了，而由于其GPIO的接口，
还可以和物理世界发生联系，所以拥有极大的想象空间。它可以用来做服务器，智能家居控制中心，机器人，无人机，甚至遥控坦克，它几乎可以做任何好玩的东西。

当然，想象很丰满，现实很凌乱。面对着一块赤裸的电路板，我能做点什么呢？

我首先做的就是上网搜索，忧伤的是，看上去资料最全的网站是个非常封闭的论坛，充斥着各种VIP邀请码，很多内容不注册不充值VIP还无法看，我认为这不仅违背了互联
网的精神，还违背了树莓派的精神，所以我决定做点违背安全的事情，我用一个并发软件穷举了这个论坛的100个账号，尝试用二十种弱口令登录，然后很顺利的发现一个弱口
令账户，用这个账户登录上去，看到了隐藏的教材，但我遗憾的发现，这些所谓的内部资源，依旧不能解决我的问题，没有一个帖子接地气的告诉你，怎么从一块板子开始，连接
和进入它的里面。

于是我转而开始寻找外文资料，经过几个小时的摸索，终于成功的进入了树莓派，当然，我还没涉及到任何物理世界的联系，离玩转树莓派还很遥远，不过万事开头难，走好第一
步总是值得高兴的。但我想，如果有简明完善的入门教程，我会更快体验到树莓派的乐趣，所以我决定趁热打铁，写一个适用于完全从0开始的小菜鸟的教程，希望能让你进步到
我这样的大菜鸟。

##  认识树莓派

我们可以在网上找树莓派的资料来看，但要拿在手上才会有感性的认识

![](http://susefood.u.qiniudn.com/rssmp.jpg)

如图所示，树莓派的能连接的地方大致有这么几种：USB，网卡，HDMI，电源，gpio，SD卡插槽。作为初学菜鸟，我们暂时用不到gpio。我们只需要接入电源/
SD卡/网络 就行了。电源没什么多说的，接上插头就行了，剩下的两个东西就稍微麻烦一些了。SD卡作为储存器，我们要把操作系统写入到这里面。

##  写入系统

你需要一张至少8个G的SD卡，注意这里有一个小坑，树莓派需要的不是大的SD卡，而是小一些的SD卡，并且， ** 不是所有SD卡都能正常工作 **
，这里有一份树莓派  [ 可工作和不可工作的SD卡清单 ](http://mall.egoman.com.cn/index.php?option=com_c
ontent&view=article&id=121:sd&catid=47:shiyongfangan-&Itemid=222) ，请自行查阅。

接下来，将SD卡用读卡器连入电脑，在电脑上将操作系统写入树莓派。由于我只试过Windows下的写入，所以如果你是Mac用户，只有在网上找找相关的流程了。Wi
ndows下，先下载树莓派的操作系统（debain）到本地并解压： [ http://pan.baidu.com/s/1o2oz0
](http://pan.baidu.com/s/1o2oz0 ) ，然后下载一个叫做win32diskimager的工具： [
http://www.onlinedown.net/soft/110173.htm
](http://www.onlinedown.net/soft/110173.htm) 。

第二步，打开win32diskimager，在软件中选择操作系统debain解压出的的img文件，“Device”下选择SD卡的盘符，然后选择“Write”

![](http://susefood.u.qiniudn.com/smp0.jpg)

中途可能会弹出一个框，选但别管他，选“Yes”，继续安装。

然后就开始安装系统了，根据你的SD速度，安装过程有快有慢。
安装结束后会弹出完成对话框，说明安装就完成了，如果不成功，请关于防火墙一类的软件，重新插入SD进行安装.

值得一提的是，安装完成后会发现SD卡只有几十M了，这不是卖SD卡的商家坑你，而是因为linux下的分区win下是看不到的，正常现象。如果用分区软件查看SD卡
，是能看到它的真实大小的。

接下来把SD卡从电脑拔出，插到树莓派里面，至此，我们完成了系统的安装，接下来，是网络了。

##

##  远程连接

有两种种方式可供树莓派连入网络

1.无线网卡

2.直接接网线

事实上，由于我没有视频设备，所以只能通过远程来控制树莓派，而这又必须要求先连入网络，问题在于，如果不设置无线网络，即使用无线网卡也是连不到网络的，所以我只有
采用网线直连的方法。

我将路由器的一条网线接到树莓派上面，路由器已经做好了设置，这意味着插入网线就可以获得一个内网IP，并且可以上网。不过问题又来了，我们怎么知道树莓派的IP呢？
如果不知道IP就无法远程连接树莓派，也就无法做任何操作。

很简单，其实在路由器的管理页面就看得到。

![](http://susefood.u.qiniudn.com/smp3.jpg)

如图，有一个名叫raspberrpi的主机，它就是树莓派，而它的IP地址是192.168.0.103，这下问题就变得轻松了许多。

我们下载远程连接工具Putty，填入树莓派的IP地址

![](http://susefood.u.qiniudn.com/smp4.jpg)

点击Open，来到登录界面

![](http://susefood.u.qiniudn.com/smp5.jpg)

输入树莓派的默认账号和密码：

账号：pi

密码：raspberry

点击回车，就看到了我们熟悉的Linux界面

![](http://susefood.u.qiniudn.com/smp6.jpg)

其实这个时候，我们已经在这块小电路板里面了！当我第一次进入树莓派的时候，简直比第一次进入生命的大和谐还要兴奋。

看着树莓派的红黄小灯灵动的闪烁，我觉得它能满足我关于这个世界的种种奇妙设想，当然，前路是坎坷的。

我给树莓派安装了远程图像连接程序，然后发现上面还有不少游戏，但它的作用远不止这点，它是物联网，它是连接，它也可以是分布式控制或去中心化主机，但最重要的是，它
激发起人们对于神奇世界的探索欲望。其实它被开发的目的就是教育孩子，从这一点上，我觉得它的意义不比苹果手机或任何优秀产品逊色。

或许，树莓派的意义就是那句计算机史上前所未有的名言警句：

“Hello，World”

分享到：  [ ](http://www.jiathis.com/share?uid=1769785)

  1. [ 曾先生 ](http://izzzzz.com/) on [ 2015 年 1 月 9 日 at 上午 11:00  ](http://www.wdk.pw/845.html#comment-1426) said: 

这第一步虽然走得有点艰难，还是辛苦作者了。

[ [ 回复 ](javascript:void\(0\)) ]

![](http://1.gravatar.com/avatar/3dc451b39d4483019792ec03c79ca17b?s=32&d=ident
icon&r=G)

[ 消灭星星 ](http://huanglv.me/p) 回复:  
一月 16th, 2015 at 下午 8:00

消灭星星 [ http://huanglv.me/p ](http://huanglv.me/p)

[ [ 回复 ](javascript:void\(0\)) ]

  2. 贾东和  on [ 2015 年 1 月 9 日 at 下午 5:17  ](http://www.wdk.pw/845.html#comment-1431) said: 

它可以代替播放器不？直接连接到显示板上

[ [ 回复 ](javascript:void\(0\)) ]

![](http://0.gravatar.com/avatar/ee2fe09d578ddb9222bc994ee8af445d?s=32&d=ident
icon&r=G)

[ DK ](http://www.wdk.pw/) 回复:  
一月 9th, 2015 at 下午 5:23

必然可以啊

[ [ 回复 ](javascript:void\(0\)) ]

  3. [ 拟月幻真 ](http://www.u509.com/) on [ 2015 年 1 月 9 日 at 下午 8:13  ](http://www.wdk.pw/845.html#comment-1433) said: 

很MINI啊，装上盒子就可以了，功耗很小，不过这LINUX带的功能足够吗？

[ [ 回复 ](javascript:void\(0\)) ]

![](http://0.gravatar.com/avatar/ee2fe09d578ddb9222bc994ee8af445d?s=32&d=ident
icon&r=G)

[ DK ](http://www.wdk.pw/) 回复:  
一月 9th, 2015 at 下午 9:08

看你做什么了，做个自己用的小服务器，翻墙路由器，或者控制中心什么的还是没问题的。当然不要处理太大量的计算。

[ [ 回复 ](javascript:void\(0\)) ]

  4. [ 秃萝卜 ](http://weibo.com/2159803014) on [ 2015 年 1 月 9 日 at 下午 10:18  ](http://www.wdk.pw/845.html#comment-1435) said: 

我有一块cubieboard这样的板子，A8的，以前也玩了一阵，做个服务器不错！地址：http://item.taobao.com/item.htm?spm
=a1z09.2.9.166.NDylfW&id=22098304838&_u=9i411mkc242 说不定他的社区有资料可以帮你！

[ [ 回复 ](javascript:void\(0\)) ]

  5. 袅残烟  on [ 2015 年 1 月 10 日 at 下午 8:58  ](http://www.wdk.pw/845.html#comment-1456) said: 

这个。。。我推荐Arch

[ [ 回复 ](javascript:void\(0\)) ]

  6. [ 半只西瓜 ](http://www.imjiayin.com) on [ 2015 年 1 月 11 日 at 下午 7:42  ](http://www.wdk.pw/845.html#comment-1463) said: 

看到树莓派，以为是树莓做的派。。。。好吧，我太肤浅了。哈哈。

[ [ 回复 ](javascript:void\(0\)) ]

![](http://0.gravatar.com/avatar/ee2fe09d578ddb9222bc994ee8af445d?s=32&d=ident
icon&r=G)

[ DK ](http://www.wdk.pw/) 回复:  
一月 14th, 2015 at 下午 12:58

我刚开始上网搜树莓派的时候也找到一大堆食谱

[ [ 回复 ](javascript:void\(0\)) ]

  7. [ Marketwatch-LZR ](http://weibo.com/1925741435) on [ 2015 年 1 月 14 日 at 下午 12:14  ](http://www.wdk.pw/845.html#comment-1470) said: 

大神，你为这个博客买空间，一年花费多少？

[ [ 回复 ](javascript:void\(0\)) ]

![](http://0.gravatar.com/avatar/ee2fe09d578ddb9222bc994ee8af445d?s=32&d=ident
icon&r=G)

[ DK ](http://www.wdk.pw/) 回复:  
一月 14th, 2015 at 下午 12:57

一百多点

[ [ 回复 ](javascript:void\(0\)) ]

![](http://0.gravatar.com/avatar/?d=identicon&s=32)

[ Marketwatch-LZR ](http://weibo.com/1925741435) 回复:  
一月 16th, 2015 at 上午 10:26

注册域名呢？我对此很感兴趣，有心想要创建博客。

[ [ 回复 ](javascript:void\(0\)) ]

![](http://0.gravatar.com/avatar/ee2fe09d578ddb9222bc994ee8af445d?s=32&d=ident
icon&r=G)

[ DK ](http://www.wdk.pw/) 回复:  
一月 16th, 2015 at 下午 12:22

注册域名一年几十块吧，很便宜

  8. [ 王语双个人网站 ](http://wangyushuang.com/) on [ 2015 年 1 月 14 日 at 下午 12:16  ](http://www.wdk.pw/845.html#comment-1471) said: 

![](http://img.t.sinajs.cn/t35/style/images/common/face/ext/normal/60/horse2_o
rg.gif) 哎，真新奇！技术原来可以这么牛B地展示出来。

[ [ 回复 ](javascript:void\(0\)) ]

  9. [ 偏方大全qianjinpianfang.com ](http://qianjinpianfang.com/) on [ 2015 年 1 月 14 日 at 下午 4:24  ](http://www.wdk.pw/845.html#comment-1474) said: 

学习了，虽然不怎么懂。

[ [ 回复 ](javascript:void\(0\)) ]

  10. [ 厦门微信营销 ](http://www.pinxun.cc/?xiaoye) on [ 2015 年 1 月 16 日 at 上午 11:33  ](http://www.wdk.pw/845.html#comment-1476) said: 

![](http://img.t.sinajs.cn/t35/style/images/common/face/ext/normal/89/hufen_or
g.gif) 支持支持！

[ [ 回复 ](javascript:void\(0\)) ]

  11. [ 商标转让 ](http://bbs.ipmhw.com/) on [ 2015 年 1 月 20 日 at 下午 12:32  ](http://www.wdk.pw/845.html#comment-1532) said: 

谢谢分享

[ [ 回复 ](javascript:void\(0\)) ]

  12. [ 大嘴巴巴 ](http://www.dazui88.com/) on [ 2015 年 2 月 1 日 at 下午 4:30  ](http://www.wdk.pw/845.html#comment-1600) said: 

感谢分享！http://www.dazui88.com

[ [ 回复 ](javascript:void\(0\)) ]

  13. nicktogo  on [ 2015 年 2 月 12 日 at 上午 10:33  ](http://www.wdk.pw/845.html#comment-1659) said: 

好想建个博客，不知道有没有教程？完全不懂这个

[ [ 回复 ](javascript:void\(0\)) ]

  14. [ jefby_plus ](http://weibo.com/2199541491) on [ 2015 年 3 月 8 日 at 下午 6:48  ](http://www.wdk.pw/845.html#comment-1742) said: 

可以去官网看资料啊，还是很齐全的

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

© 2015. | [ DK博客总访问量：1,288,962 次 ](http://www.wdk.pw/) | [ 酷燃网
](http://www.coolirand.com) | 主题作者: [ cho ](http://pagecho.com) | 本博客托管在 [
云左主机 ](http://www.cloudleft.com/aff.php?aff=086)

