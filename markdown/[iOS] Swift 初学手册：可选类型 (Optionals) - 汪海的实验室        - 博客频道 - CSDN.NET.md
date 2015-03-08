#  [ [iOS] Swift 初学手册：可选类型 (Optionals) ](/pleasecallmewhy/article/details/39523701)

[ Swift ](http://www.csdn.net/tag/Swift) [ iOS ](http://www.csdn.net/tag/iOS)

原文地址： [ http://blog.callmewhy.com/2014/09/23/beginners-guide-optionals-swift/ ](http://blog.callmewhy.com/2014/09/23/beginners-guide-optionals-swift/)

几周前 (译者注：原文发表于6月24日)，苹果发布了一个全新的编程语言： Swift 。从那时起，我一直在阅读 [ Swift 官方手册 ](https://itunes.apple.com/us/book/swift-programming-language/id881256329?mt=11) ，并且在 Xcode6 beta 上 <del> 把玩 </del> 学习。我开始喜欢上了 Swift 的简洁和语法。我和我的团队一起学习这门全新的语言，并且将它和 Objective-C 这个有着30年历史的老伙计进行对比。同时，我们也在努力探索如何能让初学者们轻松的掌握 Swift 。 

两周前，我们发布了 [ Swift 基础教程 ](http://www.appcoda.com/swift-programming-language-intro/) ，在接下来的几周里，我们将会写一系列的教程来介绍 Swift 的新特性。这一周，让我们来看看可选类型 (Optionals)。 

![](http://www.appcoda.com/wp-content/uploads/2014/06/swift-optionals-featured.jpg)

##  概述 

在前面的教程里我有提及可选类型的概念，但是没有深入讲解。 

那么，什么是可选类型？ 

在 Swift 中，当我们声明一个变量的时候，默认情况下是 非可选类型 (non-optional) ，也就是说，你必须指定一个不为 nil 的值。如果你硬是要把一个非可选类型的变量设为 nil ，那么编译器就会告诉你：“嘿你不能把它设置成 nil 好嘛”。没错就是这样： 
    
    
    var message: String = "Swift is awesome!" // OK
    message = nil // compile-time error
    

当然编译器给出的错误消息可就没这么友善了，一般会显示 ` Could not find an overload for ‘__conversion’ that accepts the supplied arguments ` 这种错误。同样，在类中声明的变量也是这样，默认情况下是费可选类型的： 
    
    
    class Messenger {
        var message1: String = "Swift is awesome!" // OK
        var message2: String // compile-time error
    }
    

在 ` message2 ` 处你会得到一个编译错误，因为它没有初始值。对于那些从 Objective-C 一路走来的小伙伴们可能会感觉很意外，在 Objective-C 里这种情况根本就不会有问题好嘛： 
    
    
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

为什么要这么设计呢？苹果官方给出的解释是，因为 Swift 是一门类型安全的语言。从前面的例子中可以看出， Swift的可选类型会进行编译检查，防止一些常见的运行时错误。让我们看一看下面的例子，这样可以更好地理解。 

比如说，在 Objective-C 中有如下代码： 
    
    
    - (NSString *)findStockCode:(NSString *)company {
        if ([company isEqualToString:@"Apple"]) {
            return @"AAPL";
        } else if ([company isEqualToString:@"Google"]) {
            return @"GOOG";
        }
    
        return nil;
    }
    

在上面的方法里，你可以用 ` findStockCode ` 方法来获取到股票的代码，显然只有 Apple 和 Google 的查询会返回值，其他情况都会返回 nil 。 

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
    

在上面的代码里， ` stockCode ` 被定义成了可选类型，这意味着它可以有一个 string 的值，也可以为 nil 。代码无法通过编译，会提示一个错误： ` value of optional type String? is not unwrapped ` 。 

正如你在例子中看到的，Swift 的可选类型加强了 nil 检测，为开发者提供了编译时的检查，合理的使用可选类型可以有效地提高代码质量。 

##  强制解析 

慢着慢着，前面说了那么多好处，但是代码还是没通过编译啊！别急，我们需要检测一下 ` stockCode ` 是否为 nil ，把代码做如下修改： 
    
    
    var stockCode:String? = findStockCode("Facebook")
    let text = "Stock Code - "
    if stockCode {
        let message = text + stockCode!
        println(message)
    }
    

和 Objective-C 中类似，我们先对它进行检测，看看它是不是有值。如果不为 nil ，我们可以在后面加上一个感叹号 ` ! ` 进行解析，这样 Xcode 就知道：“嗯我可以使用这个值了”。在 Swift 里我们称之为 强制解析 (forced unwrapping) ，通过感叹号强制获取可选类型的真实值。 

再回到上面的代码中。我们只是在强制解析之前，检测了一下看看变量是否为 nil 而已。这和 Objective-C 中常见的 nil 检测也没啥区别啊。如果我忘了检测呢？看下下面的代码： 
    
    
    var stockCode:String? = findStockCode("Facebook")
    let text = "Stock Code - "
    let message = text + stockCode!  // runtime error
    

这样我们不会得到编译错误，因为我们用了强制解析，编译器已经假定这个可选类型肯定有值。显然这样是错误的，运行的时候会得到如下错误： 
    
    
    fatal error: Can’t unwrap Optional.None
    

##  可选绑定 

除了强制解析，可选绑定 (optional binding) 是一个更值得推荐的解析方案。 你可以用可选绑定来检测一个可选类型的值有没有值，如果有值则解析出来并存储到一个临时的变量里。 

废话少说，放码过来！让我们来看看下面这个使用了可选绑定的示例代码： 
    
    
    var stockCode:String? = findStockCode("Facebook")
    let text = "Stock Code - "
    if let tempStockCode = stockCode {
        let message = text + tempStockCode
        println(message)
    }
    

代码中的 ` if let ` (或者 ` if var ` ) 是可选绑定的两个关键词。翻译成人类语言，大概是这个样子：“如果 ` stackCode ` 它有值，把它的值存到 ` tempStackCode ` 里，然后继续执行接下来的代码块。如果它没值，跳过后面的代码块。” 因为 ` tempStockCode ` 是一个新的常量，所以你不再需要添加 ` ! ` 后缀。 

你可以把方法调用放在 ` if ` 里，这样代码看起来更简洁： 
    
    
    let text = "Stock Code - "
    if var stockCode = findStockCode("Apple") {
        let message = text + stockCode
        println(message)
    }
    

这里， ` stockCode ` 不再是可选类型，我们可以直接使用。如果 ` findStockCode ` 方法返回了 nil 则会跳过后面的代码块。 

##  可选链 

在解释可选链之前，我们先对原始代码做一些小小的修改。我们创建一个新的类叫做 ` Stock ` ，它有 ` code ` 和 ` price ` 两个可选类型的属性。 ` findStockCode ` 函数用来返回一个 ` Stock ` 对象，而不是一个 ` String ` 对象： 
    
    
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
    

可选链提供了访问变量的另一种方式，代码现在看上去也更加的干净整洁。上面只是一个基础的使用，更加深入的学习可以参考 [ 官方文档 ](https://developer.apple.com/library/ios/documentation/swift/conceptual/swift_programming_language/OptionalChaining.html) 。 

##  Swift 和 Objective-C 的交互 

Swift 中的可选类型十分强大，尽管可能一开始的时候需要花点时间慢慢熟悉。可选类型让你的代码更清晰，而且可以避免一些 nil 引起的问题。 

Swift 有设计与 Objective-C 交互的 API，当我们需要和 UIKit 或者其他框架的 API 交互的时候，你肯定会遇到可选类型。下面列举一些 UITableView 中可能会遇到的可选类型： 
    
    
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

对于一名开发者来说，理解可选类型的工作原理是十分必要的。这也就是为什么我们专门写一篇文章来介绍可选类型。它可以帮助开发者在编译阶段就发现隐藏的问题，从而避免运行时错误。当你习惯了这种语法，你将会愈发欣赏可选类型的魅力所在。 

享受这个美好的世界吧。真棒。( <del> 没错这句也是我乱加的 </del> ) 

* * *

原文地址 

  * [ A Beginner’s Guide to Optionals in Swift ](http://www.appcoda.com/beginners-guide-optionals-swift/)
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/39523701](http://blog.csdn.net/pleasecallmewhy/article/details/39523701)