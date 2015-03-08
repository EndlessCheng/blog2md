#  [ [iOS6]如何在Xcode6设置UIView的圆角显示 ](/pleasecallmewhy/article/details/39613871)

很多人都有把按钮做成圆角的需求，以前我们会在代码中加入如下代码实现这个功能： 

  

    
    
    mainImgView.layer.cornerRadius = 6;

  
现在Xcode6加了 RunTime Attributes 的特性之后，我们可以直接在Xcode中设置： 

![](http://img.blog.csdn.net/20140927185135343?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


这样运行之后就会显示圆角的效果了： 

  


![](http://img.blog.csdn.net/20140927185259875?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/39613871](http://blog.csdn.net/pleasecallmewhy/article/details/39613871)