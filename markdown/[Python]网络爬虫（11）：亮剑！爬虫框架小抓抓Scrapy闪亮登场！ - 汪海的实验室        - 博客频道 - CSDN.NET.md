#  [ [Python]网络爬虫（11）：亮剑！爬虫框架小抓抓Scrapy闪亮登场！ ](/pleasecallmewhy/article/details/19354723)

[ 爬虫 ](http://www.csdn.net/tag/%e7%88%ac%e8%99%ab) [ python ](http://www.csdn.net/tag/python)

前面十章爬虫笔记陆陆续续记录了一些简单的Python爬虫知识， 

用来解决简单的贴吧下载，绩点运算自然不在话下。 

不过要想批量下载大量的内容，比如知乎的所有的问答，那便显得游刃不有余了点。 

于是乎，爬虫框架Scrapy就这样出场了！ 

Scrapy = Scrach+Python，Scrach这个单词是抓取的意思， 

暂且可以叫它：小抓抓吧。 

  


小抓抓的官网地址： [ 点我点我 ](http://doc.scrapy.org/en/latest/) 。   


  


那么下面来简单的演示一下小抓抓  Scrapy  的安装流程。 

具体流程参照： [ 官网教程 ](http://doc.scrapy.org/en/latest/intro/install.html#intro-install-platform-notes)   


友情提醒：一定要按照Python的版本下载，要不然安装的时候会提醒找不到Python。建议大家安装32位是因为有些版本的必备软件64位不好找。 

  


1.安装Python（建议32位） 

建议安装Python2.7.x，3.x貌似还不支持。 

安装完了记得配置环境，将python目录和python目录下的  Scripts  目录添加到系统环境变量的Path里。 

在cmd中输入python如果出现版本信息说明配置完毕。 

  


2.安装lxml 

lxml是一种使用 Python 编写的库，可以迅速、灵活地处理 XML。点击 [ 这里 ](https://pypi.python.org/pypi/lxml/3.3.1) 选择对应的Python版本安装。 

  


3.安装setuptools 

用来安装egg文件，点击 [ 这里 ](https://pypi.python.org/packages/2.7/s/setuptools/) 下载python2.7的对应版本的setuptools。 

  


4.安装zope.interface 

可以使用第三步下载的setuptools来安装egg文件，现在也有exe版本，点击 [ 这里 ](https://pypi.python.org/pypi/zope.interface/4.1.0#downloads) 下载。 

  


5.安装Twisted 

Twisted是用Python实现的基于事件驱动的网络引擎框架，点击 [ 这里 ](http://twistedmatrix.com/trac/wiki/Downloads) 下载。 

  


6.安装pyOpenSSL 

pyOpenSSL是Python的OpenSSL接口，点击 [ 这里 ](https://launchpad.net/pyopenssl) 下载。 

  


7.安装win32py 

提供win32api，点击 [ 这里 ](http://sourceforge.net/projects/pywin32/files/) 下载   


  


8.安装  Scrapy   


终于到了激动人心的时候了！安装了那么多小部件之后终于轮到主角登场。 

直接在cmd中输入easy_install scrapy回车即可。 

  


9.检查安装 

打开一个cmd窗口，在任意位置执行scrapy命令，得到下列页面，表示环境配置成功。 

![](http://img.blog.csdn.net/20140221175118390?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/19354723](http://blog.csdn.net/pleasecallmewhy/article/details/19354723)