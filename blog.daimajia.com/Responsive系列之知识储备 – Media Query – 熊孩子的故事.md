title: Responsive系列之知识储备 – Media Query – 熊孩子的故事

date: 2013-04-10 17:41:09

tags: []

description: 

---
## Media Query

1、Media Query是什么？

Media Query 是CSS3中用来查询设备类型(Media Type)，并且通过条件语句，加载满足条件的样式表。

2、关于设备类型：

–Media Query可以检测出以下设备–

设备名称 | 指代  
---|---  
all | 匹配所有设备  
braille | 匹配触觉反馈设备  
embossed | 凸点字符印刷设备  
handheld | 手持设备（尤其是小屏幕，有限带宽，不过注意：现在的Android，iPhone都不是Handheld设备，他们都是screen设备。所以，不要试图用handheld来识别iphone或者ipad,android等设备）PSP,NDS这种规格一般可以叫作Handheld，不过没有测试过，如有疏漏还请指正）  
print | 打印机设备  
projection | 投影仪设备  
screen | 彩色计算机显示器设备  
speech | 语音合成器设备  
tty | 栅格设备（终端，或者电传打字机）  
tv | 电视设备  
  
3、Media Query的语法：

**用法1：**
    
    
    @media 设备类型 {
    //...满足该设备条件的css属性...
    }

**用法2：**
    
    
    [逻辑表达式only或者not] 设备类型{
    ...//如果逻辑表达式是only：代表只有这一种设备，调用如下css
    ...//如果逻辑表达式是not : 代表除此之外的设备，调用如下css
    }

**用法3：**
    
    
    @media [逻辑表达式only或者not] 设备类型 [and 设备特征表达式]{
    ...//用法3比用法2多了一个[and 媒体特征表达式]，@media的强大之处在于，
    ...//他不但能选择设备类型，还能对设备的不同配置（如屏幕宽度，色彩等的）进行选择。
    //（这就是设备特征表达式所做的事情）
    ...//这个用法，就是对相同设备的不同属性进行选择，而后条用满足条件的css表达式
    ...//现在你可能还不明白[and 媒体特征表达式]，不过没有关系，后面我将认真介绍
    //媒体特征表达式的用法，你一定会惊叹@media query的强大。
    }

**用法4：**
    
    
    @media 设备特征表达式 | 设备特征表达式 |....{
    ...//满足所给出的媒体特征表达式后，调用以下css代码块
    ...//注意：只要满足设备特征就可以了，不一定要是相同设备。
    }

下面，我们用一个例子，来一步一步介绍这四种表达式的用法。

### 熊孩子的故事

想想这一种场景，你开发了个小有名气的在线阅读网站，不过后来有小孩子吐槽说：“我常常在NDS上看电子书，能不能在NDS上，将背景变为深色，字变成白色，夜里看小说，背景太亮很刺眼。”  
这时，你有两种做法：  
1、对设备UA进行检测，完全为NDS重新做一个适合手机的站点。（这是传统的做法，虽然现在多数站点都在用，在现在看来，很不聪明了！）  
2、利用css3的强大特性，轻松完成（我们当然要选择这种聪明些的做法！）  
让我们来考虑考虑实现思路：
    
    
    首先利用media query检查是否是手持设备
       如果是：
          背景为黑色，字为白色
       如果不是：
          不做处理

我们现在来看media query的第一种用法：
    
    
    @media 设备类型 {
    //...满足该设备条件的css属性...
    }

用法1正好符合我们在此情形下的筛选条件，那么我们书写的css如下：
    
    
    @media handheld{
     body{
       color:white;
       background-color:black;
     }
    }

我们的html页面便类似这个样子：


 

 

 

代码家  
我们来测试Handheld，手持设备和screen显示器设备。

用chrome打开该html，发现如下图：  
![](http://daimajia-wordpress.stor.sinaapp.com/uploads/2013/04/QQ20130406-2-300x204.png)

好像没有看到黑底白字啊？当然啦，你现在是在用电脑显示器来访问的页面，也就是满足了screen设备特征，handheld设备所书写的css都被忽略了。

那我们要如何测试在手持设备中的样式呢？难道一定要用NDS访问么，可是我没有NDS啊?！  
当然不是，我们这里要用Chrome的一个设置功能，来覆盖一些属性，模拟手持设备，按照如下操作，便可以调用Chrome中模拟各种设备的功能。  
1.首先，点击右键->审查元素  
![](http://ww4.sinaimg.cn/mw690/610dc034jw1e3g7i2zlyzj.jpg)  
2.而后，在弹出的控制窗口中，点下设置按钮  
![](http://ww1.sinaimg.cn/mw690/610dc034jw1e3g7i3nzhzj.jpg)  
3.左上角切到overrides中，寻找Emulate选项，勾上后，选中HandHeld，你就会惊奇的发现，网页整个变了个风格。正如我们预期的那样，黑底白字。  
![](http://ww2.sinaimg.cn/mw690/610dc034jw1e3g7i6cwslj.jpg)

![](http://ww2.sinaimg.cn/mw690/610dc034jw1e3g7i73akij.jpg)

做到此处，是否已经对media query有些了解，而且有很强的成就感，不过先按捺住不要激动，这才是media query功能的一部分，还有一些更为实用的用法还没有接触到。还需慢下心来继续看下去。

后来，过了一段时间，上次的那个小盆友又发来吐槽反馈，说：“哈哈哈哈，我买了个iPad2，可是我发现iPad2在横屏看书的时候字体有点儿小啊，能不能在横屏的时候把字改大一点儿？”。  
这时候，技术人员抓狂了，这可怎么改啊，iPad2也是screen设备，电脑显示器也是screen设备？！ 让我怎么识别！

冷静

我们下面介绍的东西就能很好的处理这种情形：那就是 设备特征表达式

设备特征表示 看起来是是这个样子的：设备特征：设备特征值

留意一下用法3：
    
    
    @media [逻辑表达式only或者not] 设备类型 [and 设备特征表达式]{
    ...//我们现在就要用用法3来识别iPad2
    }

现在考虑一下，虽然iPad2和电脑显示器都是screen设备，可是他们之间还是有不同之处的。比如说，ipad是有横屏特征的设备，电脑却没有。  
这个问题先搁浅到这里，我们先来研究一下设备表达式究竟是什么，等弄懂后，你自然就知道该怎么做了。

前面说到过，media query是可以识别设备特征的，可是设备特征是什么？想想，屏幕宽度算不算设备特征？设别分辨率算不算设备特征呢？设备色彩支持情况，横竖屏情况？  
没错，这些都是我们在使用电子设备时候的设备特征。Media query支持很多种设备特征的识别属性。

媒体特性 | 说明/值 | 可用媒体类型 | 接受min/max  
---|---|---|---  
width | 长度正数值(单位一般为px下同) | 视觉屏幕/触摸设备 | 是  
heigth | 长度正数值 | 视觉屏幕/触摸设备 | 是  
device-width | 长度正数值 | 视觉屏幕/触摸设备 | 是  
device-heigth | 长度正数值 | 视觉屏幕/触摸设备 | 是  
orientation | 设备手持方向(portait横向/landscape竖向) | 位图介质类型 | 否  
aspect-ratio | 浏览器、纸张长宽比 | 位图介质类型 | 是  
device-aspect-ratio | 设备屏幕长宽比 | 位图介质类型 | 是  
color | 颜色模式（例如旧的显示器为256色）整数 | 视觉媒体 | 是  
color-index | 颜色模式列表整数 | 视觉媒体 | 是  
monochrome | 整数 | 视觉媒体 | 是  
resolution | 解析度 | 位图介质类型 | 是  
scan | progressive逐行扫描/interlace隔行扫描 | 电视类 | 否  
grid | 整数，返回0或1 | 栅格设备 | 否  
  
扫了一眼表格发现不明白min/max？没有关系，后面会说到。  
这张表格来自：[zzjyingzi](http://my.opera.com/zzjyingzi/blog/2012/08/29/media-query)，尊重原创，转载请保留。

留意一下那个蓝色的orientation,这不正是我们可以用来识别ipad横屏的状态么？

我们在原来的html中加上：
    
    
    @meida screen and (orientation:landscape){
       font-size:25px;
    }

这样，你可以测试一下，在ipad横屏时。会正如我们所预料的那样，25px字体展示。一切都太完美了。  
在此之前，你或许需要用js去获取，而后调整属性。现在，只需简单几行就能实现，css3的强大之处当然不止如此，以后我也会给大家介绍更多关于css3的新特性。

正在我们说话之际，小盆友又发来消息：“我最近买了个iPhone，我也要黑底白字，保护眼睛。”

我想你也猜到了，我们这次需要识别的是同为screen设备的iPhone….

Here we go!

先来考虑iPhone与台式机显示器的不同之处：最大的区别就是屏幕大小。

那我们这次就要介绍一个属性，device-width，指代的是设备的宽度，注意，这可不是网页渲染的区域宽度。这个是与设备相关的。

iPhone的device-width就是320px，那么我们继续补充一个media-query在css中。
    
    
    @media screen and (device-width:320px){
        body{
           background-color:black;
           color:white;
        }
    }

好啦，加上以后，那个小盆友就每天很happy的看上了小数，可是过了几日，我们又收到了这个倒霉孩子的来信：“我的iPhone坏了…555555….我妈给我买了个小手机先用着，屏幕可小了，烦。。。能不能把这个小屏幕的手机也让黑体白字、”。

忽然觉得技术部门就是为他开的。

好吧，冷静。

这个时候，就要介绍min/max属性了。device-width:320px 其实类似于divice-width==320px;  
min/max 其实就是 >= 和 <=  
min-device-width : 320px; 等价于 device-width >= 320px;  
max-device-width : 320px; 等价于 device-width <= 320px;  
明白了吧，我们只要在device-width前加个max 就能轻松解决这个熊孩子的要求了（让iPhone或者iPhone屏幕小的设备都能黑底白字）。[来自Apple官方](https://developer.apple.com/library/safari/#documentation/AppleApplications/Reference/SafariWebContent/OptimizingforSafarioniPhone/OptimizingforSafarioniPhone.html)
    
    
    @media screen and (max-device-width:320px){
        body{
           background-color:black;
           color:white;
        }
    }

从此之后，这个熊孩子就成了网站的忠实用户。。

关于Media Query的初步介绍就随着这个熊孩子安静下来而在此结束，不过我们的教程还未完结，熊孩子或许有一天又会发信来吐槽。

你可以在这个gist中查看目前多数设备的Media Query语句：[点此](https://gist.github.com/xuanqinanhai/5649220)

作者：[代码家](http://weibo.com/daimajia)  
来源：[代码家的博客](http://blog.zhan-dui.com/?p=232)  
你可以订阅我的Blog以获取最新的知识文章。  
请尊重版权，转载请注明来源！
