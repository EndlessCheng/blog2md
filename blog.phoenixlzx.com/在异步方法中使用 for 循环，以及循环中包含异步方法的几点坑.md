title: 在异步方法中使用 for 循环，以及循环中包含异步方法的几点坑

date: 2014-05-18T19:18:20.000Z

tags: [Node.js, ]

description: 

---
又是熬夜干活。 

之前在 StackOverflow 上看到过 [ Array.forEach 是同步(阻塞)的 ](http://stackoverflow.com/questions/5050265/javascript-nodejs-is-array-foreach-asynchronous) ，但是实际使用的时候，特别是我在写 Node.js 程序的时候几乎没感觉到过它的阻塞—— forEach 或者其他 for 循环之后的 callback 从来都是被立即调用，没有等待整个循环执行完。<== 这个命题是个假命题，下面会说明。 

今天又一次掉进异步的坑里才发现 for 循环确实是阻塞的。至于为何它后面的回调函数会立即被调用，原因是 for 循环里有异步方法。整个循环不会等待异步方法结束，而是直接进入下一个循环，所以它 ** 看起来 ** 像是异步的，后面的回调函数「立即」被调用了。 [ StackOverflow ](http://stackoverflow.com/questions/21184340/async-for-loop-in-node-js) 上有更详细的例子和说明。 

不过如果是数组，那么直接使用 [ async ](https://github.com/caolan/async) 替代原生的 forEach 和其他 for 语句即可简单解决。但是问题出在我这里的情况是要用 ` for in ` 语句处理 Object，虽说 Javascript 里 Object 和 Array 非常相似但是毕竟没有 Array 那些好用的方法，在这种情况下也不方便使用 prototype 来给我的 object 新增类似方法。二小姐给出的解决方案是手动设置计数器，获得 object 长度的办法是使用 ` Object.keys(obj).length ` 。 

** 注意 ** ` Object.keys(obj).length ` 并不一定是要循环的次数，具体需要看 Object 的结构。我这里就是解析 DOM 得到的 Object 所以有额外的东西， ` length - 3 ` 才是需要的结果。 

代码写出来大概是这个样子 
    
    
    function(obj, callback) {
    
        var tasks = Object.keys(obj).length;
    
        
    
        var arr = ['one', 'two', 'three'];
    
        
    
        for (key in obj) {
    
    	
    
    	tasks--;
    
    	
    
    	async.eachSeries(arr, someFunc(n, cb) {
    
    	
    
    	    // do stuff here.
    
    	    
    
    	    cb();
    
    	
    
    	}, function(err) {
    
    	
    
    	    // operations after array iteration completed.
    
    	    
    
    	    if (tasks === 0) {
    
    	    
    
    		// All tasks done, return to callback
    
    		return callback();
    
    	    
    
    	    }
    
    	    
    
    	});
    
        }
    
    }  
  
---  
  
判断的语句其实也可以放在 ` async.eachSeries ` 之后，这样可以明显减少判断的计算(虽然那点计算不算啥) 但是也有可能会在没等待最后一次 async 执行结束的时候就返回了，所以保险起见还是多花点处理器来保证全部任务执行完。以及在最后 ` callback ` 的时候如果不写 ` return ` 就会失效。我还没查原因，因为已经累得不行了… 所以(当回伸手党)如果哪位童鞋知道的麻烦告知… 有灵梦的节操相送哦 >///<

==== 2014-05-20 更新 ==== 

感谢 Xuetian Weng 菊苣为了灵梦的节操不远万里给我纠错 /w\ 上面的代码在 ` async.eachSeries ` 里有异步方法时存在多次 ` tasks === 0 ` 的情况，因为同样的因为 ` for in ` 循环不会等待 async 结束，async 的回调不一定会在 ` tasks ` 下一次自减之前被调用。解决办法是 ` tasks-- ` 放在 ` async.eachSeries ` 的回调函数里。更好些的代码如下： 
    
    
    function(obj, callback) {
    
        var tasks = Object.keys(obj).length;
    
        var arr = ['one', 'two', 'three'];
    
        for (key in obj) {
    
            async.eachSeries(arr, someFunc(n, cb) {
    
                // do stuff here.
    
                cb();
    
            }, function(err) {
    
                // operations after array iteration completed.
    
    	    
    
                // tasks self-decrease should be here to ensure every async.eachSeries call has ended.
    
                tasks--;
    
                if (tasks === 0) {
    
                    // All tasks done, return to callback
    
                    return callback();
    
                }
    
            });
    
        }
    
    }  
  
---  
  
不过菊苣说最后的 return 是可有可无，我这里的测试是不加 return (不管是在前面还是后面) 这个 callback 都不会被正确调用… 所以 return 的问题并没有算是解决，于是放到后面有时间的话来满满折腾吧~看 Xuetian Weng 菊苣如此渴求节操的表情咱就给一点表示感谢好了呜(双手奉上 
