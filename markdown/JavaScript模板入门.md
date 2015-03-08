#  JavaScript模板入门

[ Yuguo ](http://yuguo.us) 2012年 09月 02日

我最开始写过一个富交互的页面，其中的JavaScript代码包含了很多html标签。

比如要在一个列表中利用ajax插入一个 ` li `
的时候，我会直接把数据跟html标签拼接成一句完整的html，然后插入到ul中。无论数据是从服务器端拿回的，或者是从用户的 ` input `
输入中拿到的——无论哪种方法都是一样。

这个拼接过程放在JavaScript文件中，显得非常不优雅。如果还把style也放在JavaScript中，那数据、结构还有样式整个就是一锅粥了，要维护这样
的代码会让人想自杀。最过分的就是把页面上最终要生成的HTML都直接放在服务器端，ajax吐出数据就包含了 ` <li> `
标签，这样的页面几乎不存在扩展性了，修改一个前台样式都要涉及后台代码的修改。

后来我们知道了不要在JavaScript中对DOM进行style定制，而是只需要在CSS文件中定义好对应的class，然后在JavaScript中使用这个c
lass就好。

接下来我们要做的就是用JavaScript模板把HTML结构（在这个案例中，是<li>标签）也从JavaScript中分离。

市面上的JavaScript模板很多了，以 [ handlebars ](http://handlebarsjs.com/) 这个优秀的模板为例吧：

我们在页面的html中定义模板：

    
    
    <script id="list-template" type="text/x-handlebars-template">
    <li>{&#123;title&#125;}</li>
    </script>
    

然后在我们的逻辑JavaScript代码中可以把数据拼接到这一模版中：

    
    
    var source = $("#list-template").html(); //模板源，一般放在html的script中，这里我们使用jQuery，也可以使用其它方法直接获得内容字符串
    var template = Handlebars.compile(source);  //编译生成一个模板template
    var context = {title:"This is a todo item"} //获得数据，数据一般从ajax或者input中取得
    var html = template(context); //数据+模板=新的html
    

这就是基本的 用法了，更多逻辑可以参考官方文档： [ http://handlebarsjs.com/
](http://handlebarsjs.com/)

[ 最近在读的 → ](/weblog/recently-read/) [ ← 谈谈项目文档 ](/weblog/project-document/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

