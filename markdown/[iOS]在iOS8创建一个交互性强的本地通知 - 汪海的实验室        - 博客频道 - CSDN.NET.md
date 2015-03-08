#  [ [iOS]在iOS8创建一个交互性强的本地通知 ](/pleasecallmewhy/article/details/42913175)

（原文： [ Creating Interactive Local Notifications in iOS 8 ](http://www.appcoda.com/local-notifications-ios8/) 作者：Gabriel Theodoropoulos 译者： [ ibenjamin ](http://weibo.com/u/2771490773) ） 

** 通知（Notifications） ** ，是App用来和用户交流的一种方式，特别是当App并没有在前台运行的时候。通知，正如它的名称所强调的，被用作向用户‘通知’一个事件，或者仅仅向用户提示一条重要信息。总而言之，通知在提示类型的App当中非常有用，甚至在一些别的类型的App当中也是如此。比如，当用户进入一个指定区域（这是iOS8的新特性），一个下载任务完成，或者当朋友给你发送一条信息的时候，一条通知就可以被显示出来。无论如何，通知的目的就是获得用户的关注，然后他们就能处理通知了。 

从编程的角度来说，通知有着一套相当标准的API，可以非常简单地被实现。不需要太多的脑力，开发者可以根据文档轻松的在App中加入通知功能。也 就是说，详细规定由系统转发的通知的内容，在App启动时处理通知，最后，从iOS8开始，处理任何由通知指定的动作（actions）。每一个App唯 一改变的只有业务逻辑而已。 

![图片1](http://api.cocoachina.com/uploads/image/20150112/1421048514859878.jpg)

从iOS8开始，本质上来说有两种通知： 

  1. ** 本地通知（local notifications） ** ：由开发者定义，App触发。触发的时间是被事先安排好的。 

  2. ** 远程通知（remote notifications） ** ：这种情况下，通知可以被分成两个类别：(a) ** 推送通知（The push notifications） ** ，被服务器初始化，然后通过APNS，最终到达用户设备。(b) ** 静默通知（The silent notifications） ** ，其实也是推送通知，但是他们并没有被展示给用户，而是立即被App处理以发起某项任务，最后当一切都完成时，一个本地通知 被显示以提示用户。 

除了以上的2种以外，iOS8引入了 ** 地点通知（location notifications） ** 。它其实也是本地通知（local notifications）,但是他们只会在用户一个特定的地理或者iBeacon区域时，才会被触发。虽然我们看不到什么细节，地点通知 （location notifications）实现起来也很容易。 

这个好消息昭示着一个重要的信息：从iOS8开始，通知被加入了新的特性。简单地说，从现在开始，当一个通知被展示时，开发者可以指定用户可触发的具体的动作（actions），而且甚至不用启动App也可以处理这个通知。 

随着新特性的引入，通知变得越来越引人注目。用户被给予一个选择清单，然后可以命令App立即执行特定的命令。用户再也不用浪费时间在启动App、处理通知上了。动作（Actions）使得通知和App越来越强大，当然也极大的提升了用户体验。 

动作（Actions）可以被归类到一个类目（categories）下。特别是当App安排了不少通知显示的时候相当方便。用类目 （categories），一个通知所有相关的动作（actions）都可以一次性的被捆绑和指定。反之，处理动作（actions）也非常简单，只需要实现其代理方法即可。每一个动作（actions）都有一个特殊的属性标示符（identifier），被App用来辨别收到的动作（actions）然后适当地处理它。 

如你所见，本篇文章的目的就是让你了解以上所有细节。尽管动作（actions）和类目（categories）是新的技术，你最后会发现，他们其实实现起来并不困难。然而，在我们进入到下一个部分之前，我需要说明我们只会就本地通知（local notifications）进行详尽说明。我认为，如果想要在本篇文章中将通知的每个种类都详尽说明，那么这篇文章就会变得很泛泛，除此之外，我们也会将文章的重点放在对iOS8新引入的功能进行说明。 

跟往常一样，我强烈地推荐你去看看官方文档。不仅仅是苹果开发者中心，还去看看 [ WWDC 2014 #713 session video ](https://developer.apple.com/videos/wwdc/2014/) 。将本篇文章和以上结合起来学习，你将会获得所有通知新特性的知识。而且，我们在这里并不会讨论远程和地点通知，官方文档是你学习他们的一个好地方。 

##  关于本地通知 

本地通知被安排在指定的日期和时间被App触发。时刻记在心中，尽管在和用户通信时通知十分有用，你也应该小心，过分的使用可能会导致较差的用户体验。 

有几种方式来提示用户一个通知，接下来会展示所有支持的通知类型。正如你已经了解的，你可以指定通知类型为他们中的几个或者所有。 

  1. Alert or Banner:通知可以用alert或者banner来显示，这取决于用户在设置中得选择。他们都应当包含通知的消息（当然是可以本地化的）。 

  2. 声音（Sound）：当一个通知被送达时，你可以‘告诉’iOS播放一段自定义或者系统默认的声音。因为用户不会一直看着设备，被展示的通知有可能会被忽略，所以声音显得很有用。但是，对于不重要的通知，声音不应该被使用。 

  3. Badge：当通知到达时，一个badge数字会在App的图标上显示。当一个通知到达时，badge数字必增加1，当通知被处理后badge数字减1。当badge数字不为0或者为0，iOS会显示或者隐藏badge。 

在iOS7时，用户只能点击通知（或者在锁屏时滑动）然后关联的App会启动，最后处理相关动作。现在开发者可以用户提供具体的预先定义的动作了。 相关联的App可以在不被启动的情况下，处理不关键或者重要的任务了，而且也可以根据用户的选择来执行不同的代码。马上我们就能通过这篇文章来学习如何实 现它。 

除了上面所说的，一个本地通知还可以包含附加的数据，此数据可以被App处理。此数据可以被包含在一个用户信息字典中，App可以通过通知来访问此数据，在启动时或者未启动时。 

可以被安排的本地通知的数量并不是无限的，最多有64个本地通知可以被安排和展示。如果多余这个数字，所有超过这个数字的通知都会被废弃。尽管如此，无论通知是以什么样的形式被安排的，最早的那个会被最先展示。 

接下来，让我们看看我们今天学习会使用的到得示例App。 

##  示例App概览 

通过开发一个示例App，我们会学习到所有通知的功能。实际上我们将会开发一款购物清单应用，用户通过此应用发送的通知会得到他需要购买的物品清单。完成这个，我们需要下面两个功能： 

  1. 添加和删除一个物品 

  2. 选择一个日期和时间通知用户。 

如你所想，我们只会实现本地通知。通过它，演示iOS8通知的新特性已经足够了。 

为了添加一个新物品，我们需要用到textfield控件。添加的物品会在一个tableview中展示出来，在tableview已经存在的物品 中，可以通过在物品cell左滑动来删除物品。然后，date picker控件可以被用来设置通知展示的日期和时间。此date picker会在一个按钮被点击了之后展示出来，当选择好了日期之后，这个按钮会被用来安排通知和重新显示tableivew。我们会以动画的形式来显示 和隐藏date picker，所以我们的App就会显得更加吸引人啦，值得注意的是这里也演示的如何在Swift中使用UIView来实现简单地动画效果。 

对于我们将要安排的本地通知，我们会定义3种不同的动作（除了默认通知以外，所有本地通知都支持让App启动）。这些动作会给用户如下的选择（我写下了动作标题和它将要做的事情）： 

  1. “好，买到了”(OK, got it):这个动作其实并不会做什么，除了让通知消失以外。在App中，没有任何任务将会执行。 

  2. “编辑清单”（Edit list）：这个动作将会启动App，然后textfield会获得焦点，然后用户可以直接写下一个新的物品。 

  3. “删除清单”（delete list）：这个动作不会启动App。现存的物品清单将会被删除，但是App并不会被启动。下次用户启动App时，物品清单就会不见啦。 

下面几张图演示了这个App的功能。正如我所说的，它很简单，但是用来达到本篇文章的目的已经足够啦： 

![图片2](http://api.cocoachina.com/uploads/image/20150112/1421048514998038.png) ![图片3](http://api.cocoachina.com/uploads/image/20150112/1421048515417927.png)

![图片4](http://api.cocoachina.com/uploads/image/20150112/1421048515194568.png) ![图片5](http://api.cocoachina.com/uploads/image/20150112/1421048515812140.png)

最后再说几句，我会在实现动作的时候具体讲到他们。所以，目前将通知动作当做是根据通知用户可触发的方法就行了，所有与他们相关的内容你马上就会看到了。 

##  基本项目 

我们的目标是了解所有和通知相关的新东西而不是从头创建一个项目，你可以从 [ 这里 ](http://pan.baidu.com/s/1mgKGr7U) 获得基本项目。下载它，解压它，打开它，这个项目将会作为我们实现通知的模板。 

这个项目已经设计好了基本界面，在你阅读下一章之前，请概览一下此项目。打开Main.storyboard，看看那些subviews和已经连接好的IBoutle和IBAction。 

除此之外，你会看到所有ViewController应该实现的协议也已经声明好了。tableview的datasouce和delegate也已经写好了，但是里面并没有逻辑相关的代码。这仅仅是为了避免Xcode报错而已。最后，在viewDidLoad方法中，你可以看到哪些对象被设置了代 理。 

这个基本项目很容易理解，所以你没有必要花太多时间来看它。但是它还是值得你快速的阅览一下的。 

##  设计一个购物清单 

首先，让我们来实现这个购物清单。本部分我们的目标是通过textfield添加一个物品和在tableivew中展示所有的物品。当然，我们也会 实现删除已经存在物品的功能。显然，我们需要一个数据结构来保存我们的数据，并且作为tableview的数据源。接下来，让我们给 ViewController类添加一个NSmutableArray属性。确保你选择的是ViewController.swift文件。在此文件中， 找到IBOutlet属性声明然后添加下面的实例变量： 
    
    
    var shoppintList: NSMutableArray!

好了，我们已经完成了第一步。注意到我们并不会在viewDidLoad方法中对它进行初始化，而是在我们会添加新的物品到它之中时初始化它。 

现在保存物品的数据结构已经声明好了，接下来让我们允许用户通过textfied添加物品。实际上，我们希望新添加的物品在添加到了数组之 后，tableivew马上更新显示它。要实现此功能，我们必须实现textFieldShouldReturn(textField:) 代理方法。正如你在基本项目中所见到的，UITextFieldDelegate协议已经被遵从了，ViewController也设置成为了 txtAddItem textfield的代理类。 

在这个代理方法中，我们希望做以下事情： 

  * 如果shoppintList为nil，初始化它 

  * 将textfield的txt添加为一个新的物品到数组 

  * 让tableview展示新的物品（我们稍后就会实现此功能） 

  * 添加新物品后清空textfield的内容 

  * 移除textfield的焦点，所以键盘就会隐藏了 

上面的事情是不是看起来很多？其实不多，以可以通过下面的代码片段来做这些事情： 
    
    
    func textFieldShouldReturn(textField: UITextField) -> Bool {
        if shoppingList == nil{
            shoppingList = NSMutableArray()
        }
        shoppingList.addObject(textField.text)
    
        tblShoppingList.reloadData()
    
        txtAddItem.text = ""
        txtAddItem.resignFirstResponder()
    
        return true
    }

上面的代码所实现的功能已经非常清楚了，所以我认为不需要更多地讨论了。 

接下来让我们在tableview中展示shoppingList的内容。在ViewController类中，tableview的 datasource和delegate方法我们已经加上去了，但是现在我们必须加上合适的代码以让它工作。让我们从简单的开始，tableview中得 section和row的数量，每个cell的高度。你可以用下面的代码整体替换项目中的活着只是简单的替换方法的内容。 
    
    
    func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 1
    }
    
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        var rows = 0
    
        if let list = shoppingList{
            rows = list.count
        }
    
        return rows
    }
    
    
    func tableView(tableView: UITableView, heightForRowAtIndexPath indexPath: NSIndexPath) -> CGFloat {
        return 50.0
    }

注意到我们对shoppingList数组进行了空指针判断。 

接下来，让我们将数组中的每个元素赋值给cell的label，然后他就会在tableview中展示出来了。在此之前，我需要强调一下，在 Interface Builder中有一个cell原型，标示符（identifier）为idCellItem。首先，让我们重用（dequeue）这个cell，然后将 数组中每个元素赋值给这个cell的label的text属性。代码如下： 
    
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        var cell = tableView.dequeueReusableCellWithIdentifier("idCellItem") as UITableViewCell
    
        cell.textLabel?.text = shoppingList.objectAtIndex(indexPath.row) as NSString
    
        return cell
    }

下面代码的类型转换部分： 
    
    
    cell.textLabel?.text = shoppingList.objectAtIndex(indexPath.row) as NSString

非常重要（as NSString部分），因为我们想让编译器清楚我们是想将一个string赋值给label。 

现在，我们终于可以添加一个新物品和展示所有的物品在tableview中啦。但其实还差一点点，这里还差最后一个功能：删除以存在的物品。 

这实现起来很简单，让我们定义一个超级简单的新方法： 
    
    
    func removeItemAtIndex(index: Int) {
        shoppingList.removeObjectAtIndex(index)
    
        tblShoppingList.reloadData()
    }

此方法只接收一个参数，待删除物品的数组下标。我们使用这个参数，删除shoppingList数组中对应的物品，然后刷新tableview的数据。 

现在让我们在左滑cell后显示的删除按钮上调用上面的方法。要实现此功能，我们需要实现 tableView(tableView:commitEditingStyle:forRowAtIndexPath:) 代理。在此代理方法中我们调用上面的删除方法。下面是代码： 
    
    
    func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == UITableViewCellEditingStyle.Delete {
            removeItemAtIndex(indexPath.row)
        }
    }

这里有两件事情需要注意一下：1.这个if判断语句是非常必要的，有了这个if判断，删除方法就只会在用户点击删除按钮后被触发。2.代理方法中的indexPath.row的row就是我们想要删除的物品的数组下标。 

你可能会想，为什么我们要定义一个新的removeItemAtIndex(index:) 方法呢？毕竟我们只需要2行代码就能在代理方法中实现删除了。嗯，现在我不会回答此问题；去搜索思考吧。 

最后，我需要强调的是我们并没有必要向这个简单的App中加入编辑物品功能。毕竟这也没什么难度。我们现在做的已经够了。 

##  保存和加载清单 

尽管前面我们已经实现了这个App的基本功能，但是我们还需要加入另外两个重要的功能来让这个App正常的工作。我们需要将清单保存到磁盘，然后在程序启动时从磁盘读取清单。 

NSMutableArray提供了将数据写入磁盘和从磁盘读取数据的方法，我们可以方便使用他们。接下来我们将会定义两个方法，来保存和读取数据。首先让我们实现保存方法，保存到的文件名字为shopping_list： 
    
    
    func saveShoppingList() {
        let pathsArray = NSSearchPathForDirectoriesInDomains(NSSearchPathDirectory.DocumentDirectory, NSSearchPathDomainMask.UserDomainMask, true)
        let documentsDirectory = pathsArray[0] as String
        let savePath = documentsDirectory.stringByAppendingPathComponent("shopping_list")
        shoppingList.writeToFile(savePath, atomically: true)
    }

方法的第一二行代码，返回了App的Ducument类目。然后我们构建保存的文件的路径。最后，调用NSMutableArray方法writeToFile(_:atomically:)。这个方法将数据保存到了磁盘。 

实现了保存方法后我们就能调用他了。如果你有对前面的App基本功能进行思考，应该能想到我们会在两个地方调用到保存方法：1.当一个新的物品被添加时，2.删除一个已经存在的物品时。 

首先，在 textFieldShouldReturn(textField:) 代理方法中的return之前添加保存方法： 
    
    
    func textFieldShouldReturn(textField: UITextField) -> Bool {
        ...
    
        saveShoppingList()
    
        return true
    }

非常好，现在我们可以将新添加的物品保存到磁盘啦。接下来，让我们到removeItemAtIndex(index:)方法中也加入保存方法： 
    
    
    func removeItemAtIndex(index: Int) {
        ...
    
        saveShoppingList()
    }

接下来任何可能对我们的数据产生影响的操作，都会被保存到磁盘啦。 

现在我们可以实现读取数据的方法啦。首先让我们来看看方法定义： 
    
    
    func loadShoppingList() {
        let pathsArray = NSSearchPathForDirectoriesInDomains(NSSearchPathDirectory.DocumentDirectory, NSSearchPathDomainMask.UserDomainMask, true)
        let documentsDirectory = pathsArray[0] as String
        let shoppingListPath = documentsDirectory.stringByAppendingPathComponent("shopping_list")
    
        if NSFileManager.defaultManager().fileExistsAtPath(shoppingListPath){
            shoppingList = NSMutableArray(contentsOfFile: shoppingListPath)
            tblShoppingList.reloadData()
        }
    }

这里需要提醒一下，在读取磁盘文件之前我们总是会检查一下这个文件存不存在。在iOS当中，我们通过NSFileManager来检查文件存不存 在。如果文件不存在那么当然什么事情都不会发生啦。如果文件存在的话，我们就会用文件的内容来初始化shoppingList数组，然后让 tableview重新加载数据。 

最后，我们当然得调用此方法。我们希望App在启动完毕后马上加载数据，在viewDidLoad方法中调用它就是一个很好的选择。 
    
    
    override func viewDidLoad() {
        ...
    
        loadShoppingList()
    }

当我们不启动App处理通知时，这两个方法将会非常有用。 

##  选择一个提醒时间 

现在textfield和tableview在我们的修改之后工作的非常好了。对物品清单的管理也几乎要完成了。我们现在可以将重心移到date picker控件上来了。在这个部分，我们将会做一些非常简单有趣的事情。我们会以动画的形式展现date picker，然后我们就能为一个通知选择一个日期和时间啦。 

如果你去看看ViewController的viewDidLoad方法，你会发现一行隐藏date picker控件的代码： 
    
    
    datePicker.hidden = true

接下来我们将会使Schedule Reminder按钮像一个开关一样工作：当点击它时，date picker将变得可见，tableview将会隐藏，再次点击它时它又会做完全相反的事情。 

如我所说，tableview和date picker之间将会以动画的形式切换，为了实现这个动画切换，我竟会定义一个新的方法。在方法中，我会使用UIView的 animateWithDuration(duration:animations:completionHandler:) 方法。这个方法帮助我们快速而方便的创建动画，如果你曾经使用过它，你应该就会知道它的方便快捷之处。 

我们先定义一个animateMyViews(viewToHide:viewToShow:)方法。从方法名就能看出，这个方法接收两个参数，第 一个是需要隐藏的view，第二个是将要显示的view。请记住，在此方法中我们需要同时隐藏或者显示tableview和date picker，所以我们需要在调用此方法是依次传入合适的参数。 

让我们挪到代码部分，首先我们来看看方法的实现，然后我们会详尽的对方法进行讨论： 
    
    
    func animateMyViews(viewToHide: UIView, viewToShow: UIView) {
        let animationDuration = 0.35
    
        UIView.animateWithDuration(animationDuration, animations: { () -> Void in
            viewToHide.transform = CGAffineTransformScale(viewToHide.transform, 0.001, 0.001)
            }) { (completion) -> Void in
    
                viewToHide.hidden = true
                viewToShow.hidden = false
    
                viewToShow.transform = CGAffineTransformScale(viewToShow.transform, 0.001, 0.001)
    
                UIView.animateWithDuration(animationDuration, animations: { () -> Void in
                    viewToShow.transform = CGAffineTransformIdentity
                })
        }
    }

让我们来看看这个方法都做了什么：首先，我们以秒为单位定义了每个动画的持续时间。注意到，这里有两个动画将会先后顺序执行。第一个动画隐藏需要被隐藏的view，第二个动画展示需要被展示的view。 

首先，我们启动第一个动画，然后转换viewToHide的transform属性，这样它的宽和高就会按比例缩小。这个view的实际frame 并不会变化，但是这个动画会产生一种拉远消失的漂亮效果。当第一个动画完成时，在它的动画完成回调闭包（closure）里我们首先设置2个view是否 可见，第一个view被隐藏，第二个view变得可见了。然后我们对第二个view的transform属性立即缩放。最后我们对第二个view的 transform逐步放大到正常值。第二个动画的最终效果就是拉近。 

注意到，如果你想改变动画的持续时间，简单的改变animationDuration值就行啦。上面的动画持续时间是0.7秒钟（0.35+0.35）。 

你应该对这个动画是如何实现的和最终的效果非常好奇吧？没关系，马上你就会知道了，现在我们还差一点点工作。我们现在需要实现唯一的一个IBAction方法。 

这个方法将要做的事情非常简单：首先检查date picker最近的状态，如果它是隐藏着的，我们会调用上面的动画方法并以tableview为第一个参数，date picker为第二个参数。如果它没有隐藏的话，我们就会给动画方法传入相反顺序的参数。 
    
    
    @IBAction func scheduleReminder(sender: AnyObject) {
        if datePicker.hidden {
            animateMyViews(tblShoppingList, viewToShow: datePicker)
        }
        else{
            animateMyViews(datePicker, viewToShow: tblShoppingList)
        }
    
        txtAddItem.enabled = !txtAddItem.enabled
    }

上面的if-else语句已经非常清楚了。在这个方法的最后，我们使用一个布尔值标志，来允许或者不允许添加物品，当tableview显示时允许，反之不允许。 

现在，Schedule Reminder按钮可以被用来切换显示tableview和date picker啦。稍后，我们会在上面的IBAction方法中加入更多代码，然后我们就能安排显示本地通知啦。 

现在你可以稍微把玩一下这个App了，在模拟器或者iPhone上面跑跑它吧。试试添加删除物品和动画切换。如果你懒得跑它下面的图片也展示了这个App目前的效果：   


![](http://api.cocoachina.com/uploads/image/20150112/1421048515838551.gif)

##  规定通知类型 

到目前为止我们已经完成了一些有趣和cool的事情，我们的App也如我们所想的运行起来了。从此部分开始，我们将学习本地通知，并实践每个新的功能。 

在开始之前，先说明一下，在本部分和接下来的部分中我们都只会在同一个一个方法中编写代码。尽管如此，我们将会一步步的实现它，这样我们就能讨论每一个新功能了。 

在本文章的开头，我简要的说明了一下本地通知。其中，我说明了通知的集中类型：在alert或者banner中显示消息（稍后我会道速你如何在他们 之中切换），声音和badge。本部分，我们会规定通知的类型。总之，我们只会实现在alert和banner中显示消息，和播放一段声音。我们不会实现 badge数字，如果你想你可以自己实现它。实现它的方法在本文章的末尾有。 

在开始下一个部分之前，有一个非常重要的地方我需要强调一下。所有有关一个App的通知的设置都会在用户设置中体现出来。如果一个App使用了通 知，那么在第一次启动程序时，App会询问用户是否允许App发送通知。不管用户选择了允许还是不允许，他都可以以后在用户设置中改变他。所以，在程序启 动时看到了下图中的alert时别惊讶，选允许，否则我们就什么通知都看不懂了。 

![](http://api.cocoachina.com/uploads/image/20150112/1421048516515089.png)

接下来我们将创建一个叫setupNotificationSettings()的方法。除去定义方法部分，我们只会在这里编写一行代码。也许你会 想，这很简单，但是其实它做了一个非常重要的工作。通过这行代码，我们告诉了App我们想要支持的通知类型。将此设置保存进一个变量，以后我们会用到它。 

下面是目前的代码： 
    
    
    func setupNotificationSettings() {
        // Specify the notification types.
        var notificationTypes: UIUserNotificationType = UIUserNotificationType.Alert | UIUserNotificationType.Sound
    
    }

UIUserNotificationType是一个枚举（enum）类型，它包含了通知所有可能的类型。如你所见，OR操作符（“|”）用来包括多种类型。在 [ 这里 ](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIUserNotificationSettings_class/index.html#//apple_ref/c/tdef/UIUserNotificationType) 你可以看到通知所有可能的类型。如果你想重温一下Swift位操作符的话， [ 这里 ](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/AdvancedOperators.html) 将会有你想要的。 

在我们使用通知类型之前让我们先看一点别的东西。 

##  创建通知动作（Notification Actions） 

前面我笼统的介绍了几次通知动作，现在让我们来详细的了解一下他们。 

一个动作就是一个UIMutableUserNotificationAction类的对象。UIMutableUserNotificationAction是iOS8新引入的类，有着许多有用的配置属性： 

  * 标示符（identifier）：字符串，标示了一个对于整个App唯一的字符串。很明显，你永远不应该在同一个App中定义两个同样地标示符。通过此标示符，我们可以决定在用户点击不同的通知时，调用哪个动作。 

  * 标题（title）：用来在展示给用户的动作按钮上。可以是简单地或者本地化的字符串。为了让用户能马上理解动作的含义，一定要仔细考虑这个标题的值，最好是1到2个字符。 

  * （destructive）：布尔值。当设置为true时，通知中相应地按钮的背景色会变成红色。这只会在banner通知中出现。通常，当动作代表着删除、移除或者其他关键的动作是都会被标记为destructive以获得用户的注意。 

  * authenticationRequired：布尔值。当设置为true时，用户在点击动作之前必须确认自己的身份。当一个动作十分关键时这非常有用，因为为认证的操作有可能会破坏App的数据。 

  * ActivationMode：枚举。决定App在通知动作点击后是应该被启动还是不被启动。此枚举有两个值： （a）UIUserNotificationActivationModeForeground, （b）UIUserNotificationActivationModeBackground。在background中，App被给予了几秒中来运行 代码。 

当我描述此App时，我说过我们将会创建3中不同的动作： 

  1. 一个简单的通知，点击后消失，不会做任何事情。 

  2. 点击通知动作后添加一个物品。 

  3. 点击通知动作后删除整个清单。 

让我们用代码来实现每个动作。对于每个动作，我都会使用到上面描述的每个属性。 
    
    
    var justInformAction = UIMutableUserNotificationAction()
    justInformAction.identifier = "justInform"
    justInformAction.title = "OK, got it"
    justInformAction.activationMode = UIUserNotificationActivationMode.Background
    justInformAction.destructive = false
    justInformAction.authenticationRequired = false

动作的标示符是“提示而已（justInform）”。动作只会在backgroun运行，不会产生任何安全问题，所以我们设置了destructive和authenticationRequired为false。 

下一个动作： 
    
    
    var modifyListAction = UIMutableUserNotificationAction()
    modifyListAction.identifier = "editList"
    modifyListAction.title = "Edit list"
    modifyListAction.activationMode = UIUserNotificationActivationMode.Foreground
    modifyListAction.destructive = false
    modifyListAction.authenticationRequired = true

很明显，为了让用户能够标记物品清单，我们需要App启动。而且我们不希望用户的物品清单被未验明身份的人乱动，我们设置了authenticationRequired为true。 

最后一个动作： 
    
    
    var trashAction = UIMutableUserNotificationAction()
    trashAction.identifier = "trashAction"
    trashAction.title = "Delete list"
    trashAction.activationMode = UIUserNotificationActivationMode.Background
    trashAction.destructive = true
    trashAction.authenticationRequired = true

通过这个动作，我们允许用户在App没有启动的情况下删除整个物品清单。这个动作可能导致用户丢失所有数据，所以我们设置了destructive和authenticationRequired为true。 

通过上面的代码，你应该了解到了配置动作其实很简单。 

现在让我们把以上三个动作配置代码片段加入到setupNotificationSettings方法中吧！ 
    
    
    func setupNotificationSettings() {
        ...    
    
        // Specify the notification actions.
        var justInformAction = UIMutableUserNotificationAction()
        justInformAction.identifier = "justInform"
        justInformAction.title = "OK, got it"
        justInformAction.activationMode = UIUserNotificationActivationMode.Background
        justInformAction.destructive = false
        justInformAction.authenticationRequired = false
    
        var modifyListAction = UIMutableUserNotificationAction()
        modifyListAction.identifier = "editList"
        modifyListAction.title = "Edit list"
        modifyListAction.activationMode = UIUserNotificationActivationMode.Foreground
        modifyListAction.destructive = false
        modifyListAction.authenticationRequired = true
    
        var trashAction = UIMutableUserNotificationAction()
        trashAction.identifier = "trashAction"
        trashAction.title = "Delete list"
        trashAction.activationMode = UIUserNotificationActivationMode.Background
        trashAction.destructive = true
        trashAction.authenticationRequired = true
    
    }

当一个通知的所有动作被配置好了之后，他们可以被包进一个类目（categories）里。如果你的通知支持动作，那么你就必须创建一个类目 （categories）。通常情况下一个类目（category）配对一个通知，假设一个App中得所有通知都支持动作，那么这个App也会有和通知一 样多的类目（categories）。 

我们只会在这个示例App中创建一个通知，所以这里也只会有一个类目（category）。从编程的角度来说，类目（category）就是一个 UIMutableUserNotificationCategory类的对象，这也是iOS8新引入的类。这个类只有一个属性和一个方法。标示符属性用 来表示一个唯一的类目（category），方法用来将多个动作包含进来。 

让我们来了解一下这个方法，先看看这个方法的声明（来自苹果官方文档）： 
    
    
    func setActions(_ actions: [AnyObject]!, forContext context: UIUserNotificationActionContext)

第一个参数指明了需要包含进来的动作。是一个包含所有动作的数组，他们在数组中的顺序也代表着他们将会在一个通知中调用的先后顺序。 

第二个参数非常重要。context形参是一个枚举类型，描述了通知alert显示时的上下文，有两个值： 

  1. UIUserNotificationActionContextDefault：在屏幕的中央展示一个完整的alert。(未锁屏时) 

  2. UIUserNotificationActionContextMinimal：展示一个banner alert。 

在默认上下文（default context）中，类目最多接受4个动作，会以预先定义好的顺序依次在屏幕中央显示。在minimal上下文中，最多可以在banner alert中设置2个动作。注意在第二个情况中，你必须选择一个较为重要的动作以显示到banner通知里。接下来我们会将这两种情况都用代码实现。 

如我所说，上述方法的第一个参数必须为一个数组。所以在我们的配置通知方法中我们首先为两个上下文创建两个数组： 
    
    
    func setupNotificationSettings() {
        ...
    
        let actionsArray = NSArray(objects: justInformAction, modifyListAction, trashAction)
        let actionsArrayMinimal = NSArray(objects: trashAction, modifyListAction)
    
    }

然后让我们来创建一个新的类目（category）吧，首先我们设置它的标示符（identifier），然后将上面的2个数组分别设置： 
    
    
    func setupNotificationSettings() {
        ...
    
        // Specify the category related to the above actions.
        var shoppingListReminderCategory = UIMutableUserNotificationCategory()
        shoppingListReminderCategory.identifier = "shoppingListReminderCategory"
        shoppingListReminderCategory.setActions(actionsArray, forContext: UIUserNotificationActionContext.Default)
        shoppingListReminderCategory.setActions(actionsArrayMinimal, forContext: UIUserNotificationActionContext.Minimal)
    
    }

然后…这样就行啦，为一个通知相关的动作创建一个类目就这样完成了。 

##  注册通知设置 

通过上面的3个部分，我们已经将本地通知的所有新功能已经实现了。现在我们需要将这些设定注册到用户设置中。为了完成这个目标，我们将会用到 UIUserNotificationSettings类（iOS8新引入），然后在下面的init方法中，我们会指定通知类型和类目 （category）。 
    
    
    convenience init(forTypes allowedUserNotificationTypes: UIUserNotificationType, categories actionSettings: NSSet?)

第一个参数是我们为通知设置的类型，第二个方法是一个集合（NSSet），在这个集合中必须包含一个App所有通知支持的类目。在本例中，我们只有一个类目，但是我们还是需要使用集合来传递它。 

下面是代码实现： 
    
    
    func setupNotificationSettings() {
        ...
    
        let categoriesForSettings = NSSet(objects: shoppingListReminderCategory)
    
    }

现在，我们就可以创建一个UIUserNotificationSettings对象了，然后传入相应的参数。 
    
    
    func setupNotificationSettings() {
        ...
    
        let newNotificationSettings = UIUserNotificationSettings(forTypes: notificationTypes, categories: categoriesForSettings)
    
    }

最后，让我们将它注册一下吧！ 
    
    
    func setupNotificationSettings() {
        ...
        UIApplication.sharedApplication().registerUserNotificationSettings(newNotificationSettings)
    }

第一次启动App时上述代码就会执行，它会在用户设置中创建一条我们的App记录。 

最后，在我展现一个完整的setupNotificationSettings()，还有一点需要注意。这个方法会在viewDidLoad方法中 被调用，这意味着每当App被启动的时候它都会执行一次。很显然一遍又一遍的设置同样地值是在做无用功，这样如果我们将上面的方法用一个if判断执行一下 的话就好了。在这个判断中，我们检查通知的类型是否已经被设定了，如果没有if块中的代码就会被执行。 
    
    
    func setupNotificationSettings() {
        let notificationSettings: UIUserNotificationSettings! = UIApplication.sharedApplication().currentUserNotificationSettings()
    
        if (notificationSettings.types == UIUserNotificationType.None){
            ...
        }
    }

首先，我们通过UIApplication的类方法currentUserNotificationSettings()来获取通知的类型。通过这 个方法返回的UIUserNotificationSettings类的对象，我们可以检查它的types枚举属性。请记住这个属性为枚举类型。如果它的 值为None，那么通知类型就还没有被注册，然后我们就运行上面的方法来注册通知类型，否则什么也不做。 

通过上面的代码我们避免了重复注册通知类型。但是如果你想修改通知类型、添加动作或者类目的话，你可以将if开始和结束行注释掉，然后运行一次App。新的设定会被添加，你就能测试一下他们了。然后移除注释，避免重复注册。 

好了，设置通知的工作已经完成了。下面你可以看到setupNotificationSettings()方法的完整版本： 
    
    
    func setupNotificationSettings() {
        let notificationSettings: UIUserNotificationSettings! = UIApplication.sharedApplication().currentUserNotificationSettings()
    
        if (notificationSettings.types == UIUserNotificationType.None){
            // Specify the notification types.
            var notificationTypes: UIUserNotificationType = UIUserNotificationType.Alert | UIUserNotificationType.Sound
    
    
            // Specify the notification actions.
            var justInformAction = UIMutableUserNotificationAction()
            justInformAction.identifier = "justInform"
            justInformAction.title = "OK, got it"
            justInformAction.activationMode = UIUserNotificationActivationMode.Background
            justInformAction.destructive = false
            justInformAction.authenticationRequired = false
    
            var modifyListAction = UIMutableUserNotificationAction()
            modifyListAction.identifier = "editList"
            modifyListAction.title = "Edit list"
            modifyListAction.activationMode = UIUserNotificationActivationMode.Foreground
            modifyListAction.destructive = false
            modifyListAction.authenticationRequired = true
    
            var trashAction = UIMutableUserNotificationAction()
            trashAction.identifier = "trashAction"
            trashAction.title = "Delete list"
            trashAction.activationMode = UIUserNotificationActivationMode.Background
            trashAction.destructive = true
            trashAction.authenticationRequired = true
    
            let actionsArray = NSArray(objects: justInformAction, modifyListAction, trashAction)
            let actionsArrayMinimal = NSArray(objects: trashAction, modifyListAction)
    
            // Specify the category related to the above actions.
            var shoppingListReminderCategory = UIMutableUserNotificationCategory()
            shoppingListReminderCategory.identifier = "shoppingListReminderCategory"
            shoppingListReminderCategory.setActions(actionsArray, forContext: UIUserNotificationActionContext.Default)
            shoppingListReminderCategory.setActions(actionsArrayMinimal, forContext: UIUserNotificationActionContext.Minimal)
    
    
            let categoriesForSettings = NSSet(objects: shoppingListReminderCategory)
    
    
            // Register the notification settings.
            let newNotificationSettings = UIUserNotificationSettings(forTypes: notificationTypes, categories: categoriesForSettings)
            UIApplication.sharedApplication().registerUserNotificationSettings(newNotificationSettings)
        }
    }

别忘了在viewDidLoad方法中调用它： 
    
    
    override func viewDidLoad() {
            ...
    
            setupNotificationSettings()
        }

##  安排本地通知 

如果你在iOS之前的版本中使用过本地通知的话，你一定知道安排一个通知是很简单地事情。在iOS8，安排一个通知并没有什么变化。事实上，所有的基本设置都是一模一样的。唯一的新东西就是必须给一个通知设置一个类目，这样通知就能知道当用户点击的时候该启动哪些动作了。 

你可能已经猜到了，我们会定义一个新的方法来配置和安排一个本地通知。在我们实现这个方法之前，我们先看看一个本地通知中得重要属性： 

  * fireDate：一个通知应当被显示的日期和时间。NSDate对象。 

  * alertBody：通知的内容。应当尽量的简洁明了，这样用户才能马上理解它。 

  * alertAction：在默认情况下，点击一个banner通知会导致App启动。在以alert形式显示的通知中，会创建一个和这个动作对应 的按钮。在此属性中，你必须指定这个按钮的标题。比如，在这个示例App中，我们将View List设置为它的标题或者alert的动作。 

牢记以上几点，现在放我们定义这个方法配置这个通知。不用说先让我们创建一个UILocalNotification对象： 
    
    
    func scheduleLocalNotification() {
        var localNotification = UILocalNotification()
        localNotification.fireDate = datePicker.date
        localNotification.alertBody = "Hey, you must go shopping, remember?"
        localNotification.alertAction = "View List"
    
    }

还有一点，我们必须指定用户点击通知后对应的类目动作。回忆一下，我们前面已经定义了一个类目和类目标示符，我们在这里就能使用到这个标示符了： 
    
    
    func scheduleLocalNotification() {
        ...
    
        localNotification.category = "shoppingListReminderCategory"
    }

这很简单。最后，我们需要使用UIApplication的scheduleLocalNotification(_:) 方法来真正的安排一个通知，不然这个通知永远都不会“通知”到你啦。 
    
    
    func scheduleLocalNotification() {
        ...
    
        UIApplication.sharedApplication().scheduleLocalNotification(localNotification)
    }

接下来，让我们调用这个方法吧。让我们在scheduleReminder(sender:) 按钮方法中加入新的代码，在显示tableview之前我们调用上面的代码。注意，这里有一点需要避免：如果我们在已经安排了一个本地通知以后在重新安排 一个，之前的通知仍然会有效。如果我们忽略了这一点，我们可能会创建许多个不需要的通知。为了避免这样，我们简单的在date picker显示的时候移除所有已经安排的通知，这样就没事啦。下面是IBAction方法代码： 
    
    
    @IBAction func scheduleReminder(sender: AnyObject) {
        if datePicker.hidden {
            animateMyViews(tblShoppingList, viewToShow: datePicker)
    
            UIApplication.sharedApplication().cancelAllLocalNotifications()
        }
        else{
            animateMyViews(datePicker, viewToShow: tblShoppingList)
    
            scheduleLocalNotification()
        }
    
        txtAddItem.enabled = !txtAddItem.enabled
    }

这就是啦。在配置了类型、动作和其他的细节之后，安排他是一件很简单的事情。有了上面的代码，现在通知已经可以如我们期望的工作了。 

##  修复安排通知的时间问题 

目前为止我们都做的很好，每个功能都工作的很完美。但是，当你运行这个程序的时候你可能会发现一个关于通知送达时间的问题尽管它看起来是正常的，我 发现它存在一点问题。所以，在我们测试通知之前，让我先深入的讲一下这个问题。也许在你运行这个App的时候并不会察觉这个问题，但是在实时性强的App 中，通知推送的时间非常重要，而且不准确的时间可能会造成非常严重的问题。 

那么这个问题是什么呢？嗯，接下来让我以一个例子来说明它：如果你在10:23:14的时候安排了一个通知在14:00被推送（不用管日期，假设是 同一天），这个通知其实不会在14:00:00的时候被推送。而是在14:00:14的时候。我认为对于通知来说这是一个非常严重的问题。为什么会这样 呢？那是因为在date picker中，我们可以设置时间，但是却不能设置到秒。然后系统就会将我们设置时的时间的秒赋值给通知的推送时间，而不是使用0。 

那么，我们该怎样修复这个BUG呢？很简单，通过代码来修复。如果你以前没有接触过日期和时间的话也不用担心。，这将是一个简单而有趣的任务。 

一个日期对象（NSDate对象）可以分为几个部分，叫做date components。这些component是NSDateComponents类的属性，可以可以同时读和写，所以当我们从date picker选择的日期得到了这些components之后我们就可以修改其中的seconds属性了。很明显，通过这些components我们可以重 新得到一个NSDate对象，有了这个对象之后，我们就可以方便的将其设置为通知的推送日期了。 

正如你在下面的实现中所看到的，将一个日期对象转换成date components依赖于NSCalendar类。这个类提供让我们完成这些工作的方法。 
    
    
    func fixNotificationDate(dateToFix: NSDate) -> NSDate {
        var dateComponets: NSDateComponents = NSCalendar.currentCalendar().components(NSCalendarUnit.DayCalendarUnit | NSCalendarUnit.MonthCalendarUnit | NSCalendarUnit.YearCalendarUnit | NSCalendarUnit.HourCalendarUnit | NSCalendarUnit.MinuteCalendarUnit, fromDate: dateToFix)
    
        dateComponets.second = 0
    
        var fixedDate: NSDate! = NSCalendar.currentCalendar().dateFromComponents(dateComponets)
    
        return fixedDate
    }

详细讨论NSCalendar并不是我们的目的。但是这也将是一个非常有趣的话题，所以你可以通过 [ 这里 ](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSCalendar_Class/index.html) 来了解更多有关NSCalendar的东西。 

现在是时候选择一个合适的地点来调用这个方法了，在设置通知推送时间的时候调用这个方法将是一个很好地选择。返回 scheduleLocalNotification()方法，将date picker选择的日期作为参数传入此方法，然后将此方法返回的日期设置为通知的fireDate。下面是更新后的 scheduleLocalNotification()方法： 
    
    
    func scheduleLocalNotification() {
        var localNotification = UILocalNotification()
        localNotification.fireDate = fixNotificationDate(datePicker.date)
        localNotification.alertBody = "Hey, you must go shopping, remember?"
        localNotification.alertAction = "View List"
        localNotification.category = "shoppingListReminderCategory"
    
        UIApplication.sharedApplication().scheduleLocalNotification(localNotification)
    }

现在，我们的通知终于可以如愿以偿的按时被推送了！ 

##  处理通知动作 

现在关于通知，我们只差最后一个部分了，那就是处理用户点击通知相关按钮时候的各种动作。和往常一样，这里有几个主要的委托方法我们需要实现。 

在我们实现和处理动作之前，让我给你介绍几个代理方法，通过他们你可以方便的开发你的App。注意，在这个示例程序中，我们并不会真正的使用到他们，我们只会通过他们打印一些消息。现在，请打开AppDelegate.swift文件。 

第一个代理方法是关于通知设置的。这个代理方法在程序启动时被调用（不管是正常启动还是通过一个本地通知），包含了所有App通知的设置选项。接下来你可以看到它的定义。我们所做的，仅仅是打印通知类型： 
    
    
    func application(application: UIApplication, didRegisterUserNotificationSettings notificationSettings: UIUserNotificationSettings) {
    
        println(notificationSettings.types.rawValue)
    }

通过上述的方法，你可以得到所有UIUserNotificationSettings支持的类型。当你需要检查你的App所支持的通知和动作的类型时，这个方法非常有用。别忘了，用户可以通过用户设置来改变通知类型，所以我们不能保证，初始的通知类型一直都有效。 

当你安排了一个通知之后，无论你的App是否在运行，这个通知都将被推送。通常情况下，开发者设置通知如何在App没有运行或者被挂起的时候被推 送，所有的代码实现也聚焦在这两个方面。但是，我们也应该处理当App在运行时通知如何被处理。感谢苹果，iOS SDK让这变得非常简单，有一个代理方法正可以处理这种情况： 
    
    
    func application(application: UIApplication, didReceiveLocalNotification notification: UILocalNotification) {
        // Do something serious in a real app.
        println("Received Local Notification:")
        println(notification.alertBody)
    }

当然在某些情况下在App运行时你并不需要处理通知。但是在另外一个情况下，上面的代理方法是处理通知动作的地方。 

现在让我们来看看当用户点击了一个通知动作按钮后将会调用的代理方法。更具我们给动作设置的标示符（identifier），我们决定那个动作被调用，然后App就会执行对应的代码了。我们会有三种动作： 

  1. 简单地让通知消失（标示符：justInform）。 

  2. 添加一个新的物品（标示符：editList）。 

  3. 删除整个物品清单（标示符：trashAction）。 

从上面我们看出，我们不需要对第一个动作做任何事情。但是我们需要处理另外两种动作。我们将根据identifier的值给每一种情况发送一个 NSNotification，在ViewController类中，我们监视这些NSNotification，然后我们处理他们。 

让我们从新的代理方法开始： 
    
    
    func application(application: UIApplication, handleActionWithIdentifier identifier: String?, forLocalNotification notification: UILocalNotification, completionHandler: () -> Void) {
    
        if identifier == "editList" {
            NSNotificationCenter.defaultCenter().postNotificationName("modifyListNotification", object: nil)
        }
        else if identifier == "trashAction" {
            NSNotificationCenter.defaultCenter().postNotificationName("deleteListNotification", object: nil)
        }
    
        completionHandler()
    }

在上述几种情况中我们根据动作的的标示符，发送不同名称的NSNotification对象。注意到，我们在方法的结束调用了 completionHandler()方法，根据规定我们必须调用它，这样系统才能知道我们已经处理完了通知动作。在处理本地通知时，这个代理方法非常 重要，在这里你通过用户的点击执行相应地代码。 

接下来，让我们打开ViewController.swift文件。首先，让我们监视我们之前发送的NSNotification。在viewDidLoad中加入下面的代码： 
    
    
    override func viewDidLoad() {
        ...
    
        NSNotificationCenter.defaultCenter().addObserver(self, selector: "handleModifyListNotification", name: "modifyListNotification", object: nil)
        NSNotificationCenter.defaultCenter().addObserver(self, selector: "handleDeleteListNotification", name: "deleteListNotification", object: nil)
    }

modifyListNotification()和deleteListNotification()方法都是我们自定义的方法，我们接下来会实现他们。 

首先我们实现第一个方法。因为App是通过用户点击了编辑物品动作启动的，所以我们需要将textfield控件设置为第一响应。完成此任务，只需加入一行代码： 
    
    
    func handleModifyListNotification() {
        txtAddItem.becomeFirstResponder()
    }

通过这行代码，键盘会自动展现然后用户就能立即添加一个新的物品了。 

通过删除清单按钮，我们希望从物品对象数组移除所有的物品。接下来，我们首先移除shoppingList数组中得所有对象，然后将它（空数组）保存到磁盘。最后我们重新加载tableview的数据，这样的话，当用户启动App时就什么物品都看不到了。 
    
    
    func handleDeleteListNotification() {
        shoppingList.removeAllObjects()
        saveShoppingList()
        tblShoppingList.reloadData()
    }

有了上面的代码实现，我们这个示例程序现在终于完成啦！ 

##  启动示例App 

是时候测试一下我们的App了，首先在模拟器或者真机中启动它。添加一些物品，然后安排一个本地通知。为了避免等待太久时间，安排他在1到2分钟之后被推送，然后退出App。下面的图片模拟了上述的几个操作，和通知在不同的情况被推送的样子。 

** 添加一个新的物品到清单: **

![](http://api.cocoachina.com/uploads/image/20150112/1421048516542677.png)

** 安排一个本地通知: **   


![](http://api.cocoachina.com/uploads/image/20150112/1421048515417927.png)

** banner形式展现通知，查看动作（minimal context）： **

![](http://api.cocoachina.com/uploads/image/20150112/1421048515194568.png)

** alert形式展现通知，所有动作（default context）： **

![](http://api.cocoachina.com/uploads/image/20150112/1421048517954153.png)

** 在通知中心展示通知（minimal context）： **

![](http://api.cocoachina.com/uploads/image/20150112/1421048517698634.png)

为了在banner和alert之间切换，在你的设备中打开设置App。找到Shopping Alert选项，点击进入。 

![](http://api.cocoachina.com/uploads/image/20150112/1421048517750752.png)

在下图标记的地方，根据你希望通知展示的样子选择alert或者banner。 

![](http://api.cocoachina.com/uploads/image/20150112/1421048517509096.png)

退出设置App，安排一个新的本地通知，这样你就能你选择的结果了。 

##  总结 

在iOS8当中，通知看起来更好用了，用户现在甚至可以直接处理通知而不用启动App。在本篇文章中我们提到了几个新的概念，有新也有旧。重要的 是，现在设置通知的类型、动作和类目都十分简单方便，如果你的App需要通知，那就使用他们吧！正如我在介绍中所说，还有另外几种通知，如远程和地点。尽 管我们没有去实现他们，在知道了本地通知是如何工作了之后，你也会知道如何实现其他通知的大致路径了。以后你只需要去搜索他们的实现具体细节。好了，上面 所有就是我敬献给你的，静下来好好思考一下。玩得开心！ 

你可以从 [ 这里 ](https://github.com/iBenjamin/ShoppingAlertFinal) 下载完整的项目以供参考。   
（本文为CocoaChina组织翻译，本译文权利归译者所有，未经允许禁止转载。） 
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/42913175](http://blog.csdn.net/pleasecallmewhy/article/details/42913175)