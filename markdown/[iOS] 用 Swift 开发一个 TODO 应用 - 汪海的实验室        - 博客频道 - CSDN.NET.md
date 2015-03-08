#  [ [iOS] 用 Swift 开发一个 TODO 应用 ](/pleasecallmewhy/article/details/39321255)

原文地址： [ http://blog.callmewhy.com/2014/09/15/todo-list-in-swift/ ](http://blog.callmewhy.com/2014/09/15/todo-list-in-swift/)

  


  


  


##  背景 

相信不少 iOS 程序员对于 Swift 依旧持以观望的态度，一来是这小家伙刚出来没几天，本身还处于完善的阶段；二来是学习的成本较高，看完官方文档怎么也要个几天的时间；三来是反正最近几年很难在工程项目里推广使用，工作又用不到，那我学个锤子呐。 

是的，我一开始也是这么想的。直到有一天，我遇到了它： [ Swift Tutorial - To Do List App ](https://www.youtube.com/watch?v=war0gHL26ns) 。这是 YouTube 上的一个很好地视屏教程，手把手教你如何完成一个 TODO 的应用，功能很简单，就是添加任务和浏览任务。将视屏内容整理了一下。虽然没有什么高深的内容，但是作为一个入门的小程序还是挺适合的。 

适用人群：有一定 Objective-C 的开发基础但是还没怎么接触 Swift 不过装有 Xcode6 想感受一下的 iOS 开发者。 

客官，都看到这里了，何不打开 Xcode6 耍两把？玩一玩噻！来吧。来嘛！ 

##  需求 

我们想做一个很简单的小东西，和官网的 Demo 一样，是一个 TODO 列表 (TODO：待办事项) ，具有以下功能： 

  * 有一个列表显示 TODO 
  * 有一个页面添加 TODO 
  * 点击添加按钮，在列表显示新的 TODO 列表 

揍是这么简单，让我们开始吧！ 

##  新建项目 

新建一个项目，选择 Tabbed Application 模板，项目名称为：MyTodoList。记得选中 Swift 作为开发语言。Xcode 会创建一个 Swift 的项目： 

![](http://callmewhy.qiniudn.com/QQ20140916-1.png)

##  添加管理类 

我们需要的第一个类是一个 TodoList 的管理器，用来存储 TODO 列表的数据，进行一些增删改查的基本操作。我们将其命名为 ` TodoManager ` 。 

在左侧文件夹上右击，选择 New File，选择 Cocoa Class ，类名为 ` TodoManager ` ，继承自 NSObject ， Xcode 会自动为我们添加一个 TodoManager.swift 文件。 

![](http://callmewhy.qiniudn.com/QQ20140916-1%402x.png)

我们在 Swift 里定义的变量和函数都是全局属性的，这样我们可以在类的外面定义一个 TodoManager 的对象 ` todoManager ` ，简单的实现了单例模式： 
    
    
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

在第一个 Tab 下，将鼠标移到 UITableView 上，按住鼠标右键拖动到 View Controller 上，选择 DataSource 和 Delegate ： 

![](http://callmewhy.qiniudn.com/QQ20140916-6%402x.png)

回到代码里，打开 FirstViewController.swift 文件，添加 ` UITableViewDelegate ` 和 ` UITableViewDataSource ` 这两个协议。按住 Command 键点击协议名称可以查看协议的声明，从而知道需要实现那些方法。方法名称和 OC 中的完全相同，只需要转换成 Swift的语法即可。完成之后的 ` FirstViewController ` 是这个样子： 
    
    
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

拖拽一些控件搭建下基本的框架，一个 Label 作为标题，两个 TextField 分别填写 TODO 的名称和描述，然后再加上添加按钮，基本的框架时候是这个样子的： 

![](http://callmewhy.qiniudn.com/QQ20140916-7%402x.png)

然后我们把这两个 TextField 的 Delegate 都指向 View Controller ，因为我们希望在我们输入完成点击 Return 之后，键盘会自动弹回去。在 ` SecondViewController.swift ` 里面添加 ` UITextFieldDelegate ` 并实现 ` textFieldShouldReturn ` 委托方法，在方法里，通过 ` resignFirstResponder ` 把键盘弹回去： 
    
    
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

删除数据和 Objective-C 版本的接口是完全一样的，通过 ` commitEditingStyle ` 方法实现。打开 FirstViewController.swift 文件，先在代码中添加一个 TableView 的属性，方便我们刷新数据： 

![](http://callmewhy.qiniudn.com/QQ20140916-10%402x.png)

删除其实也就是删除掉 ` todoManager ` 的 ` todos ` 数组里面的对应数据而已，我们可以用 ` removeAtIndex ` 实现，记得 ` reloadData ` 刷新 TableView： 
    
    
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

完整的项目源码可以点击 [ 这里 ](https://github.com/callmewhy/learn-swift/tree/todo-list) 下载。玩的开心。 

  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/39321255](http://blog.csdn.net/pleasecallmewhy/article/details/39321255)