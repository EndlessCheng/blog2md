#  15条JavaScript最佳实践

[ Yuguo ](http://yuguo.us) 2013年 01月 03日

本文档整理大部分公认的、或者少有争议的JavaScript良好书写规范（Best
Practice）。一些显而易见的常识就不再论述（比如要用对象支持识别判断，而不是浏览器识别判断；比如不要嵌套太深）。条目顺序按重要级粗略的从高到低排列。

##  把外部JavaScript文件放在HTML底部

我们的目标是相同的：为用户尽可能快地显示内容。当载入一个脚本文件的时候，HTML会停止解析，直到脚本载入完毕。因此，用户可能会长时间对着一个空白的屏幕，看上
去什么都没有发生。如果你的JavaScript代码只是增加一些功能（比如按钮的点击动作），那么尽管大胆地把文件引用放在HTML底部吧（就在</body>之前
），你会看到明显的速度提升。如果是用于其他目的的脚本文件，则需要慎重地考虑。但无论如何，这毫无疑问是一个非常值得考虑的地方。

##  优化循环

循环遍历一个数组

    
    
    //这段糟糕的代码会在每次进入循环的时候都计算一次数组的长度
    
    var names = ['George','Ringo','Paul','John'];
    
    for(var i=0;i<names.length;i++){
    
      doSomeThingWith(names[i]);
    
    }
    
    
    
    //这样的话，就只会计算一次了
    
    var names = ['George','Ringo','Paul','John'];
    
    var all = names.length;
    
    for(var i=0;i<all;i++){
    
      doSomeThingWith(names[i]);
    
    }
    
    
    
    //这样就更加简短了
    
    var names = ['George','Ringo','Paul','John'];
    
    for(var i=0,j=names.length;i<j;i++){
    
      doSomeThingWith(names[i]);
    
    }
    
    
    
    //这段代码的糟糕之处在于，它把变量声明放在循环体内了，每次循环都会创建变量
    
    for(var i = 0; i < someArray.length; i++) {
    
       var container = document.getElementById('container');
    
       container.innerHtml += 'my number: ' + i;
    
       console.log(i);
    
    }
    
    
    
    //在循环体外声明变量，变量只会创建一次
    
    var container = document.getElementById('container');
    
    for(var i = 0, len = someArray.length; i < len;  i++) {
    
       container.innerHtml += 'my number: ' + i;
    
       console.log(i);
    
    }
    

##  用尽量简短的代码

如果可以增加可读性的话，那么使用代码的简短格式是有意义的，下面是一份不完全的列表：

    
    
    //对于条件判断只有两次的，这是一种冗长的写法
    
    var direction;
    
    if(x > 100){
    
      direction = 1;
    
    } else {
    
      direction = -1;
    
    }
    
    
    
    //更好的代码
    
    var direction = (x > 100) ? 1 : -1;
    
    
    
    //判断一个 变量是否定义，如果否，就赋予一个值，糟糕的代码
    
    if(v){
    
      var x = v;
    
    } else {
    
      var x = 10;
    
    }
    
    
    
    //更好的代码
    
    var x = v || 10;
    
    
    
    //重复了变量名很多次
    
    var cow = new Object();
    
    cow.colour = 'brown';
    
    cow.commonQuestion = 'What now?';
    
    cow.moo = function(){
    
      console.log('moo');
    
    }
    
    cow.feet = 4;
    
    cow.accordingToLarson = 'will take over the world';
    
    
    
    //更好的写法是这样
    
    var cow = {
    
      colour:'brown',
    
      commonQuestion:'What now?',
    
      moo:function(){
    
        console.log('moo);
    
      },
    
      feet:4,
    
      accordingToLarson:'will take over the world'
    
    };
    
    
    
    //重复了很多次数组名
    
    var aweSomeBands = new Array();
    
    aweSomeBands[0] = 'Bad Religion';
    
    aweSomeBands[1] = 'Dropkick Murphys';
    
    aweSomeBands[2] = 'Flogging Molly';
    
    aweSomeBands[3] = 'Red Hot Chili Peppers';
    
    aweSomeBands[4] = 'Pornophonique';
    
    
    
    //更好的代码
    
    var aweSomeBands = [
    
      'Bad Religion',
    
      'Dropkick Murphys',
    
      'Flogging Molly',
    
      'Red Hot Chili Peppers',
    
      'Pornophonique'
    
    ];
    

##  单引号和双引号

为了避免混乱，我们建议在HTML中使用双引号，在JavaScript中使用单引号。

    
    
    //html
    
    <img src="picture.gif" />
    
    
    
    //JavaScript
    
    <script type="text/javascript">
    
    document.write('<p>');
    
    </script>
    
    
    
    //一段混用的jQuery代码
    
    $('h1').after('<div id="content"><h2>目录</h2><ol></ol></div>');
    

##  避免混入其他技术

CSS:假设我们的页面上有必须填入的输入框（拥有class“mandatory”），如果它没有被输入数据，周围就会加上红色边框。

    
    
    //一段混合了其他技术的代码会这样做：
    
    var f = document.getElementById('mainform');
    
    var inputs = f.getElementsByTagName('input');
    
    for(var i=0,j=inputs.length;i<j;i++){
    
      if(inputs[i].className === 'mandatory' &&
    
         inputs[i].value === ''){
    
        inputs[i].style.borderColor = '#f00';
    
        inputs[i].style.borderStyle = 'solid';
    
        inputs[i].style.borderWidth = '1px';
    
      }
    
    }
    
    
    
    //一段良好的代码会这么做：将风格化的事情交给CSS吧
    
    var f = document.getElementById('mainform');
    
    var inputs = f.getElementsByTagName('input');
    
    for(var i=0,j=inputs.length;i<j;i++){
    
      if(inputs[i].className === 'mandatory' &&
    
         inputs[i].value === ''){
    
        inputs[i].className += ' error';
    
      }
    
    }
    

HTML:假设我们有内多HTML内容需要用JavaScript来载入，那么使用Ajax载入单独的文件，而不是通过JavaScript处理DOM，后者会让代码
难以处理，并且出现难以维护的兼容性问题。

##  验证JavaScript代码

浏览器处理JavaScript代码可能会非常宽容，但我建议你不要依赖浏览器的解析能力，因此养成了懒散的编码习惯。

最简单的检测你的代码质量的方法是通过一个在线JavaScript验证工具 [ JSLint ](http://www.jslint.com/) 。

“JSLint takes a JavaScript source and scans it. If it finds a problem, it
returns a message describing the problem and an approximate location within
the source. The problem is not necessarily a syntax error, although it often
is. JSLint looks at some style conventions as well as structural problems. It
does not prove that your program is correct. It just provides another set of
eyes to help spot problems.”  
– JSLint Documentation

##  使用更简单的格式来写innerscript

    
    
    //早期的代码可能是这样的
    
    <script type="text/javascript" language="javascript">
    
    ...
    
    </script>
    
    
    
    //现在不用language属性了
    
    <script type="text/javascript">
    
    ...
    
    </script>
    

##  总是检查数据

要检查你的方法输入的所有数据，一方面是为了安全性，另一方面也是为了可用性。用户随时随地都会输入错误的数据。这不是因为他们蠢，而是因为他们很忙，并且思考的方式
跟你不同。用typeof方法来检测你的function接受的输入是否合法。

    
    
    //如果members的类型不是数组，那么下面的代码会抛出一个错误
    
    function buildMemberList(members){
    
      var all = members.length;
    
      var ul = document.createElement('ul');
    
      for(var i=0;i
    
    
    //良好的习惯是检查参数是否是一个数组
    
    function buildMemberList(members){
    
    //数组的typeof是object，所以如果要判断是否为数组的话，可以测试它是否拥有数组才有的function：slice
    
      if(typeof members === 'object' &&
    
         typeof members.slice === 'function'){
    
        var all = members.length;
    
        var ul = document.createElement('ul');
    
        for(var i=0;i

另一个安全隐患是直接从DOM中取出数据使用。比如说你的function从用户名输入框中取得用户名做某项操作，但用户名中的单引号或者双引号可能会导致你的代码崩
溃。

##  避免全局变量

全局变量和全局函数是非常糟糕的。因为在一个页面中包含的所有JavaScript都在同一个域中运行。所以如果你的代码中声明了全局变量或者全局函数的话，后面的代
码中载入的脚本文件中的同名变量和函数会覆盖掉（overwrite）你的。

    
    
    //糟糕的全局变量和全局函数
    
    var current = null;
    
    function init(){...}
    
    function change(){...}
    
    function verify(){...}
    

解决办法有很多， [ Christian Heilmann ](http://dev.opera.com/author/1037557) 建议的方法是：

    
    
    //如果变量和函数不需要在“外面”引用，那么就可以使用一个没有名字的方法将他们全都包起来。
    
    (function(){
    
      var current = null;
    
      function init(){...}
    
      function change(){...}
    
      function verify(){...}
    
    })();
    
    
    
    //如果变量和函数需要在“外面”引用，需要把你的变量和函数放在一个“命名空间”中
    
    //我们这里用一个function做命名空间而不是一个var，因为在前者中声明function更简单，而且能保护隐私数据
    
    myNameSpace = function(){
    
      var current = null;
    
      function init(){...}
    
      function change(){...}
    
      function verify(){...}
    
      //所有需要在命名空间外调用的函数和属性都要写在return里面
    
      return{
    
        init:init,
    
        //甚至你可以为函数和属性命名一个别名
    
        set:change
    
      }
    
    }();
    

##  声明变量的话，总是用var

JavaScript中的变量可能是全局域或者局部域，用var声明的话会更加直观。

    
    
    //在function中不用var引起的迷惑性问题
    
    var i=0; // This is good - creates a global variable
    
    function test() {
    
      	 for (i=0; i<10; i++) {
    
          	alert("Hello World!");
    
      	 }
    
    }
    
    test();
    
    alert(i); // The global variable i is now 10!
    
    
    
    //解决方法是在function中声明变量也用var
    
    function test() {
    
      	 for (var i=0; i<10; i++) {
    
          	alert("Hello World!");
    
      	 }
    
    }
    

##  使用前置+号来把字符串转化为数字

JavaScript中，“+”操作符即被用来作为数字加，也被用来连接字符串。如果需要求表单中几个值的和，那么用+可能会出现问题。

    
    
    //会出现问题的代码
    
    <form name="myform" action="[url]">
    
    <input type="text" name="val1" value="1">
    
    <input type="text" name="val2" value="2">
    
    </form>
    
    function total() {
    
    	var theform = document.forms["myform"];
    
    	var total = theform.elements["val1"].value + theform.elements["val2"].value;
    
    	alert(total); // This will alert "12", but what you wanted was 3!
    
    }
    
    
    
    //在字符串前面加上“+”，这是给JavaScript的一个暗示：这是一个数字而不是字符串
    
    function total() {
    
    	var theform = document.forms["myform"];
    
    	var total = (+theform.elements["val1"].value) + (+theform.elements["val2"].value);
    
    	alert(total); // This will alert 3
    
    }
    

##  避免使用eval()方法

JavaScript中的eval()方法是在运行时把任何代码当作对象来计算/运行的方法。实际上由于安全性的缘故，大部分情况下都不应该用eval()，总是有一
种更“正确”的方法来完成同样的工作的。基本原则是，eval is evil，在任何时候都不要用它，除非你是一个老手，并且知道你不得不这样做。

##  for in语句

遍历一个对象中的所有条目的时候，用for in语句是非常方便的。但有时候我们不需要遍历对象中的方法，如果不需要的话，可以加上一条filter。

    
    
    //加上了一个过滤器的for in语句
    
    for(key in object) {
    
       if(object.hasOwnProperty(key) {
    
          ...then do something...
    
       }
    
    }
    

##  不要偷懒省略”和{}

从技术上说，你可以忽略很多花括号和分号。

    
    
    //虽然看上去很不对头，大部分浏览器都能正确解析这段代码
    
    if(someVariableExists)
    
      x = false
    
    
    
    //这个代码看上去更不对头了，咋眼一看似乎下面的句都被执行了
    
    //实际上只有x=false在if中
    
    if(someVariableExists)
    
       x = false
    
       anotherFunctionCall();
    

所以，要记住的原则是：1.永远不要省略分号；2.不要省略花括号，除非在同一行中。

    
    
    //这样是OK的
    
    if(2 + 2 === 4) return 'nicely done';
    

##  获取对象属性的时候用方括号而不是点号

在JavaScript中取得某对象的属性有两种方法：

    
    
    //点号标记
    
    MyObject.property
    
    
    
    //方括号标记
    
    MyObject["property"]
    

如果是用点号标记取得对象的属性，属性名称是硬编码，无法在运行时更改；而用方括号的话，JavaScript会求得方括号内值然后通过计算结果来求得属性名。也就是
说用方括号标记的方式，属性名称可以是硬编码的，也可以是变量或者函数返回值。

    
    
    //这样是不行的
    
    MyObject.value+i
    
    
    
    //这样就没有问题
    
    MyObject["value"+i]
    

##  假设JavaScript会被禁用

我知道这样的假设会伤害JavaScript开发者的感情，可是在目前数据不明朗的情况下我们为了安全起见应该做这样的假设。这是渐进增强中很重要的一部分。

##  使用JavaScript库

现在有很多非常流行的JavaScript库，比如YUI和jQuery、Dojo。它们的缺点是需要下载一个额外的文件，优点却更多：兼容性更强；代码更简单易懂。
好的库有很多，但你不应该在一个项目中把它们都用上，因为可能存在兼容性问题。选择一个自己习惯的就好。

不要忘记的一点是，原生的JavaScript毫无疑问更快，如果是小规模的使用，最好还是用原生的。

[ 那个什么都懂的家伙 → ](/weblog/a-list-of-three/) [ ← WordPress迁移到github(jeykll)
](/weblog/wordpress-to-jeykll/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

