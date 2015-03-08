#  使用HTML5构建iOS原生APP（3）

[ Yuguo ](http://yuguo.us) 2013年 03月 15日

问题发生的场景是webview中有一些筛选器，当我点击（在手机上实际上是触摸）筛选器的时候，页面内容会发生变化，但完全是本地的，不涉及数据传输之类的。

这次要解决的体验问题是当点击事件发生的时候， ** 页面会闪烁一下 ** 。

研究之后发现解决办法是把对 ` click ` 事件的绑定替换成 ` touchend ` ：

    
    
    tagdom.addEventListener('click',function(ev){
    	...
    }
    

替换成：

    
    
    tagdom.addEventListener('touchend',function(ev){
    	...
    }
    

代码很简单，但是新的问题出现了，当我按住选择器，然后我突然不想点了，我就会滑走手指，然后放开。我的预期当然是事件被取消，但是 ` touchend `
还是执行了，并且 ` ev.target ` 仍然是之前的元素。

所以我需要检测是否发生了touchmove事件，解决办法应运而生：

    
    
    var isScrolling = false;
    window.addEventListener('touchstart', function () { isScrolling = false; });
    window.addEventListener('touchmove', function () { isScrolling = true; })
    

所以我们现在有一个变量 ` isScrolling ` 来标志是否滑动了手指，如果没有发生过滑动，那么 ` touchend ` 才生效：

    
    
    tagdom.addEventListener('touchend',function(ev){
    	if(isScrolling == false){
    		...
    	}
    }
    

现在，页面不会再发生闪烁了。

[ 使用HTML5构建iOS原生APP（4） → ](/weblog/scroll-speed-in-uiview/) [ ←
使用HTML5构建iOS原生APP（2） ](/weblog/webview-connect-with-ios/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

