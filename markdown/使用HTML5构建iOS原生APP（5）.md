#  使用HTML5构建iOS原生APP（5） 

[ Yuguo ](http://yuguo.us) 2013年 04月 10日 

我的app基本上是由一个原生的navigation controller贯穿全局，然后在每一个scene中都有一个主要的 ` UIWebView ` 作为主要逻辑： 
    
    
    - (void)viewDidLoad{
    	...
    	self.webView = [[UIWebView alloc] initWithFrame:CGRectMake(.0f, 0.f, self.view.bounds.size.width, self.view.bounds.size.height -44)];//-44是减去标题栏高度
    	self.webView.delegate = self;
    	...
    	[self.view addSubview:self.webView];
    	
    }
    

现在的问题是，当手机翻转的时候，webView的大小不会重绘，就会出现bug，解决办法很简单，就是实现翻转委托： 
    
    
    - (void)didRotateFromInterfaceOrientation:(UIInterfaceOrientation)fromInterfaceOrientation {
        	NSLog(@"I have finished rotating");
    	self.webView.frame = CGRectMake(.0f, 0.f, self.view.bounds.size.width, self.view.bounds.size.height));
    }
    

就可以了，然后在webView中做好宽度自适应： 
    
    
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scable=0, minimun-scale=1.0, maximum-scale=1.0">
    

##  备注 

介绍一下view的三种坐标属性： 

Frame A view’s frame (CGRect) is the position of its rectangle in the superview’s coordinate system. By default it starts at the top left. 

Bounds A view’s bounds (CGRect) expresses a view rectangle in its own coordinate system. 

Center A center is a CGPoint expressed in terms of the superview’s coordinate system and it determines the position of the exact center point of the view. 
#### 原文：[http://yuguo.us/weblog/iphone-rotation-webview/](http://yuguo.us/weblog/iphone-rotation-webview/)