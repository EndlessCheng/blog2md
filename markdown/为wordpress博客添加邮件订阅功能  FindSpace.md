#  为wordpress博客添加邮件订阅功能 

[ Find ](http://www.findspace.name/author/find) |  2015年2月17日  |  [ 网络文摘 ](http://www.findspace.name/category/res/fromweb) , [ 资源 ](http://www.findspace.name/category/res) |  [ 3条评论  ](http://www.findspace.name/res/1111#comments)

#  1.环境说明 

  * 虚拟主机 
  * WordPress博客系统 
  * 自己的邮箱 
  * MailPoet Newsletters wordpress的插件 

我用的是自己的域名邮箱（万网买域名赠送的），没有尝试过普通的qq邮箱或者网易邮箱等等。 

虚拟主机提供商明确说明wordpress（以下简称wp）的邮件功能被禁用，以防止博客发送垃圾邮件。 

#  2.配置插件 

##  设置 

该插件有中文语言包，装完就是中文的。这里大体说明下需要设置什么 

在wordpress后台有 ** MailPoet ** 栏，打开 ** 设置 ** –》 ** 用…发送 ** ，选择 ** 第三方 **

> SMTP主机名： smtp.findspace.name 

这里是我自己在域名解析做的解析，如果选择126或者163之类的邮箱，请填写smtp.126.com等等， 

> 用户名： 你的邮箱地址，我的 find@findspace.name 
> 
> 密码： 邮箱密码 
> 
> SMTP端口： 默认smtp的是25不用改 
> 
> 安全连接： 默认否 
> 
> 认证：默认是 

此处的配置就完成了，可以从下面的 

> Test method 

填一个邮箱来测试下是否能收到 

> 发送限制: 70封邮件每小时 

默认即可。然后保存设置。 

##  时事通讯 

就是要发送的邮件，可以选择自动时事通讯，条件为博客有更新，这样每当有更新就会发送订阅给用户。 

这个插件的强大之处就在于，用它制作的邮件非常精美，有很多模板可以用。 

在它提示第二步编写邮件的时候，可以先把里面一些内容删掉，鼠标放上去点叉，见图示。 

[ ![wordpresmail1](http://bcs.duapp.com/findspace//blog/201502//wordpresmail1.png) ](http://bcs.duapp.com/findspace//blog/201502//wordpresmail1.png)

然后拖动右边的 ** 最新自动内容 ** ，拖进去之后会自动弹出框来编辑这个内容，也就是说，这里面的内容都是拖拖放放，然后它自己生成内容，而不是手动填写。里面的选项设置都很清楚，这里不再赘述。 

在选项里有个“详细内容”文字，我这里经常是乱码，不知道为什么。 

最下面有个发送预览，可以先发给自己的邮箱看一下。 

最后点击 ** 现在激活 ** 就可以了 

##  订阅组 

默认有个电子报的分组，这个可以不用管。 

##  侧边栏小工具 

###  表单设置 

MailPoet设置里面有个 ** 表单 ** ，这个表单就是在侧边栏小工具要显示的东西，默认有个 ** 订阅我们的时事通讯 ** ，这些可以都不用修改。 

###  添加小工具 

在wordpress的 ** 外观 ** –》 ** 小工具 **

找到MailPoet Subscription Form拖过去就ok了。 

#  3.说明 

终于折腾出来了，一直没有找到合适的方案。这里还有个方案，不过返现mailpoet可以配置smtp之后，这个就几乎没用了。 

[ wordpres上关于修改Simple Subscribe插件使得它使用smtp来发送邮件 ](https://wordpress.org/support/topic/use-of-wp_mail?replies=13)

Tags:  [ wordpress ](http://www.findspace.name/tag/wordpress)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/res/1111](http://www.findspace.name/res/1111)