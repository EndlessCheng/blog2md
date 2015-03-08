#  [ [iOS]如何在iOS开发中切换显示语言实现国际化 ](/pleasecallmewhy/article/details/37873115)

[ 国际化 ](http://www.csdn.net/tag/%e5%9b%bd%e9%99%85%e5%8c%96) [ iOS ](http://www.csdn.net/tag/iOS) [ 多语言 ](http://www.csdn.net/tag/%e5%a4%9a%e8%af%ad%e8%a8%80)

1.在Project设置，添加中英两种语言： 

![](http://img.blog.csdn.net/20140716103507332?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


  


2.新建Localizable.strings文件，作为多语言对应的词典，存储多种语言，点击右侧Localization，勾选中英： 

![](http://img.blog.csdn.net/20140716103629482?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


3.添加一个字段， 

在English中，添加："SUBMIT_BTN_TITLE"  =  "Go"  ; 

在Chinese中，添加："SUBMIT_BTN_TITLE"  =  "  开始  "  ;    
  


4.一个工具类GDLocalizableController，用来切换本地语言： 
    
    
    //
    //  GDLocalizableController.h
    //  guide-book
    //
    //  Created by why on 7/16/14.
    //  Copyright (c) 2014 why. All rights reserved.
    //
    
    #import <Foundation/Foundation.h>
    
    @interface GDLocalizableController : NSObject
    
    +(NSBundle *)bundle;//获取当前资源文件
    
    +(void)initUserLanguage;//初始化语言文件
    
    +(NSString *)userLanguage;//获取应用当前语言
    
    +(void)setUserlanguage:(NSString *)language;//设置当前语言
    
    @end
    
    
    
    
    
    
    //
    //  GDLocalizableController.m
    //  guide-book
    //
    //  Created by why on 7/16/14.
    //  Copyright (c) 2014 why. All rights reserved.
    //
    
    #import "GDLocalizableController.h"
    
    @implementation GDLocalizableController
    
    static NSBundle *bundle = nil;
    
    + ( NSBundle * )bundle{
        return bundle;
    }
    +(void)initUserLanguage{
        
        NSUserDefaults *def = [NSUserDefaults standardUserDefaults];
        NSString *string = [def valueForKey:@"userLanguage"];
        if(string.length == 0){
            //获取系统当前语言版本
            NSArray* languages = [def objectForKey:@"AppleLanguages"];
            NSString *current = [languages objectAtIndex:0];
            string = current;
            [def setValue:current forKey:@"userLanguage"];
            [def synchronize];//持久化，不加的话不会保存
        }
        
        //获取文件路径
        NSString *path = [[NSBundle mainBundle] pathForResource:string ofType:@"lproj"];
        bundle = [NSBundle bundleWithPath:path];//生成bundle
    }
    
    +(NSString *)userLanguage{
        
        NSUserDefaults *def = [NSUserDefaults standardUserDefaults];
        NSString *language = [def valueForKey:@"userLanguage"];
        return language;
    }
    
    +(void)setUserlanguage:(NSString *)language{
        
        NSUserDefaults *def = [NSUserDefaults standardUserDefaults];
        
        //1.第一步改变bundle的值
        NSString *path = [[NSBundle mainBundle] pathForResource:language ofType:@"lproj" ];
        bundle = [NSBundle bundleWithPath:path];
        
        //2.持久化
        [def setValue:language forKey:@"userLanguage"];
        [def synchronize];
    }
    
    @end

  
  


  
  


5\. 自定义一个宏方便处理： 
    
    
    // ----- 多语言设置
    #define CHINESE @"zh-Hans"
    #define ENGLISH @"en"
    #define GDLocalizedString(key) [[GDLocalizableController bundle] localizedStringForKey:(key) value:@"" table:nil]
    

  
6.使用： 
    
    
        [GDLocalizableController setUserlanguage:CHINESE];
        NSLog(GDLocalizedString(@"SUBMIT_BTN_TITLE"));
        [GDLocalizableController setUserlanguage:ENGLISH];
        NSLog(GDLocalizedString(@"SUBMIT_BTN_TITLE"));

  
  


  


  


参考资料： [ iOS 应用程序内部国际化，不跟随系统语言 ](http://blog.csdn.net/yang8456211/article/details/12031667)   

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/37873115](http://blog.csdn.net/pleasecallmewhy/article/details/37873115)