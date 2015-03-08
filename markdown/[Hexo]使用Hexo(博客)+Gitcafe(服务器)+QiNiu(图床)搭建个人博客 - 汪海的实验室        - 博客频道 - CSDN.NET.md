#  [ [Hexo]使用Hexo(博客)+Gitcafe(服务器)+QiNiu(图床)搭建个人博客 ](/pleasecallmewhy/article/details/20567151)

** 最近调整了一下博客，基本确定了CSDN记录学习笔记，域名博客记录一些日常的东西，这么一个搭配。 **

**   
**

** 下面给大家简单的介绍一下我的 [ Hexo博客 ](http://blog.callmewhy.com/) 的搭建过程。 **

**   
**

** 首先，我们现在本地使用Hexo搭建一个博客系统。  **

** Hexo的安装过程如下：  **

** 1.下载Git  **

下载 [ Git ](http://msysgit.github.io/) 并执行文件便可以完成安装。   


  


2.下载Node.js 

访问 [ 官网地址 ](http://nodejs.org/) ，点击Install下载安装包，安装即可。 

  


3.安装Hexo框架 

访问 [ Hexo官网 ](http://zespia.tw/hexo/) ，可以看到安装方法。 

在命令提示行输入一下代码即可： 
    
    
    npm install hexo -g

  


4.创建个人博客 

右击后选择git bash，输入： 
    
    
    hexo init

  
初始化hexo项目。 

  


5.运行服务器 

执行一下命令： 
    
    
    hexo generate
    hexo server

  


博客部署在本地地址：http://localhost:4000/ 

查看一下效果： 

![](http://img.blog.csdn.net/20140305204456109?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  


  


具体的Hexo教程可以参考： [ Zippera's Blog ](http://zipperary.com/categories/hexo/)   


  


  


接下来需要去 [ GitCafe ](https://gitcafe.com/) 申请一个空间， 

Gitcafe和Github类似，有一个用于展示的page分支，gitcafe-pages， 

这个具体可以查看一下官方的文档，我就不再赘述了。 

注意git默认是master分支，而只有gitcafe-pages分支下的内容才是可以显示的。 

  


在使用的过程中我发现Hexo贴图片十分的不方便， 

因为MarkDown的语法需要写上图片的路径， 

而部署在本地的文件夹下再用绝对路径去显示的时候总是感觉乱糟糟的， 

并且在使用  markdown  preview预览的时候也无法正常的显示图片。 

  


于是我选择使用 [ 七牛云存储 ](https://portal.qiniu.com) 作为自己的图床。 

上传图片之后可以直接显示图片链接，这样用sublime的markdown preview插件也可以直接在本地预览图片，十分方便。 

  


  


  


总的来说，效果还是不错滴： 

  


![](http://img.blog.csdn.net/20140308003938093?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  


  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/20567151](http://blog.csdn.net/pleasecallmewhy/article/details/20567151)