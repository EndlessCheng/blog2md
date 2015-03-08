#  [ [iOS] 如何在 NSArray 中存放 weak 的引用 ](/pleasecallmewhy/article/details/41089001)

遇到一个问题，把 self 加到静态变量的 NSArray 的时候，由于被 NSArray 持有，所以无法释放，因此不能调用 dealloc 方法，也就无法将自己从 array 中 remove 掉。 

  


问题整理一下，就是如何在 NSArray 中存放 weak 的引用？ 

  


解决的方案是：在外面加上一层 NSValue。答案地址： 

  


[ http://stackoverflow.com/questions/9336288/nsarray-of-weak-references-to-objects-under-arc ](http://stackoverflow.com/questions/9336288/nsarray-of-weak-references-to-objects-under-arc)   


  


代码如下： 

  

    
    
    NSValue *value = [NSValue valueWithNonretainedObject:myObj];
    [array addObject:value];

  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/41089001](http://blog.csdn.net/pleasecallmewhy/article/details/41089001)