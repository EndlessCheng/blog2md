#  [ [iOS]xcode5中64位iphone5s引用第三方库报错的解决办法 ](/pleasecallmewhy/article/details/17411907)

现在5s初到64位了，以前打的包好多都会报错： 

  


ignoring file /Users/why/Desktop/PhoneFax/UMSocial_Sdk_3.1/libUMSocial_Sdk_3.1.a, missing required architecture x86_64 in file /Users/why/Desktop/PhoneFax/UMSocial_Sdk_3.1/libUMSocial_Sdk_3.1.a (3 slices) 

  


  


  


友盟的分享什么的都失效了。 

解决方案如下：   


** targets ->build setting 下的 **

** architectures 设置为 standard architetures(armv7,armv7s) **

** vaild architectures 设置为armv7,armv7s **

具体如下图 

![](http://img.blog.csdn.net/20131203160427265?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3VueXVhbnlhbmc2MjU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  


  


  


![](http://img.blog.csdn.net/20131203160438734?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3VueXVhbnlhbmc2MjU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/17411907](http://blog.csdn.net/pleasecallmewhy/article/details/17411907)