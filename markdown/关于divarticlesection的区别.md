#  关于div/article/section的区别

[ Yuguo ](http://yuguo.us) 2010年 09月 18日

关于html5中新元素section/article和div的区别，虽然有一种感觉应该用什么，但没有明确的指导。以下是html5doctor的文章中的一节，
我觉得这一节非常精准地描述了三者的区别。

篇幅越是短小，意味着原文的遣词越是精准，所以也放上原文以供批评。

原文地址： [ http://html5doctor.com/the-section-element/ ](http://html5doctor.com
/the-section-element/) 译文地址： [ http://yuguo.us/weblog/div-vs-article-vs-
section/ ](http://yuguo.us/weblog/div-vs-article-vs-section/) 以下是译文

##  使用法则

凡事有例外，但以下法则适用于99%的情况:

  * 不要用section和article作为样式化和脚本化的钩子（hook），那是div的工作 
  * 如果article更适合，不要使用section 
  * 如果在一个section里开始部分（不是之外）没有一个自然的标题，那么不要使用section 
  * [ W3C文档 ](http://www.whatwg.org/specs/web-apps/current-work/multipage/semantics.html) ： > 如果把一些内容能联合起来组成一个有意义的页面的时候，那么这一块内容应该是article而不是section。 博客文章和评论（包括作者和评论）组成了一个页面，那么它们应该是article而不是section。 

###  Rules of thumb for using section

Of course, there are always exceptions, but these should give useful guidance
for 99% of cases:

  * Don’t use it just as hook for styling or scripting; that’s a ` div `
  * Don’t use it if [ article ](http://www.whatwg.org/specs/web-apps/current-work/multipage/semantics.html#the-article-element) , [ aside ](http://www.whatwg.org/specs/web-apps/current-work/multipage/semantics.html#the-nav-element) or [ nav ](http://www.whatwg.org/specs/web-apps/current-work/multipage/semantics.html#the-nav-element) is more appropriate 
  * Don’t use it unless there is naturally a heading at the start of the section 
  * The revised spec (as of 16 September) says: > Authors are encouraged to use the article element instead of the section element when it would make sense to syndicate the contents of the element. As blogposts and comments are often syndicated (by being pulled into other blogs or being linked via twitter, reddit etc) they should be articles. 

[ 第九周流水记 → ](/weblog/week-9/) [ ← 14条关于jQuery的知识【上】 ](/weblog/14-jquery-
notes-1/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

