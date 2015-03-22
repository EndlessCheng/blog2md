title: 用优雅的方式在 OS X 中为单个应用设置语言

date: 2014-11-10T23:42:27.000Z

tags: [OS X, ]

description: 

---
买到 CLIP STUDIO PAINT Pro，激活之后发现不给启动，显示 ` Unsupported OS ` 并退出。搜索了下发现是因为语言设置的问题导致，需要将系统环境设置为应用所支持的语言才能运行。 

嘛。日本人做事情也是让人无话可说，那么多应用都没有多语言支持的… 用能支持的语言来显示就好了嘛。 

话说回来，我一开始设置的系统语言是简体中文，虽然后备语言加了 English 和日本語，不过有些不能自动变更语言的应用在更换系统语言为 English 之后变得很别扭。于是寻找可以单独设置应用语言的方法。 

用惯了 Linux 再用 OS X 其实并没有那么容易的改变习惯… 当我准备尝试单独 export 一份 locale 再运行 app 的时候 OS X 直接告诉我不适用我的表情简直和伊莉雅一样。 

… 

睡了一觉起来继续 Google。找到了可以单独为应用设置语言并且 launch 的 app [ Language Switcher ](http://www.tj-hd.co.uk/en-gb/languageswitcher/) ，看起来不错，但是每次启动 CLIP STUDIO PAINT 都要先打开这货，这不是我想要的效果。 

于是最终找到一个合适的解决方案：用 ` defaults ` 命令。 

原帖在 [ 这里 ](http://hints.macworld.com/article.php?story=20061001065101830) 。 

设置 CLIP STUDIO PAINT Pro 语言环境命令： 
    
    
    defaults write jp.co.celsys.CLIPSTUDIOPAINT.lip AppleLanguages '("en-US")'  
  
---  
  
其中 ` jp.co.celsys.CLIPSTUDIOPAINT.lip ` 可以在应用的显示包信息 -> Contents -> Info.plist 中找到。 

执行后就可以直接双击启动啦~ 

最后献丑一张w 

![Kira\( > ◡╹\)~](http://blog.phoenixlzx.com/static/img/posts/2014111601.png)
