#  [ [iOS]通过JS调用iOS函数时的URL编码问题 ](/pleasecallmewhy/article/details/29842745)

在前面的文章： [ [iOS]在WebApp中如何使用JS调用iOS的函数 ](http://blog.csdn.net/pleasecallmewhy/article/details/28403347) 中，提到了如何使用JS通过修改URL调用iOS的内部函数。 

  


其中会遇到一个问题，就是编码问题，比如通过URL调用弹窗，在里面写上内容：你好汪海。 

  


那链接大概就是这样的：http://xxx.com#ios?action=alert&param=你好汪海 

  


但是在iOS中接收到的时候会出现中文的乱码： 

http://xxx.com#ios?action=alert&param=%25E6%2596%2587%25E4 

遇到这个问题主要是URL在转化中的编码问题，解决方案感谢这篇博文： [ iOS中的编码问题 ](http://blog.csdn.net/flyter/article/details/7540918) 。 

  


将转码函数封装： 

** **
    
    
    // 将URL编码
    - (NSString *)encodeToPercentEscapeString: (NSString *) input
    {
        NSString *outputStr = (NSString *) CFBridgingRelease(CFURLCreateStringByAddingPercentEscapes(kCFAllocatorDefault,
                                                (CFStringRef)input,
                                                NULL,
                                                (CFStringRef)@"!*'();:@&=+$,/?%#[]",
                                                kCFStringEncodingUTF8));
        return outputStr;
    }
    
    // 将URL解码
    - (NSString *)decodeFromPercentEscapeString: (NSString *) input
    {
        NSMutableString *outputStr = [NSMutableString stringWithString:input];
        [outputStr replaceOccurrencesOfString:@"+"
                                   withString:@" "
                                      options:NSLiteralSearch
                                        range:NSMakeRange(0, [outputStr length])];
        
        return [outputStr stringByReplacingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
    }

  


  


演示一下上面的封装函数： 
    
    
        NSString * testUrl = @"http://search.google.com?keywords=($# it's {a*123})00!*'();:@&=+$,/?%#[]";
        NSLog(@"original: %@", testUrl);
    
    
        NSString * encodeStr = [self encodeToPercentEscapeString:testUrl];
        NSLog(@"encoded: %@", encodeStr);
        
        NSString * encodeStr2 = [testUrl stringByAddingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
        NSLog(@"encoded2:%@", encodeStr2);
        
        NSString * decodeStr = [self decodeFromPercentEscapeString:encodeStr];
        NSLog(@"decoded: %@", decodeStr);
    

  
  


  


结果如下： 

>> original: http://search.google.com?keywords=($# it's {a*123})00!*'();:@&=+$,/?%#[]   
>> encoded:  http%3A%2F%2Fsearch.google.com%3Fkeywords%3D%28%24%23%20it%27s%20%7Ba%2A123%7D%2900%21%2A%27%28%29%3B%3A%40%26%3D%2B%24%2C%2F%3F%25%23%5B%5D   
>> encoded2: http://search.google.com?keywords=($%23%20it's%20%7Ba*123%7D)00!*'();:@&=+$,/?%25%23%5B%5D   
>> decoded:  http://search.google.com?keywords=($# it's {a*123})00!*'();:@&=+$,/?%#[]   


  


  


  


演示一下自带的URL转码测试代码： 
    
    
      NSString* string1 = @"https://www.cloudsafe.com/文件夹";
        
        NSString* string2 = [string1 stringByAddingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
        
        NSString* string3 = [string2 stringByAddingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
        
        NSString* string4 = [string2 stringByReplacingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
        
        NSString* string5 = [string3 stringByReplacingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
        
        NSString* string6 = [string4 stringByReplacingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
        
        NSString* string7 = [string5 stringByReplacingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
        
        
        NSLog(@"原始数据%@",string1);
        NSLog(@"一层编码%@",string2);
        NSLog(@"两层编码%@",string3);
        NSLog(@"一层编码的一层解码%@",string4);
        NSLog(@"两层编码的一层解码%@",string5);
        NSLog(@"一层编码的两层解码%@",string6);
        NSLog(@"两层编码的两层解码%@",string7);
        

  
  
  


** 打印结果：  **

** **

** 2014-06-10 15:00:02.425 DareWayApp[7400:671651] ** ** 原始数据 ** ** https://www.cloudsafe.com/ ** ** 文件夹 **

** 2014-06-10 15:00:02.426 DareWayApp[7400:671651] ** ** 一层编码 ** ** https://www.cloudsafe.com/%E6%96%87%E4%BB%B6%E5%A4%B9 **

** 2014-06-10 15:00:02.427 DareWayApp[7400:671651] ** ** 两层编码 ** ** https://www.cloudsafe.com/%25E6%2596%2587%25E4%25BB%25B6%25E5%25A4%25B9 **

** 2014-06-10 15:00:02.427 DareWayApp[7400:671651] ** ** 一层编码的一层解码 ** ** https://www.cloudsafe.com/ ** ** 文件夹 **

** 2014-06-10 15:00:02.427 DareWayApp[7400:671651] ** ** 两层编码的一层解码 ** ** https://www.cloudsafe.com/%E6%96%87%E4%BB%B6%E5%A4%B9 **

** 2014-06-10 15:00:02.427 DareWayApp[7400:671651] ** ** 一层编码的两层解码 ** ** https://www.cloudsafe.com/ ** ** 文件夹 **

** 2014-06-10 15:00:02.427 DareWayApp[7400:671651] ** ** 两层编码的两层解码 ** ** https://www.cloudsafe.com/ ** ** 文件夹 **

  


  


  


  


如果服务器用的是GBK编码，只要把上面的UTF改成下面的encoding就可以了： 
    
    
     NSStringEncoding gbkEncoding = CFStringConvertEncodingToNSStringEncoding(kCFStringEncodingGB_18030_2000);
            urlString = [urlString stringByReplacingPercentEscapesUsingEncoding:gbkEncoding];
          

  
  
  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/29842745](http://blog.csdn.net/pleasecallmewhy/article/details/29842745)