#  Bigpipe用Nodejs的实现

[ Yuguo ](http://yuguo.us) 2013年 12月 06日

本文是一个ppt分享的大纲，感谢 [ https://github.com/undoZen ](https://github.com/undoZen)
提供代码。

##  什么是Bigpipe

  * 是一种不局限于语言的前后端整合技术方案 
  * 由Facebook首创 
  * 适合比较大型的，需要大量服务器运算的站点 
  * 有效减少HTTP请求 
  * 兼容多浏览器 

##  Bigpipe解决的问题

  * 下载阻塞 
  * 服务器与浏览器算力浪费 

##  现有的阻塞模型

![](/files/2013/12/traditional-network.jpg)

##  页面解析步骤

  1. 浏览器发送HTTP请求 
  2. 服务器接收到HTTP请求，解析请求，从存储层拉取数据，拼接HTML，发回一个HTTP响应 
  3. 这个请求通过网络传输到浏览器 
  4. 浏览器解析接收到的数据，构造DOM树，下载CSS和JavaScript 
  5. 浏览器下载了CSS之后，开始解析CSS，渲染页面 
  6. 下载JavaScript之后，开始解析JavaScript，执行JavaScript 

##  传统流程

** 整个完整的页面 ** 渲染依次经过以下步骤。 

##  Bigpipe解析步骤

** 每一个Pagelet ** 都经过以下每一个步骤才会出现在浏览器中，但是多个Pagelet可以同步进行处理。 

##  Bigpipe的速度提升

Facebook的Pagelet

![](/files/2013/12/facebook.jpg)

##  Bigpipe的速度提升

Facebook的Pagelet

![](/files/2013/12/facebook-page-parts.jpg)

##  Bigpipe的速度提升

页面分片越多，性能提升越明显

![](/files/2013/12/facebook-bigpipe.jpg)

##  Bigpipe不适合

简单页面，适合服务器直出全部HTML

##  YSlow优化建议

提早flush

##  flush()

PHP中的 ` flush() ` 函数可以建立一个HTTP持久链接，达到分块传输的效果，YSlow建议在输出 ` <head> ` 之后马上 `
flush() ` ，以便浏览器下载资源。

##  Nodejs是什么

  * 一个JavaScript运行环境 

##  Nodejs不是什么

  * 不是一个库 

##  Bigpipe in Nodejs

是一种技术方案（Bigpipe）在一种环境（Nodejs）中的实现。

Bigpipe的服务器端可以用各种语言来实现

##  为什么使用Nodejs？

注：Bigpipe技术的服务器端需要HTTP1.1支持，浏览器端需要JavaScript支持。

##  Why Nodejs?

  1. 异步特性适合Web，适合用少量服务器服务海量用户 
  2. 同一种语言模板同时运行在服务器和浏览器中 
  3. 开源社区支持 

##  关键技术点

HTTP 1.1引入分块传输编码

注：HTTP分块传输编码允许服务器为动态生成的内容维持HTTP持久链接。

##  HTTP分块传输编码格式

    
    
    Transfer-Encoding: chunked
    

如果一个HTTP消息（请求消息或应答消息）的Transfer-
Encoding消息头的值为chunked，那么，消息体由数量未定的块组成，并以最后一个大小为0的块为结束。

##  Nodejs自动开启 chunked encoding

除非通过sendHeader()设置Content-Length头。

##  Nodejs Express

使用Express简单架设一个web服务器（简化原生Nodejs http api），并使用jade来渲染页面模板（让代码简单）。

##  res.render

    
    
    res.render('view', option);
    

只有两个参数时， ` res.render() ` 自动调用 ` res.send() ` ，res.send包括 ` res.end() `

##  res.render设置第三个参数

    
    
    res.render('view', option, function(err, html){
        res.write(html);
        res.end();
    });
    

设置了第三个参数时，不会自动 ` res.end() ` ，Good！

##  发送多个pagelet

    
    
    res.render(view, options, function (err, str) {
        if (err) return res.req.next(err)
        res.setHeader('content-type', 'text/html; charset=utf-8')
        res.write(str)
        if (!res.pipeCount) res.end()
      })
    

如果要发送n个pagelet，就可以在每渲染一个pagelet之后计数-1，当全部渲染完成之后才调用 ` res.end() `

##  layout.jade

    
    
    doctype html
    
    head
      title Hello, World!
      link(href="/static/style.css", rel="stylesheet")
      script(src="/static/jquery.js")
      script(src="/static/jade.js")
    
    section#s1!=s1
    section#s2!=s2
    

##  第一部分数据

    
    
    <!DOCTYPE html>
    <head><title>Hello, World!</title>
    <link href="/static/style.css" rel="stylesheet">
    <script src="/static/jquery.js"></script>
    <script src="/static/jade.js"></script>
    </head>
    <section id="s1">
    <span id="pipe_08554240758530796_1386255294914"></span>
    </section>
    <section id="s2">
    <span id="pipe_020325828110799193_1386255294914"></span>
    </section>
    

##  第二部分数据

    
    
    <script>
    $("#pipe_08554240758530796_1386255294914")
    .replaceWith("<h1>Partial 1</h1><div class=\"content\">"+
    +"Hello, I'm the first section.</div>");
    </script>
    

##  第三部分数据

    
    
    <script>
    $("#pipe_020325828110799193_1386255294914")
    .replaceWith("<h1>Partial 2</h1><div class=\"content\">"
    +"Hello, I'm the second section. Takes 5 seconds to render.</div>");
    </script>
    

##  第四部分数据

空数据（END）

##  更复杂的实现

    
    
    <script type="text/javascript">
    big_pipe.onPageletArrive(
    {id:"pagelet_composer",
    content:"<HTML>",
    css:"[..]",
    js:"[..]",
    …}
    );
    </script>
    

#  Thank You!

Created by [ Yuguo ](http://yuguo.us)

##  课后问答

Bigpipe对SEO的影响是什么？如何解决？

#### 原文：[http://yuguo.us/weblog/bigpipe-in-nodejs/](http://yuguo.us/weblog/bigpipe-in-nodejs/)