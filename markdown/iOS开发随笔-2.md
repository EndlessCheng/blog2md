#  iOS开发随笔-2

[ Yuguo ](http://yuguo.us) 2012年 12月 18日

##  关于segue

segue就是在storyboard中描述两个场景（scene）的过渡关系的一个对象。

比如在tableview和collectionview中常见的一种模式就是点击列表页中的一项之后“跳转”到详情页，这个“跳转”的逻辑和动画就是一个segue
，实现方法也很简单，再tableview或者collectionview中实现prepareForSegue:sender方法即可，代码示例： [
https://gist.github.com/f0cd3f56050c30fc4a40
](https://gist.github.com/f0cd3f56050c30fc4a40)
第一步，我们需要知道被点击的条目的一些信息，比如是第几个tableCell被点击了，或者第几个collectionCell被点击了：

tableCell：

    
    
    // get the selected index
    
    NSInteger selectedIndex = [[self.tableView indexPathForSelectedRow] row];

collectionCell

    
    
    NSInteger *selectedIndex = [[[self.collectionView indexPathsForSelectedItems] objectAtIndex:0] row];

第二步，基本上我们还需要传递一些数据给详情页，告诉详情页是第几个条目被点击了，这个条目上的一些信息是啥，可以使用这个模式：

    
    
    DetailViewController *detailViewController = [segue destinationViewController]; //获取目标控制器 detailViewController.image = image; //数据传递

##  关于数组

数组有两种，一种是不可变的NSArray，另一种是可变的NSMutableArray。

对于NSArray，只能存储objective-c对象，而不能存储c语言中的基本数据类型，如int，float，或者NSArray中的随机指针。同时你不能用
NSArray来存储nil。因为他要用nil放在最末尾，来代表结束，下面的例子你会看到。

    
    
    NSArray * array;
    
    array = [NSArray arrayWithObjects: @"one", @"two", @"three", nill];
    
    for(int i=0; i<[array count]; i++)
    
    {
    
        NSLog(@"index %d has %@.", i , [array objectAtIndex: i ]);
    
    }

NSArray创建的是不可变数组，一旦你用特定数量的对象创建了一个数组，那么他就固定下来了：你既不能添加也不能删除人和元素。当然，数组中的对像是可以改变的，
但数组对象一直不变。

NSMutableArray是NSArray的补充类，他所创建的是一个可变数组，可以随意的添加和删除数组中的元素。NSMutableArray通过方法arr
ayWithCapacity来创建新的可变数组，但这里的数组容量只是一个参考，不会真的限制数组的大小，它是为了能够对代码进行优化而存在的，也不会预写入数组。

    
    
    NSMutableArray * array;
    
    array = [NSMutableArray arrayWithCapacity:9];
    
    for (int i=0; i<4; i++){
    
        Tire * tire = [Tire new];
    
        [array addObject: tire];
    
    }
    
    [array removeObjectAtIndex:1]

NSMutableArray使用addObject: 来在末尾添加对象；用removeObjectAtIndexx:
来删除指定索引处的对象，删除对象后，被删除对象后面的数组元素被前移来填补空缺。

[ 2012总结 → ](/weblog/2012-end/) [ ← iOS开发随笔 ](/weblog/ios-develop/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

