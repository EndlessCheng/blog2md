#  [ [iOS]统一设置返回按钮为自定义图片的方法 ](/pleasecallmewhy/article/details/42027463)

  


  


我们可以通过基类设置BackButton的样式，也可以设置LeftButton然后隐藏BackButton，但是那样的话手势返回就没了。 

  


现在找到的方案是：设置返回按钮的背景图片为自定义的图片，为了解决会显示Back字样的问题，设置Title偏移到屏幕不可见的位置即可。 

  


完整代码如下： 

  

    
    
        UIImage *backImage = [UIImage imageNamed:@"backNor"];
        [[UIBarButtonItem appearance] setBackButtonBackgroundImage:[backImage resizableImageWithCapInsets:UIEdgeInsetsMake(0, backImage.size.width, 0, 0)]
                                                          forState:UIControlStateNormal barMetrics:UIBarMetricsDefault];
        [[UIBarButtonItem appearance] setBackButtonTitlePositionAdjustment:UIOffsetMake(-233, 0) forBarMetrics:UIBarMetricsDefault];
    

  
  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/42027463](http://blog.csdn.net/pleasecallmewhy/article/details/42027463)