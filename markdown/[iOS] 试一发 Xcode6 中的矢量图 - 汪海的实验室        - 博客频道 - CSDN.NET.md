#  [ [iOS] 试一发 Xcode6 中的矢量图 ](/pleasecallmewhy/article/details/39496169)

Xcode6中有一个十分方便的功能，就是导入的图片资源支持矢量图格式。这对于开发者来说无疑是个天大的好消息。 

  


不过，这矢量图怎么搞？有什么好处？效果到底如何？不妨打开 Xcode6 来一发试试看，亲自体验一下矢量图的魅力。 

  


我们先用Sketch制作了一个30*30的图标，导出了pdf和png格式： 

  


![](http://img.blog.csdn.net/20140923114113769?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


然后在Xcode6的 Images.xcassets中添加两个图标。首先是矢量图版本的： 

![](http://img.blog.csdn.net/20140923114413482?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


  


接下来是PNG版本的，我们只上传了@1x 版本的位图： 

![](http://img.blog.csdn.net/20140923114354968?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


然后我们找一个页面，同时放上两个图片进行比较。 

  


第一次实验：长宽均为100，即非等比拉伸： 

  


![](http://img.blog.csdn.net/20140923114735861?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


可以看到@1x的图因为没有做@2x和@3x 版本，细节处有很多模糊的情况。 

  


第二次试验：长宽均为240，等比显示： 

  


![](http://img.blog.csdn.net/20140923115624780?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


  


差距是比较明显的。 

  


  


Xcode6在使用矢量图的时候，会生成对应的@1x、@2x、@3x版本的位图，相当于帮我们做了适配的工作。比如30*30的矢量图导入，运行时会生成下面三个尺寸的位图： 

@1x = 30*30 

@2x = 60*60 

@3x = 90*90 

  


嗯大概就是这样。所以个人开发者们可以尝试一下用矢量图减少自己的工作量。公司里就算了，让美工们忙碌起来吧！ 

  


  


  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/39496169](http://blog.csdn.net/pleasecallmewhy/article/details/39496169)