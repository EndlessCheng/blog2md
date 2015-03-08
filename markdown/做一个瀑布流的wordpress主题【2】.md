#  做一个瀑布流的wordpress主题【2】

[ Yuguo ](http://yuguo.us) 2012年 02月 16日

上一篇已经实现了瀑布流wordpress主题的基本布局，接下来讲ajax加载内容。

##  翻页代码

标准的wordpress翻页代码是在大循环之外有以下代码：

    
    
    <div id="nav-previous">
    
     <?php next_posts_link( __( 'Older posts') ); ?>
    
    </div>

也就是说后台设置了每页显示10篇文章之后，就会每10篇一个翻页。 [ ![](http://yuguo.us/files/2012/02/1.png)
](http://yuguo.us/files/2012/02/1.png) <h2>无限滚动</h2>
当屏幕滚动到页面底部的时候，我们希望触发一个事件来ajax载入新的文章进来。有一个js插件可以很方便的做到这一点： [ infinitescroll.js
](https://github.com/paulirish/infinite-scroll) infinitescroll有一个 [ 官网
](http://www.infinite-scroll.com/) ，但已经停止更新好多年了，代码和文档都已经失效。最新的代码在 [ github
](https://github.com/paulirish/infinite-scroll) 可以下载。读源代码也有比较清晰的说明。

引入infinitescroll.js之后可以在你的站点js中加入以下代码：

    
    
    $container.infinitescroll({//这里是所有条目的容器，我们在上一篇中已经有了jQuery Object，就是$container
    
    
        navSelector  : "#nav-previous",
    
                       // 页面导航的选择器，这个会被隐藏
    
        nextSelector : "#nav-previous a",
    
                       // 这个是触发器，页面滚动到触发器的时候，就会开始ajax加载
    
        itemSelector : ".goods"
    
                       // selector for all items you'll retrieve
    
      });

除了基本的用法之外，插件还提供了一些参数来配置一些自定义风格，比如载入的动画。

此外，在masonry的官网也有介绍 [ 如何跟infinitescroll插件 ](http://masonry.desandro.com/demos
/infinite-scroll.html) 结合。

ajax载入就讲到这里，下一篇《自定义文章数据》。

[ JavaScript中的面向对象函数 → ](/weblog/oo-javascript/) [ ← 做一个瀑布流的wordpress主题【1】
](/weblog/make-a-waterfall-wordpress-theme-1/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

