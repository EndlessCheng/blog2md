#  jQuery要杀死js了

[ Yuguo ](http://yuguo.us) 2012年 04月 20日

今天在stackoverflow上看到这么一个问题： [ http://stackoverflow.com/questions/406192/how-to-
get-the-current-url-in-jquery ](http://stackoverflow.com/questions/406192/how-
to-get-the-current-url-in-jquery) LZ说：

【169】我是jQuery玩家，我想获得当前URL的参数，比如

    
    
    http://localhost/menuname.de?foo=bar&amp;number=0

这个问题相当具有代表性，有169个赞。 ` 1L回答： ` 【261】要得到参数你应该这样搞：

    
    
    $(document).ready(function() { var pathname = window.location.pathname; });

简洁明了的回答获得了261个赞。然后有趣的是在这个回答下面的评论，方括号中的数字是认为这条评论有用的人：  【19】关于location对象的详细说明： [
developer.mozilla.org/en/DOM/window.location
](https://developer.mozilla.org/en/DOM/window.location)
【35】这TMD应该是常识啊，jQuery要毁了JS。

【46】谈不上杀死JS，jQuery是让JS获得了新生。新的C#/Java程序员了解指针吗？不。他们需要了解吗？他们不需要，新的抽象足够强大，所以指针不再是
必需的知识。

【68】“我怎样用jQuery ooxx？”这种问题，而答案是原生JS的这种情况很常见。你可能知道如何用原生JS完成某任务；但是由于浏览器的不一致性，你可能
更喜欢用jQuery的封装方法去做。我记得在jQuery之前我会受限查阅手头的各种浏览器列表。所以jQuery是在杀死原生js，对的……但是，这也让它获得了
新的生命。

【18】不用等到document.ready就可以使用这个方法了……

[ 前端交互视觉——众妙之门2 → ](/weblog/smashing-book-2/) [ ← 单入口、MVC和Restful Service
](/weblog/mvc-and-restful-service/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

