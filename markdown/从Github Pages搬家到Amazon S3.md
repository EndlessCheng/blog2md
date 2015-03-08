#  从Github Pages搬家到Amazon S3

[ Yuguo ](http://yuguo.us) 2013年 01月 22日

Github的被墙经历了这样几个阶段，首先是pages被墙（也就是 ` .github.com ` 字符串进黑名单），这个时候自定义域名的pages还是可以
访问的，经历了两天的各地区抽风，后来https主站无法访问，最后DNS污染攻击全站，自定义域名的pages也无法访问了。

现在要访问github要么翻墙，要么配host。

这是常见的和谐节奏，我不会天真的相信只是短期抽风。有人把这次和谐跟抢票插件联系起来，说是铁老大干的，其实不关铁老大得事，1%都不到。真正的不稳定因素是git
hub pages是一个方便的创建页面的办法。

也就是说和谐3定理：

  1. 定理1：优秀的服务一定被墙； 
  2. 定理2：被墙的一定是优秀的服务； 
  3. 定理3：某个服务可以生成一个页面（或者一句话，或者图片，或者任何资源）方便的在互联网上通过浏览器的方式查看，而且这个服务不受政府监管，那一定会被墙。 

想当初也因为功夫墙的事情搬家过几次，包括因为机房公用IP被和谐，还有域名进黑名单。最狠的就是域名进黑名单，yuguodesign.com是2009年左右的域
名，域名进黑名单之后，换IP，cname等各种办法都没办法了。所以才换了现在的yuguo.us。

v2ex上有个帖子号召 [ IT人员拿出点骨气来 ](http://www.v2ex.com/t/58318)
，去工信部网站上提交反馈。因为IT人员可能属于被蹂躏最惨的那一类，针对github被墙，最广泛的观点是“提交了他们也不会看的”和“常年翻墙无压力路过”。

老实说，我也属于这两种心态并存的，以为轻松一句玩笑话“求早日人肉翻墙”就可以解决。常年自嘲的人往往会有这样的“看客心理”，无论这个社会变得多糟，也跟我无关了
，我只求独善其身。

最后我还是提交了申诉，不能因为声音微小就不呐喊。

##  Github

Github还是会用，因为它是最好的程序员社区没有之一，我自己VPN就好了，我也推荐大家还没有开始用的也可以翻墙来用，毕竟这样的被动“过滤”会让它在你的简历
中更有分量，不是吗？

Github pages是github提供的静态页服务，非常方便，只要创建 ` gh-pages ` 分支就可以用 `
xxx.github.com/projectname ` 的域名访问，而且可以方便的绑定域名，这一切都是免费的。

如果你像我一样把博客托管在github pages上，或者静态页是你的主要产品，那可以考虑把页面迁移到其他没有被和谐的服务上，比如amazon s3。

##  Amazon S3

[ Amazon S3 ](http://aws.amazon.com/cn/s3/)
是一个静态资源托管服务，默认就有较大的容量和流量，在流量超标时会选择性付费，你现在访问的博客就是托管在s3上的，速度还不错吧？

注册之前需要准备：

  * 国际信用卡（visa或者mastercard），跟apple id一样，先绑定，会扣除1美元手续费（不知道会不会还我），后续会按需扣费 
  * 手机，会有电话验证，机器打电话过来的时候输入4位pin即可 
  * 英语知识，因为页面大部分都是英文的 

然后就可以了，另外之前github-pages是自带 [ jekyll ](https://github.com/mojombo/jekyll) ，所以我把
源文件push到github就会自动生成_sites静态页，而现在s3就是资源托管而已，所以我在本地安装jekyll把源码（基本上是markdown语言，y
aml语法，还有liquid语法）之后先生成静态_sites（也就是静态文件，html），再上传到s3文件夹。

最后就是绑定顶级域名，自己在s3新建一个名为域名的bucket，比如我就是yuguo.us，然后在dns设置那里选择我的域名（也就是@）cname到 `
yuguo.us.s3-website-us-east-1.amazonaws.com. ` ，推荐使用 [ dnspod
](https://www.dnspod.cn)
的托管服务，非常方便设置，并且会有监控短信提醒，生效也非常快，我在godaddy买的域名，dns全部托管在dnspod。

有什么问题可以留言问我。

[ 残忍的COC哲学 → ](/weblog/coc-and-life/) [ ← 缓存和NSURLConnection ](/weblog
/caching-and-nsurlconnection/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

