#  14条关于jQuery的知识【下】

[ Yuguo ](http://yuguo.us) 2010年 09月 20日

本文是 [ 《14 Helpful jQuery Tricks, Notes, and Best Practices》
](http://net.tutsplus.com/tutorials/javascript-ajax/14-helpful-jquery-tricks-
notes-and-best-practices/) 的下半部分译文，上半部分为： [ 《14条关于jQuery的知识【上】》
](http://yuguo.us/weblog/14-jquery-notes-1/) 译后记：我觉得jQuery的目标应该是三点：

  1. 让程序员写出更_优雅、清晰_的的代码 
  2. 让前端新手和设计师、重构人员_容易上手_，感受js的乐趣 
  3. 以_开放的心态_和其他类库并存 以下是译文 

##  8.获取原生js属性和方法

从之前的例子中我们学到我们可以直接取得元素比如a标签的属性： var anchor =
document.getElementById(‘someAnchor’);

    
    
    //anchor.id
    
    // anchor.href
    
    // anchor.title
    
    // .etc
    

但是当你想通过jQuery取得DOM元素的时候，是不能通过这种方法来取得属性的：

    
    
    // Fails
    
    var id = $('#someAnchor').id;
    

所以，当你需要获取href属性或者其他属性的是，你需要使用其他方法，方法很多：

    
    
    // OPTION 1 - Use jQuery
    
    var id = $('#someAnchor').attr('id');
    
    // OPTION 2 - 取到DOM元素再取值
    
    var id = $('#someAnchor')[0].id;
    
    // OPTION 3 - 用jQuery的get方法
    
    var id = $('#someAnchor').get(0).id;
    
    // OPTION 3b - 用不带参数的get
    
    anchorsArray = $('.someAnchors').get();
    
    var thirdId = anchorsArray[2].id;
    

get()方法十分有效，它能把jQuery对象集合转化成一个数组。

##  9.用PHP检测Ajax请求

事实是，在我们的大多数项目中不能依赖js来完成所有工作比如验证或者Ajax，假如js被禁用了怎么办呢？一个通用的解决办法是使用服务器端程序验证Ajax请求是
否被发起。

jQuery使得这一做法变得很简单，可以通过$.ajax方法很方便地设置请求的头部。

    
    
    // 设置头部，这样接受请求的服务器端语言知道这是一个XMLHttpRequest
    
    // Only send the header if it's not a remote XHR
    
    if ( !remote ) {
    
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    
    }
    

设置了这个头部之后，我们可以用PHP（或者其他服务器编程语言）来检查这个头部，然后相应地做出反应。用PHP的话，可以通过 `
$_SERVER['HTTP_X_REQUESTED_WITH'] ` 来判断。

    
    
    function isXhr() {
    
      return $_SERVER['HTTP_X_REQUESTED_WITH'] === 'XMLHttpRequest';
    
    }
    

##  10.jQuery和$

知道为什么jQuery和$可以互换么？看看jQuery的源码：

    
    
    window.jQuery = window.$ = jQuery;
    

由于jQuery本身运行在一个很大 的function中，这样做的好处是能最大程度地避免全局变量的出现。但也因为如此$在外面是undefined的，为了解决
这个问题，把jQuery裸露给全局变量window，同时还给它一个别名$。

##  11.根据条件载入jQuery

我们都喜欢CDN，特别是Google的免费CDN，可是让我们不使用googleapi提供的CDN的一个阻挠就是大陆功夫墙的不可预知性。但是可以这么写，是 [
HTML5 Boilerplate ](http://html5boilerplate.com/) 提供的方法：

    
    
    &lt;!-- Grab Google CDN jQuery. fall back to local if necessary --&gt;
    
    &lt;script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"&gt;&lt;/script&gt;
    
    &lt;script&gt;!window.jQuery &amp;&amp; document.write('&lt;script src="js/jquery-1.4.2.min.js"&gt;&lt;\/script&gt;')&lt;/script&gt;
    

相当直观，如果window.jQuery是未定义的，那就是说下载js文件出了问题，这时候&&右边的句子就会为ture，所以就会插入一个本地版本的jQuery
。Really brillant, isn’t it?

##  12.jQuery Filters

    
    
    &lt;scrip&gt;
    
    $('p:first').data('info', 'value'); // 填充 $的data对象，下文展示用
    
    $.extend(
    
    	jQuery.expr[":"], {
    
    		block: function(elem) {
    
    			return $(elem).css("display") === "block";
    
    		},
    
    		hasData : function(elem) {
    
    			return !$.isEmptyObject( $(elem).data() );
    
    		}
    
    	}
    
    );
    
    $("p:hasData").text("has data"); // 可以获取所有有data属性的元素
    
    $("p:block").text("are block level"); // 获取所有拥有display:block属性的元素
    
    &lt;/scrip&gt;
    

jQuery.expr[’:’]是jQuery.expr.filters的别名，上面的代码用$.extend扩展了jQuery的:也就是filter。

##  13.单参数的hover方法

在jQuery1.4之前，hover必须接受两个参数，分别显示in和out时候的handler function，而现在hover可以只接受一个参数了，每当
产生mouseenter和mouseout事件的时候就会用这个function参数（一般是匿名的）来处理，如果处理得当的话，可以用一个function就完成
两个function的效果，可以节省字符。

余果注：官方API [ http://api.jquery.com/hover/ ](http://api.jquery.com/hover/)
上有很好的例子。 [](http://api.jquery.com/hover/)

##  14.属性对象作参数

之前

    
    
    $('<a>')
    
      .attr({
    
        id : 'someId',
    
        className : 'someClass',
    
        href : 'somePath.html'
    
      });
    

现在

    
    
    $('</code></a><code>', {
    
        id : 'someId',
    
        className : 'someClass',
    
        href : 'somePath.html'
    
    });
    

jQuery1.4以后，可以在新建DOM元素的时候给它传递一个（通常是匿名的）对象作为第二个参数，这样代码更加清晰简单，我们设置可以给这个对象里面传递一些j
Query特有的属性和事件，比如click和text。

[ 960px宽的网格已经过时了？ → ](/weblog/960-grid-system-is-getting-old/) [ ← 第九周流水记
](/weblog/week-9/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

