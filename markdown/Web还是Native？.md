#  Web还是Native？

[ Yuguo ](http://yuguo.us) 2012年 10月 02日

概述：本文主要描述的问题是，在智能手机端（ios和android），怎样提供服务是更好的方法？Web app还是Native
app？我的个人意见是在富应用上，最好是用Native app，而不是web应用。

背景：我大学有3个室友，我本科毕业后，在腾讯做前端，他们读研，后来也都走上了前端道路，但都略有其他方向的专攻，今年分别在百度和微软中国拿到了offer。所以
我们都对前端技术有比较深的感情。

以下是群里的对话，略有编辑。

Yuguo: 23:34:52

准备学ios开发。就好像刚翻译的那本书里说的，当你只有一个锤子，你看啥都是钉子，我只会前端开发，就什么问题都想用web的方式去解决，就是从技术去思考，不是从
需求。

杨继红: 23:35:26

我觉得你对需求的把握挺好的啊

Yuguo: 23:35:34

其实ios端的web页面都是辅助，最终要全部归于native app

杨继红: 23:36:01

提供数据才是最重要的？

Yuguo: 00:03:36

其实是关于平台文化的，系统平台如windows、linux、ios，都有不同的样式和习惯，做app的是和考虑这些文化，就可以做出优秀的app。web的优势是
部署一次，在所有平台都可以一致地访问，但缺点就是没有符合各平台的文化，跟java一样，是一种抽象层级更高的平台，平台之上的平台，这个平台的体验是单独抽离出来
的另一种文化。

Yuguo: 00:05:13

web（响应式，富应用）是有它的优点，但是没有针对各个系统的文化去优化，这就是它的缺点，对应项目还是要区分考虑，不能自己只有锤子就啥都当钉子。

Yuguo: 00:06:23

咱仨应该对前端技术都很有感情，都是靠这个走上工作的，但我想感情归感情，技术真正要做出好产品才靠谱。

杨继红: 00:06:31

上次听百度的工程师讲座，貌似他们正在努力做好web aqq，因为现在手机浏览器兼容html5越来越好，不像PC那么不均衡，所以以后webaqq的希望更大

Yuguo: 00:07:26

唉，我觉得用html5在手机端做太重的app是方向错了

杨继红: 00:07:29

native aqq安装和更新是瓶颈，好处就是功能强大，所以他们就在想怎么能够将强大的native aqq的功能嫁接过来

Yuguo: 00:08:27

ios比windows平台的一个很大的提升就是有统一的app
store，更新和安装都比以前更方便。而且根据数据，活跃用户更新软件、甚至更新ios版本的速度都是非常快的。

Yuguo: 00:10:03 [ http://www.chinaz.com/news/2012/0912/274067.shtml
](http://www.chinaz.com/news/2012/0912/274067.shtml) 杨继红: 00:10:08

这还有个开发周期和上线周期的问题，发布一个新版本，并且宣传用户更新是需要一个时间段的，不能做好一个小功能就更新

Yuguo: 00:10:12

扎克伯格认为，在移动策略上最大的错误是在HTML5上投入过大，而在原生应用上投入太少，这也使得Facebook的移动策略收到了影响。Facebook在两年前
确定了大力发展HTML5，但现在看起来当初的判断出现了问题。

杨继红: 00:11:01

嗯，现在很多公司就把移动端的未来压住在html5上了

Yuguo: 00:11:10

是要做，但是不要投入太多精力

杨继红: 00:11:42

现在应该都是在两方面同时进行，但是native app现在还是占据主导吧

Yuguo: 00:12:10

用web未必比原生开发周期更快，用移动框架实现模仿原生的特性终归还是要依赖框架，这不如依赖objective-c

Yuguo: 00:12:47

腾讯就有web app占据主导，而native app其次的产品，我觉得这种方向是不对的

Yuguo: 00:13:20

web app的目的是跨平台，不是取代各平台

杨继红: 00:13:50

嗯，公司希望通过这种跨平台减轻一些开发成本吧

Yuguo: 00:14:46

之前跟dowson有见面会，他谈了SNG未来战略的

杨继红: 00:14:58

每种平台都要特殊定制一种版本，对他们来说是比较浪费资源的，当前都是这样做的，但是他们希望以后能减轻这么开发成本

Yuguo: 00:15:23

就是我们的目标是产品服务在3大平台上都可以轻松取得（windows、web、mobile）

杨继红: 00:16:06

嗯，应该都是这个目标，他说了怎么来统一这些了嘛？

杨继红: 00:15:27

但是这种企求执行性暂时来说是比较小的

Yuguo: 00:16:34

对，你说的这个就是web的优势，但这样的缺点就是体验无法做到最优，在每个平台上都一般的体验，可能在每个平台上都被不同的竞争对手打败。还不如先把ios做到极致
，再扩散。

Yuguo: 00:16:52

他没有说web app和native app之争

Yuguo: 00:17:10

老板的目标是就是三大平台都可以上，方法无所谓

杨继红: 00:17:15

嗯，目前来说，web app的体验上跟native app差距比较大

最后补一个链接，Web App和Native App相结合拉动Native App的方案，我觉得这种方法很赞。 [ Promoting Apps with
Smart App Banners ](https://developer.apple.com/library/safari/#documentation/
AppleApplications/Reference/SafariWebContent/PromotingAppswithAppBanners/Promo
tingAppswithAppBanners.html#//apple_ref/doc/uid/TP40002051-CH6-SW1)

[ TO-DO驱动的阅读（以及所有事情） → ](/weblog/to-do-driven-reading-and-everything/) [ ←
jQuery模板 ](/weblog/jquery-template/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

