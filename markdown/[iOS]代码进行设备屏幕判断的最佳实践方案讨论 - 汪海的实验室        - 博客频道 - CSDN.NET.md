#  [ [iOS]代码进行设备屏幕判断的最佳实践方案讨论 ](/pleasecallmewhy/article/details/41861957)

目前开发的项目由于历史原因均用代码编写UI，所以判断设备尺寸成了不可避免的任务。 

目前我是这样进行尺寸判断的。 

首先定义一个枚举类，包含了所有的尺寸类型： 
    
    
    // 屏幕尺寸的枚举类型
    typedef NS_ENUM(NSUInteger, ScreenSizeType) {
        iPhone4Size,    // 480
        iPhone5Size,    // 568
        iPhone6Size,    // 667
        iPhone6pSize,   // 736
    };
    

然后写一个静态函数获取当前的尺寸类型： 
    
    
    +(ScreenSizeType)getScreenSizeType {
        if (kScreenBounds.size.height == 736) {
            return iPhone6pSize;
        } else if (kScreenBounds.size.height == 667) {
            return iPhone6Size;
        } else if (kScreenBounds.size.height == 568) {
            return iPhone5Size;
        }
        return iPhone4Size;
    }
    

然后再通过宏获取这个类型： 
    
    
    #define kScreenSizeType [PublicFunction getScreenSizeType]
    

最后，使用的时候这样： 
    
    
    int a = kScreenSizeType == iPhone6pSize ? 1 : 0;
    

不清楚大家是怎么实现的。希望可以评论讨论下。 

  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/41861957](http://blog.csdn.net/pleasecallmewhy/article/details/41861957)