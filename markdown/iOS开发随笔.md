#  iOS开发随笔

[ Yuguo ](http://yuguo.us) 2012年 12月 14日

随意记录一下一些经验，对新手可能有帮助。

##  数组NSArray

操作数组的时候计算数组包含的对象个数是：

    
    
    [dataArray count]

获取索引处的对象

    
    
    [dataArray objectAtIndex:2]

删除指定索引处对象

    
    
    [dataArray removeObjectAtIndex:1];

##  词典NSDictionary

获取对应key的object：

    
    
    - (id)objectForKey:(id)aKey

##  类方法和实例方法

在类方法中调用类方法

    
    
    + (void)classMethodB { 
    
    
    // ... 
    
    
    [self classMethodA]; 
    
    
    // ... 
    
    
    }

在实例方法中调用类方法

    
    
    - (void)instanceMethodB { 
    
    
    // ...
    
    
     [[self class] classMethodA];
    
    
    // ...
    
    
    }

##  NSLog

用NSLog记录debug数据，是一个很常用的方法。

    
    
    NSLog(@"String"); NSLog(@"%@",someString); NSLog(@"%d",someInteger); NSLog(@"my float is %f",someFloat);

##  tag

在运行时获取某些视图可以用方法

    
    
    - (UIView *)viewWithTag:(NSInteger)tag

在storyboard中可以看到所有视图的默认tag都是0，可以改成特定的值，比如1。

如果要获得某个视图里的tag为某值的子视图，可以用这个自定义类方法

    
    
    +(UIView*) getSubViewInViewWithTag:(UIView*)view withTag:(NSInteger)tag { for (UIView *subview in view.subviews) { if(subview.tag==tag) return subview; } return nil; }

##  indexPath转成整数？

在委托tableView或者collectionView的时候，需要实现的方法比如：

    
    
    - (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath

有一个参数是NSIndexPath，用来表示绘制第几个表格或者collectionCell，我需要得到它的整数值以便跟我自己的数据数组对应，方法很简单

    
    
    indexPath.row

##  自己释放内存的图片

以下代码不会产生内存泄漏，因为这个newImage是一个自释放内存的图片。

    
    
    UIImage *newImage = [UIImage imageNamed:@"sampleImage"]; [yourImageView setImage:newImage];

-imageNamed: returns an autoreleased image, which, as deanWombourne says, will be autoreleased at some time in the future (the exact time is undefined). 

但是如果图片在其他地方生成，在这里使用，那么可能需要手动释放内存。

[ iOS开发随笔-2 → ](/weblog/ios-develop-2/) [ ← 香港设计营商周论坛 ](/weblog/bodw-2012/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

