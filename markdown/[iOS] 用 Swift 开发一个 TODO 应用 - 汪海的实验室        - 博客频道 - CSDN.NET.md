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

#  [ [iOS] 用 Swift 开发一个 TODO 应用 ](/pleasecallmewhy/article/details/39321255)

分类： [ iOS ](/wxg694175346/article/category/1512775) 2014-09-16 19:04  3905人阅读
评论  (8)  [ 收藏 ](javascript:void\(0\);) 举报

原文地址： [ http://blog.callmewhy.com/2014/09/15/todo-list-in-swift/
](http://blog.callmewhy.com/2014/09/15/todo-list-in-swift/)

  

  

  

##  背景

相信不少 iOS 程序员对于 Swift 依旧持以观望的态度，一来是这小家伙刚出来没几天，本身还处于完善的阶段；二来是学习的成本较高，看完官方文档怎么也要个
几天的时间；三来是反正最近几年很难在工程项目里推广使用，工作又用不到，那我学个锤子呐。

是的，我一开始也是这么想的。直到有一天，我遇到了它： [ Swift Tutorial - To Do List App
](https://www.youtube.com/watch?v=war0gHL26ns) 。这是 YouTube
上的一个很好地视屏教程，手把手教你如何完成一个 TODO
的应用，功能很简单，就是添加任务和浏览任务。将视屏内容整理了一下。虽然没有什么高深的内容，但是作为一个入门的小程序还是挺适合的。

适用人群：有一定 Objective-C 的开发基础但是还没怎么接触 Swift 不过装有 Xcode6 想感受一下的 iOS 开发者。

客官，都看到这里了，何不打开 Xcode6 耍两把？玩一玩噻！来吧。来嘛！

##  需求

我们想做一个很简单的小东西，和官网的 Demo 一样，是一个 TODO 列表 (TODO：待办事项) ，具有以下功能：

  * 有一个列表显示 TODO 
  * 有一个页面添加 TODO 
  * 点击添加按钮，在列表显示新的 TODO 列表 

揍是这么简单，让我们开始吧！

##  新建项目

新建一个项目，选择 Tabbed Application 模板，项目名称为：MyTodoList。记得选中 Swift 作为开发语言。Xcode 会创建一个
Swift 的项目：

![](http://callmewhy.qiniudn.com/QQ20140916-1.png)

##  添加管理类

我们需要的第一个类是一个 TodoList 的管理器，用来存储 TODO 列表的数据，进行一些增删改查的基本操作。我们将其命名为 ` TodoManager
` 。

在左侧文件夹上右击，选择 New File，选择 Cocoa Class ，类名为 ` TodoManager ` ，继承自 NSObject ，
Xcode 会自动为我们添加一个 TodoManager.swift 文件。

![](http://callmewhy.qiniudn.com/QQ20140916-1%402x.png)

我们在 Swift 里定义的变量和函数都是全局属性的，这样我们可以在类的外面定义一个 TodoManager 的对象 ` todoManager `
，简单的实现了单例模式：

    
    
    import UIKit
    
    var todoManager : TodoManager = TodoManager ()
    
    class TodoManager: NSObject {
    
    }
    

接下来定义一个结构体 (struct) 来表示一个 TODO 项，它有两个属性，一个是任务名称，一个是任务描述：

    
    
    struct todo {
        var name = "Un-Named"
        var desc = "Un-Described"
    }
    

在 TodoManager 里面添加一个 todos 数组，用来存储所有的任务：

    
    
    class TodoManager: NSObject {
    
        var todos = [todo]()
    
    }
    

最后定义一个方法 ` addTask ` ，用来添加任务：

    
    
    class TodoManager: NSObject {
    
        var todos = [todo]()
    
        func addTask(name: String, desc: String) {
            todos.append(todo(name: name, desc: desc))
        }
    
    }
    

OK，这样 ` TodoManager ` 就算基本完成了。

##  开发界面

回到 StoryBoard ，我们把页面上系统自动生成的内容 (几个Label) 删除：

![](http://callmewhy.qiniudn.com/QQ20140916-2%402x.png)

然后加个 UITableView 到 FirstViewController 上：

![](http://callmewhy.qiniudn.com/QQ20140916-3%402x.png)

选中 Tab Bar ，可以编辑 Tab Bar 的显示名称和图片：

![](http://callmewhy.qiniudn.com/QQ20140916-4%402x.png)

接下来看下 Second View 。把第二个 Tab Bar 的 Title 改成 Add ：

![](http://callmewhy.qiniudn.com/QQ20140916-5%402x.png)

这样基本的页面就算是搞定了。

##  数据显示

###  First View Controller

在第一个 Tab 下，将鼠标移到 UITableView 上，按住鼠标右键拖动到 View Controller 上，选择 DataSource 和
Delegate ：

![](http://callmewhy.qiniudn.com/QQ20140916-6%402x.png)

回到代码里，打开 FirstViewController.swift 文件，添加 ` UITableViewDelegate ` 和 `
UITableViewDataSource ` 这两个协议。按住 Command 键点击协议名称可以查看协议的声明，从而知道需要实现那些方法。方法名称和
OC 中的完全相同，只需要转换成 Swift的语法即可。完成之后的 ` FirstViewController ` 是这个样子：

    
    
    class FirstViewController: UIViewController, UITableViewDelegate, UITableViewDataSource
    {
    
        override func viewDidLoad() {
            super.viewDidLoad()
            // Do any additional setup after loading the view, typically from a nib.
        }
    
        override func didReceiveMemoryWarning() {
            super.didReceiveMemoryWarning()
            // Dispose of any resources that can be recreated.
        }
    
    
        // UITableView DataSource
        func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
            return todoManager.todos.count;
        }
    
    
        func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
            let cell: UITableViewCell = UITableViewCell(style: UITableViewCellStyle.Subtitle, reuseIdentifier: "Default")
    
            cell.textLabel?.text = todoManager.todos[indexPath.row].name
            cell.detailTextLabel?.text = todoManager.todos[indexPath.row].desc
    
            return cell
        }
    
    
    }
    

###  Second View Controller

拖拽一些控件搭建下基本的框架，一个 Label 作为标题，两个 TextField 分别填写 TODO
的名称和描述，然后再加上添加按钮，基本的框架时候是这个样子的：

![](http://callmewhy.qiniudn.com/QQ20140916-7%402x.png)

然后我们把这两个 TextField 的 Delegate 都指向 View Controller ，因为我们希望在我们输入完成点击 Return
之后，键盘会自动弹回去。在 ` SecondViewController.swift ` 里面添加 ` UITextFieldDelegate ` 并实现
` textFieldShouldReturn ` 委托方法，在方法里，通过 ` resignFirstResponder ` 把键盘弹回去：

    
    
    // UITextField Delegate
    func textFieldShouldReturn(textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }
    

我们希望用户在点击背景图片的时候就可以把键盘收回来，我们可以重写 ` touchsBegan ` 方法，在里面加上 ` endEditing ` 方法：

    
    
    override func touchesBegan(touches: NSSet, withEvent event: UIEvent) {
        self.view.endEditing(true)
    }
    

定义两个属性来获取文本框中的值，切换到 Assistant 视图，通过鼠标右键拖拽新建两个变量：

![](http://callmewhy.qiniudn.com/QQ20140916-8%402x.png)

然后我们再新建一个 IBAction ，用来处理 Add 按钮的点击事件：

![](http://callmewhy.qiniudn.com/QQ20140916-9%402x.png)

在点击事件里，我们希望完成以下任务：

  * 在 todoManager 里面添加一个 TODO 项 
  * 把键盘收起 
  * 清空 TextField 中的内容 
  * TabBar 切换到 TODO 那个标签下，即时查看结果 

OK完成之后的 ` addBtnClick ` 方法如下：

    
    
    @IBAction func addBtnClick(sender: AnyObject) {
        todoManager.addTask(todoText.text, desc: descText.text)
        self.view.endEditing(true)
        todoText.text = ""
        descText.text = ""
        self.tabBarController?.selectedIndex = 0
    }
    

这样，添加 TODO 的任务就完成了。

##  删除数据

删除数据和 Objective-C 版本的接口是完全一样的，通过 ` commitEditingStyle ` 方法实现。打开
FirstViewController.swift 文件，先在代码中添加一个 TableView 的属性，方便我们刷新数据：

![](http://callmewhy.qiniudn.com/QQ20140916-10%402x.png)

删除其实也就是删除掉 ` todoManager ` 的 ` todos ` 数组里面的对应数据而已，我们可以用 ` removeAtIndex `
实现，记得 ` reloadData ` 刷新 TableView：

    
    
    func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if(editingStyle == UITableViewCellEditingStyle.Delete) {
            todoManager.todos.removeAtIndex(indexPath.row)
        }
    
        todoTableView.reloadData()
    }
    

##  测试

基本的开发工作到此就结束啦，我们可以运行应用跑跑看。

首先添加一个 TODO：

![](http://callmewhy.qiniudn.com/QQ20140916-11%402x.png)

点击 Add 之后可以看到 TableView 里已经有了添加的 TODO 项：

![](http://callmewhy.qiniudn.com/QQ20140916-12%402x.png)

滑动可以看到删除按钮：

![](http://callmewhy.qiniudn.com/QQ20140916-13%402x.png)

点击删除，删除成功：

![](http://callmewhy.qiniudn.com/QQ20140916-14%402x.png)

##  小结

不知道各位看到这里感觉如何，反正我感觉：水爆了！也没什么深奥的技术点，也没什么创新的东西，就是一个中规中矩的小应用而已。

是的，确实这样。不过希望通过这样一个简单的例子可以和大家一起熟悉一下 Swift ，熟悉一下这个新来的小伙伴^_^

完整的项目源码可以点击 [ 这里 ](https://github.com/callmewhy/learn-swift/tree/todo-list)
下载。玩的开心。

  

  * 上一篇  [ [iOS] Swift的函数式API ](/pleasecallmewhy/article/details/39313843)
  * 下一篇  [ [Web] 一个插件告诉你，这个网站是基于什么技术开发的 ](/pleasecallmewhy/article/details/39476187)

顶

     5 

踩

     0 

主题推荐

     [ ios ](http://www.csdn.net/tag/ios) [ swift ](http://www.csdn.net/tag/swift) [ uiviewcontroller ](http://www.csdn.net/tag/uiviewcontroller) [ 开发语言 ](http://www.csdn.net/tag/开发语言) [ objective-c ](http://www.csdn.net/tag/objective-c)

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

    * 访问：  1035579次 
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

