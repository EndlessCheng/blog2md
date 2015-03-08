#  Win8 UI web design kit

[ Yuguo ](http://yuguo.us) 2011年 11月 06日

  * 之前有分享一个Win8 UI的PSD。这几天做了一套类似的web界面，demo地址是 [ http://win8ui.sinaapp.com/ ](http://win8ui.sinaapp.com/)
  * <del> demo是完全开源的，可以通过SVN地址来checkout源码： [ https://svn.sinaapp.com/win8ui/ ](https://svn.sinaapp.com/win8ui/) </del> （需要权限才能checkout，我以为默认跟google code一样开放checkout，那需要checkout的留言留下邮箱吧，真不方便） 
  * 图标如果希望自定义，可以自己找矢量图，选择实角风格的图标会好一些 
  * SAE注册免费，也可以多人合作，希望跟我拉分支的可以留言让我开权限。如果没有注册可以用我的邀请链接：  [ http://sae.sina.com.cn/activity/invite/36052/weibo ](http://sae.sina.com.cn/activity/invite/36052/weibo)

[ ![Win8 ui web design](http://yuguo.us/files/2011/11/QQ拼音截图未命名.png)
](http://win8ui.sinaapp.com/) 这里是一些技术要点：（博客文章更新不如SVN更新方便，所以，一切以源码为最新最准）

  * 采用 [ Responsive Web Design ](http://www.qianduan.net/responsive-web-design.html) 的设计方式，在手机上上、ipad上、超大屏幕上会看到不同的排版设计。 
  * 采用CSS3的3D API来实现小图片跟文字的翻转，完全无脚本（用最新版的Chrome看效果）。 
  * 图片icon采用了i标签，而不是img标签，方便合并雪碧图。源码及外网未合并图片，因为SAE没有源码环境和发布环境的区别。但是我已经把可以合并的图片已经在slice文件夹，可以通过 [ CssGaga ](http://www.99css.com/archives/542) 一键合并雪碧图。合并过后图片请求只会有两个，一个合并图，一个背景2x2px的小图。 
  * 未测Chrome和IE8之外的浏览器，如有兼容性问题或者建议，请留言告知。 

[ 众妙之门——The Smashing Book → ](/weblog/the-smashing-book/) [ ← Windows8
UI给web设计的启示 ](/weblog/web-design-inspired-by-windows-8-ui/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

