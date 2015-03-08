#  jQuery模板

[ Yuguo ](http://yuguo.us) 2012年 09月 29日

之前写过一篇文章 [ JavaScript模板入门 ](http://yuguo.us/weblog/javascript-template/) ，在那篇文
章中介绍了handlebar这个模板库，本文介绍另一种，对于熟悉jQuery语法的同学会用起来更方便，那就是jQuery模板，目前还在beta阶段。

在jQuery的官网上可以看到有两种语法，但是其中一种已经不推荐了（ [ http://api.jquery.com/tmpl/
](http://api.jquery.com/tmpl/) ），而是推荐jQuery.tmpl()（ [
http://api.jquery.com/jquery.tmpl/ ](http://api.jquery.com/jquery.tmpl/)
），本文也只会介绍这种方法。

##  $.tmpl()

语法很简单，在页面引入了jQuery.js和jQuery.tmpl.js（ [
http://api.jquery.com/category/plugins/templates/
](http://api.jquery.com/category/plugins/templates/) ）以后，使用代码：

    
    
    $.tmpl( "<li>${Name}</li>", { "Name" : "John Doe" }).appendTo( "#target" );

$.tmpl第一个参数是html模板，里面可以包含html标签，变量（比如${Name}），逻辑（比如）等；

第二个可选参数是数据，可以是JavaScript对象或者数组（其实JavaScript数组就是对象，而不像大多数语言那样，是一种更快的原生数据）。

当然在实际代码中，我们不会直接在一个string中定义html模板，我们更推荐使用一个script标签：

    
    
    <script id="pageTmpl" type="text/x-jquery-tmpl">
    
    <p>${value1},<i>${value2}</i><>
    
    </script>

然后获得里面的字符串：

    
    
    var pageTmpl = $('#pageTmpl').html();

另外我们在实际代码中也不会用一个匿名的对象作为数据，而是会创建一个有名有姓的对象：

    
    
    var pageData;
    
    pageData.value1 = 'string 1';
    
    pageData.value2 = 'string 2';

最后就可以使用了：

$.tmpl(pageTmpl,pageData).appendTo(‘#target’);

当然我的例子很烂，更好的例子可以直接去看官网： [ http://api.jquery.com/jquery.tmpl/
](http://api.jquery.com/jquery.tmpl/) ，里面还有使用ajax数据的例子，可以直接把远程取得的数据解析为jsonp。

##  $.template()

有的时候我们会希望创建一个可以重复使用的模板，而不是每次都从字符串来解析，这时候我们可以用$.template()方法创建一个编译过的模板函数。

    
    
    $.template( "summaryTemplate", "<li>${Name}</li>" );

用法还是类似：

    
    
    $.tmpl("summaryTemplate",pageData).appendTo('#target');
    
    
    $.tmpl("summaryTemplate",pageData2).appendTo('#target');
    
    
    创建重复使用的模板函数除了性能上的考虑（编译过程只会发生一次），还有一个功能就是在其他的模板中嵌套使用，语法是：

[ Web还是Native？ → ](/weblog/web-or-native/) [ ← 使用Showdown来把markdown语法转化成html
](/weblog/use-showdown-to-convert-markdown-to-html/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

