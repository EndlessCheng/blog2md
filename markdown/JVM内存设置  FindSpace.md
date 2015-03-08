#  JVM内存设置 

[ Find ](http://www.findspace.name/author/find) |  2015年2月14日  |  [ 网络文摘 ](http://www.findspace.name/category/res/fromweb) , [ 资源 ](http://www.findspace.name/category/res) |  [ 没有评论  ](http://www.findspace.name/res/1086#comments)

#  问题出现 

eclipse中写好安卓app在虚拟机中运行时，clipse长时间停留在100%那个进度。 

最后Eclipse报告unable to execute dex:GC overhead limit exceeded错误 

原因：运行中占用的堆内存超过了jvm设置的限制。 

#  设置jm内存设置 

##  1.设置JVM内存的参数有四个： 
    
    
    -Xmx    Java Heap最大值，默认值为物理内存的1/4，最佳设值应该视物理内存大小及计算机内其他内存开销而定；
            -Xmx 
             此设置控制 Java 堆的最大大小。正确调整此参数有助于降低垃圾回收开销，从而缩短服务器响应时间并提
            高吞吐量。
             对于某些应用程序来说，此选项的缺省设置可能会太低，从而导致发生大量小型垃圾回收。
             缺省值： 512 MB 
             建议值： 随工作负载的不同而有所变化，但高于缺省值。 
             用法： -Xmx512m 将最大堆大小设置为 512 兆字节
    -Xms    Java Heap初始值，Server端JVM最好将-Xms和-Xmx设为相同值，开发测试机JVM可以保留默认值；
             设置堆大小 下列命令行参数对于设置堆大小来说很有用。 
             -Xms 
             此设置控制 Java 堆的初始大小。正确调整此参数有助于降低垃圾回收开销，从而缩短服务器响应时间并提高
            吞吐量。
             对于某些应用程序来说，此选项的缺省设置可能会太低，从而导致发生大量小型垃圾回收。
             缺省值： 256 MB 
             建议值： 随工作负载的不同而有所变化，但高于缺省值。 
             用法： -Xms256m 将初始堆大小设置为 256 兆字节
    -Xmn    Java Heap Young区大小，不熟悉最好保留默认值；
             -Xmn 
             此设置控制允许新生成的对象在堆中耗用的空间量。正确调整此参数有助于降低垃圾回收开销，从而缩短服务
            器响应时间并提高吞吐 量。此参数的缺省设置通常过低，这将导致执行大量的小型垃圾回收操作。如果将此参
            数设置得过高，可能会导致 JVM 仅执行大型（ 全面）垃圾回收。这些垃圾回收操作通常会耗时几秒钟，这将
            严重影响服务器的整体性能。您必须保持将此参数设置为小于整个堆大 小的一半，以避免这种情况出现。
             缺省值： 2228224 字节 
             建议值： 大约整个堆大小的 1/4 
             用法： -Xmn256m 将大小设置为 256 兆字节。  
    -Xss    每个线程的Stack大小，不熟悉最好保留默认值；
    

##  2\. 如何设置JVM内存分配： 

（1）当在命令提示符下启动并使用JVM时（只对当前运行的类Test生效）： 

java -Xmx128m -Xms64m -Xmn32m -Xss16m Test 

（2）当在集成开发环境下（如eclipse）启动并使用JVM时： 

a. 在eclipse根目录下打开eclipse.ini，默认内容为（这里设置的是运行当前开发工具的JVM内存分配）： 

1.-vmargs 2.-Xms40m 3.-Xmx256m -vmargs表示以下为虚拟机设置参数，可修改其中的参数值，也可添加-Xmn，-Xss，另外，eclipse.ini内还可以设置非堆内存，如：-XX:PermSize=56m，-XX:MaxPermSize=128m。 

此处设置的参数值可以通过以下配置在开发工具的状态栏显示： 

在eclipse根目录下创建文件options，文件内容为：org.eclipse.ui/perf/showHeapStatus=true 

修改eclipse根目录下的eclipse.ini文件，在开头处添加如下内容： 

1.-debug 2.options 3.-vm 4.javaw.exe 重新启动eclipse，就可以看到下方状态条多了JVM信息。 

b. 打开eclipse－窗口－首选项－Java－已安装的JRE（对在当前开发环境中运行的java程序皆生效） 

编辑当前使用的JRE，在缺省VM参数中输入：-Xmx128m -Xms64m -Xmn32m -Xss16m 

c. 打开eclipse－运行－运行－Java应用程序（只对所设置的java类生效） 

选定需设置内存分配的类－自变量，在VM自变量中输入：-Xmx128m -Xms64m -Xmn32m -Xss16m 

注：如果在同一开发环境中同时进行了b和c设置，则b设置生效，c设置无效，如： 

开发环境的设置为：-Xmx256m，而类Test的设置为：-Xmx128m -Xms64m，则运行Test时生效的设置为： 

-Xmx256m -Xms64m 

（3）当在服务器环境下（如Tomcat）启动并使用JVM时（对当前服务器环境下所以Java程序生效）： 

a. 设置环境变量： 

变量名：CATALINA_OPTS 

变量值：-Xmx128m -Xms64m -Xmn32m -Xss16m 

b. 打开Tomcat根目录下的bin文件夹，编辑catalina.bat，将其中的%CATALINA_OPTS%（共有四处）替换为：-Xmx128m -Xms64m -Xmn32m -Xss16m 

##  参考设置文件： 
    
    
    -startup
    plugins/org.eclipse.equinox.launcher_1.3.0.v20140415-2008.jar
    --launcher.library
    plugins/org.eclipse.equinox.launcher.gtk.linux.x86_64_1.1.200.v20140603-1326
    -product
    org.eclipse.epp.package.java.product
    --launcher.defaultAction
    openFile
    -showsplash
    org.eclipse.platform
    --launcher.XXMaxPermSize
    256m   //注意这个不要太大
    --launcher.defaultAction
    openFile
    --launcher.appendVmargs
    -vmargs
    -Dosgi.requiredJavaVersion=1.6
    -XX:MaxPermSize=1024m
    -Xms512m
    -Xmx1024m
    

主要关注那几个m参数设置，过高的数值设置也会出问题。 

##  Reference： 

[ http://www.cnblogs.com/yaozhongxiao/p/3521428.html ](http://www.cnblogs.com/yaozhongxiao/p/3521428.html)

[ http://wuce7758.iteye.com/blog/1068661 ](http://wuce7758.iteye.com/blog/1068661)

Tags:  [ Eclipse ](http://www.findspace.name/tag/eclipse) , [ Java ](http://www.findspace.name/tag/java)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/res/1086](http://www.findspace.name/res/1086)