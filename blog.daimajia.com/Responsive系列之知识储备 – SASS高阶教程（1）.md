title: Responsive系列之知识储备 – SASS高阶教程（1）

date: 2013-04-02 19:00:13

tags: []

description: 

---
如果你还不了解什么是sass，请点击[Responsive系列之知识储备 – SASS基础教程](http://blog.zhan-dui.com/?p=106)

## SASS中的控制指令

sass支持一些基本的控制指令，通过条件判断来输出某些特定的样式。

_**1、@if :**_
    
    
    @if 条件语句 {...（返回的样式）}

如；
    
    
    p {
      @if 1 + 1 == 2 { border: 1px solid;  }
      @if 5 < 3      { border: 2px dotted; }
      @if null       { border: 3px double; }
    }

生成的css如下：
    
    
    p {
      border: 1px solid; }

@if 同样可以跟 @else if  
如：
    
    
    $type: monster;
    p {
      @if $type == ocean {
        color: blue;
      } @else if $type == matador {
        color: red;
      } @else if $type == monster {
        color: green;
      } @else {
        color: black;
      }
    }

生成的css如下：
    
    
    p {
      color: green; }

**_2、@for_**  
_@for_指令用来重复输出一系列的样式，通过一个循环语句，指定一个变量名，一个开始和一个结尾，而后在执行体中写入想要输出的样式格式，sass会自动循环的输出一系列的样式结构。  
_注：sass的循环 包含 开始和结尾_  
如：
    
    
    @for $i from 1 through 3 {
      .item-#{$i} { width: 2em * $i; }
    }

生成的css如下：
    
    
    .item-1 {
      width: 2em; }
    .item-2 {
      width: 4em; }
    .item-3 {
      width: 6em; }

**_3、@each_**  
_@each_指令用来遍历一个序列，每次将序列中的一个值设为声明的一个_变量_，并且进行特定操作，操作完成后，循环到下一个值，直到结束。  
如：
    
    
    @each $animal in dog, cat, bird {
      .#{$animal}-icon {
        background-image: url('/images/#{$animal}.png');
      }
    }

生成的css如下：
    
    
     .dog-icon {
      background-image: url('/images/dog.png'); }
    .cat-icon {
      background-image: url('/images/cat.png'); }
    .bird-icon {
      background-image: url('/images/bird.png'); }

设想如果有很多重复性的css要生成，sass多么的方便。  
**_4、@while_**  
_@while_语句首先判断是否满足给定条件，满足条件的情况下重复输出某一样式表达式，直到条件为false为止。  
_@while_是一个比较少用的表达式，通常用来实现_@for_语句难以实现的复杂循环结构.  
如：
    
    
    $i: 6;
    @while $i > 0 {
      .item-#{$i} { width: 2em * $i; }
      $i: $i - 2;
    }

生成的css如下:
    
    
    .item-6 {
      width: 12em; }
    
    .item-4 {
      width: 8em; }
    
    .item-2 {
      width: 4em; }

## Mixins高级用法

在[Responsive系列之知识储备 – SASS基础教程](http://blog.zhan-dui.com/?p=106)中，介绍了Mixins的基础用法，_@include_以及传递参数。  
现在我将介绍一下关于Mixins的更多功能：  
1、Mixins的声明内部可以_@include_其他的Mixins  
如：
    
    
    @mixin compound {
      @include highlighted-background;
      @include header-text;
    }
    
    @mixin highlighted-background { background-color: #fc0; }
    @mixin header-text { font-size: 20px; }

2、Mixins的参数传递功能可以有默认值  
如：
    
    
    @mixin sexy-border($color, $width: 1in) {
      border: {
        color: $color;
        width: $width;
        style: dashed;
      }
    }
    p { @include sexy-border(blue); }
    h1 { @include sexy-border(blue, 2in); }

生成的css如下：
    
    
    p {
      border-color: blue;
      border-width: 1in;
      border-style: dashed; }
    
    h1 {
      border-color: blue;
      border-width: 2in;
      border-style: dashed; }

3、Mixins同样可以显式声明要传递的参数/也可以叫作关键字传参 （Keyword arguments）  
如：
    
    
    p { @include sexy-border($color: blue); }
    h1 { @include sexy-border($color: blue, $width: 2in); }

显式传递会让sass代码更加易读，而且在有很多参数的情况下，不用过多的在意参数传递的顺序，建议多用这种方式去传递参数。

4、Mixins也支持不定参数传递  
在某些情况下，我们可能无法确定一个Mixins要传递的参数个数，这个时候，我们就可以利用这一特性来传递参数。参数书写规则类似其他语言，在参数变量后加`…` 代表不定参数。  
如我们要实现shadow效果，而shadow的参数往往比较多样，无法确定：
    
    
    @mixin box-shadow($shadows...) {
      -moz-box-shadow: $shadows;
      -webkit-box-shadow: $shadows;
      box-shadow: $shadows;
    }
    
    .shadows {
      @include box-shadow(0px 4px 5px #666, 2px 6px 10px #999);
    }

生成的css如下：
    
    
    .shadowed {
      -moz-box-shadow: 0px 4px 5px #666, 2px 6px 10px #999;
      -webkit-box-shadow: 0px 4px 5px #666, 2px 6px 10px #999;
      box-shadow: 0px 4px 5px #666, 2px 6px 10px #999;
    }

5、调用Mixins，也可以用类似不定参数的方法调用。  
可以提前声明一个数值List,而后在调用时传入这个List+`…`，sass会自动分配List中的value给每个参数。  
如下：
    
    
    @mixin colors($text, $background, $border) {
      color: $text;
      background-color: $background;
      border-color: $border;
    }
    
    $values: #ff0000, #00ff00, #0000ff;
    .primary {
      @include colors($values...);/*留意这里*/
    }

生成的css如下：
    
    
    .primary {
      color: #ff0000;
      background-color: #00ff00;
      border-color: #0000ff;
    }

6、如果你想扩展一个已有的Mixins（如：添加某些新的属性），又不希望打破旧的结构，这时新的Mixins可以包装旧的Mixins，并且可以利用不定参数的方式来实现参数传递，是不是听起来略微抽象，没有关系，看个例子就明白了。  
假如有个Mixins叫stylish-mixin，我们现在想扩展出一个新的Mixins，让他的字体变为bold
    
    
    @mixin stylish-mixin($color,$width){
    	color:$color;
    	font-size:$width;
    }
    @mixin wrapped-stylish-mixin($args...) {
      font-weight: bold;
      @include stylish-mixin($args...);
    }
    
    .stylish {
      @include wrapped-stylish-mixin(#eeeeee,$width: 100px);
    }

生成的css如下：
    
    
    .stylish {
      font-weight: bold;
      color: #eeeeee;
      font-size: 100px; }

7、传递内容块（content blocks）给Mixins  
这个比较抽象，我会从一个例子下手，而后讲解此功能的用法。  
首先，我们在此引入一个@指令，即`@content`,`@content`表示一个未来要被替换的文本。  
看如下scss文件:
    
    
    @mixin apply-to-ie6-only {
      * html {
        @content; /*这个@content,表示未来此处会被传递的值重新替换的样式文本*/
      }
    }
    /*而后，我们利用@include指令来调用 apply-to-ie6-only mixins*/
    
    /*但是在调用的时候，我们得考虑到替换@content ， 因而我们要使用 @include 的另一种使用方式 ，如下：*/
    
    @include apply-to-ie6-only {/*这个代码段内的文本将替换 apply-to-ie6-only中的@content部分 */
      #logo {
        background-image: url(/logo.gif);
      }
    }

而后sass在编译后的文本内容其实如下:
    
    
    @mixin apply-to-ie6-only {
      * html {
         #logo {
           background-image: url(/logo.gif);
        }
      }
    }
    
    @include apply-to-ie6-only;

最终生成的 css文件如下：
    
    
    * html #logo {
      background-image: url(/logo.gif);
    }

这种看似麻烦的方法是用来做什么的呢？  
实际上是用来提供抽象接口的，看看这种结构像不像C++中的abstract类（抽象类）。想想C++的抽象类是用来干什么的？

## 函数指令

sass允许你定义自己的函数。  
使用方法：  
@function 函数名（参数1，参数2…）{  
…一些处理语句;  
@return 返回的内容;  
}  
举个例子：
    
    
    $grid-width: 40px;
    $gutter-width: 10px;
    
    @function grid-width($n) {
      @return $n * $grid-width + ($n - 1) * $gutter-width;
    }
    
    #sidebar { width: grid-width(5); }

生成如下css:
    
    
    #sidebar {
      width: 240px; }

函数跟mixin的传参方法很类似，同样支持关键字传参，如上面的grid-width也可以如下调用：
    
    
    #sidebar { width: grid-width($n: 5); }

同样函数也支持不定参数的传递方式。  
_注意：为了不发生命名冲突或者为了不使阅读你代码的人误以为函数是sass内部提供的函数，建议在属于你自己的函数上加入前缀，如你在google工作，可以在grid-width前加入google，变成为google-grid-width_

下一节，我将补充介绍一些@规则指令，并且介绍一些常用的css格式。  
也会补充介绍一些平台下的便利开发工具。

作者：[代码家](http://www.weibo.com/daimajia)  
来源：[代码家的博客](http://blog.zhan-dui.com)  
你可以订阅我的Blog以获取最新的知识文章。  
请尊重版权，转载请注明来源！

SASS系列：  
[Responsive系列之知识储备 – SASS基础教程](http://blog.zhan-dui.com/?p=106)  
[Responsive系列之知识储备 – SASS高阶教程（1）](http://blog.zhan-dui.com/?p=167)  
[Responsive系列之知识储备 – SASS高阶教程（2）](http://blog.zhan-dui.com/?p=207)
