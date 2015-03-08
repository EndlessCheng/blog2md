#  [ [Cocos2d-x]Mac下cocos2d-x连接pomelo服务器 ](/pleasecallmewhy/article/details/34128199)

[ Pomelo ](https://github.com/NetEase/pomelo) 是由网易开发的基于node.js 开发的高性能、分布式游戏服务器框架， 也可作为高实时web应用框架。 

Polemo的配置这里就不赘述了，Github的wiki很全面。 

在此记录一下使用官方的libpomelo配置cocos2d-x 3.1连接pomelo的全部流程。 

必备工具： 

  * [ GYP(Generate Your Projects) ](http://code.google.com/p/gyp/)
  * [ libpomelo ](https://github.com/NetEase/libpomelo)

###  GYP(Generate Your Projects) 

1.去官网下载gpy 
    
    
    svn checkout http://gyp.googlecode.com/svn/trunk/ gyp-read-only  
    

2.安装gpy 
    
    
    cd gyp-read-only 
    sudo ./setup.py install
    

###  libpomelo 

3.下载libpomelo 
    
    
    git clone https://github.com/NetEase/libpomelo.git
    

4.使用gyp生成项目，以iOS为例，其他参见 [ 多平台配置命令 ](https://github.com/NetEase/libpomelo)
    
    
    cd libpomelo
    ./pomelo_gyp -DTO=ios
    

5.编译生成虚拟机环境 
    
    
    ./build_iossim
    

注意，这里可能会报错，提示找不到sdk6，可以这样编辑build_iossim文件中的参数： 
    
    
    vi build_iossim
    

然后把其中的 ` iphonesimulator6.1 ` 换成自己的sdk版本。 比如我是7.1的sdk，则改成： 
    
    
    xcodebuild -project deps/jansson/jansson.xcodeproj -sdk iphonesimulator7.1 -arch i386
    xcodebuild -project deps/uv/uv.xcodeproj -sdk iphonesimulator7.1 -arch i386
    xcodebuild -project pomelo.xcodeproj -sdk iphonesimulator7.1 -arch i386
    

###  Xocde 

6.运行生成的pomelo.xcodeproj项目文件，编译运行。 

7.查看build文件夹，在对应目录下已经有编译好的libpomelo.a文件了。 

8.使用cocos命令创建一个新项目测试pomelo连接 
    
    
    cocos new hello-pomelo -l cpp
    

9.配置项目（以iOS为例，其他项目自行参考 [ pomelo-cocos2dchat ](https://github.com/NetEase/pomelo-cocos2dchat) ） 

  * 把以下内容加到Build Settings中的 ` User Header Search Paths ` 里面（LIBPOMELO_ROOT是libpomelo的根目录）： 

    * LIBPOMELO_ROOT/include 
    * LIBPOMELO_ROOT/deps/uv/incude 
    * LIBPOMELO_ROOT/deps/jansson/src 
  * 添加libpomelo libraries的路径到 ` Library Search Paths ` 里（LIBPOMELO_ROOT是libpomelo的根目录），以iOS项目为例： 

    * LIBPOMELO_ROOT/build/Default-iphonesimulator 
    * LIBPOMELO_ROOT/deps/uv/build/Default-iphonesimulator 
    * LIBPOMELO_ROOT/deps/jansson/build/Default-iphonesimulator 
  * 添加以下linker flags到 ` Other Linker Flags ` 中： 

    * ljansson 
    * luv 
    * lpomelo 

10.一些测试代码 

可以下载一个 [ chatofpomelo-websocket ](https://github.com/NetEase/chatofpomelo-websocket) 和 [ CCPomeloWrapper ](https://github.com/laoyur/CCPomeloWrapper) 测试一下联网功能。 

参考文档： 

  * [ pomelo-cocos2dchat ](https://github.com/NetEase/pomelo-cocos2dchat)
  * [ CCPomeloWrapper ](https://github.com/laoyur/CCPomeloWrapper)
  * [ CCPomelo ](https://github.com/xdxttt/CCPomelo)
  * [ COCOS2D-X + LIBPOMELO 实战手记 ](http://laoyur.ml/?p=318)
  * [ ](http://laoyur.ml/?p=318)
  * [ ](https://github.com/laoyur/CCPomeloWrapper)
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/34128199](http://blog.csdn.net/pleasecallmewhy/article/details/34128199)