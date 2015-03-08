#  [ [iOS]NSURLConnection的一个小例子 ](/pleasecallmewhy/article/details/43267359)

直接上代码了。。。 

  


在iOS7之后可以使用NSURLSession，但是考虑到兼顾iOS6还是使用NSURLConnection。 

  


  

    
    
    @interface ViewController() <NSURLConnectionDataDelegate>
    @property (nonatomic,strong) NSMutableData *receivedData;
    @end
    
    @implementation ViewController
    
    - (void)viewDidLoad {
        [super viewDidLoad];
    
        NSURLRequest *theRequest = [NSURLRequest requestWithURL:[NSURL URLWithString:@"http://www.baidu.com"]
                                                    cachePolicy:NSURLRequestUseProtocolCachePolicy
                                                timeoutInterval:10.0];
    
        NSURLConnection *theConncetion=[[NSURLConnection alloc] initWithRequest:theRequest delegate:self];
    
        if (theConncetion) {
            _receivedData = [NSMutableData data];
        }
    
    }
    
    -(void)connection:(NSURLConnection *)connection didReceiveData:(NSData *)data {
        [_receivedData appendData:data];
        NSLog(@"Downloading...");
    }
    
    -(void)connectionDidFinishLoading:(NSURLConnection *)connection {
        NSLog(@"Finished");
    }
    
    @end
    

  


也可以直接用Block发个异步请求： 
    
    
        [NSURLConnection sendAsynchronousRequest:theRequest queue:[NSOperationQueue mainQueue] completionHandler:^(NSURLResponse *response, NSData *data, NSError *connectionError) {
            NSLog(@"Finished");
        }];

  
  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/43267359](http://blog.csdn.net/pleasecallmewhy/article/details/43267359)