#  使用HTML5构建iOS原生APP（2） 

[ Yuguo ](http://yuguo.us) 2013年 03月 12日 

有时候我们在内嵌的webview中希望点击一个链接之后，触发iOS原生事件，而不是webview内页面跳转（因为webview的跳转很生硬，而ajax+js模拟则不如原生segue平滑）。 

有时候我们希望在页面内 ` consloe.log('log something') ` 的时候在控制台里看到输出，但手机里没有控制台，所以我们希望可以利用xcode的控制台输出信息。 

因为iOS没有提供API让我们直接用html或者js来跟外部交互，所以我们必须用另外一种巧妙的办法来实现这两个功能。这种方法可以满足我们两种需求。 

##  console.log 

在html页面中重新定义 ` console.log ` : 
    
    
    <script>
    // Debug
    console = new Object();
    console.log = function(log) {
    	var iframe = document.createElement("IFRAME");
    	iframe.setAttribute("src", "ios-log:#iOS#" + log);
    	document.documentElement.appendChild(iframe);
    	iframe.parentNode.removeChild(iframe);
    	iframe = null;
    }
    console.debug = console.log;
    console.info = console.log;
    console.warn = console.log;
    console.error = console.log;
    </script>
    

然后在需要捕获的viewController.m中实现协议： 
    
    
    - (BOOL)webView: (UIWebView *)webView shouldStartLoadWithRequest:(NSURLRequest *)request navigationType:(UIWebViewNavigationType)navigationType{
    
        NSString *requestString = [[[request URL] absoluteString] stringByReplacingPercentEscapesUsingEncoding: NSUTF8StringEncoding];
    	//NSLog(requestString);
    
    	if ([requestString hasPrefix:@"ios-log:"]) {
        	NSString* logString = [[requestString componentsSeparatedByString:@":#iOS#"] objectAtIndex:1];
        	NSLog(@"UIWebView console: %@", logString);
        	return NO;
    	}
    	return YES;
    }
    

当然前提是webView需要把委托设定为当前控制器： 
    
    
    self.webView =[[UIWebView alloc] initWithFrame:CGRectMake(0.0f,0.0f,self.view.bounds.size.width,self.view.bounds.size.height-44)];
    self.webView.delegate=self;
    

原理很简单，我们重新定义了 ` console.log ` 函数，还有 ` console.debug ` ， ` console.info ` ， ` console.warn ` ， ` console.error ` 。当我们在页面js中调用 ` console.log ` 的时候，就会创建一个iframe发出请求，请求的协议为 ` ios-log: ` ，路径就是我们的log字符串。发出请求之后，迅速把这个iframe清理掉。 

这样，在webview中我们发出了一个请求，然后就没了。外部我们用objective-c实现了一个协议，就是webview开始发出请求之前就会调用的函数。在这个函数中我们过滤所有的请求（因为除了 ` ios-log ` ，还有一些“正常”的请求比如http和mailto），当前缀为 ` ios-log ` 的时候，我们就 ` NSLog ` 即可。 

` if ` 最后的 ` return NO ` 的意思是该webview的请求被捕获，不再请求（这个实际上不存在的页面）。我们希望一些合法请求（比如http、mailto等）不被捕获，所以最后 ` if ` 外面丢了一个 ` return YES ` 。 

##  利用链接触发场景变换 

iOS原生的场景变换叫做segue，xcode为我们内置了几种原生动画，比如导航条总是固定在上面的push，这样页面前后推动的时候，导航条保持不变（当然里面的内容可以变），内容的切换也很流畅。segue还可以在interface builder中设置动画效果，包括全屏翻转或者渐进等。 

![](/files/2013/03/segue.png)

有一些第三方js库可以让我们在webview中模拟这种场景变换，也就是说用css设计一个导航条放在webview中置顶，然后用js或者css3来模拟push或者flip3d的效果。比如iScroll是模拟顶部和底部固定的，jQtouch（这个要翻墙搜索）是模拟push和flip3d效果的。 

我强烈反对在原生应用中使用js库来实现场景变换动画，因为非常不流畅、不跟手指、动画效果跟原生不同，还有最后一个原因，我们是可以在webview中触发外部场景变换的，原生的！用html5制作流畅的原生app的关键就是能够方便地调用原生接口的功能或者效果我们都用原生的，而不去用笨拙的方法实现。 

webview中的代码： 
    
    
    <a href="myapp://somepagename">一个按钮</a>
    

非常简单，myapp这个协议你可以自己随便命名，稍后我们会在objective-c中捕获它。 

还是要实现该webview的委托controller的协议方法，如果你已经定义这个方法了（就像上面那个例子），你只需要在方法体里加入方法体里面的内容，否则会提醒你重复定义。 
    
    
    - (BOOL)webView: (UIWebView *)webView shouldStartLoadWithRequest:(NSURLRequest *)request navigationType:(UIWebViewNavigationType)navigationType{
    
    	NSURL *url = [request URL];
    	if ( [[url scheme] isEqualToString:@"myapp"] )
    	{
        	NSString *slug = [url path];
        	[self performSegueWithIdentifier:@"heroSegue" sender:slug];
        	return NO;
    	}
    	return YES;
    }
    

另外我在interface builder中已经拖拽了一个新的控制器，在新的控制器跟导航控制器之间，我直接拖了一个segue，命名id为 ` heroSegue ` ，所以这里可以用 ` performSegueWithIdentifier ` 来调用segue。 

现在，还是在本controller中，我们实现另一个委托方法： 
    
    
    /*
     * 页面转换时触发
     */
    - (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    	if ([segue.identifier isEqualToString:@"heroSegue"]) {
        	NSLog(@"%@",sender);
        	[self.webView stopLoading];
        	YUGHeroDetailViewController *destViewController = segue.destinationViewController;
        	destViewController.heroSlug = (NSString *)sender;
    	}
    }
    

也就是说，发生segue变化之前，就会执行这一方法，首先判断identifier是不是等于heroSegue，如果是，自己的webview不再载入，目标控制器（也就是即将切换过去的子页面的控制器）中设置公有属性heroSlug的值。 

然后，我们在目标页面的controller的H中定义： 
    
    
    @property (strong) NSString *heroSlug;
    

最后，在目标页面中，我们定义的congroller中的M能拿到heroSlug这个参数。 
    
    
    NSLog(@"%@",self.heroSlug);
    

这样就可以了，拿到slug之后，我们实际上就可以调用一个本地页面，带上slug参数，然后通过ajax的方式读取远程页面或者json数据，这个就不属于本文内容了。 

如果你是新手，在做上面的这些操作的时候可能会漏掉一两个步骤，编辑器会报错，这时候仔细阅读并校对你的代码。如果实在不行，说明清楚操作和报错信息，再给我留言。 

练习题：原生title的好处是它在字符数较短时是居中的，而字符更长一点时会偏右显示，更长一些时显示省略号。那么webview载入一个ajax数据的页面的时候，如何在页面载入成功时，设置原生title？ 

提示，还是自定义协议。 
#### 原文：[http://yuguo.us/weblog/webview-connect-with-ios/](http://yuguo.us/weblog/webview-connect-with-ios/)