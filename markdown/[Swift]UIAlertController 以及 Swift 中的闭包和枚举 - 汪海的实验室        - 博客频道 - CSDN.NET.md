#  [ [Swift]UIAlertController 以及 Swift 中的闭包和枚举 ](/pleasecallmewhy/article/details/39931821)

原文地址： [ http://blog.callmewhy.com/2014/10/08/uialertcontroller-swift-closures-enum/ ](http://blog.callmewhy.com/2014/10/08/uialertcontroller-swift-closures-enum/)

在 iOS8 的 SDK 中， UIKit 框架里两个常用的 API 有了比较大的改动。UIActionSheet 和 UIAlertView 都被 UIAlertController 替换了。 

在 iOS8 里，如果你想要弹出消息，你应该使用 UIAlertController 而不是那两个不建议使用的类了。 ActionSheet 和 AlertView 都变成了 UIAlertController 的风格。在创建 UIAlertController 的时候你可以选择不同的风格，按钮事件的处理方法也重新设计了，不再需要像以前那样使用 delegate 处理用户操作。当使用 UIAlertController 的时候，你可以把事件和控制器关联起来，事件在 Objective-C 中是一个 block 而在 Swift 中则是一个闭包 (closure)。 

在这篇教程里，我们将会介绍 UIAlertController 并且演示如何使用它来弹出消息和表单。借此机会，我刚好简单的讲解一些 Swift 中闭包和枚举的内容。 

![](http://www.appcoda.com/wp-content/uploads/2014/08/uialertcontroller-featured.png)

##  创建 Xcode 项目 

通过项目来学习是最好的方法，我们新建一个 Single View Application 的项目并将其命名为 UIAlertDemo 。记得选中 Swift 作为默认的开发语言。 

在 Xcode6 中， Size Class 是默认开启的状态，为了让代码尽量的简单易懂，在此教程中我们不会使用相关的新特性，选中 Main.storyboard 文件并且在属性中去掉 Use Size Classes 的勾选。取消勾选之后会提醒选择默认设备类型，选中 iPhone 并且点击 Disable Size Classes 即可。这样我们的 ViewController 看起来就是 iPhone 的尺寸了。 

拖拽一个按钮到视图中并且设置标题为 ` Hello Alert ` ，这样就完成了 <del> 前戏 </del> 准备工作。 

![](http://www.appcoda.com/wp-content/uploads/2014/08/uialertcontroller-demo-storyboard.png)

##  添加 Action 方法 

在 ` ViewController.swift ` 里，为按钮添加一个方法，接下来我们会将它和 Storyboard 关联起来： 
    
    
    @IBAction func showAlert() {
    
    }
    

Outlet 和 Action 让我们可以把源码和 UI 对象关联起来，在 Swift 里，我们在方法名前添加 ` @IBAction ` 关键字，表明这是一个 Action 方法。这个方法将会和 Storyboard 关联起来。 

接下来我们将会把按钮和方法关联起来。在左侧的缩略图中，按住 Control 键并从按钮拖拽到 ViewController 上，松开按钮，选择 ` showAlert ` 方法： 

![](http://www.appcoda.com/wp-content/uploads/2014/08/uialertcontroller-connect-actions.png)

##  使用 UIAlertViewController 弹框 

我们已经完成了基本的项目配置，现在可以开始学习 UIAlertController 类的使用了。大致来说，为了弹出提示信息，大致需要完成以下几个步骤： 

  * 创建一个 UIAlertController ，设置它的标题、内容以及式样。 
  * 定义 UIAlertAction 对象，并且把它加到 AlertController 中。 
  * 通过调用 ` presentViewController ` 方法弹出内容。 

如果用 Swift 写，看起来大概是这个样子的： 
    
    
    @IBAction func showAlert() {
        let alertController = UIAlertController(title: "Hey AppCoda", message: "What do you want to do?", preferredStyle: .Alert)
    
        let defaultAction = UIAlertAction(title: "OK", style: .Default, handler: nil)
        alertController.addAction(defaultAction)
    
        presentViewController(alertController, animated: true, completion: nil)
    }
    

很简单，不是吗？我们只需要设定 ` Style ` 值就可以选择弹出的是消息还是表单。如果是 ` .Alert ` 则是弹出消息， ` .ActionSheet ` 则对应表单。 

默认情况下， ` AlertController ` 并没有和任何 ` Action ` 关联起来。如果你没有添加任何 ` Action ` 会导致无法关闭弹出的内容。在上面的代码中，我们创建了一个 ` UIAlertAction ` 的实例，并且通过 ` addAction ` 方法把它和 ` AlertController ` 关联起来。在初始化 ` UIAlertAction ` 的时候，你需要指定标题 (Title)，样式 (Style) 和处理器 (Handler) 。 ` Handler ` 是一个代码块，会在按钮被点击的时候执行。我们只需要把 Handler 设置成 nil 就可以关闭弹出的窗口。在后面的内容里会有详细的讲解。 

最后，我们调用 ` presentViewController ` 方法弹出页面，如果你运行一下示例程序，点击按钮你会得到一个弹出的消息 (取决于你设定的样式) ： 

![](http://www.appcoda.com/wp-content/uploads/2014/08/uialertcontroller-style.png)

##  简要的谈谈 Swift 中的枚举 

如果你是第一次编写 Swift 的代码，你可能不太熟悉在设定样式时使用的 ` . ` 语法。你可以这样重写一下前面的代码： 
    
    
    let alertController = UIAlertController(title: "Hey AppCoda", message: "What do you want to do?", preferredStyle: UIAlertControllerStyle.Alert)
    

代码是完全一样的，我们只是准确的指定了枚举类型， ` UIAlertControllerStyle ` 实际上是一个枚举类： 
    
    
    enum UIAlertControllerStyle : Int { 
         case ActionSheet 
         case Alert 
    }
    

Swift 中的枚举类型可以让你把相关的值放到一个组里，枚举中定义的值 (例如： ` AlertSheet ` 和 ` Alert ` ) 就是成员的值。 Objective-C 里，成员在创建的时候会指定一个常量值，比如0和1，而 Swift 中则不是这样。以 ` UIAlertControllerStyle ` 为例， ` ActionSheet ` 和 ` Alert ` 并没有定义为0和1，每个成员在枚举中都是完整的值。 

你可以通过枚举类型 (比如 ` UIAlertControllerStyle ` ) 加上点和成员值的方式来指定枚举值。 ` UIAlertControllerStyle.Alert ` 就是一个典型的例子。得益于 [Swift 的类型推导特性]，我们在指定枚举值的时候可以去掉前面的枚举类型，这也就是为什么可以写作 ` .Alert ` 和 ` .ActionSheet ` 的原因。 
    
    
    let alertController = UIAlertController(title: "Hey AppCoda", message: "What do you want to do?", preferredStyle: .Alert)
    

这种缩略形式的 ` 点语法 ` 可以让你少写代码并且让你的代码更具有可读性。 

##  Handler 和闭包 

让我们回到 UIAlertController 里，我们还没有讨论 UIAlertAction 中的 handler 。当我们创建一个 UIAlertAction 的时候，我们可以把一个代码块指定为 handler 。当用户触发了 Action 事件的时候便会执行这段代码。我们可以在 ` showAlert ` 方法里插入如下代码添加一个新的 action ： 
    
    
    let callActionHandler = { (action:UIAlertAction!) -> Void in
        let alertMessage = UIAlertController(title: "Service Unavailable", message: "Sorry, the call feature is not available yet. Please retry later.", preferredStyle: .Alert)
        alertMessage.addAction(UIAlertAction(title: "OK", style: .Default, handler: nil))
        self.presentViewController(alertMessage, animated: true, completion: nil)
    }
    let callAction = UIAlertAction(title: "Call", style: .Default, handler: callActionHandler)
    alertController.addAction(callAction)
    

在这里我们添加了一个 callAction 用来弹出提示。在 Swift 里，这样的代码块叫做闭包 (Closure) 。闭包是可传递的功能代码块，很像 Objective-C 中的 block 。正如上面的例子那样，如果想要声明某个 action 的闭包，方法之一是把这个代码块声明成一个常量或者变量。第一个部分定义了 handler 的参数为 UIAlertAction 类型，关键词 ` in ` 表明前面的参数和返回类型都已经定义完毕，后面便是闭包的内容： 

![](http://www.appcoda.com/wp-content/uploads/2014/08/closure-in-swift.png)

其实我们并没有必要声明一个单独的变量来存储闭包的内容，我们可以直接把闭包作为一个参数传过去。 Swfit 可以推测参数的类型，所以我们可以这样简化代码： 
    
    
    let callAction = UIAlertAction(title: "Call", style: .Default, handler: {
        action in
            let alertMessage = UIAlertController(title: "Service Unavailable", message: "Sorry, the call feature is not available yet. Please retry later.", preferredStyle: .Alert)
            alertMessage.addAction(UIAlertAction(title: "OK", style: .Default, handler: nil))
            self.presentViewController(alertMessage, animated: true, completion: nil)
            }
    )
    alertController.addAction(callAction)
    

##  总结 

通过这篇教程，我希望你能理解 UIAlertController 的基本使用方法。希望你喜欢这个 iOS8 里的新伙计！ 

你可以在 [ 这里 ](https://www.dropbox.com/s/x9nhs1ps899qkn3/UIAlertDemo.zip) 下载源码。 

* * *

原文地址： 

  * [ Introduction to UIAlertController, Swift Closures and Enumeration ](http://www.appcoda.com/uialertcontroller-swift-closures-enum/)
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/39931821](http://blog.csdn.net/pleasecallmewhy/article/details/39931821)