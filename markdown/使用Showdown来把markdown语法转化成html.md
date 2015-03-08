#  使用Showdown来把markdown语法转化成html

[ Yuguo ](http://yuguo.us) 2012年 09月 27日

有的时候我们会有这样一种需求，我们有一个用markdown格式编写的文档，希望在一个页面上展示出来（很有可能是github），我不能用任何服务器端的语言，只
能用静态数据和JavaScript。我也不希望使用任何桌面转义软件，因为这样每次发布都会很复杂——编写markdown，转义html，发布html。

而我最开始使用markdown而不是html的原因是它非常快，而且在纯文本的状态下就非常具有可读性。

而且我不需要一个web端的编辑器，我会在本地的APP上编写markdown，这也是为了方便版本管理。

综合考虑之后，我使用showdown来实现markdown->html的转化。 [ demo
](http://softwaremaniacs.org/playground/showdown-highlight/) [ download
](http://softwaremaniacs.org/playground/showdown-highlight/showdown.js) usage：

    
    
    var text = "Markdown *rocks*.";
    
    var converter = new Showdown.converter();  
    
    var html = converter.makeHtml(text); 
    
    alert(html);

` 就是这么简单。 ` 请注意markdown->html转化是不可逆的 ，所以总是需要保存一份markdown文件。如果你有一个数据库，而且不希望每次都由
浏览器来渲染所有的markdown，那么你可以把markdown渲染生成的html保存在数据库中，不太优雅，但性能能有不错的提升。

[ jQuery模板 → ](/weblog/jquery-template/) [ ← SAE与Cron ](/weblog/sae-and-cron/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

