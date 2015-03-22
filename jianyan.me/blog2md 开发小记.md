title: blog2md 开发小记

date: 2015-03-09T01:10:00.000Z

tags: [Python, 爬虫, markdown, Beautiful Soup, html2text, ]

description: 傲游、360 等浏览器有一个小功能：阅读模式。 How to do that?

---
本文项目地址： [ https://github.com/EndlessCheng/blog2md ](https://github.com/EndlessCheng/blog2md)

#  缘起 

傲游、360 等浏览器有一个小功能：阅读模式，效果如下： 

![](http://endless.qiniudn.com/blogblog2md.png)

转换后 

![](http://endless.qiniudn.com/blogblog2md2.png)

去掉了一些杂七杂八的东西。 

How to do that? 

识别出那些「垃圾标签」然后去掉就行，比如下图的 ` <div class="tag2box"> ` 。 

![](http://endless.qiniudn.com/blogblog2md3.png)

#  编码 

知道原理后编码就简单了。 

  1. ` requests.session().get(url).content ` 获取 HTML 文本； 
  2. 通过 ` BeautifulSoup ` 中的 ` extract() ` 函数来「修剪」网页； 
  3. ` html2text(html) ` 将 html 转成 markdown 文本，然后写入文件，搞定。 

这里指出 ` html2text ` 的一个 bug：在 ` html2text\config.py ` 文件中有这么一行 
    
    
    BODY_WIDTH = 78  
  
---  
  
这会导致转换后的 markdown 中某段文字莫名其妙地被换行，将其修改成 
    
    
    BODY_WIDTH = 0  
  
---  
  
即可。 

如果要获取博客的全部文章的话，还需要爬虫爬更多页面的信息，详见 [ 源码 ](https://github.com/EndlessCheng/blog2md) 。 
