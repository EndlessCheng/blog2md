#  CMS的能力和责任

[ Yuguo ](http://yuguo.us) 2011年 09月 27日

看到一篇很好玩而且有意义的文章： [ With Great (CMS) Power Comes Great Responsibility
](http://sixrevisions.com/user-interface/with-great-cms-power-comes-great-
responsibility/) 文章的主要观点是对现代强大的CMS的质疑：

###  CMS提供功能异常强大的后台文本编辑器（比如WYSIWYG）是否有必要？

其实WYSIWYG是与web语义化背道而驰的的。WYSIWYG带来的是更多的inline-style。牛逼而简约的编辑器只要提供以下html标签就好：

  * Heading 1 
  * Heading 2 
  * Heading 3 
  * Heading 4 (if needed) 
  * Blockquote 
  * Ordered and unordered lists 
  * Italics 
  * Bold 
  * One or two special CSS classes for emphasizing or de-emphasizing text 

让用户能自定义文本的颜色的话，页面就会乱七八糟的，如果只允许使用i和b的话，就会好很多了。

###  用户编辑CSS和HTML是否有必要？

极少数用户能熟练掌握CSS和HTML，或者能理解HTML标签的语义化。所以不应该给与太大的自由度。

###  给与的特性太多

在编辑器中加入用户不需要的特性，反而是对用户的困扰，使得他不能完成特定操作。

##  结论

作为CMS的开发者，我们需要保证用户能方便地使用工具来管理站点内容，但也要珍视他们的时间。给他们太多选择和能力的话，他们会花上更多的时间把网站搞的乱七八糟。
我们不要给与太多选项、特性，让他们困扰，而应该给出方便、一致的选项。

[ Kindle DXG越狱+汉化 → ](/weblog/kindle-dxg-jailbreak/) [ ← Instapaper Friendly
-- dos and don'ts ](/weblog/instapaper-friendly-dos-and-donts/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

