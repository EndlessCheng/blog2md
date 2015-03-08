[ ![简言](/img/logo.png) ](/)

#  [ 简言 ](/)

##  言简意赅，技术远没那么复杂

    * [ Home ](/)
    * [ Archives ](/archives)
    * [ About ](/about)
    * Search 

#  [ Django 中设置 css/js/images 路径的方法 ](/2014/09/18/django-sets-the-css-js-
images-path/)

By [ 简言 ](https://plus.google.com/103441795113657293146?rel=author)

Published Sep 18 2014

** Contents **

在 settings.py 的最后一行你可以看到 ` STATIC_URL = '/static/' ` 这句话，在其后面加上：

    
    
    1
    
    2
    
    3
    
    4
    
    5
    
    6
    
    7

|

    
    
    STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
    
    STATICFILES_DIRS = (
    
        ('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/') ),
    
        ('js', os.path.join(STATIC_ROOT, 'js').replace('\\', '/') ),
    
        ('images', os.path.join(STATIC_ROOT, 'images').replace('\\', '/') ),
    
    )  
  
---|---  
  
然后把你的 css/js/images 那些文件夹都丢进 static 文件夹中（此文件夹应建立在你的 view.py 所在目录下）  
模板里面这么写：

    
    
    1

|

    
    
    <link type="text/css" rel="stylesheet" href="/static/css/login.css">  
  
---|---  
  
如果设置之后出现了与 Unicode 有关的错误，打开 ` /Python27/Lib/mimetypes.py ` ，在 import 语句之后加入：

    
    
    1
    
    2
    
    3

|

    
    
    if sys.getdefaultencoding() != 'gbk':
    
        reload(sys)
    
        sys.setdefaultencoding('gbk')  
  
---|---  
  
[ Django ](/tags/Django/)

[ ** 上一篇： **  
GitHub 秘籍  ](/2014/09/23/github-cheats/)

[ ** 下一篇： **  
Git 用的越早，你就活得越久  ](/2014/07/04/earlier-for-git-youll-live-longer/)

Please enable JavaScript to view the [ comments powered by Disqus.
](//disqus.com/?ref_noscript)

** Contents **

Tag Cloud

[ Android ](/tags/Android/) [ C ](/tags/C/) [ Django ](/tags/Django/) [ GHC
](/tags/GHC/) [ Git ](/tags/Git/) [ GitHub ](/tags/GitHub/) [ Hexo
](/tags/Hexo/) [ JNI ](/tags/JNI/) [ Jacman ](/tags/Jacman/) [ Java
](/tags/Java/) [ Markdown ](/tags/Markdown/) [ PIL ](/tags/PIL/) [ Pillow
](/tags/Pillow/) [ Python ](/tags/Python/) [ SAE ](/tags/SAE/) [ macro
](/tags/macro/) [ 「Hello World」 ](/tags/「Hello-World」/) [ 杂谈 ](/tags/杂谈/) [
混合编程 ](/tags/混合编程/) [ 爬虫 ](/tags/爬虫/) [ 网络传输协议 ](/tags/网络传输协议/)

Links

  * [ Logdown 博客 ](http://endless.logdown.com/)
  * [ CSDN 博客 ](http://blog.csdn.net/synapse7?viewmode=list)
  * [ GitHub ](https://github.com/EndlessCheng)

[ RSS ](/atom.xml)

[ ](https://github.com/EndlessCheng) [
](http://stackoverflow.com/users/3208881) [
](https://www.douban.com/people/52879216) [
](https://www.zhihu.com/people/endlesscheng) [
](https://plus.google.com/103441795113657293146?rel=author) [
](mailto:loli.con@qq.com)

Powered by [ hexo ](http://zespia.tw/hexo/) and Theme by [ Jacman
](https://github.com/wuchong/jacman) © 2015 [ 简言 ](http://jianyan.me/about)

![](/img/scrollup.png)

