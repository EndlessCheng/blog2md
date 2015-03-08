#  14条关于jQuery的知识【上】

[ Yuguo ](http://yuguo.us) 2010年 09月 17日

边翻译这篇文章，变学习一下周边知识，所以效率不太高，先放出上部分：前7条。

以下是译文

如果说jQuery也有缺点，那就是它太容易上手了，所以吸引了大量没有任何JavaScript的新手来使用。一方面来说，这真的很神奇。另一方面，这也导致了一大
堆糟糕的代码诞生（有一些是出自我手！）

但是没关系，糟糕的代码是你的成年礼，关键是要越过这道坎，这就是今天要讨论的内容。

##  1.一些方法会返回jQuery对象

大多数方法会返回jQuery对象。这是很棒的特性，使得我们的代码可以像锁链一样从头到尾链起来。

    
    
    $someDiv
    
    .attr('class', 'someClass')
    
    .hide()
    
    .html('new stuff');
    

这样做的好处是：1.代码更加简洁 2.减少了我们必须遍历整个DOM来寻找这个元素的时间

##  2.The Find Selector

只要你的选择符不要烂的跟屎一样，jQuery都能帮你方便地找到需要的元素，你不需要操心细节。但是有一些细节你可以注意一下，以此来提高你的JavaScript
执行性能。

其中之一就是，只要有可能，就使用.find()方法。主要原因就是：如果不是逼不得已，那就不要让jQuery使用它的Sizzle引擎。当然，也会有些情况不能用
find()方法，那也没有关系，只要知道有这个区别就好。

    
    
    // 在现代浏览器上都可以正常运行，但是却是通过Sizzle引擎来完成的
    
    $('#someDiv p.someClass').hide();
    
    // 一样正常运行，原生浏览器支持，效率更高
    
    $('#someDiv').find('p.someClass').hide();
    

_ 除IE6/7的现代浏览器_都有_QuerySelectorAll_支持，能允许你传递一个像一样的CSS选择器，而不需要用到jQuery的内部代码。jQu
ery会在使用自己的引擎之前检查是否存在这个函数。 _但对于IE6/IE7而言 _ ，就会需要jQuery使用Sizzle引擎，这是一套十分强大的引擎，但非
常复杂。简单的说，jQuery会把你的选择器转化成一个数组，并且通过从后往前的方法来迭代匹配。

    
    
    // 数组
    
    ['#someDiv, 'p'];
    

它会从右到左，通过正则表达式匹配页面每一个元素，也就是说， _ 你的选择器最右边一定要尽可能的明确 _ ，比如_ID或者标签名_。

底线是：

1.保持代码简单

2.使用find()方法，这样的话，我们就能够使用浏览器的原生查找函数

3.当使用Sizzle的时候，尽可能地把最右边的部分指明，比如ID或者标签名

##  3.不要滥用$(this)

如果不了解基本的DOM属性和方法的话，很容易滥用jQuery对象。例如

    
    
    $('#someAnchor').click(function() {
    
    	// 又生成了一次jQuery对象
    
    	alert( $(this).attr('href') );
    
    });
    

如果只是为了获取某a的href属性可以简单地用以下代码：

    
    
    $('#someAnchor').click(function() {
    
    	// 没有jQuery对象
    
    	alert( this.href );
    
    });
    

##  4.jQuery的快速ready方法

原生的ready方法是这样的

    
    
    $(document).ready(function() {
    
    	// let's get up in heeya
    
    });
    

而jQuery的方法是这样的：

    
    
    $(function() {
    
    	// let's get up in heeya
    
    });
    

看上去有点困扰+不放心？别担心，看看jQuery的源码：

    
    
    // HANDLE: $(function)
    
    // Shortcut for document ready
    
    if ( jQuery.isFunction( selector ) ) {
    
    	return rootjQuery.ready( selector );
    
    }
    

完全一样的哦

##  5.代码安全

如果希望代码能和其他人协同工作的话，一定要确保不要命名冲突。万一在你的脚本之后导入了其他人的代码，对方用到了$变量，那该怎么办呢？

第一种方法，noConflict()方法：

    
    
    var j = jQuery.noConflict();
    
    // Now, instead of $, we use j.
    
    j('#someDiv').hide();
    
    // The line below will reference some other library's $ function.
    
    $('someDiv').style.display = 'none';
    

第二种方法，把你的代码放在一个匿名函数里面，然后把jQuery作为参数传递给它，那么在这个函数体中的$是不会影响外面或者被外面影响的。

    
    
    (function($) {
    
    	// Within this function, $ will always refer to jQuery
    
    })(jQuery);
    

第三种方法，

    
    
    jQuery(document).ready(function($) {
    
     // $ refers to jQuery
    
    });
    
    // $ is either undefined, or refers to some other library's function.
    

##  6.写聪明的代码

    
    
    someDivs.each(function() {
    
    	$('#anotherDiv')[0].innerHTML += $(this).text();
    
    });
    

以上代码的_糟糕_之处在于：

1.在_每一次遍历循环_中都会搜寻anotherDiv 这个ID的元素

2._两次_获取innerHTML属性

3.创建了一个_jQuery对象_，只是为了获取元素的text属性

    
    
    var someDivs = $('#container').find('.someDivs'),
    
          contents = [];
    
    someDivs.each(function() {
    
    	contents.push( this.innerHTML );
    
    });
    

$(‘#anotherDiv’).html( contents.join(‘’) );

这样，在每一个遍历循环中所做的操作仅仅是把元素放进一个数组中。这一条tip更适用于所有的JavaScript代码，而不仅仅是jQuery。

说到这儿，就不得不提一下Document编程（Document Fragments），基本上也是说， _ 用原生的js对象，而不是jQuery对象 _
，更有效率。

    
    
    var someDivs = $('#container').find('.someDivs'),
    
          contents = [];
    
    someDivs.each(function() {
    
    	contents.push( this.innerHTML );
    
    });
    
    $('#anotherDiv').html( contents.join('') );
    

越久使用jQuery和JavaScript，你就会发现你更喜欢用js完成某些简单任务，多好！

jQuery提供了一个很高的抽象程度，但这不意味着我们应该停止学习如何使用原生的js方法，例如上面的代码中我们就用了jQuery的each方法。

##  7.Ajax方法

一个新手开始学习jQuery和Ajax的时候，它提供的诸多接口可能让你困扰。其实很多方法都是helper method（译者注：我专门查了下helper
method和jQuery UI里helper的区别，下一篇post详细地说一下）。我们经常用到的方法不过以下几种：

  * ** get **
  * ** getJSON **
  * ** post **
  * ** ajax ** 以下是getJSON的调用语法 

$.getJSON(‘path/to/json’, function(results) {

// callback

// results contains the returned data object

});

这是实现代码：

    
    
    getJSON: function( url, data, callback ) {
    
    return jQuery.get(url, data, callback, "json");
    
    }
    

进入下一层梦境：

    
    
    get: function( url, data, callback, type ) {
    
    // shift arguments if data argument was omited
    
    if ( jQuery.isFunction( data ) ) {
    
    	type = type || callback;
    
    	callback = data;
    
    	data = null;
    
    }
    
    return jQuery.ajax({
    
    	type: "GET",
    
    	url: url,
    
    	data: data,
    
    	success: callback,
    
    	dataType: type
    
    });
    
    }
    

最终，还是通过ajax()方法来执行这么多的操作，它是保证跨浏览器操作的基础。
_也就是说_你可以直接使用ajax()方法来完成所有的ajax操作，而不是一大堆的helper method。

原来是这样的代码：

    
    
    $.getJSON('path/to/json', function(results) {
    
    // callback
    
    // results contains the returned data object
    
    });
    

更高效（并且接口统一）的代码：

    
    
    $.ajax({
    
    type: 'GET',
    
    url : 'path/to/json',
    
    data : yourData,
    
    dataType : 'json',
    
    success : function( results ) {
    
    	console.log('success');
    
    })
    
    });
    

上半部分完，转载保留原文地址和本文地址：

原文地址：http://net.tutsplus.com/tutorials/javascript-ajax/14-helpful-jquery-
tricks-notes-and-best-practices/

本文地址：http://yuguo.us/weblog/14-jquery-notes-1/

[ 关于div/article/section的区别 → ](/weblog/div-vs-article-vs-section/) [ ←
bugfix+newfeature ](/weblog/bugfixnewfeature/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

