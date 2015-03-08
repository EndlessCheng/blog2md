#  [ 返璞归真，被遗忘的NSUserDefaults ](/pleasecallmewhy/article/details/38386857)

在iOS程序中，有许多种方法来存储数据。 

Core Data，SQlite和UIDocuments都可以使用，但往往用NSUserDefaults来存储数据是一种非常快速和容易的方法。一般都是使用键值对来存储数据，许多开发者忘记了NSUserDefaults一些原始的使用方法，默认设置就是其中一种。 

这里我要介绍的方法是  [ – (void)registerDefaults:(NSDictionary *)dictionary  ](https://developer.apple.com/library/iOS/documentation/Cocoa/Reference/Foundation/Classes/NSUserDefaults_Class/Reference/Reference.html#//apple_ref/occ/instm/NSUserDefaults/registerDefaults:) 。这个方法跟NSUserDefaults中别的方法一样，在iOS2.0开始的时候就有了。 

如下代码我遇到过多次了： 
    
    
    NSUserDefaults *standardDefaults = [NSUserDefaults standardUserDefaults];
    if ([standardDefaults stringForKey:@"favoriteColor"] == nil) {
    [standardDefaults setObject:@"Green" forKey:@"favoriteColor"];
    [standardDefaults synchronize];
    }

上面的代码首先检测一下，某个键是否已经设置值了，如果没有，就设置一个默认值。这样设置之后，在程序中，就可以使用这样 的代码来查询这个值：  [standardDefaults stringForKey:@“favoriteColor”]  ，这样能保证获得一个有效的值。实际上，  registerDefaults:  正是做这样事情的。 

上面的代码完全可以用下面的代码来替换： 
    
    
    NSUserDefaults *standardDefaults = [NSUserDefaults standardUserDefaults];
    [standardDefaults registerDefaults:@{@"favoriteColor": @"Green"}];
    [standardDefaults synchronize];

每次程序启动的时候调用  registerDefaults:  方法都是安全的。完全可以将这个方法的调用放到applicationDidFinishLaunching:方法中. 这个方法永远都不会覆盖用户设置的值。如果之后在程序中用户设置了一个Red值：  [standardDefaults setObject:@“Red” forKey:@“favoriteColor”];  下次程序启动运行registerDefaults: 时，并不会用Green覆盖Red值。 

iOS系统默认已经包含NSUserDefaults接口了。关于NSUserDefaults除了常用的键值存储，还有很多可用接口。理解NSUserDefaults提供的接口，可以写出更好的程序。强烈建议在苹果官网上阅读一下相关更多信息：  [ NSUserDefaults 文档  ](https://developer.apple.com/library/iOS/#documentation/Cocoa/Reference/Foundation/Classes/NSUserDefaults_Class/Reference/Reference.html) 。 

_________________________________________ 

本文由破船译自：  [ doubleencore  ](http://www.doubleencore.com/2013/03/back-to-basics-forgotten-nsuserdefaults/)   
转载请注明出处：  [ BeyondVincent的博客  ](http://www.beyondvincent.com/)   
_________________________________________ 
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/38386857](http://blog.csdn.net/pleasecallmewhy/article/details/38386857)