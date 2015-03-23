title: Responsive系列之知识储备 – SASS高阶教程（2）

date: 2013-04-04 06:45:24

tags: []

description: 

---
在上一篇[Responsive系列之知识储备 – SASS高阶教程（1）](http://blog.zhan-dui.com/?p=167)中，我带大家介绍了一些sass的高级特性。在这篇中，我将介绍另外一些比较常用的@指令。

如果你还不知道什么是sass，可以看[Responsive系列之知识储备 – SASS基础教程](http://blog.zhan-dui.com/?p=106)

## @extend

@extend 是一种扩展功能，通常用在有一定递进关系的样式中。  
比如说有两个class,一个叫 .error ,一个叫 .seriousError。很明显 .seriousError应该是 .error的一个扩展。

假设所有的 .error 都用红体字显示：
    
    
    .error{
      color:red;
    }

.seriousError不但要红体字，还要粗体！
    
    
    .seriousError{
      font-weight:bold;
    }

过去，我们通常是这样来表现这个seriousError的

…

其实这种写法并不合理，有语义学上的重叠。 seriousError本身就是一种error，而我们重复的写下error 和 seriousError 是不合理的，并且当一个div有两个class样式同时作用时，我们在维护的时候就得小心翼翼了，无疑增加了维护负担。  
我们如果能写成如下，就显得合理和精简了许多

…

但是想要写成这样，我们就得对css做一番修改。
    
    
    .error, .seriousError{
      color:red;
    }
    .seriousError{
      font-weight:bold;
    }

很明显seriousError扩展了error样式。我们前面说到的@extend指令便实现了这种开发逻辑。
    
    
    .error{
      color:red;
    }
    .seriousError{
      @extend .error; /*请留意此处的语法*/
      font-weight:bold;
    }

生成的css：
    
    
    .error, .seriousError{
      color:red;
    }
    .seriousError{
      font-weight:bold;
    }

@extend不但可以扩展class,也可以扩展伪类。
    
    
    .hoverlink {
      @extend a:hover;
    }
    a:hover {
      text-decoration: underline;
    }

生成的css如下:
    
    
    a:hover, .hoverlink {
      text-decoration: underline; }

@extend还能保持被扩展元素的父子关系。  
假使 error类下还有个 instruction 类用来显示错误的说明信息，因为字比较多的原因，为了让他能放得下，我们指定他的字体是小号的字体。
    
    
    .error{
      color:red;
    }
    .error.instruction{
      font-size:small
    }

.seriousError下自然也有关于错误的说明，也就是instruction.  
sass对此考虑周到，对父类的子类在扩展的时候也考虑了进来。
    
    
    .error{
      color:red;
    }
    .error .instruction{//instruction可以理解为error的子类
      font-size:small;
    }
    .seriousError{
      @extend .error;
      font-weight:bold;
    }

请留意生成的css:
    
    
    .error, .seriousError {
      color: red; }
    
    .error .instruction, .seriousError .instruction { //.seriousError也包含了.instruction
      font-size: small; }
    
    .seriousError {
      font-weight: bold; }

@extend同样支持多重扩展  
前面我们有了一个error和seriousError的例子，想想后来，我们又生成了一种attention的样式，为了提起人们的注意，为此我们设置了边框为红色。
    
    
    .error{
      color:red;  
    }
    
    .attention{
      border:1px solid red;
    }

现在，我们相对seriousError进行一番修改，毕竟是serious，一定要确保引起了用户的注意，因此，我们也需要将attention样式集成进来，这时多重扩展便起了作用。
    
    
    .error{
     color:red;
    }
    .attention{
     border:1px solid red;
    }
    .seriousError{
     @extend .error;
     @extend .attention;
    /*
    当然，也可以这样书写  @extend .error, .attention;
    */
     font-weight:bold;
    }

生成的css如下:
    
    
    .error, .seriousError {
      color: red; }
    
    .attention, .seriousError {
      border: 1px solid red; }
    
    .seriousError {
      font-weight: bold; }

这样的样式用着用着，有一天发现又有一种更危险的error出现了，情况极其严重，一旦出现，就一定要引起用户注意并且修改，如果不改，简直要天崩地裂。

好吧，我们姑且叫他 criticalError ,他依旧用鲜艳的红色，粗体，并且要有像attention一样的红色边框，只不过他需要更大，达到40px才解气。

很显然，criticalError是seriousError情况的加深。因此我们选择extend seriousError。

这样，便形成了一种链式extend结构。
    
    
    .error{
     color:red;
    }
    .attention{
     border:1px solid red;
    }
    .seriousError{
      @extend .error, .attention;
     font-weight:bold;
    }
    .criticalError{
      @extend .seriousError;
      font-size:40px;
    }

生成的css如下：
    
    
    .error, .seriousError, .criticalError {
      color: red; }
    
    .attention, .seriousError, .criticalError {
      border: 1px solid red; }
    
    .seriousError, .criticalError {
      font-weight: bold; }
    
    .criticalError {
      font-size: 40px; }

现在，这个error系统用着很棒，但是忽然有一天，技术总监说：“上面又发了一个新的error系统我们需要完成，我认为我们应当用现在的sass错误系统建立一个快速的error**开发框架**”  
这时，问题来了，如何用sass建立一个error开发框架呢？这时，让我们引出extend的另一个特性，这个特性就是为建立框架而生的。

让我们先来做个简单的实验，粘贴下面的sass代码然后编译看看：
    
    
    %baseError{
      color:red;
    }

是不是发现生成的css空空如也。  
现在 试试这个
    
    
    %baseError{
      color:red;
    }
    .Error{
      @extend %baseError;
    }

生成的css是否如下:
    
    
    .Error {
      color: red; }

这便是一个最最简单的框架结构。%Name 告诉sass这时框架结构，不要输出这些。 @extend %name告诉sass我要扩展这个name选择器样式，调用一下这个框架。

框架在书写的时候，需要debug，在用户使用的时候需要对错误的输入警告，这时就需要@debug和@warn

## @debug

用在测试时候的输出，可以在控制台看到。  
如  
@debug 10em + 12em;  
你就会在控制台看到：  
Line 1 DEBUG: 22em

## @warn

看个例子：
    
    
    @mixin adjust-location($x, $y) {
      @if unitless($x) {
        @warn "没有赋予单位，假设#{$x}按像素来算";
        $x: 1px * $x;
      }
      @if unitless($y) {
        @warn "没有赋予单位，假设#{$y}按像素来算";
        $y: 1px * $y;
      }
      position: relative; left: $x; top: $y;
    }
    .box{
      @include adjust-location(10,20);//我们在这里故意不加入像素值
    }

生成的css如下:
    
    
    .box {
      position: relative;
      left: 10px;
      top: 20px; }

但是这不是重点，请留意你的控制台。
    
    
    WARNING: 没有赋予单位，假设10按像素来算
             on line 3 of style.scss, in `adjust-location'
             from line 13 of style.scss
    
    WARNING: 没有赋予单位，假设20按像素来算
             on line 7 of style.scss, in `adjust-location'
             from line 13 of style.scss

至此，我大致介绍了大致85%左右关于sass的常用知识，随后我将推荐和分析几个sass框架，来带着大家一起摸索sass的开发模式。  
在探索过程中，我们将一起来制作一个基于Responsive和SASS的站点。

作者：[代码家](http://www.weibo.com/daimajia)  
来源：[代码家的博客](http://blog.zhan-dui.com)  
你可以订阅我的Blog以获取最新的知识文章。  
请尊重版权，转载请注明来源！

SASS系列：  
[Responsive系列之知识储备 – SASS基础教程](http://blog.zhan-dui.com/?p=106)  
[Responsive系列之知识储备 – SASS高阶教程（1）](http://blog.zhan-dui.com/?p=167)  
[Responsive系列之知识储备 – SASS高阶教程（2）](http://blog.zhan-dui.com/?p=207)
