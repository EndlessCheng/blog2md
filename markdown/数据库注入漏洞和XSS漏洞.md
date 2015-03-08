#  数据库注入漏洞和XSS漏洞 

[ Yuguo ](http://yuguo.us) 2013年 03月 27日 

v2ex上的一个热心网友使用我的开源程序“ [ 33号铺 ](https://github.com/yuguo/33pu) ”的时候发现程序存在SQL注入漏洞，然后邮件告知了我。 

我之前没有考虑过这方面的问题，搜索了解了一下，确实比较严重，然后修复了这个问题。 

简单的说，程序员在编写代码的时候，没有对用户输入数据的合法性进行判断，使应用程序存在安全隐患。用户可以提交一段数据库查询代码，根据程序返回的结果，获得某些他想得知的数据，这就是所谓的SQL Injection，即SQL注入。 

##  SQL Injection 

简单的判断漏洞的方法就是在查询url后面加上一个引号’。比如http://33pu.net/home/search?keyword=%E6%AF%9B%E8%A1%A3后面加一个引号’ 

这时候会出现服务器报错： 

![](/files/2013/03/sql-injection.png)

根据错误详情我们可以看出对于用户输入（url）没有进行过滤和检测，而直接丢到sql查询里面去运行，这时候就会暴露出一些重要的信息，比如用户名和密码。 

详情可以看看 [ 这篇文章 ](http://www.blueidea.com/tech/program/2004/1810.asp)

然后我的解决办法也很简单，使用CI的 [ Active Record类 ](http://codeigniter.org.cn/user_guide/database/active_record.html) 来操作数据库，而不用拼接的SQL语法，原因是系统会自动对素有输入值进行转义。 

##  XSS漏洞 

我在检查的时候发现的33号铺存在另一个漏洞是XSS漏洞，这个跟数据库注入的方法很像，但原理不同。SQL注入漏洞是请求时生效，会直接让服务器返回数据库相关的重要信息。XSS是输入时没有问题，黑客输入的JavaScript代码会储存在数据库中，但是正常用户访问时，会运行这个JavaScript代码，然后把自己的cookie等信息暴露给黑客。 

解决办法更简单，使用CI的 [ 输入类 ](http://codeigniter.org.cn/user_guide/libraries/input.html) 来接收POST和GET的数据，系统会进行JS的转义。 

现在我已经修复了这两个漏洞，所以请大家下载 [ 最新的33pu代码 ](https://github.com/yuguo/33pu) 。 
#### 原文：[http://yuguo.us/weblog/sql-injection/](http://yuguo.us/weblog/sql-injection/)