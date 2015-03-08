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

#  [ [iOS] Swift 初学手册：可选类型 (Optionals)
](/pleasecallmewhy/article/details/39523701)

分类： [ Swift ](/wxg694175346/article/category/2582661) 2014-09-24 15:29  700人阅读
评论  (0)  [ 收藏 ](javascript:void\(0\);) 举报

[ Swift ](http://www.csdn.net/tag/Swift) [ iOS ](http://www.csdn.net/tag/iOS)

原文地址： [ http://blog.callmewhy.com/2014/09/23/beginners-guide-optionals-swift/
](http://blog.callmewhy.com/2014/09/23/beginners-guide-optionals-swift/)

几周前 (译者注：原文发表于6月24日)，苹果发布了一个全新的编程语言： Swift 。从那时起，我一直在阅读 [ Swift 官方手册
](https://itunes.apple.com/us/book/swift-programming-
language/id881256329?mt=11) ，并且在 Xcode6 beta 上 <del> 把玩 </del> 学习。我开始喜欢上了
Swift 的简洁和语法。我和我的团队一起学习这门全新的语言，并且将它和 Objective-C
这个有着30年历史的老伙计进行对比。同时，我们也在努力探索如何能让初学者们轻松的掌握 Swift 。

两周前，我们发布了 [ Swift 基础教程 ](http://www.appcoda.com/swift-programming-language-
intro/) ，在接下来的几周里，我们将会写一系列的教程来介绍 Swift 的新特性。这一周，让我们来看看可选类型 (Optionals)。

![](http://www.appcoda.com/wp-content/uploads/2014/06/swift-optionals-
featured.jpg)

##  概述

在前面的教程里我有提及可选类型的概念，但是没有深入讲解。

那么，什么是可选类型？

在 Swift 中，当我们声明一个变量的时候，默认情况下是 非可选类型 (non-optional) ，也就是说，你必须指定一个不为 nil
的值。如果你硬是要把一个非可选类型的变量设为 nil ，那么编译器就会告诉你：“嘿你不能把它设置成 nil 好嘛”。没错就是这样：

    
    
    var message: String = "Swift is awesome!" // OK
    message = nil // compile-time error
    

当然编译器给出的错误消息可就没这么友善了，一般会显示 ` Could not find an overload for ‘__conversion’
that accepts the supplied arguments ` 这种错误。同样，在类中声明的变量也是这样，默认情况下是费可选类型的：

    
    
    class Messenger {
        var message1: String = "Swift is awesome!" // OK
        var message2: String // compile-time error
    }
    

在 ` message2 ` 处你会得到一个编译错误，因为它没有初始值。对于那些从 Objective-C 一路走来的小伙伴们可能会感觉很意外，在
Objective-C 里这种情况根本就不会有问题好嘛：

    
    
    NSString *message = @"Objective-C will never die!";
    message = nil;
    
    class Messenger {
        NSString *message1 = @"Objective will never die!";
        NSString *message2;
    }
    

不过，你也可以在 Swift 中声明一个没有初始化的变量， Swift 提供了可选类型来表示没有值的情况。只需要在声明的类型后面加上问号 ` ? ` 即可：

    
    
    class Messenger {
        var message1: String = "Swift is awesome!" // OK
        var message2: String? // OK
    }
    

你也可以给可选类型的变量们赋值，如果不赋值那么它的值自动就设为 nil 。

##  缘由

为什么要这么设计呢？苹果官方给出的解释是，因为 Swift 是一门类型安全的语言。从前面的例子中可以看出，
Swift的可选类型会进行编译检查，防止一些常见的运行时错误。让我们看一看下面的例子，这样可以更好地理解。

比如说，在 Objective-C 中有如下代码：

    
    
    - (NSString *)findStockCode:(NSString *)company {
        if ([company isEqualToString:@"Apple"]) {
            return @"AAPL";
        } else if ([company isEqualToString:@"Google"]) {
            return @"GOOG";
        }
    
        return nil;
    }
    

在上面的方法里，你可以用 ` findStockCode ` 方法来获取到股票的代码，显然只有 Apple 和 Google
的查询会返回值，其他情况都会返回 nil 。

假设我们在下面的代码中会调用这个方法：

    
    
    NSString *stockCode = [self findStockCode:@"Facebook"]; // nil is returned
    NSString *text = @"Stock Code - ";
    NSString *message = [text stringByAppendingString:stockCode]; // runtime error
    NSLog(@"%@", message);
    

这段代码在编译时不会有任何问题，但是如果输入的是 Facbook 则会返回 nil ，导致运行时错误。

而在 Swift 里，和运行时错误不用， Swift 会在编译时就提示错误信息，我们可以把上面的代码在 Swift 中重写：

    
    
    func findStockCode(company: String) -> String? {
       if (company == "Apple") {
          return "AAPL"
       } else if (company == "Google") {
          return "GOOG"
       }
    
       return nil
    }
    
    var stockCode:String? = findStockCode("Facebook")
    let text = "Stock Code - "
    let message = text + stockCode  // compile-time error
    println(message)
    

在上面的代码里， ` stockCode ` 被定义成了可选类型，这意味着它可以有一个 string 的值，也可以为 nil
。代码无法通过编译，会提示一个错误： ` value of optional type String? is not unwrapped ` 。

正如你在例子中看到的，Swift 的可选类型加强了 nil 检测，为开发者提供了编译时的检查，合理的使用可选类型可以有效地提高代码质量。

##  强制解析

慢着慢着，前面说了那么多好处，但是代码还是没通过编译啊！别急，我们需要检测一下 ` stockCode ` 是否为 nil ，把代码做如下修改：

    
    
    var stockCode:String? = findStockCode("Facebook")
    let text = "Stock Code - "
    if stockCode {
        let message = text + stockCode!
        println(message)
    }
    

和 Objective-C 中类似，我们先对它进行检测，看看它是不是有值。如果不为 nil ，我们可以在后面加上一个感叹号 ` ! ` 进行解析，这样
Xcode 就知道：“嗯我可以使用这个值了”。在 Swift 里我们称之为 强制解析 (forced unwrapping)
，通过感叹号强制获取可选类型的真实值。

再回到上面的代码中。我们只是在强制解析之前，检测了一下看看变量是否为 nil 而已。这和 Objective-C 中常见的 nil
检测也没啥区别啊。如果我忘了检测呢？看下下面的代码：

    
    
    var stockCode:String? = findStockCode("Facebook")
    let text = "Stock Code - "
    let message = text + stockCode!  // runtime error
    

这样我们不会得到编译错误，因为我们用了强制解析，编译器已经假定这个可选类型肯定有值。显然这样是错误的，运行的时候会得到如下错误：

    
    
    fatal error: Can’t unwrap Optional.None
    

##  可选绑定

除了强制解析，可选绑定 (optional binding) 是一个更值得推荐的解析方案。
你可以用可选绑定来检测一个可选类型的值有没有值，如果有值则解析出来并存储到一个临时的变量里。

废话少说，放码过来！让我们来看看下面这个使用了可选绑定的示例代码：

    
    
    var stockCode:String? = findStockCode("Facebook")
    let text = "Stock Code - "
    if let tempStockCode = stockCode {
        let message = text + tempStockCode
        println(message)
    }
    

代码中的 ` if let ` (或者 ` if var ` ) 是可选绑定的两个关键词。翻译成人类语言，大概是这个样子：“如果 ` stackCode `
它有值，把它的值存到 ` tempStackCode ` 里，然后继续执行接下来的代码块。如果它没值，跳过后面的代码块。” 因为 `
tempStockCode ` 是一个新的常量，所以你不再需要添加 ` ! ` 后缀。

你可以把方法调用放在 ` if ` 里，这样代码看起来更简洁：

    
    
    let text = "Stock Code - "
    if var stockCode = findStockCode("Apple") {
        let message = text + stockCode
        println(message)
    }
    

这里， ` stockCode ` 不再是可选类型，我们可以直接使用。如果 ` findStockCode ` 方法返回了 nil 则会跳过后面的代码块。

##  可选链

在解释可选链之前，我们先对原始代码做一些小小的修改。我们创建一个新的类叫做 ` Stock ` ，它有 ` code ` 和 ` price `
两个可选类型的属性。 ` findStockCode ` 函数用来返回一个 ` Stock ` 对象，而不是一个 ` String ` 对象：

    
    
    class Stock {
        var code: String? 
        var price: Double? 
    }
    
    func findStockCode(company: String) -> Stock? {
        if (company == "Apple") {
            let aapl: Stock = Stock()
            aapl.code = "AAPL"
            aapl.price = 90.32
    
            return aapl
    
        } else if (company == "Google") {
            let goog: Stock = Stock()
            goog.code = "GOOG"
            goog.price = 556.36
    
            return goog
        }
    
        return nil
    }
    

接下来，我们先用 ` findStockCode ` 函数查找股票的代码，然后计算购买100股所需要的总价：

    
    
    if let stock = findStockCode("Apple") {
        if let sharePrice = stock.price {
            let totalCost = sharePrice * 100
            println(totalCost)
        }
    }
    

函数的返回值是可选类型，我们通过可选绑定来检测是否有值，显然股票的价格也是一个可选类型，于是我们继续使用 ` if let ` 来检测它是否有值。

上面的代码没有任何问题，不过这一层一层的 ` if ` 嵌套实在是太麻烦了，如果可选类型层次多点，很可能形成下面的情况：

    
    
    if let x = xxx() {
        if let x = xxx() {
            if let x = xxx() {
                if let x = xxx() {
                    if let x = xxx() {
                        if let x = xxx() {
                            if let x = xxx() {
                                if let x = xxx() {
                                    if let x = xxx() {
                                        if let x = xxx() {
                                            if let x = xxx() {
                                                if let x = xxx() {
    
                                                }        
                                            }
                                        }
                                    }
                                }   
                            }
                        }        
                    }
                }
            }
        }   
    }
    

<del> 呃上面这段代码是我自己瞎写的，原文中并没有嗯。 </del>

除了使用 ` if let ` ，我们可以通过可选链来简化代码。我们可以用问号将多个可选类型串联起来：

    
    
    if let sharePrice = findStockCode("Apple")?.price {
        let totalCost = sharePrice * 100
        println(totalCost)
    }
    

可选链提供了访问变量的另一种方式，代码现在看上去也更加的干净整洁。上面只是一个基础的使用，更加深入的学习可以参考 [ 官方文档 ](https://deve
loper.apple.com/library/ios/documentation/swift/conceptual/swift_programming_l
anguage/OptionalChaining.html) 。

##  Swift 和 Objective-C 的交互

Swift 中的可选类型十分强大，尽管可能一开始的时候需要花点时间慢慢熟悉。可选类型让你的代码更清晰，而且可以避免一些 nil 引起的问题。

Swift 有设计与 Objective-C 交互的 API，当我们需要和 UIKit 或者其他框架的 API
交互的时候，你肯定会遇到可选类型。下面列举一些 UITableView 中可能会遇到的可选类型：

    
    
    func numberOfSectionsInTableView(tableView: UITableView?) -> Int {
        // Return the number of sections.
        return 1
    }
    
    func tableView(tableView: UITableView?, numberOfRowsInSection section: Int) -> Int {
        // Return the number of rows in the section.
        return recipes.count
    }
    
    
    func tableView(tableView: UITableView!, cellForRowAtIndexPath indexPath: NSIndexPath!) -> UITableViewCell! {
        let cell = tableView.dequeueReusableCellWithIdentifier("Cell", forIndexPath: indexPath) as UITableViewCell
    
        cell.textLabel.text = recipes[indexPath.row]
    
        return cell
    }
    

##  总结

对于一名开发者来说，理解可选类型的工作原理是十分必要的。这也就是为什么我们专门写一篇文章来介绍可选类型。它可以帮助开发者在编译阶段就发现隐藏的问题，从而避免
运行时错误。当你习惯了这种语法，你将会愈发欣赏可选类型的魅力所在。

享受这个美好的世界吧。真棒。( <del> 没错这句也是我乱加的 </del> )

* * *

原文地址

  * [ A Beginner’s Guide to Optionals in Swift ](http://www.appcoda.com/beginners-guide-optionals-swift/)

  * 上一篇  [ [iOS] 推荐几个提高移动应用开发效率的第三方服务 ](/pleasecallmewhy/article/details/39501327)
  * 下一篇  [ [iOS6]如何在Xcode6设置UIView的圆角显示 ](/pleasecallmewhy/article/details/39613871)

顶

     0 

踩

     0 

主题推荐

     [ ios ](http://www.csdn.net/tag/ios) [ 类 ](http://www.csdn.net/tag/类) [ swift ](http://www.csdn.net/tag/swift) [ uitableviewcell ](http://www.csdn.net/tag/uitableviewcell) [ 编程语言 ](http://www.csdn.net/tag/编程语言)

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

  * [ 计算机图形学 ](http://blog.csdn.net/wxg694175346/article/category/1278424) (32) 
  * [ 数据结构 ](http://blog.csdn.net/wxg694175346/article/category/1278425) (30) 
  * [ Linux ](http://blog.csdn.net/wxg694175346/article/category/1278588) (5) 
  * [ 数据库 ](http://blog.csdn.net/wxg694175346/article/category/1280693) (5) 
  * [ Matlab ](http://blog.csdn.net/wxg694175346/article/category/1283631) (8) 
  * [ Unity3D ](http://blog.csdn.net/wxg694175346/article/category/1302926) (35) 
  * [ C++ ](http://blog.csdn.net/wxg694175346/article/category/1303968) (38) 
  * [ 计算机组成原理 ](http://blog.csdn.net/wxg694175346/article/category/1305100) (4) 
  * [ JavaScript ](http://blog.csdn.net/wxg694175346/article/category/1335773) (9) 
  * [ Axure ](http://blog.csdn.net/wxg694175346/article/category/1338189) (2) 
  * [ SAE ](http://blog.csdn.net/wxg694175346/article/category/1338860) (4) 
  * [ PowerDesign ](http://blog.csdn.net/wxg694175346/article/category/1338951) (3) 
  * [ PHP ](http://blog.csdn.net/wxg694175346/article/category/1341271) (31) 
  * [ SVN ](http://blog.csdn.net/wxg694175346/article/category/1341321) (1) 
  * [ XML ](http://blog.csdn.net/wxg694175346/article/category/1342505) (1) 
  * [ CSS ](http://blog.csdn.net/wxg694175346/article/category/1342677) (6) 
  * [ C# ](http://blog.csdn.net/wxg694175346/article/category/1342952) (2) 
  * [ CodeIgniter ](http://blog.csdn.net/wxg694175346/article/category/1343659) (15) 
  * [ Python ](http://blog.csdn.net/wxg694175346/article/category/1344887) (27) 
  * [ jQuery ](http://blog.csdn.net/wxg694175346/article/category/1345185) (6) 
  * [ Windows8 ](http://blog.csdn.net/wxg694175346/article/category/1370237) (17) 
  * [ Java ](http://blog.csdn.net/wxg694175346/article/category/1387661) (9) 
  * [ PhotoShop ](http://blog.csdn.net/wxg694175346/article/category/1388288) (2) 
  * [ Django ](http://blog.csdn.net/wxg694175346/article/category/1413227) (5) 
  * [ SQL ](http://blog.csdn.net/wxg694175346/article/category/1416701) (1) 
  * [ 爬虫 ](http://blog.csdn.net/wxg694175346/article/category/1418998) (19) 
  * [ Ajax ](http://blog.csdn.net/wxg694175346/article/category/1430006) (1) 
  * [ 操作系统 ](http://blog.csdn.net/wxg694175346/article/category/1431103) (2) 
  * [ C ](http://blog.csdn.net/wxg694175346/article/category/1431104) (1) 
  * [ wifi ](http://blog.csdn.net/wxg694175346/article/category/1474173) (1) 
  * [ Android ](http://blog.csdn.net/wxg694175346/article/category/1494279) (1) 
  * [ iOS ](http://blog.csdn.net/wxg694175346/article/category/1512775) (29) 
  * [ Chrome ](http://blog.csdn.net/wxg694175346/article/category/1554113) (1) 
  * [ OGRE ](http://blog.csdn.net/wxg694175346/article/category/1660481) (12) 
  * [ Cocos2D-X ](http://blog.csdn.net/wxg694175346/article/category/1683931) (4) 
  * [ OpenGL ](http://blog.csdn.net/wxg694175346/article/category/1690953) (5) 
  * [ OpenCV ](http://blog.csdn.net/wxg694175346/article/category/1710675) (2) 
  * [ 数字图像处理 ](http://blog.csdn.net/wxg694175346/article/category/1824293) (1) 
  * [ Html ](http://blog.csdn.net/wxg694175346/article/category/1851815) (1) 
  * [ Grails ](http://blog.csdn.net/wxg694175346/article/category/1875691) (1) 
  * [ Groovy ](http://blog.csdn.net/wxg694175346/article/category/1875693) (1) 
  * [ MCM ](http://blog.csdn.net/wxg694175346/article/category/1882757) (1) 
  * [ Node.js ](http://blog.csdn.net/wxg694175346/article/category/2036855) (4) 
  * [ Hexo ](http://blog.csdn.net/wxg694175346/article/category/2036859) (1) 
  * [ Worktile ](http://blog.csdn.net/wxg694175346/article/category/2283405) (1) 
  * [ Git ](http://blog.csdn.net/wxg694175346/article/category/2310295) (1) 
  * [ API ](http://blog.csdn.net/wxg694175346/article/category/2316053) (1) 
  * [ PostgreSQL ](http://blog.csdn.net/wxg694175346/article/category/2343533) (1) 
  * [ Swift ](http://blog.csdn.net/wxg694175346/article/category/2582661) (4) 

文章存档

  * [ 2015年02月 ](http://blog.csdn.net/wxg694175346/article/month/2015/02) (1) 
  * [ 2015年01月 ](http://blog.csdn.net/wxg694175346/article/month/2015/01) (2) 
  * [ 2014年12月 ](http://blog.csdn.net/wxg694175346/article/month/2014/12) (2) 
  * [ 2014年11月 ](http://blog.csdn.net/wxg694175346/article/month/2014/11) (1) 
  * [ 2014年10月 ](http://blog.csdn.net/wxg694175346/article/month/2014/10) (2) 
  * [ 2014年09月 ](http://blog.csdn.net/wxg694175346/article/month/2014/09) (11) 
  * [ 2014年08月 ](http://blog.csdn.net/wxg694175346/article/month/2014/08) (3) 
  * [ 2014年07月 ](http://blog.csdn.net/wxg694175346/article/month/2014/07) (3) 
  * [ 2014年06月 ](http://blog.csdn.net/wxg694175346/article/month/2014/06) (15) 
  * [ 2014年05月 ](http://blog.csdn.net/wxg694175346/article/month/2014/05) (6) 
  * [ 2014年04月 ](http://blog.csdn.net/wxg694175346/article/month/2014/04) (2) 
  * [ 2014年03月 ](http://blog.csdn.net/wxg694175346/article/month/2014/03) (1) 
  * [ 2014年02月 ](http://blog.csdn.net/wxg694175346/article/month/2014/02) (3) 
  * [ 2014年01月 ](http://blog.csdn.net/wxg694175346/article/month/2014/01) (5) 
  * [ 2013年12月 ](http://blog.csdn.net/wxg694175346/article/month/2013/12) (15) 
  * [ 2013年10月 ](http://blog.csdn.net/wxg694175346/article/month/2013/10) (13) 
  * [ 2013年09月 ](http://blog.csdn.net/wxg694175346/article/month/2013/09) (5) 
  * [ 2013年08月 ](http://blog.csdn.net/wxg694175346/article/month/2013/08) (4) 
  * [ 2013年07月 ](http://blog.csdn.net/wxg694175346/article/month/2013/07) (4) 
  * [ 2013年06月 ](http://blog.csdn.net/wxg694175346/article/month/2013/06) (3) 
  * [ 2013年05月 ](http://blog.csdn.net/wxg694175346/article/month/2013/05) (19) 
  * [ 2013年04月 ](http://blog.csdn.net/wxg694175346/article/month/2013/04) (12) 
  * [ 2013年03月 ](http://blog.csdn.net/wxg694175346/article/month/2013/03) (26) 
  * [ 2013年02月 ](http://blog.csdn.net/wxg694175346/article/month/2013/02) (36) 
  * [ 2013年01月 ](http://blog.csdn.net/wxg694175346/article/month/2013/01) (41) 
  * [ 2012年12月 ](http://blog.csdn.net/wxg694175346/article/month/2012/12) (28) 
  * [ 2012年11月 ](http://blog.csdn.net/wxg694175346/article/month/2012/11) (38) 

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

