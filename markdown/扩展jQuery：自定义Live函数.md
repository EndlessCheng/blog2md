#  扩展jQuery：自定义Live函数

[ Yuguo ](http://yuguo.us) 2011年 04月 27日

平时在使用jQuery进行AJAX操作的时候，新生成的元素事件会失效，有时候不得不重新绑定一下事件，但是这样做很麻烦。jQuery1.3增加了一个live(
)方法，下面是手册上的说明：

> jQuery 1.3中新增的方法。给所有当前以及将来会匹配的元素绑定一个事件处理函数（比如click事件）。也能绑定自定义事件。

目前支持 click, dblclick, mousedown, mouseup, mousemove, mouseover, mouseout,
keydown, keypress, keyup。

还不支持 blur, focus, mouseenter, mouseleave, change, submit

与bind()不同的是，live()一次只能绑定一个事件。

这个方法跟传统的bind很像，区别在于用live来绑定事件会给所有当前以及将来在页面上的元素绑定事件(使用委派的方式)。比如说，如果你给页面上所有的li用l
ive绑定了click事件。那么当在以后增加一个li到这个页面时，对于这个新增加的li，其click事件依然可用。而无需重新给这种新增加的元素绑定事件。</
blockquote><pre>.live( eventType, handler )

eventType 包含JavaScript事件类型的一个字符串，比如“click”和“keydown”。

自从jQuery1.4以后字符串能包含多个由空格隔开的事件类型，也能包含自定义类型的名字。

handler 回调函数。</pre> live的第一个参数是触发live的事件类型，举个例子：

1.对于一个在页面上新增的div元素，希望让它拥有droppable的能力，那么直接写

` $('div').droppable({...}) `

是不会生效的，因为在调用这句代码的时候，这个新增的div还没有被创建，所以被创建之后的它没有droppable的能力。

2.如果写

    
    
    ``$('div').live('mouseover',function({
    
    $(this).droppable({...});
    
    }));``
    

则会在这种情况下生效：创建了这个div之后，鼠标滑过div，那么live事件触发，这个div拥有了droppable能力。

在这种情况下暂时不生效：创建了这个div之后，这个div还不拥有droppable能力，这时候它不会接受拖拽过来的draggable，除非进行（至少）一次上
面的操作。

3.如果写

    
    
    ``$('div').live('myCustomEvent',function({
    
    $(this).droppable({...});
    
    }));
    
    $(".draggable_object").mouseover(function () {
    
    $("div").trigger("myCustomEvent");
    
    });``
    

这样就会出现在这种情况下生效：创建了这个div之后，鼠标滑过一个含有class：.draggable_object的页面元素之后，所有的div都触发myCu
stomEvent事件，而这个事件会导致所有的div都会重新具有droppable的能力。

在这种情况下暂时不生效：创建这个div之后，鼠标不滑过.draggable_object的页面元素，这个时候新建的div不具有droppable能力。

4.在某种情况下，我们经常需要做live的操作，让我们更进一步，扩展jQuery的方法。

    
    
    ``jQuery.fn.liveDroppable = function(opts){
    
    this.live("myCustomEvent",function(){
    
    if(!$(this).data("init")){$(this).data("init",true).droppable(opts)};
    
    });
    
    }
    
    $(".draggable_object").mouseover(function () {
    
    $("div").trigger("myCustomEvent");
    
    });``
    

现在，可以不再使用：

    
    
    ``$(selector).draggable({opts});``
    

用下面的代码代替：

    
    
    ``$(selector).liveDraggable({opts})``
    

在实际项目中需要灵活运用各种方法来实现live。

[ 为什么飞机票越到后面买越贵 → ](/weblog/air-ticket/) [ ← 第三节羽毛球课 ](/weblog/badminton-3/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

