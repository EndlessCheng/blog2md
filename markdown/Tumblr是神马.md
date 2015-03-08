#  Tumblr是神马

[ Yuguo ](http://yuguo.us) 2010年 08月 14日

Tumblr是我很喜欢的一个产品，超轻量级，现在已经被block了，看到这篇文章还是翻译过来。用户体验确实不错，产品经理和设计师，还有开发者都可以学习一下。

原文地址：http://www.smashingmagazine.com/2010/07/22/a-complete-guide-to-tumblr/

译者：余果（https://yuguo.us）

可以认为Tumblr是一个小型博客。Twitter和腾讯围脖在国内称为“微博”实际上是个不准确的宣传用语，属于商业上的命名规则。如果按学术上的命名规则来说，
他们不属于“博客”科的。围脖允许人们发表140字以内的文字和图片，而Tumblr允许你发表任意文字数量的日志，但它更适合（同时也在鼓励）小型的日志。它是14
0字微博和大型博客（像我这个yuguo.us/weblog）之间的一个过渡。

[ ![Tumblr后台界面](http://yuguo.us/files/2010/08/photopost.jpg)
](http://yuguo.us/files/2010/08/photopost.jpg)

Tumblr对于喜欢自定义的人才们也是一个很好的选择，因为它给予用户对于博客外观有完全的控制力。它也为主题设计师提供了机会，那些高级主题都会被定价为US$9
~$49，厉害哦~本文为使用和设计Tumblr完全指南。

##  为嘛使用Tumblr

因为Tumblr超简单，同时它的社交圈机制可以让你非常方便地follow其他的Tumblr用户，并且分享他们的内容（有点像Qzone囧）。

###  日志类型

与其他博客托管商不同的是，Tumblr有一系列内置的日志类型。它们包括文本，相片，视频，歌曲，引用，链接和简单的对话。大部分主题都会利用这些不同的日志类型指
定特定的格式或者样式。所有这些日志类型里面都可以加上纯文本，比如可以在一首歌下面添加一些心得。

[ ![Tumblr的日志类型](http://yuguo.us/files/2010/08/posttypes.jpg)
](http://yuguo.us/files/2010/08/posttypes.jpg)

由于Tumblr把这些日志类型很好地分开，所以可以很方便地把博客变成一个图片博客，或者播客。

###  Tumblr API

Tumblr开放API导致一大堆第三方应用的衍生。比如iPhone应用，桌面应用，或者是widgets和web插件。也可以设置Tumblr自动同步到Twit
ter和Facebook帐号（天朝网民纷纷表示这些网站是不存在的）。

对开发者来说，开放API就等于……吃全家福一样，是超赞的一件事。用一些PHP和XML的知识就能快速用API做出好玩的东西来。已经有大量的应用程序可以使用，它
们还会更多。

###  其他牛逼之处

像Twitter一样，Tumblr可以让你关注（参加Follow）其他用户并且在你的后台查看他们的日志。你也可以ReBlog（参见ReTweet）或者hea
rt（参见favorite）任何日志，无论是否follow他们。

Follow其他用户很简单，Tumblr页面顶部右上角都会有链接。

[ ![Tumblr的Reblog](http://yuguo.us/files/2010/08/reblogdashboard.jpg)
](http://yuguo.us/files/2010/08/reblogdashboard.jpg)

###  开始注册什么的吧

这一部分免翻译，英文稍微OK就可以用了，图标做的也很好，即使是日文应该也没什么问题。咱快速略过这一段进入到开发者感兴趣的环节吧。

[ ![简单的注册页面](http://yuguo.us/files/2010/08/signup.jpg)
](http://yuguo.us/files/2010/08/signup.jpg)

###  选一个主题

即时身无美分的穷人也可以选到很好的免费主题。

[ ![选择一个主题](http://yuguo.us/files/2010/08/tumblrthemes.jpg)
](http://yuguo.us/files/2010/08/tumblrthemes.jpg)

大部分主题都可以自定义颜色。

[ ![自定义颜色](http://yuguo.us/files/2010/08/appearanceoptions.jpg)
](http://yuguo.us/files/2010/08/appearanceoptions.jpg)

和CSS

[ ![大部分主题都可以自定义CSS](http://yuguo.us/files/2010/08/customcss.jpg)
](http://yuguo.us/files/2010/08/customcss.jpg)

和HTML……

[ ![所有主题都可以自定义HTML](http://yuguo.us/files/2010/08/customhtml.jpg)
](http://yuguo.us/files/2010/08/customhtml.jpg)

从更改别人的HTML开始上手来设计Tumblr主题是一个很好的方法，这可比从0开始方便多了。

###  书签

Tumblr使得从web上任何地方发表内容到Tumblr都非常容易。把它拖到（或者存到）你的书签栏里面，当发现值得post的内容的时候就可以快速到达对应的日
志类型页面。

大部分页面都会默认“链接”类型，但是如果你在访问Flickr，那么默认会到“照片”类型。类似的，如果你在看YouTube页面（天朝网民……），默认会是“视频
”类型。

[ ![方便的书签功能](http://yuguo.us/files/2010/08/bookmarklet.jpg)
](http://yuguo.us/files/2010/08/bookmarklet.jpg)

##  创建Tumblr主题

Tumblr已经提供了非常简单的方法可以让你改别人的HTML和CSS来做自己的样式，即便如此还是有些人犯贱喜欢从头开始，Tumblr考虑到了这种需求。

[ ![自定义一个新的Tumblr主题](http://yuguo.us/files/2010/08/customtheme.jpg)
](http://yuguo.us/files/2010/08/customtheme.jpg)

###  基本结构

Tumblr主题包括一些不变的基本部分。基本上是头部和主题部分，边栏和footer是可选的。Tumblr主题被切分为一些代码块，每一块都包含一些数据。例如，
对于每一种日志类型都有一个单独的代码块，还有一些代码块用来描述你的Tumblr，或者“上一页”“下一页”的样式之类的。

主题定制的过程中有很多变量可以利用。变量是很好的事情，我们这些找不到女盆友的IT从业者都爱变量。有一些简单的变量如主题名称、作者页面链接、favicon（这
个……怎么翻译呢，就是在url栏出现的16px小图标）。完全的变量手册参见 [ Creating a Custom HTML Theme
](http://www.tumblr.com/docs/en/custom_themes) 这是Tumblr的官方页面。

你需要为每种日志类型都定义代码块以便日志正常显示。

虽然没有女盆友，可是我们这些乐于分享的工程师都喜欢创建一个public theme，public theme和private theme的区别就是它允许用户
配置一些自己的属性比如字体颜色或者哪些部分显示哪些部分不显示。你如果感兴趣可以看看其他的主题允许哪些定制变量，然后查看变量的用法。

[ ![创建一个公共主题](http://yuguo.us/files/2010/08/submittheme.jpg)
](http://yuguo.us/files/2010/08/submittheme.jpg)

相比于自用主题，public theme确实有一些_要求_：

  * 主题的所有部分必须放在Tumblr（什么javascript啊图片啊都是） 
  * 三方插件必须被注释掉。这意味着你可以放入这些代码，并且给出文字说明如何enable它们，但是它们必须默认禁用。 
  * 你的主题必须支持所有的日志格式 
  * 必须支持标准tags（参见变量列表，看看有什么） 
  * 必须漂亮好看功能齐全。Tumblr主题按质量投票排序，强者如林的世界中弱者无法生存 现在，你把公共主题上传到Tumblr的是，它默认是免费的。想要卖美元的话，必须申请或者被邀请。 

其实你也可以在黑市卖主题，Theme Forest就有一系列Tumblr主题出售。也有在自己的个人网站上出售主题的，淘宝拍拍也行啊。

##  总结

无论你是在寻找一个方便和简单的平台来写博客，还是多人博客，还是小小的吐槽空间，还是开发者，还是想赚钱的开发者都可以用Tumblr达到目标。

[ 第四周流水记 → ](/weblog/week-4/) [ ← W3C Unicorn Validator 书签 ](/weblog/w3c-
unicorn-validator-bookmark/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

