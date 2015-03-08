#  css框架[1]-oocss

[ Yuguo ](http://yuguo.us) 2010年 09月 03日

##  不使用CSS框架的理由

  1. 不知道为什么这样做 
  2. 使用别人编写的框架，总是会落在技术的后面 
  3. 一个站点被设计出来的时候直接使用他人的框架即放弃了对布局的思考、不通过分析站点地图来提取公共模块就等于把定制布局的权利转让出去，这对个人和团队发展是非常不利的 

##  使用CSS框架的理由

通常来说使用css框架的理由有三点：

  1. 快速开发 
  2. 完美兼容 
  3. 快速上手 [ ![CSS框架搜索趋势](http://yuguo.us/files/2010/08/1.png) ](http://www.google.com/trends?q=css+framework) 关于快速上手，我觉得不是那么简单。诚然任何人可以下载一个css框架开始在实际中开始使用，可是每个CSS框架有各自的适用环境。而选择一个适合自己项目的框架（ _ 或者从不使用框架到使用框架的思维转变 _ ）需要对当前流行的大部分框架有所了解和研究。这是一个陡峭的学习曲线。基于此，我决定分别研究这些知名框架。 

##  OOCSS是什么

[ oocss ](http://oocss.org/) 是一个CSS框架，它的主要设计原则是：

1.分离struct和skin（官方用到skin这个词，这里的skin跟内容不太一样。皮肤是用来extend基本的模块的，如果不设置皮肤，页面也可以精确地显
示内容，并且内容有合理的位置和宽度和高度，但是没有特定的圆角或者颜色），这一点在后面有详细的说明

2.分离容器和内容（所有的包含了一个独立块的div都可以认为是容器【或许html5里面的Article元素可以更准确地描述”容器”这个词】，容器和内容分开，
确保布局不会因为内容的问题溢出或者错乱。并且可维护性也很强。）

##  OOCSS的文件结构

oocss包含4个基本文件和 一些扩展样式。

![OOCSS文件请求](http://yuguo.us/files/2010/09/2010-9-1-16-56-08.png)

4个基本文件包括：

libraries.css 用来定义Reset和文字的基本设置。

templete.css 用来定义头部和底部、以及中部的布局。oocss支持最多三栏布局，左右定宽之后中间会自适应。

grids.css 用来定义小范围内的浮动布局。这个很有意思的是所有的浮动条目都用百分比来定宽，并且最后一个条目.lastunit不设定宽度，这样前面的条目
过宽或者过窄的话也不会把最后一条挤下来。

content.css
是对内容和定义的样式。它对所有标题和P都加上padding:10，太有魄力了，不过这种大规模的对HTML元素定义padding，总让人觉得心里不安啊。

此外还有扩展文件。在这个 [ 官方sample ](http://oocss.org/velocity/exercise3.html) 中，除了载入上述文件
以外，还载入了两个特定的样式文件：mod.css和mod_skins.css。这两个样式根据特定项目可以自行编写，oocss只是做一个示例，告诉我们模块化是
怎么工作的。

##  OOCSS的特点

###  1.分离容器（container）和内容（content）

当我第一次用Firebug查看OOCSS的示例代码结构的时候，我有一种被震惊的感觉，然后就是长久的“我怎么没想到呢”这样的思考。

![oocss的container和content是分离的](http://yuguo.us/files/2010/09/2010-9-1-17-18-33
-copy1.png)

它把容器设置为padding:0;margin:0;这样就可以直接设置容器的宽度（像素或者百分比），而不用担心掉下去。

布局用的templete.css

###  2.mod.css这一个文件专门定义基类，而mod_skins.css用来美化基类

在编程语言中，对象是可扩展的，oocss中引进了这个概念。mod.css和mod_skins.css分别是定义基类mod和子类mod_extend的地方。

[ ![oocss的模块性](http://yuguo.us/files/2010/09/2010-9-2-20-34-591.png)
](http://yuguo.us/files/2010/09/2010-9-2-20-34-591.png)

###  3.mod具有相当的通用性

[ ![oocss中mod的结构](http://yuguo.us/files/2010/09/2010-9-3-14-27-35.png)
](http://yuguo.us/files/2010/09/2010-9-3-14-27-35.png)

mod具有通用性的一个必须的缺陷是，具有冗余代码。mod是可扩展，可拉伸的（设定不同的宽度就会以不同的宽度延展开来），这样就必须在四个角上使用空标签。ooc
ss采用空的b标签，对此，oocss的官方解释是： > 屏幕阅读器会忽略空的b标签。使用这个表象标签（b是加粗）来实现表象具有优势。这个标签可以通过服务器端
或者脚本引入，以至于有一天所有的CSS圆角和阴影都被支持了，可以关闭脚本并拥有漂亮，干净，语义化的HTML。 此外b标签超短，还能节省字节。

不过我觉得上面代码有一点不好的就是，除了mod扩展出了onlinestore之外，hd也扩展除了online类，这很奇怪。

既然onlinestore扩展自mod，那么应该假设onlinestore一定具有mod所具有的结构也就是hd，所以不需要用

.onlinestore .online {}这样来定义样式，只需要

.onlinestore .hd{}来扩展这个头部，不是吗？

###  4.注释短小实用

mod_skins.css中的注释会清晰地表明是扩展自哪个模块类，这样当需要写出class=”mod
mod_extend”这样的class的时候，就不会像class=”mod_extend”这样漏掉基类。

[ ![oocss的css注释](http://yuguo.us/files/2010/09/2010-9-3-15-44-111.png)
](http://yuguo.us/files/2010/09/2010-9-3-15-44-111.png)

###  5.下划线_IE hack

oocss使用了_width这种IE hack，对此oocss的官方解释是：

  1. 添加一个单独的样式表奖增加一个额外的HTTP请求，增加整体文件的大小，这早已是浏览器性能的对立点 
  2. 我喜欢把一个对象的代码放在一个地方。我认为这有助于减少hack的数量，尤其是当项目随时间而发展 
  3. IE6-的开发工具非常原始，这使得hack和普通代码放在一起更加重要。我想能尽快找到一个可以使用属性的IE bug。同样，我认为这有助于减少hack 
  4. 规则表明浏览器理解不了的属性会被忽略。对IE6-使用_早已众所周知，可以合理的预料好的浏览器将会忽略这个属性 
  5. 使用条件注释意味着每个HTML页面必须包含一个IE专用样式。某一天（我不能等了！）当IE6的市场份额下降至像IE5那样低时，我将去除这些代码，但最后我要做的是触及百级或千级的HTML页面。我宁愿只有依赖CSS hack的CSS，而不是把它放在HTML中。不幸的是，恕我直言，IE6兼容性的末日比我们期望的要更加长远，因为IE中的quirksmode会回落到IE5.5的模式 

##  oocss的缺点

###  1.HTTP请求教多

4个基本CSS+2个模块CSS就是6个HTTP请求，这在大公司的多PV的网页上是绝对不允许出现的。

诚然，文件多的优点是功能细分，需要修改模块样式的就不会去改grid或者content。缺点则是多余的HTTP请求导致的用户loading时间。

要解决这个问题就需要把样式合并，然后加上详细的注释。把全站需要用到的4个公共样式合并成一个，用明显的注释和空行（可以的话，给两行空行）分开。另外全站用到的m
od.css也可以合并到这个公共样式中。其它各个站点需要的剩下文件则合并到各自样式文件中。

另外介绍一下鬼哥 [ @ghostzhang ](http://t.qq.com/ghostzhang) 的 [ 模块注释
](http://www.cssforest.org/blog/index.php?id=168) ：

[ ![mod的注释](http://yuguo.us/files/2010/09/2010-9-3-16-03-10.png)
](http://yuguo.us/files/2010/09/2010-9-3-16-03-10.png)

由于合并后没有一个单独的文件保存所有的mod或者所有的mod_extend，所以需要详细的注释来标明这个mod或者mod_extend。

###  2.类命名，看上去很美

提供的sample里的class-name都太短，掩饰了其本质的复杂性，怎么说呢？

官方提供的sample里面mod.css中有两个基类提供给大家扩展，分别是mod和complex，囧，以mod命名怎么看都过于敷衍并且不具备扩展性。comp
lex更像是mod的扩展，而实际上一点都不复杂。

我想说的是，在真正的页面多、扩展多的页面中，css的命名不会很简单，sample里面出现的class=”mod
onlinestore”看上去很美，更现实的情况可能是class=”mod_box_sidebar
mod_outline_store”这样的，看上去有点纠结是不是？

###  3.没有考虑到（或者强调）免入侵性

为了避免在写CSS样式的时候出现很纠结的 > .mod_box_sidebar .mod_box_cont .mod_box_more {}
这样的的命名，一般希望在定下最开始的.mod_box_sidebar之后后面的名字少一点，否则一个样式表下来可能有一半的字节数用在定位选择器了。 >
.mod_box_sidebar .cont .more {} 是不是好的多？

但是！

有一个问题。

什么问题？

.mod_box_sidebar 中不能有嵌套模块，否则.cont这样的短命名就可能影响到它的内容中去。我称之为_容器入侵了内容。_
这就是为什么鬼哥要在模块的注释里面注明是否“可嵌套”。作为不可嵌套的模块，才能用.hd .ft这样的类名哦。

##  总结

oocss上手非常容易，扩展方便，代码不兼容W3C，不适合大型站点。

参考资料：

oocss官方： [ http://oocss.org/ ](http://oocss.org/) 涛哥翻译的oocss FAQ： [
http://www.99css.com/?p=65 ](http://www.99css.com/?p=65)
stackoverflow上关于css框架的讨论： [ What is the best CSS Framework and are they worth
the effort? ](http://stackoverflow.com/questions/203069/what-is-the-best-css-
framework-and-are-they-worth-the-effort) 当然最重要的参考资料还是Chrome的开发者工具、HttpWatch :)

PS：本来准备研究完oocss、YUI、960column之后再一起发表出来，因为只是研究一个框架的话无法全面的比较和对比数据。现在想想，还是先发出来，热烈
欢迎各位批评指点 :)

[ 第七周流水记 → ](/weblog/week-7/) [ ← 动态运营 ](/weblog/moving/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

