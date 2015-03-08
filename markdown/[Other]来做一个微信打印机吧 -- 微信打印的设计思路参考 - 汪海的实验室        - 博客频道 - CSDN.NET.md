#  [ [Other]来做一个微信打印机吧 -- 微信打印的设计思路参考 ](/pleasecallmewhy/article/details/26100659)

** 项目源码地址： [ https://github.com/callmewhy/why-wechat-printer ](https://github.com/callmewhy/why-wechat-printer) **

最近微信打印机小火了一把，比如印美团，747微信打印机，都是利用微信公共平台实现照片的打印。 

具体流程： 

  1. 扫描二维码关注公共主页 
  2. 发送图片 
  3. 发送微信打印机上的打印码 

简单三步，实现微信打印照片的功能。 

那么它是怎么实现的呢？在此提供一下自己的思路供大家参考  。 

源码已经写好了  ，确实可行。 

  
如果大家有好的思路欢迎一起分享^_^   
  


#  微信的后台接口 

用户把照片发给微信公共账号，在接收到的时候是有图片的url的，所以我们不用考虑图片的存储问题。 

  * 在接收到用户发送图片消息的时候，把用户的ID和图片的地址写入到数据库的wx_images表中， 
  * 在接受到用户的文字信息的时候，判断一下是不是四位数字的打印码，然后写入到刚刚那条记录里，以供打印机根据打印码获取。 

至此，微信接口的任务就算是完成了。 

  


  


#  打印机的后台接口 

打印机在运行之后，首先要做的事情是获取打印码。   
设置打印码的目的，是为了防止有人随便发送照片捣乱。所以在打印机刚运行的时候，要去服务器获取它自己的打印码。   
为了防止打印码重复，我新建了一个wx_printers表。   
用random随机插入了100条数据，也就是100个随机的打印码，然后用一个状态标示符来标记这个打印码的状态是已用还是未用。   
打印机运行之后会先去服务器获取一个打印码并存到本地，然后根据这个打印码不断地访问服务器，获取打印任务。   
获取到打印任务之后，直接下载图片并存到本地的临时文件，然后调用打印的借口。   


  


  


** 基本的流程图：  **

  


![](http://img.blog.csdn.net/20140517223500718?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


源码下载地址： [ https://github.com/callmewhy/why-wechat-printer ](https://github.com/callmewhy/why-wechat-printer)
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/26100659](http://blog.csdn.net/pleasecallmewhy/article/details/26100659)