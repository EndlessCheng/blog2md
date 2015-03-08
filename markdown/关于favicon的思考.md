#  关于favicon的思考

[ Yuguo ](http://yuguo.us) 2013年 01月 29日

.ico是一种什么样的格式？

> ico是微软的Windows下面的图标格式，这种文件的特点是在一个ico文件中储存多个图标图层信息，每个图标图层可以拥有不同的尺寸和位深。桌面程序都接受
一个ico文件作为应用程序图标，在web端，Windows也沿用了这个方法。

.ico支持Alpha通道吗？

> 图层的位深采用32位图片（RGBA）储存时，支持Alpha通道。

使用favicon.ico作为图标是开放标准吗？

> 不是标准。

>

> 微软支持的link标签不遵从World Wide Web Consortium（W3C，万维网联盟）的HTML建议[1]，因为：

>

>   1. rel属性必须包含一个用空格作分隔符的link类型的列表，所以一个包含两词的link类型不能被遵守标准的浏览器理解。

>

>   2. “.ico”文件类型（一种用于Microsoft Windows上图标的光栅格式）没有一个注册的MIME类型，而且似乎在当时也不能被多数浏览器
理解。然而2003年，这一格式在IANA获得注册，其MIME类型是image/vnd.microsoft.icon，进而消除了此问题的第一部分。

>

>   3. 在网站上使用保留地址（reserved location）与Architecture of the World Wide
Web（互联网的结构）矛盾，同时被认为是link squatting（链接劫持）或URI squatting（URI劫持）。

.ico中的图层有多少种位深？各自兼容性如何？

> 按照从大到小的顺序：

>

> RGB / Alpha Channel(RGB/A -32 bits)

>

> True Colors(RGB - 24 bits)

>

> 256 Indexed Colors(8 bits)

>

> 16 Colors(4 bits)

>

> Monochrome(1 bit)

>

> 兼容性：IE6以上浏览器都支持各种位深。

使用favicon的高级场景有哪些？

> 一种是Windows 7的IE9的pin bar，会在工具栏生成一个网站的快捷方式，需要的尺寸是32x32，所以如果使用16x16的图片，会有一个白边，
很难看。但实际上这样操作的用户并不多，除非用户是你的网站的铁杆粉丝，并且知道这一操作。

>

> 另一种是Retina上的浏览器在标签栏显示，会需要32x32的图片。

我可以给IE8以下使用16x16的图片，而给Retina，IE9使用32x32的图片吗？

> 可以的，方法是在 ` <head> ` 标签中指定一个32x32的png图片，IE8-不支持：

>

> ` <link rel='icon' href='images/favicon.png' type='image/png' /> `

>

> 然后在你的根目录仍然放一个16x16的favicon.ico。这样不认识png的IE就可以使用ico文件。

>

> 但是这样做没有太大的现实意义。

使用16x16和32x32图片分离的办法有什么实际意义？

> 没什么实际意义。

>

> 因为从流量上来看，节省的2-3k图片可以直接忽略，比起内容中的图片，还有各种样式、脚本中的冗余样式，2-3k显得太小了。从加载速度上看也没有什么意义，因
为favicon最后加载，不会阻塞页面渲染（就像css和js那样）。

>

> 而且这增加了开发人员的维护成本。

>

> 这也是为什么世界知名的网站，比如google.com会直接使用一个包含了16x16和32x32的favicon.ico。

那你推荐的最佳实践是什么？

> 推荐使用同一个16x16和32x32的ico。使用PS，32px的png直接保存ico就可以生成这两个图层，默认位深为32位（RGBA）。

怎样单独编辑16x16的图层？

> 专门的图标编辑器，比如Iconworkshop就很好用，可以单独编辑某个尺寸图层。

[ webview页面制作经验 → ](/weblog/mobile-slice-font/) [ ← git子模块 ](/weblog/git-
submodule/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

