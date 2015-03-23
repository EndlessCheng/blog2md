title: Responsive系列之知识储备 – SASS基础教程

date: 2013-04-01 03:55:25

tags: []

description: 

---
SASS 是一 CSS 的预处理标记语言。为CSS加入了如 变量、判断、嵌套、导入等功能。

### 安装：

第一步：SASS需要Ruby环境

Windows下的安装点此：[Ruby Installer](http://rubyinstaller.org/downloads/)

Mac OS 是自带Ruby环境的，所以无需再装

第二步：在命令行下安装SASS

在命令行下执行：
    
    
    gem install sass

等待片刻就可以装上了。

### 入门：

1、新建一个style.scss文件

2、输入并且保存
    
    
    /* style.scss */
    $width:23px; /*此处是sass变量*/
    #navbar {
      height: 80%;
      width: $width;
    }

3、在控制台中，cd到所在目录，然后输入
    
    
    sass --watch style.scss:style.css

输入后，sass会自动监测style.scss文件的变化，并且重新生成style.css。

4、观察在该目录下是否生成了一个style.css文件，并且是否发现width属性被设置成了23px呢？这就是scss的基本操作流程。

### 语法

## **一、变量：******

sass允许使用变量，变量以`$`符号开始，类似属性的声明方式，值可以为颜色，数字（带单位），以及文本,而后以分号结尾。

_变量可以使你不用重复去书写一些属性值，而且为修改提供了很大的便利，可以在一处轻松修改整体风格。_

例子：
    
    
    /* style.scss */
    $color:#eeeeee;
    $width:960px;
    div.header{
        width:$width;
        background-color:$color;
    }

生成的style.css如下
    
    
    /* style.css */
    div.header{
        width:960px;
        background-color:#eeeeee;
    }

## **二、嵌套**

在书写css的过程中，经常会利用后代选择器(也叫上下文选择器)

如：想对p元素下的em元素做特殊样式处理，就可以用后代选择器

p{…}

p em{…}

在sass中可以对一书写进行简化。
    
    
    p{
      ...
      em{
        ...
      }
    }

来一个稍微复杂一点儿的例子：
    
    
    /* style.scss */
    
    #navbar {
      width: 80%;
      height: 23px;
    
      ul { list-style-type: none; } /*嵌套样式*/
      li { /*嵌套样式*/
        float: left;
        a { font-weight: bold; }/*嵌套样式*/
      }
    }

由sass处理后css的如下：
    
    
    /* style.css */
    
    #navbar {
      width: 80%;
      height: 23px; 
    } /*sass将嵌套元素拆解成后代选择器*/
      #navbar ul { list-style-type: none; }
      #navbar li { float: left; }
      #navbar li a { font-weight: bold; }

## **三、父元素简写**

常用在伪类中，如 a:hover , li:hover，sass将伪类也添加了嵌套写法。  
在嵌套中用符号 `&` 来指代 父元素。如下例子，&:hover {…} 中 &就指代 父元素 a
    
    
    /* style.scss */
    a {
      color: #ce4dd6;
      &:hover { color: #ffb3ff; }/*嵌套样式*/
      &:visited { color: #c458cb; }/*嵌套样式*/
    }

生成的style.css如下
    
    
    /* style.css */
    a { color: #ce4dd6; }
    a:hover { color: #ffb3ff; }
    a:visited {color: #c458cb; }

## **四、融合/代码片段（ Mixins )**

Mixins 是sass很强大的一个特征，他可以让你重复使用样式，属性，选择器。就类似于代码片段的重复使用。  
Mixins 的定义是以 `@mixin` 声明作为开始，而后给一个调用名称，紧跟可以被融合的代码块片段。  
在需要使用这一代码片段的时候，使用 `@include 片段名`  
比如下面的例子，通常我们我们想让css某一部分圆角，就得给某一元素加入以下css
    
    
    -webkit-border-radius: 20px;
    border-radius: 20px;

如果想要圆角的部分非常多，就得不断地复制粘贴这一代码片段，而且如果以后想同意修改圆角大小，就得一个一个改，sass就将这一过程简化，提供了更方便的书写，修改起来也变得易如反掌。
    
    
    /*style.scss*/
    $radius:20px;
    @mixin rounded{/*可以将这个视为一个代码片段*/
      -webkit-border-radius: $radius;
      border-radius: $radius;
    }
    /*比如我想在header上圆角*/
    div.header{
    @include rounded;/*引入这一代码片段*/
    }

产生的css如下：
    
    
    /*比如我想在header上圆角*/
    div.header {
      -webkit-border-radius: 20px;
      border-radius: 20px; }

## **五、融合/代码片段 传参**

sass最强大的地方就是你可以为你的代码片段进行参数传递。  
回想刚才的那个rounded代码片段，可能我们不想要全局的设置radius为20px，我们想要在div.footer中设置为10px，在div.header中设置为20px,这个时候传参显得很有意义。并且我们可能还想给border加入一个色彩属性。

如下代码所示：
    
    
    /*style.scss*/
    @mixin rounded($radius,$border-color){/*支持参数传入和参数列表*/
      -webkit-border-radius: $radius;
      border-radius: $radius;
      border-color:$border-color;
    }
    div.header{
    	@include rounded(20px,#ff0000);
    }
    div.footer{
    	@include rounded(10px,#0000ff);
    }

生成的css如下:
    
    
    /*style.css*/
    div.header {
      -webkit-border-radius: 20px;
      border-radius: 20px;
      border-color: red; }
    
    div.footer {
      -webkit-border-radius: 10px;
      border-radius: 10px;
      border-color: blue; }

## **六、利用@import来管理mixins片段和变量**

如果我们的一个页面的css文件很多，这无疑会浪费一部分时间在http request上。  
但是  
又如果我们在一个scss文件中写入大量的mixins片段，又使得整个文件结构变得不清晰，想要修改某一部分时，又得找半边天。  
这时  
将不同的mixins分文件存放，需要哪个载入哪个，这样就实现了分块管理。一旦某部分需要修改，只要找到该文件并且修改即可。  
sass利用@import实现了这一功能

用刚才的rounded的例子：  
在目录下建立名为 _rounded.scss 文件，写入rounded的mixin：
    
    
    /*_rounded.scss*/
    @mixin rounded($radius,$border-color){
      -webkit-border-radius: $radius;
      border-radius: $radius;
      border-color:$border-color;
    }
    
    
    /*style.scss*/
    @import "rounded";
    div.header{
    	@include rounded(25px,#ff0000);
    }

生成的css文件如下：
    
    
    /*style.css*/
    div.header {
      -webkit-border-radius: 25px;
      border-radius: 25px;
      border-color: red; }

sass对Minis文件命名约定如下：  
1、以下划线开始。 如刚才的rounded，如果要以mixins存放，就得以 _rounded.scss 文件名存放。  
2、后缀可以是scss或者sass

@import约定如下：  
1、无需添加下划线  
2、无需加入文件后缀名

例如想要加入rounded的mixin： @import “rounded”;

## **七、插值 Interpolation **

变量不仅仅可以用在_属性值_上，还可以用 #{} 的方式，将变量插入到_属性名_中。__
    
    
    /* style.scss */
    
    $vert: top;
    $horz: left;
    $radius: 10px;
    
    .rounded-#{$vert}-#{$horz} {
      border-#{$vert}-#{$horz}-radius: $radius;
      -moz-border-radius-#{$vert}#{$horz}: $radius;
      -webkit-border-#{$vert}-#{$horz}-radius: $radius;
    }

生成的css文件如下:
    
    
    /* style.scss */
    .rounded-top-left {
      border-top-left-radius: 10px;
      -moz-border-radius-topleft: 10px;
      -webkit-border-top-left-radius: 10px; }

## 八、操作和函数 （Operations and Functions）

sass支持变量的数学运算，同时也可以调用一些预设的函数方法来实现计算元素大小和动态着色以及处理字符串，条件判断等等。  
这个我将会重新开一篇文章详细介绍函数的一些用法和技巧。

 

以上只是sass的一些基本用法，后续我将继续介绍sass的一些高级用法。你可以订阅我的blog，随时获取更新。

作者：[代码家](http://www.weibo.com/daimajia)  
来源：[代码家的博客](http://blog.zhan-dui.com)  
你可以订阅我的Blog以获取最新的知识文章。  
请尊重版权，转载请注明来源！

SASS系列：  
[Responsive系列之知识储备 – SASS基础教程](http://blog.zhan-dui.com/?p=106)  
[Responsive系列之知识储备 – SASS高阶教程（1）](http://blog.zhan-dui.com/?p=167)  
[Responsive系列之知识储备 – SASS高阶教程（2）](http://blog.zhan-dui.com/?p=207)
