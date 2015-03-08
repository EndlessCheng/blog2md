#  CSS3 @font-face 语法分析

[ Yuguo ](http://yuguo.us) 2012年 07月 30日

使用CSS3自定义字体的时候，为了兼容所有浏览器，服务器需要输出4种格式的字体，分别是eot、svg、ttf和woff。

CSS代码：

    
    
    @font-face {
     font-family: 'qzficon';
     src: url('font/qzficon-regular.eot'); /* IE9兼容模式 */
     src: url('font/qzficon-regular.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
     url('font/qzficon-regular.woff') format('woff'),
     url('font/qzficon-regular.ttf') format('truetype'), /* Chrome,Firefox 3.5 and Safari */
     url('font/qzficon-regular.svg#qzficon') format('svg'); /* Google Chrome, Opera 9, and the iPhone. */
     font-weight: normal;
     font-style: normal;
    }
    

.qzficon{font-family:qzficon;}

那么这几种格式分别支持哪些浏览器，顺序为什么是这样的？

这个@font-face里实际上有两条src属性定义，按照CSS的层叠覆盖规则，后面的属性会把前面的覆盖（todo
除非浏览器不支持后面的值，会认为该值非法而完全忽视它）。

而且按照CSS3的@font-face属性定义，一条属性可以支持多个值，用逗号分隔，多个属性同时生效。W3C标准是这样的：

    
    
    [ &lt;uri&gt; [format(&lt;string&gt; [, &lt;string&gt;]*)] | &lt;font-face-name&gt; ] [, &lt;uri&gt; [format(&lt;string&gt; [, &lt;string&gt;]*)] | &lt;font-face-name&gt; ]*
    

此描述指定了资源中包含的字体数据。无论字体是下载的或者是本地安装的，这个描述都是必需的，以逗号作为分隔的外部引用或本地安装的字体名称的列表中各值的优先级依次
递减。当遇到不合理的数据则被当作未找到字体处理。

##  造成的影响

若在使用 ‘@font-face’ 规则时仅仅考虑一种字体格式，则可能在某些浏览器中无法应用规则所引入的字体。

##  受影响的浏览器

IE6  |  仅支持 Embedded OpenType(.eot) 格式。  
---|---  
IE7  |  仅支持 Embedded OpenType(.eot) 格式。  
IE8  |  仅支持 Embedded OpenType(.eot) 格式。  
Firefox 3.5  |  支持 TrueType、OpenType(.ttf, .otf) 格式。  
Firefox 3.6  |  支持 TrueType、OpenType(.ttf, .otf) 及 WOFF 格式。  
Chrome  |  支持 TrueType、OpenType(.ttf, .otf) 及 SVG Font(.svg) 格式。  
Safari  |  支持 TrueType、OpenType(.ttf, .otf) 及 SVG Font(.svg) 格式。  
Opera  |  支持 TrueType、OpenType(.ttf, .otf) 及 SVG Font(.svg) 格式。  
  
##  两个EOT

看上面的代码我们会发现声明了两次EOT文件，而且语法不相同，原因是：

IE6-8都只支持eot这种格式，同时在src的解析上也采用了一种很挫的解析语法：如果你在src中声明了多个字体格式，IE会在载入字体的时候直接404，原因
是IE6-8会试图把最开始的圆括号到最后一个圆括号中间的所有东西当作一个字体来载入。为了应对这种错误的行为，我们可以在eot结束之后加上一个问号?来糊弄IE
6-8，让它认为问号后面的都是url的请求参数然后就只会载入EOT文件。其他现代浏览器会遵循规范的指引，分别解析多种format，选择自己支持的字体。

本来只要后面这条定义，看上去就OK了。但是当IE9以兼容模式运行的时候，浏览器仍然会解析EOT而不是WOFF字体，并且它还修复了我们的hack……所以必须为
这种模式再声明一句src，放在句首。

[ http://www.fontspring.com/blog/the-new-bulletproof-font-face-syntax
](http://www.fontspring.com/blog/the-new-bulletproof-font-face-syntax)

随后为了解决IE9兼容性的fix： [ http://www.fontspring.com/blog/further-hardening-of-the-
bulletproof-syntax ](http://www.fontspring.com/blog/further-hardening-of-the-
bulletproof-syntax)

[ http://w3help.org/zh-cn/causes/RF1001 ](http://w3help.org/zh-
cn/causes/RF1001)

[ http://stackoverflow.com/questions/4607560/font-face-works-in-ie8-but-not-
ie9 ](http://stackoverflow.com/questions/4607560/font-face-works-in-ie8-but-
not-ie9)

[ CSS3字体的MIME TYPE → ](/weblog/css3-font-mime-type/) [ ← 开源代码 ](/weblog/open-
source-code/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

