##  [ 汪海的实验室 ](http://blog.csdn.net/pleasecallmewhy)

###  一名普通小程序员的学习笔记。 博客地址：http://blog.callmewhy.com

  * [ ![](http://static.blog.csdn.net/images/ico_list.gif) 目录视图  ](http://blog.csdn.net/pleasecallmewhy?viewmode=contents)
  * [ ![](http://static.blog.csdn.net/images/ico_summary.gif) 摘要视图  ](http://blog.csdn.net/pleasecallmewhy?viewmode=list)
  * [ ![](http://static.blog.csdn.net/images/ico_rss.gif) 订阅  ](http://blog.csdn.net/pleasecallmewhy/rss/list)

[ CSDN学院讲师招募，诚邀您加入！  ](http://blog.csdn.net/csdnedu/article/details/43306129)
[ 博客Markdown编辑器上线啦
](http://blog.csdn.net/csdnproduct/article/details/43561659) [
那些年我们追过的Wrox精品红皮计算机图书
](http://blog.csdn.net/blogdevteam/article/details/42918959) [ PMBOK第五版精讲视频教程
](http://edu.csdn.net/lecturer/lecturer_detail?lecturer_id=95) [ 火星人敏捷开发1001问
](http://edu.csdn.net/course/detail/443)

#  [ [Other]面试复习笔记：线程与进程复习 ](/pleasecallmewhy/article/details/28649167)

分类： [ 操作系统 ](/wxg694175346/article/category/1431103) 2014-06-05 17:24  790人阅读
评论  (0)  [ 收藏 ](javascript:void\(0\);) 举报

##  基本概念

#  1\. 进程的基本概念

线程(thread)是进程(processes)中某个单一顺序的控制流，也被称为轻量进程(lightweight processes)。  
进程是表示资源分配的基本单位，又是调度运行的基本单位。 例如：
用户运行自己的程序，系统就创建一个进程，并为它分配资源，包括各种表格、内存空间、磁盘空间、I／O设备等。
然后，把该进程放人进程的就绪队列。进程调度程序选中它，为它分配CPU以及其它有关资源，该进程才真正运行。 所以，进程是系统中的并发执行的单位。

#  2\. 线程的基本概念

在Mac、Windows NT等采用微内核结构的操作系统中，进程的功能发生了变化：它只是资源分配的单位，而不再是调度运行的单位。
在微内核系统中，真正调度运行的基本单位是线程。因此，实现并发功能的单位是线程。 线程是进程中执行运算的最小单位，也就是执行处理机调度的基本单位。
如果把进程理解为在逻辑上操作系统所完成的任务，那么线程表示完成该任务的许多可能的子任务之一。

例如： 假设用户启动了一个窗口中的数据库应用程序，操作系统就将对数据库的调用表示为一个进程。
假设用户要从数据库中产生一份工资单报表，并传到一个文件中，这是一个子任务； 在产生工资单报表的过程中，用户又可以输人数据库查询请求，这又是一个子任务。
这样，操作系统则把每一个请求――工资单报表和新输人的数据查询表示为数据库进程中的独立的线程。
线程可以在处理器上独立调度执行，这样，在多处理器环境下就允许几个线程各自在单独处理器上进行。 操作系统提供线程就是为了方便而有效地实现这种并发性

引入线程的好处 1. 易于调度。 2. 提高并发性。通过线程可方便有效地实现并发性。进程可创建多个线程来执行同一程序的不同部分。 3.
开销少。创建线程比创建进程要快，所需开销很少。。 4.
利于充分发挥多处理器的功能。通过创建多线程进程，每个线程在一个处理器上运行，从而实现应用程序的并发性，使每个处理器都得到充分运行。

#  3\. 线程的基本状态

就绪：调用线程的start方法后线程进入就绪状态  
阻塞：线程调度系统将就绪状态的线程转为运行状态  
运行：遇到synchronized语句时，由运行状态转为阻塞  
结束：当线程关联的代码执行完后，线程变为结束状态

#  4\. 线程与进程的区别

线程与进程的区别可以归纳为以下4点： 1）地址空间：进程间相互独立，同一进程的各线程间共享。某进程内的线程在其它进程不可见。  
2）通信方式：进程间通信IPC，线程间可以直接读写进程数据段（如全局变量）来进行通信。需要进程同步和互斥手段的辅助，以保证数据的一致性。  
3）调度切换：线程上下文切换比进程上下文切换要快得多。  
4）二者均可并发执行，在多线程OS中，进程不是一个可执行的实体。

简而言之，一个程序至少有一个进程，一个进程至少有一个线程。 线程的划分尺度小于进程，使得多线程程序的并发性高。
另外，进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大地提高了程序的运行效率。
线程在执行过程中与进程还是有区别的。每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。
但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。 从逻辑角度来看，多线程的意义在于一个应用程序中，有多个执行部分可以同时执行。
但操作系统并没有将多个线程看做多个独立的应用，来实现进程的调度和管理以及资源分配。这就是进程和线程的重要区别。

进程是具有一定独立功能的程序关于某个数据集合上的一次运行活动，进程是系统进行资源分配和调度的一个独立单位。
线程是进程的一个实体，是CPU调度和分派的基本单位，它是比进程更小的能独立运行的基本单位。
线程自己基本上不拥有系统资源，只拥有一点在运行中必不可少的资源(如程序计数器，一组寄存器和栈)，
但是它可与同属一个进程的其他的线程共享进程所拥有的全部资源。 一个线程可以创建和撤销另一个线程；同一个进程中的多个线程之间可以并发执行。

#  5\. 多线程有几种实现方法

多线程有两种实现方法。一种是继承Thread类，一种是实现Runnable接口。  
同步有两种方法。一种同步方法，一种同步代码。分别是synchronized，wait与notify

#  6\. 多线程同步和互斥异同

线程同步是指线程之间所具有的一种制约关系，一个线程的执行依赖另一个线程的消息，当它没有得到另一个线程的消息时应等待，直到消息到达时才被唤醒。
线程互斥是指对于共享的进程系统资源，在各单个线程访问时的排它性。 当有若干个线程都要使用某一共享资源时，任何时刻最多只允许一个线程去使用，
其它要使用该资源的线程必须等待，直到占用资源者释放该资源。线程互斥可以看成是一种特殊的线程同步。

  * 上一篇  [ [Git]常用Git操作笔记 ](/pleasecallmewhy/article/details/28648949)
  * 下一篇  [ [iOS]Objective-C基础回顾：继承和委托 ](/pleasecallmewhy/article/details/28649393)

顶

     1 

踩

     0 

主题推荐

     [ 面试 ](http://www.csdn.net/tag/面试) [ 线程 ](http://www.csdn.net/tag/线程) [ 操作系统 ](http://www.csdn.net/tag/操作系统) [ 应用程序 ](http://www.csdn.net/tag/应用程序) [ 全局变量 ](http://www.csdn.net/tag/全局变量)

猜你在找

查看评论

* 以上用户言论只代表其个人观点，不代表CSDN网站的观点或立场 

![快速回复](http://static.blog.csdn.net/images/blog-icon-reply.png)
![TOP](http://static.blog.csdn.net/images/top.png)

#####  [ 核心技术类目 ](http://www.csdn.net/tag/)

[ 全部主题 ](http://www.csdn.net/tag) [ Hadoop ](http://g.csdn.net/5272865) [ AWS
](http://g.csdn.net/5272866) [ 移动游戏 ](http://g.csdn.net/5272870) [ Java
](http://g.csdn.net/5272871) [ Android ](http://g.csdn.net/5272872) [ iOS
](http://g.csdn.net/5272873) [ Swift ](http://g.csdn.net/5272868) [ 智能硬件
](http://g.csdn.net/5272869) [ Docker ](http://g.csdn.net/5272867) [ OpenStack
](http://g.csdn.net/5272925) [ VPN ](http://www.csdn.net/tag/vpn) [ Spark
](http://g.csdn.net/5272924) [ ERP ](http://www.csdn.net/tag/erp) [ IE10
](http://www.csdn.net/tag/ie10) [ Eclipse ](http://www.csdn.net/tag/eclipse) [
CRM ](http://www.csdn.net/tag/crm) [ JavaScript
](http://www.csdn.net/tag/javascript) [ 数据库 ](http://www.csdn.net/tag/数据库) [
Ubuntu ](http://www.csdn.net/tag/ubuntu) [ NFC ](http://www.csdn.net/tag/nfc)
[ WAP ](http://www.csdn.net/tag/wap) [ jQuery
](http://www.csdn.net/tag/jquery) [ BI ](http://www.csdn.net/tag/bi) [ HTML5
](http://www.csdn.net/tag/html5) [ Spring ](http://www.csdn.net/tag/spring) [
Apache ](http://www.csdn.net/tag/apache) [ .NET
](http://www.csdn.net/tag/.net) [ API ](http://www.csdn.net/tag/api) [ HTML
](http://www.csdn.net/tag/html) [ SDK ](http://www.csdn.net/tag/sdk) [ IIS
](http://www.csdn.net/tag/iis) [ Fedora ](http://www.csdn.net/tag/fedora) [
XML ](http://www.csdn.net/tag/xml) [ LBS ](http://www.csdn.net/tag/lbs) [
Unity ](http://www.csdn.net/tag/unity) [ Splashtop
](http://www.csdn.net/tag/splashtop) [ UML ](http://www.csdn.net/tag/uml) [
components ](http://www.csdn.net/tag/components) [ Windows Mobile
](http://www.csdn.net/tag/windowsmobile) [ Rails
](http://www.csdn.net/tag/rails) [ QEMU ](http://www.csdn.net/tag/qemu) [ KDE
](http://www.csdn.net/tag/kde) [ Cassandra
](http://www.csdn.net/tag/cassandra) [ CloudStack
](http://www.csdn.net/tag/cloudstack) [ FTC ](http://www.csdn.net/tag/ftc) [
coremail ](http://www.csdn.net/tag/coremail) [ OPhone
](http://www.csdn.net/tag/ophone ) [ CouchBase
](http://www.csdn.net/tag/couchbase) [ 云计算 ](http://www.csdn.net/tag/云计算) [
iOS6 ](http://www.csdn.net/tag/iOS6) [ Rackspace
](http://www.csdn.net/tag/rackspace ) [ Web App
](http://www.csdn.net/tag/webapp) [ SpringSide
](http://www.csdn.net/tag/springside) [ Maemo ](http://www.csdn.net/tag/maemo)
[ Compuware ](http://www.csdn.net/tag/compuware) [ 大数据
](http://www.csdn.net/tag/大数据) [ aptech ](http://www.csdn.net/tag/aptech) [
Perl ](http://www.csdn.net/tag/perl) [ Tornado
](http://www.csdn.net/tag/tornado) [ Ruby ](http://www.csdn.net/tag/ruby) [
Hibernate ](http://www.csdn.net/hibernate) [ ThinkPHP
](http://www.csdn.net/tag/thinkphp) [ HBase ](http://www.csdn.net/tag/hbase) [
Pure ](http://www.csdn.net/tag/pure) [ Solr ](http://www.csdn.net/tag/solr) [
Angular ](http://www.csdn.net/tag/angular) [ Cloud Foundry
](http://www.csdn.net/tag/cloudfoundry) [ Redis
](http://www.csdn.net/tag/redis) [ Scala ](http://www.csdn.net/tag/scala) [
Django ](http://www.csdn.net/tag/django) [ Bootstrap
](http://www.csdn.net/tag/bootstrap)

个人资料

[ ![](http://avatar.csdn.net/5/D/9/1_wxg694175346.jpg)
](http://my.csdn.net/wxg694175346)  
[ wxg694175346 ](http://my.csdn.net/wxg694175346)

[ ](javascript:void\(0\);) [ ](javascript:void\(0\);)

![2](http://csdnimg.cn/jifen/images/xunzhang/xunzhang/zhuanlandaren.png)
![1](http://csdnimg.cn/jifen/images/xunzhang/xunzhang/chizhiyiheng.png)

    * 访问：  1035559次 
    * 积分：  12112 
    * 等级：  ![](http://csdnimg.cn/jifen/images/xunzhang/jianzhang/blog7.png)

积分：12112

    * 排名：  第390名 
    * 原创：  270篇 
    * 转载：  15篇 
    * 译文：  14篇 
    * 评论：  856条 

我的邮箱  whywanghai@gmail.com

新浪微博  [ ![](http://img.my.csdn.net/uploads/201312/15/1387088999_1404.png)
](http://weibo.com/small1030light)

文章搜索

博客专栏  [ ![](http://avatar.csdn.net/blogpic/20131003093705406.jpg)
](http://blog.csdn.net/column/details/call-me-ogre.html) |  [ 谈一谈OGRE游戏引擎
](http://blog.csdn.net/column/details/call-me-ogre.html)

文章：12篇

阅读：12540  
---|---  
[ ![](http://avatar.csdn.net/blogpic/20130515134502305.jpg)
](http://blog.csdn.net/column/details/why-bug.html) |  [ Python爬虫入门教程
](http://blog.csdn.net/column/details/why-bug.html)

文章：12篇

阅读：458675  
---|---  
[ ![](http://avatar.csdn.net/blogpic/20130208175124735.jpg)
](http://blog.csdn.net/column/details/call-me-why.html) |  [ PHP学习笔记
](http://blog.csdn.net/column/details/call-me-why.html)

文章：23篇

阅读：43213  
---|---  
[ ![](http://avatar.csdn.net/blogpic/20130107235224912.jpg)
](http://blog.csdn.net/column/details/i-am-why.html) |  [ 汪海带你做游戏--
Unity3D的开发与应用 ](http://blog.csdn.net/column/details/i-am-why.html)

文章：35篇

阅读：111909  
---|---  
  
文章分类

  * [ 计算机图形学 ](http://blog.csdn.net/pleasecallmewhy/article/category/1278424) (32) 
  * [ 数据结构 ](http://blog.csdn.net/pleasecallmewhy/article/category/1278425) (30) 
  * [ Linux ](http://blog.csdn.net/pleasecallmewhy/article/category/1278588) (5) 
  * [ 数据库 ](http://blog.csdn.net/pleasecallmewhy/article/category/1280693) (5) 
  * [ Matlab ](http://blog.csdn.net/pleasecallmewhy/article/category/1283631) (8) 
  * [ Unity3D ](http://blog.csdn.net/pleasecallmewhy/article/category/1302926) (35) 
  * [ C++ ](http://blog.csdn.net/pleasecallmewhy/article/category/1303968) (38) 
  * [ 计算机组成原理 ](http://blog.csdn.net/pleasecallmewhy/article/category/1305100) (4) 
  * [ JavaScript ](http://blog.csdn.net/pleasecallmewhy/article/category/1335773) (9) 
  * [ Axure ](http://blog.csdn.net/pleasecallmewhy/article/category/1338189) (2) 
  * [ SAE ](http://blog.csdn.net/pleasecallmewhy/article/category/1338860) (4) 
  * [ PowerDesign ](http://blog.csdn.net/pleasecallmewhy/article/category/1338951) (3) 
  * [ PHP ](http://blog.csdn.net/pleasecallmewhy/article/category/1341271) (31) 
  * [ SVN ](http://blog.csdn.net/pleasecallmewhy/article/category/1341321) (1) 
  * [ XML ](http://blog.csdn.net/pleasecallmewhy/article/category/1342505) (1) 
  * [ CSS ](http://blog.csdn.net/pleasecallmewhy/article/category/1342677) (6) 
  * [ C# ](http://blog.csdn.net/pleasecallmewhy/article/category/1342952) (2) 
  * [ CodeIgniter ](http://blog.csdn.net/pleasecallmewhy/article/category/1343659) (15) 
  * [ Python ](http://blog.csdn.net/pleasecallmewhy/article/category/1344887) (27) 
  * [ jQuery ](http://blog.csdn.net/pleasecallmewhy/article/category/1345185) (6) 
  * [ Windows8 ](http://blog.csdn.net/pleasecallmewhy/article/category/1370237) (17) 
  * [ Java ](http://blog.csdn.net/pleasecallmewhy/article/category/1387661) (9) 
  * [ PhotoShop ](http://blog.csdn.net/pleasecallmewhy/article/category/1388288) (2) 
  * [ Django ](http://blog.csdn.net/pleasecallmewhy/article/category/1413227) (5) 
  * [ SQL ](http://blog.csdn.net/pleasecallmewhy/article/category/1416701) (1) 
  * [ 爬虫 ](http://blog.csdn.net/pleasecallmewhy/article/category/1418998) (19) 
  * [ Ajax ](http://blog.csdn.net/pleasecallmewhy/article/category/1430006) (1) 
  * [ 操作系统 ](http://blog.csdn.net/pleasecallmewhy/article/category/1431103) (2) 
  * [ C ](http://blog.csdn.net/pleasecallmewhy/article/category/1431104) (1) 
  * [ wifi ](http://blog.csdn.net/pleasecallmewhy/article/category/1474173) (1) 
  * [ Android ](http://blog.csdn.net/pleasecallmewhy/article/category/1494279) (1) 
  * [ iOS ](http://blog.csdn.net/pleasecallmewhy/article/category/1512775) (29) 
  * [ Chrome ](http://blog.csdn.net/pleasecallmewhy/article/category/1554113) (1) 
  * [ OGRE ](http://blog.csdn.net/pleasecallmewhy/article/category/1660481) (12) 
  * [ Cocos2D-X ](http://blog.csdn.net/pleasecallmewhy/article/category/1683931) (4) 
  * [ OpenGL ](http://blog.csdn.net/pleasecallmewhy/article/category/1690953) (5) 
  * [ OpenCV ](http://blog.csdn.net/pleasecallmewhy/article/category/1710675) (2) 
  * [ 数字图像处理 ](http://blog.csdn.net/pleasecallmewhy/article/category/1824293) (1) 
  * [ Html ](http://blog.csdn.net/pleasecallmewhy/article/category/1851815) (1) 
  * [ Grails ](http://blog.csdn.net/pleasecallmewhy/article/category/1875691) (1) 
  * [ Groovy ](http://blog.csdn.net/pleasecallmewhy/article/category/1875693) (1) 
  * [ MCM ](http://blog.csdn.net/pleasecallmewhy/article/category/1882757) (1) 
  * [ Node.js ](http://blog.csdn.net/pleasecallmewhy/article/category/2036855) (4) 
  * [ Hexo ](http://blog.csdn.net/pleasecallmewhy/article/category/2036859) (1) 
  * [ Worktile ](http://blog.csdn.net/pleasecallmewhy/article/category/2283405) (1) 
  * [ Git ](http://blog.csdn.net/pleasecallmewhy/article/category/2310295) (1) 
  * [ API ](http://blog.csdn.net/pleasecallmewhy/article/category/2316053) (1) 
  * [ PostgreSQL ](http://blog.csdn.net/pleasecallmewhy/article/category/2343533) (1) 
  * [ Swift ](http://blog.csdn.net/pleasecallmewhy/article/category/2582661) (4) 

文章存档

  * [ 2015年02月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2015/02) (1) 
  * [ 2015年01月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2015/01) (2) 
  * [ 2014年12月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2014/12) (2) 
  * [ 2014年11月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2014/11) (1) 
  * [ 2014年10月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2014/10) (2) 
  * [ 2014年09月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2014/09) (11) 
  * [ 2014年08月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2014/08) (3) 
  * [ 2014年07月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2014/07) (3) 
  * [ 2014年06月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2014/06) (15) 
  * [ 2014年05月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2014/05) (6) 
  * [ 2014年04月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2014/04) (2) 
  * [ 2014年03月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2014/03) (1) 
  * [ 2014年02月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2014/02) (3) 
  * [ 2014年01月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2014/01) (5) 
  * [ 2013年12月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2013/12) (15) 
  * [ 2013年10月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2013/10) (13) 
  * [ 2013年09月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2013/09) (5) 
  * [ 2013年08月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2013/08) (4) 
  * [ 2013年07月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2013/07) (4) 
  * [ 2013年06月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2013/06) (3) 
  * [ 2013年05月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2013/05) (19) 
  * [ 2013年04月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2013/04) (12) 
  * [ 2013年03月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2013/03) (26) 
  * [ 2013年02月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2013/02) (36) 
  * [ 2013年01月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2013/01) (41) 
  * [ 2012年12月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2012/12) (28) 
  * [ 2012年11月 ](http://blog.csdn.net/pleasecallmewhy/article/month/2012/11) (38) 

阅读排行

  * [ [Python]网络爬虫（二）：利用urllib2通过指定的URL抓取网页内容 ](/pleasecallmewhy/article/details/8923067) (72317) 
  * [ [Python]网络爬虫（一）：抓取网页的含义和URL基本构成 ](/pleasecallmewhy/article/details/8922826) (61829) 
  * [ [Python]网络爬虫（三）：异常的处理和HTTP状态码的分类 ](/pleasecallmewhy/article/details/8923725) (39773) 
  * [ [Python]网络爬虫（五）：urllib2的使用细节与抓站技巧 ](/pleasecallmewhy/article/details/8925978) (39301) 
  * [ [Python]网络爬虫（七）：Python中的正则表达式教程 ](/pleasecallmewhy/article/details/8929576) (39070) 
  * [ [Python]网络爬虫（12）：爬虫框架Scrapy的第一个爬虫示例入门教程 ](/pleasecallmewhy/article/details/19642329) (36601) 
  * [ [Python]网络爬虫（六）：一个简单的百度贴吧的小爬虫 ](/pleasecallmewhy/article/details/8927832) (33369) 
  * [ [Python]网络爬虫（四）：Opener与Handler的介绍和实例应用 ](/pleasecallmewhy/article/details/8924889) (32705) 
  * [ [Python]网络爬虫（八）：糗事百科的网络爬虫（v0.3）源码及解析(简化更新) ](/pleasecallmewhy/article/details/8932310) (31985) 
  * [ [Python]网络爬虫（十）：一个爬虫的诞生全过程（以山东大学绩点运算为例） ](/pleasecallmewhy/article/details/9305229) (28040) 

评论排行

  * [ [Python]网络爬虫（八）：糗事百科的网络爬虫（v0.3）源码及解析(简化更新) ](/pleasecallmewhy/article/details/8932310) (138) 
  * [ [Python]网络爬虫（十）：一个爬虫的诞生全过程（以山东大学绩点运算为例） ](/pleasecallmewhy/article/details/9305229) (78) 
  * [ [Python]网络爬虫（二）：利用urllib2通过指定的URL抓取网页内容 ](/pleasecallmewhy/article/details/8923067) (64) 
  * [ [Python]网络爬虫（六）：一个简单的百度贴吧的小爬虫 ](/pleasecallmewhy/article/details/8927832) (56) 
  * [ [Python]网络爬虫（12）：爬虫框架Scrapy的第一个爬虫示例入门教程 ](/pleasecallmewhy/article/details/19642329) (53) 
  * [ [Python]网络爬虫（九）：百度贴吧的网络爬虫（v0.4）源码及解析 ](/pleasecallmewhy/article/details/8934726) (49) 
  * [ [Python]网络爬虫（一）：抓取网页的含义和URL基本构成 ](/pleasecallmewhy/article/details/8922826) (41) 
  * [ [Python]项目打包：5步将py文件打包成exe文件 ](/pleasecallmewhy/article/details/8935135) (26) 
  * [ [Python]网络爬虫（三）：异常的处理和HTTP状态码的分类 ](/pleasecallmewhy/article/details/8923725) (25) 
  * [ [Review]To be coder(2011.08.01~2014.01.11-Grails-ing) ](/pleasecallmewhy/article/details/8515820) (17) 

推荐文章

最新评论

  * [ [Python]网络爬虫（12）：爬虫框架Scrapy的第一个爬虫示例入门教程 ](/pleasecallmewhy/article/details/19642329#comments)

[ u014375100 ](/u014375100) :
@u012230838:http://jgjz.hzjg.gov.cn/jgjz/getMrcjAl...

  * [ [Python]网络爬虫（二）：利用urllib2通过指定的URL抓取网页内容 ](/pleasecallmewhy/article/details/8923067#comments)

[ yunixiang ](/yunixiang) :
@Tassadar_map:博主代码中这句应该删掉，否则不能运行，这句的语法相当于并列了几个查询条件...

  * [ [Python]网络爬虫（八）：糗事百科的网络爬虫（v0.3）源码及解析(简化更新) ](/pleasecallmewhy/article/details/8932310#comments)

[ lixu_puppet ](/lixu_puppet) :
我使用的linux操作系统，不管是那个代码都是无法链接。。我猜是user_agent的问题，但是我不...

  * [ [Python]网络爬虫（十）：一个爬虫的诞生全过程（以山东大学绩点运算为例） ](/pleasecallmewhy/article/details/9305229#comments)

[ oDaHua12 ](/oDaHua12) :
作者前半部分分析post的提交地址走了很多弯路，在HTTPfox抓包显示在POST那行后面的URL就...

  * [ [Python]网络爬虫（十）：一个爬虫的诞生全过程（以山东大学绩点运算为例） ](/pleasecallmewhy/article/details/9305229#comments)

[ dingding_1983 ](/dingding_1983) :
楼主你好，我是外行的。刚才试着用火狐抓取下面这个网址，http://www.sse.com.cn/d...

  * [ [Python]网络爬虫（一）：抓取网页的含义和URL基本构成 ](/pleasecallmewhy/article/details/8922826#comments)

[ colouful987 ](/colouful987) : 想学点python写个爬虫，来看看。又逛了你的各站，发现你居然也搞swift，哈哈哈 有缘啊

  * [ [Python]网络爬虫（九）：百度贴吧的网络爬虫（v0.4）源码及解析 ](/pleasecallmewhy/article/details/8934726#comments)

[ sinat_25837091 ](/sinat_25837091) :
非常感谢博主的分享，我现在正在尝试把爬虫修改之后爬tripadvisor的用户评价，但是在评论中有很...

  * [ [Python]网络爬虫（六）：一个简单的百度贴吧的小爬虫 ](/pleasecallmewhy/article/details/8927832#comments)

[ sinat_24746081 ](/sinat_24746081) :
弱弱的问一个小白问题，可以爬有css和js的网页么？如果不能顺便问一下我用模板做的H5页面，通过浏览...

  * [ [Python]网络爬虫（六）：一个简单的百度贴吧的小爬虫 ](/pleasecallmewhy/article/details/8927832#comments)

[ jiaxingpride ](/jiaxingpride) : 楼主你好！小白求教一个问题：bdurl =
str(raw_input(u'请输入贴吧的地址，去掉p...

  * [ [Python]网络爬虫（二）：利用urllib2通过指定的URL抓取网页内容 ](/pleasecallmewhy/article/details/8927832#comments)

[ Tassadar_map ](/Tassadar_map) :
name=Somebody+Here&language=Python&location=Northa...

