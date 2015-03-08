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

#  [ [iOS] 初探 iOS8 中的 Size Class ](/pleasecallmewhy/article/details/39295327)

分类： [ iOS ](/wxg694175346/article/category/1512775) 2014-09-15 17:15  5033人阅读
评论  (8)  [ 收藏 ](javascript:void\(0\);) 举报

[ ios ](http://www.csdn.net/tag/ios)

原文地址： [ http://blog.callmewhy.com/2014/09/12/learn-ios8-size-class/
](http://blog.callmewhy.com/2014/09/12/learn-ios8-size-class/)

  

以前和安卓的同学聊天的时候，谈到适配一直是一个非常开心的话题，看到他们被各种屏幕适配折磨的欲仙欲死，心里真替他们高兴。不过在做到 iPhone 和 iPad
的适配的时候，一个页面需要配置多个 xib 进行开发还是个很头疼的事情。再加上 iPhone6 和 iPhone6 plus
的发布，适配似乎也变得麻烦起来。今天了解了 iOS8 中的 Size Class 之后，真的笑，笑出声。

##  简介

先来看一下我们的新伙伴：Size Classes。在 iOS8 中，我们不用再像以前那样，一个页面新建多个 xib
文件来适配不同类型的屏幕，现在我们可以把各种尺寸屏幕的适配工作放在一个文件中完成，然后可以通过不同类别的 Size 来定制各种尺寸的界面。换句话说，你眼前的
Storyboard 不是一个普通的 Storyboard ，而是一个九合一的 Storyboard ，可以管理九种类型的屏幕。

对于宽度和高度而言，都有三种情况：紧凑 (Compact) 、任意 (Any) 、 正常 (Regular) ，所以一共有9个类别，在设置 Size
Class 的时候页面会有提示。比如宽为 Compact 高为 Any 的情况，提示为 3.5-inch、4-inch、4.7-inch的横竖状态下的屏幕：

![](http://callmewhy.qiniudn.com/size-class-indicator.png)

[ 苹果官网文档 ](https://developer.apple.com/library/prerelease/ios/releasenotes/Gen
eral/WhatsNewIniOS/Articles/iOS8.html#//apple_ref/doc/uid/TP40014205-SW1)
举了一些例子，比如 iPad ：

![](http://callmewhy.qiniudn.com/ipad_size_class_v_2x.png)

![](http://callmewhy.qiniudn.com/ipad_size_class_h_2x.png)

比如 iPhone ：

![](http://callmewhy.qiniudn.com/iphone01_size_class_v_2x.png)

![](http://callmewhy.qiniudn.com/iphone01_size_class_h_2x.png)

比如 iPhone6 plus 的横屏状态：

![](http://callmewhy.qiniudn.com/iphone02_size_class_h_2x.png)

##  实验

Size Class 的作用是将不同尺寸的屏幕进行分类处理，而最后进行布局管理的还是Autolayout。

下面我们来搞个小项目试验一下。项目源码可以在 [ 这里 ](https://github.com/callmewhy/learn-swift/tree
/learn-ios8-size-class) 下载。

新建一个项目，进入到 Storyboard ，发现默认的尺寸是宽高均为 Any 的：

![](http://callmewhy.qiniudn.com/screen-of-new-xoce6-project.png)

我们可以在右侧的视图中选择开启还是关闭 Size Class ：

![](http://callmewhy.qiniudn.com/panel-to-open-size-classes.png)

因为 Size Class 是依赖于 Autolayout 的，所以当你尝试关闭 AutoLayout 而打开 Size Class 的时候会有如下的提醒：

![](http://callmewhy.qiniudn.com/warning-while-closing-autolayout.png)

接下来我们先搞个 View 看看，测试一下直接扔进去会是什么效果：

![](http://callmewhy.qiniudn.com/views-without-autolayout.png)

看起来好像不错啊，难道不用做适配就可以了？

想太多。

我们把 Size 切换到 Compact 看下：

![](http://callmewhy.qiniudn.com/compact-view-without-autolayout.png)

喔真的好 Compact 啊！

在不手动添加 Constraints 的情况下， Xcode 会自动自动分配一套默认的 Constraints ，以确保你在任何尺寸的屏幕下都看到一样坐标一
样大小的页面。这就意味着我们有时可以忽视自动布局，不再需要设置那些自动布局且效果不错的控件，只需要为某些特定的视图创建 Constraints 。

不过现在我们想让这个正方形时刻保持居中，所以分别给它加上了四个 Constraints ：

![](http://callmewhy.qiniudn.com/view-with-autolayout.png)

啊哈这样似乎就可以…就可以了…吗？

我们随便换了个 Size 看下效果，突然发现刚刚加的 Constraints 居然无效了，在导航栏里变成了灰色，在 Storyboard 里也看不到
Constraints 的影子：

![](http://callmewhy.qiniudn.com/error-while-change-to-other-size.png)

这是因为刚刚我们的 Constraints 是在宽高均为 Compact 的 Size
中设置的，所以并不适用于其他尺寸的屏幕。这么说难道我们以后都要配置九份 Constraints
吗！这也太苦逼了吧！老板我们要涨工资啊！显然不是，我们只需要把默认的 Constraints 放在宽高均为 Any 的 Size 中即可：

![](http://callmewhy.qiniudn.com/set-view-with-any-size.png)

这时再切换到其他尺寸就都没有问题了：

![](http://callmewhy.qiniudn.com/compact-height-view-with-constraints.png)

接下来，假设我们想在 iPhone 设备上显示两个 Label ，但是想在 iPad 上显示四个 Label，可以这样搞。

先把 Size 切换到 iPhone 的尺寸，然后添加两个 Label ：

![](http://callmewhy.qiniudn.com/labels-only-appear-in-iphone.png)

再把 Size 切换到 Regular ，添加三个 Label ：

![](http://callmewhy.qiniudn.com/regular-size-and-three-labels.png)

这时在 iPhone 中查看一下效果：

![](http://callmewhy.qiniudn.com/iphone-simulator-of-two-labels.png)

再去 iPad 里看下效果：

![](http://callmewhy.qiniudn.com/ipad-simulator-of-three-labels.png)

OK 就是这么简单。

##  实战

接下来我们来看一看如何利用 Size Class 来做适配。前面有说过， Size Class
不能解决适配问题，它的功能只是将屏幕进行分类，便于管理。真正搞适配的苦力还是 AutoLayout 。苹果的 [ 帮助文档
](https://developer.apple.com/library/prerelease/ios/recipes/xcode_help-
IB_adaptive_sizes/chapters/ChangeViewPosition.html) 给出三种方案解决 View 的适配问题。

我们先把项目改成最原始的版本，只留一个 View 在视图的正中央。原始版本的项目可以在 [ 这里
](https://github.com/callmewhy/learn-swift/tree/base-storyboard) 下载。运行一下是这样的：

![](http://callmewhy.qiniudn.com/base-storyboard-without-anything.png)

###  修改 Constraints

适配的第一个方案是针对不同尺寸的屏幕设置不同大小的 Constrain 。

我们选中一个 Constraint ，在右侧面板观察它的属性：

![](http://callmewhy.qiniudn.com/QQ20140914-9%402x.png)

在右侧面板就是 Constraints 的值，第一行是默认值，适用于所有尺寸。如果要添加不同尺寸下的自定义值，可以点击加号：

![](http://callmewhy.qiniudn.com/QQ20140914-7.png)

这样就可以添加自定义的 Constraint 值了。其中， ` w ` 和 ` h ` 分别指宽 (width) 和 高(height) 。 ` C `
是指 Size Class 中的 Compact， ` R ` 则对应 Regular ， ` A ` 对应 Any 。

如果希望这个正方形在 iPad 下可以保持100的边距，在 iPhone 下可以保持0的边距，可以把每个 Constrant
的值都设为100，然后再添加一个 wC hA 的值为0：

![](http://callmewhy.qiniudn.com/QQ20140914-10%402x.png)

运行一下程序看下，首先是 iPad 下：

![](http://callmewhy.qiniudn.com/QQ20140914-11%402x.png)

简直完美，再看下 iPhone4s 下的效果：

![](http://callmewhy.qiniudn.com/QQ20140914-12%402x.png)

哈哈似乎也不错。。。等下，说好的填满呢！怎么左右两边空了这么多空白？

突然想起了前几天在公司用 Xcode6 打开的项目再用 Xcode5 打开之后有些 xib 文件会报错，大意是： Xcode6 加了一些 Margin
我不认识。会不会是这些 Margin 在作怪呢？查了一下官方文档，确实在 iOS8 中多了一个 [ layoutMargin ](https://devel
oper.apple.com/library/prerelease/ios/documentation/UIKit/Reference/UIView_cla
ss/index.html#//apple_ref/occ/instp/UIView/layoutMargins) 的属性。偷偷拿 PS
量了一下，确实默认值是8个 point ，虚惊一场，还以为是 AutoLayout 坏了呢。

不过现在我不是很想要这个 Margin ，怎么把它关了呢？点击下方的 Pin 按钮，把 Margin 的勾选去掉即可：

![](http://callmewhy.qiniudn.com/QQ20140914-13%402x.png)

然后再重新设置一下 Constraint ，OK它终于成功的填满了整个屏幕：

![](http://callmewhy.qiniudn.com/QQ20140914-15%402x.png)

完整的源码可以在 [ 这里 ](https://github.com/callmewhy/learn-swift/tree/changing-
constraint-constants) 下载。

###  安装和卸载 Constraints

有时候我们可能会遇到比较复杂的设计，针对不同的尺寸需要有不同的布局，这和 Web 开发中的响应式设计颇有几分相似。

假设我们需要这样一个 View ：在 iPad 下固定宽度，居中对齐，在 iPhone 下，则希望它保持左右边距居中对齐。

我们只需要添加 top 、 bottom 、 center x 、 width ，分分钟就可以搞出这样一个布局：

![](http://callmewhy.qiniudn.com/QQ20140914-16%402x.png)

现在我们完成了第一步：在 iPad 下固定宽度，居中对齐。

接下来我们需要把 width 属性在 iPhone 中删除。选中 width 之后在右侧可以看到这样一个区域：

![](http://callmewhy.qiniudn.com/QQ20140914-17%402x.png)

它表示，当前这个 Constraint 适用宽高均为 Any 的屏幕，和上一步相似，我们可以点击加号添加不同屏幕下的设置：

![](http://callmewhy.qiniudn.com/QQ20140914-18%402x.png)

installed 前面打上勾，表示这个 Constraint 是适用这个尺寸的，如果没有打勾，则表明在那个尺寸下这个 Constraint
是无效的。比如下面的这个例子表示这个 Constraint 仅在宽高均为 Regular 的情况下 ( 也就是 iPad ) 有效：

![](http://callmewhy.qiniudn.com/QQ20140914-19%402x.png)

接下来我们再添加上 leading 和 trailing 为0：

![](http://callmewhy.qiniudn.com/QQ20140914-20%402x.png)

这样就能实现在 iPhone 下保持左右边距居中对齐的效果了：

![](http://callmewhy.qiniudn.com/QQ20140914-21%402x.png)

但是打开 iPad 之后发现本来设置的固定宽度的效果失效了，变成了和 iPhone 一样的左右间距固定的情况。这是因为我们没有在 iPad 的屏幕下“卸载”
(uninstall) 掉刚刚设置的 leading 和 trailing 。我们有两种方式解决这个问题。

第一种方案，选中 leading 和 trailing 这两个 Constraint 之后，在右侧添加宽高均为 Regular 的选项并去掉勾选，表明，这个
Constraint 适用于所有情况，就是不要用在宽高均为 Regular 的屏幕上：

![](http://callmewhy.qiniudn.com/QQ20140914-22%402x.png)

第二种方案，切换到 Regular Regular 的尺寸之后，选中那两个 Constraint 然后按下Command+Delete ( 注意要按下
Command 键，要不然就是彻底删除了)，就可以把这两个 Constraint 在当前的 Size 中卸载了：

![](http://callmewhy.qiniudn.com/QQ20140914-23%402x.png)

运行一下， iPad 果然也没有问题了：

![](http://callmewhy.qiniudn.com/QQ20140914-24%402x.png)

完整的源码可以在 [ 这里 ](https://github.com/callmewhy/learn-swift/tree/installing-and-
uninstalling-constraints) 下载。

###  安装和卸载 View

有时候光设置 Constraint 是无法满足比较复杂的需求的，比如大屏下我希望能显示三个按钮，分别对应：吃早饭，吃午饭，吃晚饭。但是在 iPhone
等小屏下可能放不下这么多按钮，只能显示一个按钮：吃饭。遇到这种情况，我们只能对 View 进行安装 (install) 和卸载 (uninstall)。

我们先在 View 里面加上三个按钮：

![](http://callmewhy.qiniudn.com/QQ20140914-25%402x.png)

但是我们并不希望这三个按钮出现在 iPhone 中，所以我们可以在右侧面板添加适用的尺寸，并去掉 Any 的勾选。这一步和上一章中 Constraint
的安装卸载十分类似：

![](http://callmewhy.qiniudn.com/QQ20140914-26%402x.png)

可以看到左侧的 Button 变成了灰色，表示这个按钮在当前 Any 的尺寸下是不会显示的。我们再添加一个吃饭的按钮，添加 Regular
的尺寸并去掉勾选，表明自己不会在 Regular 屏幕中出现：

![](http://callmewhy.qiniudn.com/QQ20140914-27%402x.png)

这样，在 iPhone 中我们可以看到 吃饭 的按钮：

![](http://callmewhy.qiniudn.com/QQ20140914-28%402x.png)

而在 iPad 中可以看到 吃早饭 吃午饭 吃晚饭 的按钮：

![](http://callmewhy.qiniudn.com/QQ20140914-29%402x.png)

完整的源码可以在 [ 这里 ](https://github.com/callmewhy/learn-swift/tree/installing-and-
uninstalling-views) 下载。

###  其他

最后，无意中看到仿佛 Font 的左边多了点什么：

![](http://callmewhy.qiniudn.com/QQ20140914-30%402x.png)

相信大家早已轻车熟路了，不妨动手试试看。可以参考苹果官方的 [ 帮助文档
](https://developer.apple.com/library/prerelease/ios/recipes/xcode_help-
IB_adaptive_sizes/chapters/ChangingtheFontforaSizeClass.html) 学习。

##  后话

第一次接触 Size Class ，还没有在实际项目中应用过，可能有些理解偏差，如有错误，还望指正，不胜感激。

一路走来，感觉有了 Size Class 之后，iOS 开发的适配工作可能并没有想象中的复杂，哪怕屏幕比更大还大，我们依旧能够真的笑，笑出声。

* * *

参考资料：

  * [ iOS8 Constraints and Size Classes ](https://www.youtube.com/watch?v=IwSTXY0awng)
  * [ What’s New in iOS8 ](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS8.html#//apple_ref/doc/uid/TP40014205-SW30)
  * [ Size Classes Design Help ](https://developer.apple.com/library/prerelease/ios/recipes/xcode_help-IB_adaptive_sizes/chapters/EnablingAdaptiveSizeDesign.html)
  * [ Auto Layout In iOS 8 - Layout Margins ](http://carpeaqua.com/2014/07/24/auto-layout-in-ios-8-layout-margins/)
  * [ Layout attributes relative to the layout margin on iOS versions prior to 8.0 ](http://stackoverflow.com/questions/25261326/layout-attributes-relative-to-the-layout-margin-on-ios-versions-prior-to-8-0)

  * 上一篇  [ [PHP]CodeIgniter数据库报错以及mysql_connect(): No such file or directory报错 ](/pleasecallmewhy/article/details/39099093)
  * 下一篇  [ [iOS] Swift的函数式API ](/pleasecallmewhy/article/details/39313843)

顶

     2 

踩

     0 

主题推荐

     [ ios ](http://www.csdn.net/tag/ios) [ 响应式设计 ](http://www.csdn.net/tag/响应式设计) [ 布局 ](http://www.csdn.net/tag/布局) [ 文档 ](http://www.csdn.net/tag/文档) [ 源码 ](http://www.csdn.net/tag/源码)

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

    * 访问：  1035561次 
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

