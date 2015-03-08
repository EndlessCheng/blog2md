#  iOS开发随笔——异步编程

[ Yuguo ](http://yuguo.us) 2012年 12月 23日

` Grand Central Dispatch `
简称（GCD，这个缩写有点大不敬……）是苹果公司开发的一种多线程技术，它提供了一个比较简单的接口来让开发者操作多线程，而不用关心太多底层实现。

##  Blocks

首先要知晓的一个概念就是 ` Blocks ` 。在其他语言中， ` Blocks `
实际上就是闭包。它定义了一小片代码去运行。你可以把它认为是一种华丽的回调函数，在他们接收到数据的时候就可以去 运行。

Block的语法是这样的：

    
    
    ^{ printf("this is a block!\n"); }     
    

很简单。

##  Dispatch Queues

基本上你会吧blocks放在 ` dispatch queues ` （派遣队列）中去执行。有两种队列，并行队列，和FIFO（First in First 
out）队列。无论是那种队列，你放在某一个派遣队列中的各个blocks都会按顺序去执行。不同的是，再并行队列中，它们会在不同的线程中去运行，而再FIFO队列
中，它们会一个接一个去运行，要等前一个完成才进行下一个。

你可以通过这三种方法获得一个队列：

  1. 调用 `dispatch_get_global_queue()`。这样会得到内置的并行队列。有三个内置的并行队列，每一个有不同的优先级（低，中，高） 
  2. 调用 `dispatch_get_main_queue()`。这样会得到主线程的派遣队列。这是一个FIFO的队列，任务随时都在运行（也就是说处于运行循环之中） 
  3. 创建你自己的队列 `dispatch_queue_create()`。这样你会创建一个自己的FIFO队列。 

并行队列会创建尽量多的线程来。线程数目是由GCD来决定，而不是你的任务数量，对于这一点开发者并没有控制权，事实上也无需关注。开发者只需要知道队列中的任务会大
体上并行运行。

##  队列VS线程

队列跟线程没有关系。

有一个方法 dispatch_get_current_queue()
可以在一个block中运行，来获取当前的队列，如果再block外部运行会得到默认的并行队列，这没有多大意义。（这其实是第四种方法来获得一个队列）

而如果你创建一个线程，它跟GCD没有任何关系。

使用GCD的派遣队列和block几乎可以完成你用线程实现的任何任务。你甚至可以不用锁就可以实现同步。

##  运行任务

如果要开始一个异步任务，要使用dispatc_async()方法。比如如果我们想运行上面的block，这就是我们的代码：

    
    
    	dispatch_queue_t queue = dispatch_get_global_queue( DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    
    	dispatch_async(queue, ^{ printf("this is a block!\n"); }); 
    

这就是全部代码。首先我们得到全局并行队列中的一个（总共有三个，还记得吗？），优先级为普通，然后我们调用dispatch_async，指定这个队列还有一个要运
行的block。

block的行为就像闭包，他们会跟自己的运行的上下文环境去交换信息。

    
    
    int i = 20;    
    
    dispatch_async(queue, ^{ printf("The number was %d\n", i); });     
    

输出：

    
    
    The number was 20     
    

block在创建的时候，所有的变量都可以在block的执行中获得，所以我们可以在block中获得i变量。

如果在block中运行任务结束之后需要让主线程知道，可以再次使用dispatch_async：

    
    
    dispatch_async(queue, ^{ NSArray *results = ComputeBigKnarlyThingThatWouldBlockForAWhile();    
    
     // tell the main thread     
    
     dispatch_async(dispatch_get_main_queue(), ^{ ProcessResults(results); });     
    
    });     
    

这样，在这个长任务完成之后，我们再次调用dispatch_async()来在主线程中运行ProcessResults。

[ WordPress迁移到github(jeykll) → ](/weblog/wordpress-to-jeykll/) [ ← 2012总结
](/weblog/2012-end/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

