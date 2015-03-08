#  Objective-C中的“委托（delegate）”和“协议（protocal）”

[ Yuguo ](http://yuguo.us) 2012年 10月 22日

委托是Objective-C中最常用的一种回调机制。大部分情况下，“协议”的用法是跟“委托”同义的，所以本文一起来讲。

委托是一个指向一个对象的指针，该对象有一系列方法，该对象的委托人（另一个对象）非常清楚这些方法，并且会在某些事件发生的时候调用这些方法。简单的说，这是一种机
制，允许后创建的对象（later-created object）来调用 _ 特定的回调函数 _ 。

一个简单的例子是 [ UIAlertView ](http://developer.apple.com/library/ios/#documentation
/uikit/reference/UIAlertView_Class/UIAlertView/UIAlertView.html) （没有编辑器写长类名真不习
惯），你创建一个UIAlertView的实例来显示一个对话框，用户会点击OK或者Cancel，那么对话框得知哪个按钮被点击之后，它需要告诉你这一信息（调用你
的方法），但它不知道调用哪个对象，调用哪个方法。

解决办法就是把self指针发送给UIAlertView作为一个委托对象（ _ 以此告诉它调用哪个对象 _
），作为交换，你同意实现（implement）一些UIAlertView知道的方法（称为协议， _ 以此告诉它调用哪些方法 _
），这样UIAlertView对象就知道调用你的某某方法。如何实现这些方法呢？在你对象的头文件中声明UIAlertViewDelegate即可。

这些方法可能是：alertView:clickedButtenAtIndex:

那么UIAlertView的第一个按钮被按下之后，它就直接调用它的委托对象的clickedButtenAtIndex方法。

委托方法通常包括3种动词：should、will、did。

should表示一个动作发生前，通常带有返回值，可以在动作发生之前改变对象状态。

will在动作发生前，委托可以对动作做出响应，但不带有返回值。

did在动作发生后做出的响应。

从方法的定义我们不难看出委托模式能够起到两方面的作用：

第一：委托协助对象主体完成某项操作，将需要定制化的操作通过委托对象来自定义实现，达到和子类化对象主体同样的作用。

第二：事件监听，委托对象监听对象主体的某些重要事件，对事件做出具体响应或广播事件交给需要作出响应的对象。

[ 《众妙之门3》——第一章：重新设计的商业思考 → ](/weblog/the-business-side-of-redesign/) [ ←
《众妙之门3》译后感 ](/weblog/smashing-book-3-translate/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

