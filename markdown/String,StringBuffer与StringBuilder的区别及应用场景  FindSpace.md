#  String,StringBuffer与StringBuilder的区别及应用场景 

[ Find ](http://www.findspace.name/author/find) |  2015年2月15日  |  [ Java ](http://www.findspace.name/category/easycoding/java) , [ 随意Coding ](http://www.findspace.name/category/easycoding) |  [ 没有评论  ](http://www.findspace.name/easycoding/1090#comments)

##  文章一 

#  介绍 

String 字符串常量   
StringBuffer 字符串变量（线程安全）   
StringBuilder 字符串变量（非线程安全） 

#  深入说明 

简要的说， String 类型和 StringBuffer 类型的主要性能区别其实在于 String 是不可变的对象, 因此在每次对 String 类型进行改变的时候其实都等同于生成了一个新的 String 对象，然后将指针指向新的 String 对象，所以经常改变内容的字符串最好不要用 String ，因为每次生成对象都会对系统性能产生影响，特别当内存中无引用对象多了以后， JVM 的 GC 就会开始工作，那速度是一定会相当慢的。   
而如果是使用 StringBuffer 类则结果就不一样了，每次结果都会对 StringBuffer 对象本身进行操作，而不是生成新的对象，再改变对象引用。所以在一般情况下我们推荐使用 StringBuffer ，特别是字符串对象经常改变的情况下。   
而在某些特别情况下， String 对象的字符串拼接其实是被 JVM 解释成了 StringBuffer 对象的拼接，所以这些时候 String 对象的速度并不会比 StringBuffer 对象慢，而特别是以下的字符串对象生成中， String 效率是远要比 StringBuffer 快的： 
    
    
     String S1 = “This is only a” + “ simple” + “ test”;
     StringBuffer Sb = new StringBuilder(“This is only a”).append(“simple”).append(“ test”);
    

你会很惊讶的发现，生成 String S1 对象的速度简直太快了，而这个时候 StringBuffer 居然速度上根本一点都不占优势。其实这是 JVM 的一个把戏，在 JVM 眼里，这个   
String S1 = “This is only a” + “ simple” + “test”; 其实就是：   
String S1 = “This is only a simple test”; 所以当然不需要太多的时间了。但大家这里要注意的是，如果你的字符串是来自另外的 String 对象的话，速度就没那么快了，譬如： 
    
    
    String S2 = “This is only a”;
    String S3 = “ simple”;
    String S4 = “ test”;
    String S1 = S2 +S3 + S4;
    

这时候 JVM 会规规矩矩的按照原来的方式去做 

在大部分情况下 StringBuffer > String   
StringBuffer   
Java.lang.StringBuffer线程安全的可变字符序列。一个类似于 String 的字符串缓冲区，但不能修改。虽然在任意时间点上它都包含某种特定的字符序列，但通过某些方法调用可以改变该序列的长度和内容。   
可将字符串缓冲区安全地用于多个线程。可以在必要时对这些方法进行同步，因此任意特定实例上的所有操作就好像是以串行顺序发生的，该顺序与所涉及的每个线程进行的方法调用顺序一致。   
StringBuffer 上的主要操作是 append 和 insert 方法，可重载这些方法，以接受任意类型的数据。每个方法都能有效地将给定的数据转换成字符串，然后将该字符串的字符追加或插入到字符串缓冲区中。append 方法始终将这些字符添加到缓冲区的末端；而 insert 方法则在指定的点添加字符。   
例如，如果 z 引用一个当前内容是“start”的字符串缓冲区对象，则此方法调用 z.append(“le”) 会使字符串缓冲区包含“startle”，而 z.insert(4, “le”) 将更改字符串缓冲区，使之包含“starlet”。   
在大部分情况下 StringBuilder > StringBuffer   
java.lang.StringBuilde   
java.lang.StringBuilder一个可变的字符序列是5.0新增的。此类提供一个与 StringBuffer 兼容的 API，但不保证同步。该类被设计用作 StringBuffer 的一个简易替换，用在字符串缓冲区被单个线程使用的时候（这种情况很普遍）。如果可能，建议优先采用该类，因为在大多数实现中，它比 StringBuffer 要快。两者的方法基本相同。 

##  文章二 

做项目中经常用到String和StringBuilder，String可以用“+”来对字符串进行拼接，StringBuilder用append进行拼接，一直不明白既然可以用String，问什么还要用StringBuilder。尽管在做数据库查询的时候，习惯性的用了StringBuilder对查询语句进行拼接，但仍然不知道原因。今天看视频的时候，又看到了StringBuffer，感觉用法又差不多，所以特意查了一下这些东西的区别。   
归纳如下：   
1.在执行速度方面的比较：StringBuilder > StringBuffer 

2.StringBuffer与StringBuilder，他们是字符串变量，是可改变的对象，每当我们用它们对字符串做操作时，实际上是在一个对象上操作的，不像String一样创建一些对象进行操作，所以速度就快了。 

3.StringBuilder：线程非安全的   
StringBuffer：线程安全的 

当我们在字符串缓冲去被多个线程使用是，JVM不能保证StringBuilder的操作是安全的，虽然他的速度最快，但是可以保证StringBuffer是可以正确操作的。当然大多数情况下就是我们是在单线程下进行的操作，所以大多数情况下是建议用StringBuilder而不用StringBuffer的，就是速度的原因。   
对于三者使用的总结：   
1.如果要操作少量的数据用 String   
2.单线程操作字符串缓冲区 下操作大量数据 StringBuilder   
3.多线程操作字符串缓冲区 下操作大量数据 StringBuffer 

* * *

#  Reference: 

[ http://blog.csdn.net/rmn190/article/details/1492013 ](http://blog.csdn.net/rmn190/article/details/1492013)   
[ http://www.jb51.net/article/39775.htm ](http://www.jb51.net/article/39775.htm)

Tags:  [ Java ](http://www.findspace.name/tag/java)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/easycoding/1090](http://www.findspace.name/easycoding/1090)