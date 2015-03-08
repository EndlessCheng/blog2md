#  [ [iOS]在WebApp中如何使用JS调用iOS的函数 ](/pleasecallmewhy/article/details/28403347)

实现功能：点击HTML的标签，通过JS调用iOS内部的原生函数 

  


基本流程： 

![](http://img.blog.csdn.net/20140605094109421?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


先看一下Web中，我们给h1标签添加一个onclick事件，让它在被点击之后，修改当前的url。 

Web中的HTML代码： 
    
    
    <html>
    <head>
    <script>
    
    function getInfo(name)
    {
    	window.location = "/getInfo/"+name;
    }
    
    
    </script>
    
    </head>
    
    <body>
    	<h1 onclick="getInfo('why')">Name</h1>
    </body>
    
    </html>

  


  


  


iOS中，先拖拽WebView，访问localhost，然后通过WebView的委托事件监听url跳转操作，并且把跳转截取下来。 

也就是说，在onclick的时候，普通浏览器灰跳转到那个url，但是在iOS的这个WebView里面，这个跳转会被拦截， 

用这种方式可以巧妙地实现JS调用iOS的原生代码： 

  

    
    
    //
    //  DWViewController.m
    //  DareWayApp
    //
    //  Created by why on 14-6-3.
    //  Copyright (c) 2014年 DareWay. All rights reserved.
    //
    
    #import "DWViewController.h"
    
    @interface DWViewController ()
    
    @property (weak, nonatomic) IBOutlet UIWebView *myWebview;  // 主页面
    
    @end
    
    @implementation DWViewController
    
    - (void)viewDidLoad
    {
        [super viewDidLoad];
    	// Do any additional setup after loading the view, typically from a nib.
        
        
        
        // 适配iOS6的状态栏
        if ([[[UIDevice currentDevice] systemVersion] floatValue] >= 7) {
            _myWebview.frame =  CGRectMake(0,20,self.view.frame.size.width,self.view.frame.size.height-20);
        }
        
        
        // 加载制定的URL
        NSURL *url =[NSURL URLWithString:@"http://localhost"];
        NSURLRequest *request =[NSURLRequest requestWithURL:url];
        [_myWebview setDelegate:self];
        [_myWebview loadRequest:request];
    
    }
    
    // 网页中的每一个请求都会被触发
    -(BOOL)webView:(UIWebView *)webView shouldStartLoadWithRequest:(NSURLRequest *)request navigationType:(UIWebViewNavigationType)navigationType
    {
          
        // 每次跳转时候判断URL
        
        if([request.mainDocumentURL.relativePath isEqualToString:@"/getInfo/why"])
        {
            NSLog(@"why");
            return NO;
        }
        
        
        return YES;
    }
    
    - (void)didReceiveMemoryWarning
    {
        [super didReceiveMemoryWarning];
        // Dispose of any resources that can be recreated.
    }
    
    @end
    

  
  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/28403347](http://blog.csdn.net/pleasecallmewhy/article/details/28403347)