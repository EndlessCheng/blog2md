#  使用Chrome的持续绘制模式侦测页面绘制时间

[ Yuguo ](http://yuguo.us) 2013年 02月 21日

页面的 ** 绘制 ** 时间（paint time）是每一个前端开发都需要关注的的重要指标，它决定了你的页面流畅程度。

Chrome开发工具的Timeline标签页中有一个Frame工具，可以用来检测页面渲染中的瓶颈所在。详情查看这篇文章：

[ Improving Web App Performance With the Chrome DevTools Timeline and Profiles
](http://addyosmani.com/blog/performance-optimisation-with-timeline-profiles/)

大意是说如果希望创建流畅的体验和交互，页面渲染应该在每秒60帧以上（即60FPS以上），根据FPS的定义：1000 ms / 60 Hz = 16.6
ms。记住这一指标： ** 每一帧的渲染时间应该保持在16ms以下 ** 。

本文介绍的 [ Chrome Canery
](https://www.google.com/intl/en/chrome/browser/canary.html) 的新功能——持续绘制模式——可以非
常方便地测试你的页面在webkit浏览器中的渲染时间。开启持续绘制模式之后，不必像刚才的文章中介绍的那样，很麻烦地在Timeline标签页中查看绘制状态，而
是可以安心在Elements标签页调试DOM和样式，同时随时查看绘制状态，因为浏览器会持续不断地重绘页面的可见部分。

引用HTML5ROCK的一张图：

![持续绘制模式](/files/2013/02/fps-2.png)

嗯，很像玩游戏的时候即时显示的帧数一样，还记得我们之前计算的时间么，要想页面流畅滚动，需要保持每一帧的平均渲染时间在16.6ms以下。

开启方法：

  1. 下载 [ Chrome Canery ](https://www.google.com/intl/en/chrome/browser/canary.html) ，这是Chrome的开发者版本，有一些最新的强大功能，图标是漂亮的黄色。 
  2. Mac系统和Linux系统需要在Chrome中开启混合模式，方法是地址栏输入 ` about:flags ` ，然后“对所有网页执行 GPU 合成 Mac, Windows, Linux”设置为“已启用”。 
  3. 打开开发工具，在Rendering中勾选“Enable continuous page repainting”这一项。 
  4. 成功了，现在打开任意页面，打开开发者工具，都能看见右上角的持续绘制模式状态表。 

调试方法：

当发现页面每帧渲染时间很高的时候，打开Elements面板，使用上下左右来切换选择DOM，然后按下快捷键 ` H `
来hide或者显示元素，同时观察每帧渲染时间，定位到某个DOM的绘制成本很高时，可以依次取消面板中的CSS样式再观察每帧渲染时间。

在我的MBP上，Qzone的每帧渲染时间是达标的：

![qzone fps](/files/2013/02/fps.png)

当然需要注意的是，每帧渲染时间跟很多因素有关：

  * 硬件性能 
  * 浏览器内核（IE会更慢） 
  * 窗口可见区域大小（你可以试试缩小窗口，观察每帧渲染时间会变小） 

所以不要觉得FPS在我们的开发机上时间达标就OK，要考虑更多用户的机器性能是远远不如我们的。

最后补充一点，持续绘制模式的绘制方法跟浏览器的默认绘制方式是不一样的，浏览器默认不会不停地重绘页面，只会在有需要的时候才重绘一次（产生一帧），关于这一点可以
使用Timeline标签页中的Frame条目详细查看每一帧的计算量。

最后的最后留给大家一个作业，请使用持续绘制模式观察这个页面： [ http://css3exp.com/moon/
](http://css3exp.com/moon/)
的渲染速度，在我的MPB上是50ms+每帧渲染时间，找出CSS成本最高的两个元素上的CSS属性，在Elements面板中去掉它，使FPS降到10以下。

[ 《专业主义》 → ](/weblog/about-customers/) [ ← MongoDB、Mongoose和MongoHQ ](/weblog
/mongodb-and-mongoose-and-mongohq/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

