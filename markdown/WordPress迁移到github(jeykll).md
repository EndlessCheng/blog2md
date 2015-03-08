#  WordPress迁移到github(jeykll)

[ Yuguo ](http://yuguo.us) 2013年 01月 02日

昨天在WordPress的编辑器里写一篇关于jade语法的文章，因为有很多代码片段，有的需要格式化，有的只是要使用code标签。我在编辑模式和html模式下
各种抓狂之后，我决定放弃WordPress，使用github。这样我就可以在我喜欢的编辑器中，用我熟悉的markdown语法来写博客。

迁移需要这样几步工作：

  * 先阅读阮一峰的一篇很赞的文章 [ 搭建一个免费的，无限流量的Blog—-github Pages和Jekyll入门 ](http://www.ruanyifeng.com/blog/2012/08/blogging_with_jekyll.html)

  * 把wordpress的文章导出为静态.md，放在第一步生成的 ` _posts ` 文件夹中 

  * 对于上一步中产生的所有.md，可能会有一些非法标签，比如 ` <div> ` 这样的。用你的编辑器做一下全局性的搜索，用markdown语法替换之。 

  * 评论转移，然后用discus之类的第三方js插件实现（事实上我没有做这一步，因为不喜欢discus这种非开源的方法，我希望会有兼容gravtar的方案） 

  * 处理首页和日志页的样式 

  * feedburner支持很简单，因为之前对访客的入口是feedburner的烧录地址，所以我只需要在github根目录生成新的 [ feed.xml ](https://github.com/yuguo/yuguo.github.com/blob/master/feed.xml) ，然后再feedburner中修改源路径即可，用户感知不到这个变化。 

最后补充一些资源：

  * 了解一下很赞的 [ makrdown语法 ](http://wowubuntu.com/markdown/)

  * 修改模板的时候请参考 [ Template Data ](https://github.com/mojombo/jekyll/wiki/Template-Data)

  * 顶级域名的绑定非常方便，如果你像我一样在 [ dnspod ](http://dnspod.cn) 托管dns，那么登陆之后直接把顶级域名的A记录修改为，请参考 [ 官方指南 ](https://help.github.com/articles/setting-up-a-custom-domain-with-pages)

  * 对于html页，使用的是 [ liquid模板 ](https://github.com/shopify/liquid/wiki/liquid-for-designers)

  * 对于每篇post前面的信息，叫做 [ YAML头 ](https://github.com/mojombo/jekyll/wiki/YAML-Front-Matter) ，有一些是官方的，有一些是可以自定义，然后在liquid模板中使用 

  * 如果希望所有的新的文章路径全部跟之前的路径一样，可以在绑定了顶级域名的基础上，试试 [ 修改permalinks ](https://github.com/mojombo/jekyll/wiki/Permalinks)

  * 如果希望让一些文章为草稿，在首页不显示，但是可以通过url访问，可以参考 [ 这个问答 ](https://gist.github.com/2870636)

  * 如果希望初次加载50篇文章，滚动异步加载更多文章，可以参考 [ 用jekyll和jQuery实现异步加载文章列表 ](http://yanping.me/cn/blog/2012/10/10/asynchronous-loading-post-list-with-jekyll-and-jQuery/)

  * 除了利用github自带的jekyll实现静态页，还可以自己下载本机生成站点，参考 [ bloggering like a hacker ](http://tom.preston-werner.com/2008/11/17/blogging-like-a-hacker.html)

最后，这整个博客都是开源的，我的样式、模板、都可以直接使用，但文章内容和图片内容保留版权，请不要无良复制。

[ 15条JavaScript最佳实践 → ](/weblog/15-best-javascript-practice/) [ ←
iOS开发随笔——异步编程 ](/weblog/ios-develop-3/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

