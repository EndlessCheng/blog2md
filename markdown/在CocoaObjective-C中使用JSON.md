#  在Cocoa/Objective-C中使用JSON

[ Yuguo ](http://yuguo.us) 2012年 10月 16日

我在做一个参考类的APP，因为经常有数据需要更新，而我又不希望以更新APP版本的方式来进行，所以首先想到的就是与服务器端通信，通信的格式当然就是JSON了，
我在服务器端可以有非常方便的方法创建JSON，而在APP端也可以非常方便地把JSON转成原生对象（NSDictionary或者NSArray）。

stig的开源JSON框架是一个非常易用的框架，它可以把任何JSON字符串转化成原生Objective-C对象。这个开源项目包含的文件有打包好的框架、Mac
和iPhone的SDK、还有源代码。最简单的使用这个框架的方法就是直接把源代码引入你的APP，因为它十分轻量。

1\. [ 下载 ](https://github.com/stig/json-framework)
2.把下载来的文件解压，把Classes文件夹拖到xcode中，选择Copy items into destination group’s folder
(if needed)。

3.源码引入你的项目中后，你需要import到你的代码中：

    
    
    #import "SBJson.h"

4.以下是一个有名值对的JSON字符串，所以转化成了NSDictionary。

    
    
    NSString *someJSONDemo = @"{\"name\":\"yuguo\"}";
    
    NSLog(@"The name is : %@",[(NSDictionary *)[someJSONDemo JSONValue] objectForKey:@"name"]);

5.如果需要把NSDictionary或者NSArray转化成JSON字符串：

    
    
    [obj JSONRepresentation]

[ 《众妙之门3》译后感 → ](/weblog/smashing-book-3-translate/) [ ← 学习iOS开发——一些经验
](/weblog/learning-ios/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

