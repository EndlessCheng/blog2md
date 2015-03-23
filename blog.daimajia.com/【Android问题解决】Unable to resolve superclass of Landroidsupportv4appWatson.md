title: 【Android问题解决】Unable to resolve superclass of Landroidsupportv4appWatson

date: 2013-06-06 07:26:19

tags: []

description: 

---
之前一直在Eclipse上开发小熊词典，Google I/O上推出Android Studio后，就转到Studio上了，但是项目依赖的文件太多，配置总是失败（因为尝试的Git方式管理），就打算重新在Eclipse上配置好再导入到Android Studio中。但是…Eclipse编译通过了，当在手机上运行的时候就出问题了。问题很传统，就是ClassNotFound，这种问题普遍是由于Android.manifest文件中的类名或者包名写错的原因。网上解决方案一大堆，我再三检查根本不是这个问题，我还总是不相信自己的眼睛，删掉ANdorid:name 认真粘贴的路径。。。

但是，这种屌丝的作法根本不解决问题，依然爆出如下错误：（橘黄色是Warning 红色是Error）

  1. **Unable to resolve superclass of Landroid/support/v4/app/Watson;** (149)
  2. **Link of class ‘Landroid/support/v4/app/Watson;’ failed**
  3. **Unable to resolve superclass of Lcom/actionbarsherlock/app/SherlockFragmentActivity; (161)**

….直到最后：

4\.  **java.lang.RuntimeException: Unable to instantiate activity ComponentInfo  java.lang.ClassNotFoundException**

连续搜索了很多此 **Unable to instantiate activity ComponentInfo ClassNotFoundException** (因为总觉得Warning是不足轻重的！)… 看了一堆stackoverflow的帖子，都类似类名出错….最后看到那个warning抱着试一试的态度搜了一下 **Unable to resolve superclass of Landroid/support/v4/app/Watson 在**GitHub的ActionBarSherlock的issue中终于找到了答案，而后百感交集啊。。。总结如下：

问题原因：更新到了SDK 22    具体看此处： [GoogleCode](https://code.google.com/p/android/issues/detail?id=55304) [GitHub Issue](https://github.com/JakeWharton/ActionBarSherlock/issues/857)

问题解决：

  1. 右键项目，选择属性
  2. Java Build Path – > Order and Export
  3. 选中 Android Private Libraries

教训：不要忽略warning！
