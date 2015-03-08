#  Python Tornado框架 

[ Find ](http://www.findspace.name/author/find) |  2015年2月6日  |  [ Python ](http://www.findspace.name/category/easycoding/python) , [ 小工具 ](http://www.findspace.name/category/easycoding/tools) , [ 随意Coding ](http://www.findspace.name/category/easycoding) |  [ 没有评论  ](http://www.findspace.name/easycoding/1082#comments)

  * Tornado介绍 
  * 说明 
  * 项目开发说明 
    * 文件夹树结构 
      * apps文件夹 
      * database.sql 
      * settings.py 
      * static文件夹 
      * templates 
      * urls.py 
    * 思路 
      * 实现的功能 
        * 数据库设计 
        * url约定 
        * 过程 
    * PS 

#  Tornado介绍 

** [ 官网 ](http://www.tornadoweb.org/en/stable/) **   
Tornado异步非阻塞的I/O模型的确让人耳目一新，Tornado的优势主要在于对大量Comet长轮询连接的维护上。这也是FriendFeed开发Tornado的原因—–因为FriendFeed需要实时更新Timeline，而Comet又是目前最好，最流行的方法。 

#  说明 

其实本来是想用tornado来实现一个高仿notepad.cc的网站，做了一点，做不下去了。因为这个需求级别比较低，不是很强烈。就让步给别的了。现在说明一下自己的思路以及掌握的东西。 

#  项目开发说明 

##  文件夹树结构 
    
    
    ├── apps
    │   ├── code.py
    │   └── __init__.py
    ├── config.yaml
    ├── database.sql
    ├── dev.md
    ├── index.wsgi
    ├── __init__.py
    ├── LICENSE
    ├── MIT-LICENSE.txt
    ├── README.md
    ├── settings.py
    ├── static
    │   └── custome.css
    ├── templates
    │   ├── custome.css
    │   └── home.html
    └── urls.py

###  apps文件夹 

包含的主要的处理代码，其中的code.py是对发过来的请求的应答处理代码。 

  * BaseHandler是基础结构来接收request，并连接数据库。 
  * HomeHandler则类似basehandler的扩展，对传入的basehandler中的get，post处理。 
  * PageHandler和HomeHandler同等级的，来处理不同的需求，不过他们的使用都是在urls里面定义的。 

类似的都可以自己定义。 

###  database.sql 

这是数据库文件，直接以文本形式打开查看会发现是mysql的命令，在最开始建立sae app并开通mysql服务之后，把这个文件导入进去即可。mysql的命令不再详述，根据自己的需要来写命令即可。 

###  settings.py 

类似一个全局静态变量库。忘记是不是sae必需的了。里面有中文说明，很明确。   
db数据库设置部分是固定的，默认这种方式访问，想用其他方法参考sae的手册。 

###  static文件夹 

自定义的文件夹，用来存放css样式表。 

###  templates 

Tornado默认的模板文件夹，来存放网页。   
这里面的css样式表忘记删掉了。   
注意这个html和普通的不一样，因为肯定要使用从tornado传过去的数据，写法参照上面给的教程连接。   
这个现在这个home里面的代码很简单，结合着code.py看几遍就能看懂。 

###  urls.py 

这个就是负责什么请求对应什么处理函数。   
每个映射左边是正则表达式的连接，右边是处理的函数。 

##  思路 

###  实现的功能 

在线笔记，只需要记住url即可访问，可加密。 

####  数据库设计 

直接一个表，表结构： 

  * url 利用这个连接登录可以编辑该文档 
  * shareurl 打开这个连接看到的是不可编辑的 
  * passwd 密码 
  * post 笔记的内容 
  * published 推送的时间 
  * updated 更新的时间 

####  url约定 

因为是十六进制的，所以约定如下：   
url：默认是5位，且第一个字符一定不是a。当然在修改url时无所谓，不过至少5位   
shareurl ：默认是6位，首字母一定是a开头。不可修改 

####  过程 

  * 用户访问首页，自动分配一个随机的五位的url，保证这个url是新的，原来的数据库里面是没有这条记录的。   
在下面有：当前url，加密，分享链接，保存，修改url，这几个功能。（保存功能是因为没想到怎么实现时时保存）   
此时数据库已经有了这样一条记录，然后用户编辑更新保存，则数据库中的数据也更新。 
  * 用户访问一个未加密的url，则从数据库中查找并渲染页面，如果之前没有该条记录，则新建该条记录。 
  * 用户访问加密的url，则先验证用户的合法性（这一块还没做，可以参考 [ codeshare这个项目 ](https://github.com/SerhoLiu/CodeShare) ，基础代码都是参考的它的） 

这里的关键部分就是code.py和html页面的配合，还没太搞清楚怎么写。   
可以参考 [ 开发日志 ](https://github.com/Findxiaoxun/notepader/blob/master/dev.md)

##  PS 

欢迎朋友来交流，共同开发。   
右边有QQ群号和微博。 

Tags:  [ python ](http://www.findspace.name/tag/python-2) , [ 小工具 ](http://www.findspace.name/tag/%e5%b0%8f%e5%b7%a5%e5%85%b7)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/easycoding/1082](http://www.findspace.name/easycoding/1082)