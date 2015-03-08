[ ![简言](/img/logo.png) ](/)

#  [ 简言 ](/)

##  言简意赅，技术远没那么复杂

    * [ Home ](/)
    * [ Archives ](/archives)
    * [ About ](/about)
    * Search 

#  [ 如何在 SAE 上正确地设置 Django 静态文件 ](/2014/12/29/how-to-properly-configure-the-
django-static-files-on-sae/)

By [ 简言 ](https://plus.google.com/103441795113657293146?rel=author)

Published Dec 29 2014

** Contents **

1.目录结构如下：（请无视 ` .idea ` 文件夹）

![](http://endless.qiniudn.com/blogsae-django-static.png)

2\. ` config.yaml ` 只需要两行：

    
    
    1
    
    2
    
    3

|

    
    
    libraries:
    
    - name: "django"
    
      version: "1.5"  
  
---|---  
  
3\. ` settings.py ` 里面这样写：

    
    
    1
    
    2
    
    3
    
    4
    
    5
    
    6
    
    7

|

    
    
    STATIC_ROOT = ''
    
    STATIC_URL = '/static/'
    
    STATICFILES_DIRS = (
    
        os.path.join('static'),
    
    )  
  
---|---  
  
4\. ` urls.py ` 只需要加上你的 view 就行。

5.模板里面这样写：

![](http://endless.qiniudn.com/blogsae-django-static2.png)

搞定。

PS： ` USE_TZ ` 要设置成 ` False ` ，否则插入时间到数据库的时候会变成 UTC 时间而不是北京时间。

参考资料：

  1. [ Managing static files (CSS, images) ](https://docs.djangoproject.com/en/dev/howto/static-files/)
  2. [ The staticfiles app ](https://docs.djangoproject.com/en/1.5/ref/contrib/staticfiles/)
  3. [ Settings Documentation ](https://docs.djangoproject.com/en/1.5/ref/settings/)

[ Django ](/tags/Django/) [ SAE ](/tags/SAE/)

[ ** 上一篇： **  
访问网页的过程——常见网络传输协议汇总  ](/2015/01/13/access-pages-common-network-transport-
protocol-summary/)

[ ** 下一篇： **  
Pillow 模块小记：在图片上添加文字  ](/2014/12/09/notes-of-the-pillow-moudle-adding-text-on-
the-picture/)

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

