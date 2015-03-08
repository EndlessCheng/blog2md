#  使用HTML5构建iOS原生APP（1）

[ Yuguo ](http://yuguo.us) 2013年 03月 08日

读了 [ Exclusive: How LinkedIn used Node.js and HTML5 to build a better, faster
app ](http://venturebeat.com/2011/08/16/linkedin-node/)
之后，我感觉在原生软件中嵌套一部分HTML5页面也许是一个很好的方向：

  * 原生跟HTML5的比例可以灵活协调，更适合原生的就使用原生组件，更适合HTML5的就用HTML5 
  * 前端开发者可以使用我们已经熟悉的技术：用CSS3设计，用JavaScript处理逻辑 
  * 可以更方便移植到Android或者Win Phone等平台 
  * 性能跟原生一样优秀 

下面是我在研究制作HTML5 APP的过程中用到的技术清单：

  * 【nodejs】我的服务器端需要输出一系列API，以方便我更新数据，所以采用了nodejs，原因我在 [ 上一篇日志 ](http://yuguo.us/weblog/node/) 有说； 
  * 【 [ expressjs ](http://expressjs.com/) 】nodejs框架，提供了MVC分离的架构，路由中间件； 
  * 【 [ mongodb ](http://www.mongodb.org/) \+ [ mongoose ](http://mongoosejs.com/) 】mongodb提供数据库，mongoose作为封装对象，能让我更方便地处理数据库连接和查询操作； 
  * 【 [ ejs ](https://github.com/visionmedia/ejs) 】服务器端的js模板语言，其实后来没有实际用到这个，因为我选择了传输json数据，然后在客户端（也就是原生app中的webview里）解析数据。另外nodejs的模板语言还可以选择jade； 
  * 【 [ handlebarsjs ](http://handlebarsjs.com/) 】handlerbars与ejs不同，ejs是nodejs采用的一种模板语言，在服务器端渲染出页面然后吐出来，handlebars是客户端模板，浏览器接收模板+json之后用客户端的计算能力来处理。后者传输的数据更少； 
  * 【Objective-C】当然少不了iOS原生语言。 

其实在做服务器的时候我没有用自己的服务器和数据库，而是使用第三方托管，我相信这是未来主流。

  * 【 [ heroku ](http://heroku.com) 】我把nodejs服务器架设在heroku上，更新代码使用git，快速而方便。 
  * 【 [ MongoHQ ](https://www.mongohq.com/) 】我把数据库托管在mongohq上，mongohq跟heroku是无缝衔接在一起的。 

整个流程还是略显复杂，国外第三方托管速度也略慢，希望跑通之后可以进行优化。

[ 使用HTML5构建iOS原生APP（2） → ](/weblog/webview-connect-with-ios/) [ ← Nodejs擅长什么？
](/weblog/node/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

