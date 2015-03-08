#  W3C Unicorn Validator 书签

[ Yuguo ](http://yuguo.us) 2010年 08月 13日

今天发现W3C推出了一个新的验证工具：Unicorn（独角兽）。这真是一个有趣的名字，传闻HTC 未来 Windows Phone 7 手机的命名规则，全系
列都将会使用艺术家的名字，比如莫扎特什么的，W3C是要走神话路线吗？据官方介绍，Unicorn是W3C的统一验证器，通过执行一系列的验证来帮助开发者改善他们
的代码。

它可以一次性验证以下几点：

  * HTML — 包括  HTML4, XHTML 和 HTML5 
  * CSS 1, 2, 2.1, 和 3 (默认版本是 2.1) 
  * SVG basic and tiny 
  * mobile device ’suitability’ 
  * feed checkers for formats including RSS and Atom 验证可以通过官方网站http://validator.w3.org/unicorn/来验证——包括输入url、上传文件、粘贴代码三种方式，也可以通过下载Java程序到本地进行验证。 

下载Java程序不太方便，我就想到做一个书签，通过点击来直接通过url验证当前页面，如果是本地文件就跳转到文件上传页面自行上传。添加方法如下：在你的浏览器（
任何支持JavaScript的浏览器）中新建一个书签：

名称：W3C Unicorn Validator

地址： ` javascript:{var%20loc=document.location.href;if(loc.length&gt;9%26%26loc
.substr(0,8)=='file:///'){document.location.href='http://validator.w3.org/unic
orn/?ucn_task=conformance&amp;ucn_lang=zh-Hans#validate-by-upload+task_conform
ance'}else{document.location.href='http://validator.w3.org/unicorn/check?ucn_t
ask=conformance&amp;ucn_uri='+escape(loc);}}void(0); ` 描述：一个W3C Unicorn验证器

OK，希望对你有用，有什么问题或者建议记得在此反馈~

PS：IE下添加收藏夹好纠结，我不得不新建一个当前页的收藏夹，然后再更改属性中的目标地址为以上代码。

转载请保留：http://yuguo.us/weblog/w3c-unicorn-validator-bookmark/

[ Tumblr是神马 → ](/weblog/a-complete-guide-to-tumblr/) [ ← 第三周流水记（王道）
](/weblog/week-3/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

