#  LESS in Action

[ http://yuguo.us/weblog/less ](http://yuguo.us/weblog/less)

Created by [ Yuguo ](http://yuguo.us)

##  CSS 是一门非程序式语言

  * CSS 需要书写大量看似没有逻辑的代码，不方便维护及扩展，不利于复用 
  * 没有变量 
  * 没有函数 
  * 没有SCOPE（作用域） 
  * 非前端开发工程师来讲，往往会因为缺少 CSS 编写经验而很难写出组织良好且易于维护的 CSS 代码 

##  LESS的目标

LESS 并没有裁剪 CSS 原有的特性，更不是用来取代 CSS 的，而是在现有 CSS 语法的基础上，为 CSS 加入程序式语言的特性。

#  LESS语法介绍

##  变量

@color: #4D926F; #header { color: @color; } h2 { color: @color; }

##  优点

可以将相同的值定义成变量统一管理起来。

#header { color: #4D926F; } h2 { color: #4D926F; }

##  作用域

@width : 20px; #homeDiv { @width : 30px; #centerDiv{ width : @width;//
此处应该取最近定义的变量 width 的值 30px } } #leftDiv { width : @width; // 此处应该取最上面定义的变量
width 的值 20px }

##  Mixins（混入）

混入是指在一个 CLASS 中引入另外一个已经定义的 CLASS，就像在当前 CLASS 中增加一个属性一样。

##  LESS

// 定义一个样式选择器 .roundedCorners(@radius:5px) { -moz-border-radius: @radius;
-webkit-border-radius: @radius; border-radius: @radius; } // 在另外的样式选择器中使用
#header { .roundedCorners; //默认值 } #footer { .roundedCorners(10px); //参数 }

##  CSS

#header { -moz-border-radius:5px; -webkit-border-radius:5px; border-
radius:5px; } #footer { -moz-border-radius:10px; -webkit-border-radius:10px;
border-radius:10px; }

` @arguments ` 在 Mixins 中具是一个很特别的参数，当 Mixins
引用这个参数时，该参数表示所有的变量，很多情况下，这个参数可以省去你很多代码。

##  LESS

.boxShadow(@x:0,@y:0,@blur:1px,@color:#000){ -moz-box-shadow: @arguments;
-webkit-box-shadow: @arguments; box-shadow: @arguments; } #header {
.boxShadow(2px,2px,3px,#f36); }

##  CSS

#header { -moz-box-shadow: 2px 2px 3px #FF36; -webkit-box-shadow: 2px 2px 3px
#FF36; box-shadow: 2px 2px 3px #FF36; }

#  嵌套

LESS 的嵌套规则的写法是 HTML 中的 DOM 结构相对应的，这样使我们的样式表书写更加简洁和更好的可读性。

##  HTML

top

left

right

##  LESS

#home{ color : blue; width : 600px; height : 500px; border:outset; #top{
border:outset; width : 90%; } #center{ border:outset; height : 300px; width :
90%; #left{ border:outset; float : left; width : 40%; } #right{ border:outset;
float : left; width : 40%; } } }

##  CSS

#home { color: blue; width: 600px; height: 500px; border: outset; } #home #top
{ border: outset; width: 90%; } #home #center { border: outset; height: 300px;
width: 90%; } #home #center #left { border: outset; float: left; width: 40%; }
#home #center #right { border: outset; float: left; width: 40%; }

##  伪类

a { color: red; text-decoration: none; &:hover {// 有 & 时解析的是同一个元素或此元素的伪类，没有 &
解析是后代元素 color: black; text-decoration: underline; } }

##  CSS

a { color: red; text-decoration: none; } a:hover { color: black; text-
decoration: underline; }

##  普通运算

@init: #111111; @transition: @init*2; .switchColor { color: @transition; }

##  CSS

.switchColor { color: #222222; }

##  针对 ` color ` 的函数

lighten(@color, 10%); // return a color which is 10% *lighter* than @color
darken(@color, 10%); // return a color which is 10% *darker* than @color
saturate(@color, 10%); // return a color 10% *more* saturated than @color
desaturate(@color, 10%);// return a color 10% *less* saturated than @color
fadein(@color, 10%); // return a color 10% *less* transparent than @color
fadeout(@color, 10%); // return a color 10% *more* transparent than @color
spin(@color, 10); // return a color with a 10 degree larger in hue than @color
spin(@color, -10); // return a color with a 10 degree smaller hue than @color

##  LESS VS SASS

* LESS 和 SASS 互相促进互相影响，相比之下 LESS 更接近 CSS 语法 * LESS更多开源软件支持 * 本地调试时，SASS可以用Chrome直接调试，而LESS需要加载脚本 

##  Chrome issue

Firefox可以直接在html中加入`script`进行调试 Less.js browser script currently won’t work if
you’re using Chrome and the path to your page starts with “file:///” due to a
known Chrome issue.

##  解决办法

* Develop your local projects with a web server. * Add the command-line switch -allow-file-access-from-files to your shortcut and Chrome will allow you to load LESS.JS without a fuss. 

#  Thanks!

[ http://yuguo.us/weblog/less ](http://yuguo.us/weblog/less)

Created by [ Yuguo ](http://yuguo.us)

