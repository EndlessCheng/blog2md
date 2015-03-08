#  用HTML5构建移动APP，时机到了

[ Yuguo ](http://yuguo.us) 2013年 02月 07日

之前我在翻译 [ 《移动用户体验设计考虑的因素：“是Web，还是原生？”》 ](http://yuguo.us/weblog/web-or-
native-2/) 时，学习到的一个观点是：

> 当我们提一个应用是原生的还是Web的时候，我们更多地是从开发者的角度在考虑问题，是一种“由内而外”的思考方法，这种思考方向是错误的。正确的方向是“由外而
内”，由用户需求来判定技术方案。

>

> “原生”或者“Web”的选择更多的是平台和文化的选择。

看到一些框架或者demo可以用html/css/js来非常逼真地模拟iOS的各种光影、按钮、动画，这种方向就是错误的，当我们使用Web来编写iOS
app的时候，我们的目标不应该是可以多么逼真地模拟iOS组件。因为既然想要模拟iOS组件，为什么不干脆用原生objective-c来写呢？

用原生代码的好处更多：

  * 系统级的性能优化 
  * 用户操作习惯，比如毫秒级的动画，Web可能很难模仿得100%一样，那么就会出现跟原生不一致的情况 
  * 设计的对比原则：如果两个元素看上去不一样，那就要设计得完全不一样，而不是有一点相似但又不太一样，这会让用户觉得是设计错误 

##  未来趋势

我相信未来趋势是混合应用（原生和Web相结合），并且Web在其中所占的比例可能越来越大。

因为之前看到一篇文章 [ 应用开发者不再遵循苹果iOS设计惯例
](http://game.donews.com/news/201301/1717996.html) ：

> 在苹果自己的平台上，有些最受欢迎的和最美观的应用最近都放弃了iOS的纹理、阴影和3D特效，转向更加平面、干净和简洁的设计风格。但这种设计新主张并不是一种
离经叛道，反而有望成为iOS设计的未来。奇怪的是，苹果自己却还没赶上这股潮流。

也就是说，在平台文化上这一点上，未来的App是会呈现一种百花齐放的状态，所以原生SDK不再满足开发者和设计师的需求。

而Web方便定制的特性更容易满足这一需求。

##  性能？

大家对Web App一个很大的担忧就是会有严重的性能问题，比如操作不流畅，频繁崩溃等。

这是因为移动设备机的性能相对PC还有一定差距，而Web开发者不了解这一局限，只是把移动设备当做PC一样在设计和编程，从而导致一些性能问题。但是最近，已经有一
些Web App的最佳实践产生。

比如：

  * 不要使用CSS3圆角，渐变，盒阴影 
  * 尽量减少DOM数量 
  * 减少图片数量 
  * 使用visibility:hidden;甚至删除节点来清除内存 

参考资料：

[ 用HTML5实现iPad应用无限平滑滚动 ](http://blog.csdn.net/hfahe/article/details/7535914)

[ 那些耗费比较的的CSS属性 ](http://www.w3cplus.com/blog/605.html)

[ You’ll never believe how LinkedIn built its new iPad app (exclusive)
](http://venturebeat.com/2012/05/02/linkedin-ipad-app-
engineering/#s:profile_ipad_frame)

结论是：通过最佳实践，以及Web开发者技艺的提高，对这个平台的熟悉，以及对设计的折中，最终Web应用的性能不是问题。

[ MongoDB、Mongoose和MongoHQ → ](/weblog/mongodb-and-mongoose-and-mongohq/) [ ←
M型社会和低智商社会 ](/weblog/m-society/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

