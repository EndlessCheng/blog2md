#  网站对iPad适配

[ Yuguo ](http://yuguo.us) 2013年 01月 09日

说到网站适配iPad，感觉挺时髦的，无论是对客户说、对上司说、对前端界来说都会觉得很上流，很国际化。但根据我的体验，有些“优化”真的是为了KPI而优化（不是
产品KPI，而是前端组需要有iPad优化项目的经验而制定的KPI）。说实话，我也做过对iPad，对iPhone的网站优化，但有的时候真仔细体验，却有很多值得
商榷的地方，并不是吃力就可以让用户觉得“爽”。

多 _ 体验 _ 才是正道。

根据我的iPad上网经验，我大概列了这样一个打分表，不知道有没有漏：

页面  |  评分  
---|---  
页面是多列布局，我可以通过双击一列来放大这一列。  |  +20  
面是单列布局，并且没有使用 ` width=device-width ` ，那么iPad会默认把宽度设置为1024宽来缩小，这样文字和可点击区域都会变小。
|  -30  
有 ` position:fixed ` 的元素，并且缩小页面的时候挡住屏幕。  |  -50  
弹出框绝对定位超出屏幕尺寸（看不见，无法继续操作，只能刷新）。  |  -50  
使用Flash做内容。  |  -30  
对retina屏有更清晰的图片和图标。  |  +10  
轻页面，没有太多互动元素和异步内容。  |  +10  
重页面，滚动页面卡，操作需要点击多次。  |  -10  
可点击区域清晰，尺寸合适。  |  +10  
可点击区域小。  |  -10  
使用原生控件，html5表单，select等。  |  +10  
使用模拟控件，模拟滚动条，div模拟的select等。  |  -20  
做一个iPad单独版，优化事件和体验。  |  +10  
单独做的iPad版缺少PC web端上的某个重要功能。  |  -30  
  
得分为正就不错了，使用起来毫无障碍。

按这样的算法，几乎没有做任何事情的豆瓣页得分也相当不错。

这也是我一直坚持的一个观点，身为前端，不要把浏览器开发者的工作也做了。不要嫌 ` title `
的样式不好看，自定义一个，不要嫌浏览器滚动条不好看，模拟一个，不要嫌 ` select ` 不好看，自己做一个 ` div `
绝对定位出来……这种做法是一种很短视的做法：只看到了自己优化的浏览器（IE），忽视了更多系统，更多平台，更多浏览器的体验，忽视了用户自定义的权利。

用原生的、标准的控件即可，使用CSS3对支持的浏览器进行控件样式优化，而不支持的，就使用用户习惯的外观，习惯的行为。让浏览器厂商去优化控件的样式和行为，这是
他的工作，不是你的。

参考资料： [ Safari对于meta标签的官方指南 ](http://developer.apple.com/library/safari/#docum
entation/appleapplications/reference/SafariHTMLRef/Articles/MetaTags.html)

[ Linux哲学 → ](/weblog/linux-philosophy/) [ ← 一个404bug
](/weblog/catch-a-404-bug/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

