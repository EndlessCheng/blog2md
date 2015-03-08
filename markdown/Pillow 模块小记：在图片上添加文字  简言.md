[ ![简言](/img/logo.png) ](/)

#  [ 简言 ](/)

##  言简意赅，技术远没那么复杂

    * [ Home ](/)
    * [ Archives ](/archives)
    * [ About ](/about)
    * Search 

#  [ Pillow 模块小记：在图片上添加文字 ](/2014/12/09/notes-of-the-pillow-moudle-adding-
text-on-the-picture/)

By [ 简言 ](https://plus.google.com/103441795113657293146?rel=author)

Published Dec 9 2014

** Contents **

首先 ` pip install Pillow ` 安装 Pillow 模块。（这名字挺萌的）

直接上代码：

    
    
    1
    
    2
    
    3
    
    4
    
    5
    
    6
    
    7
    
    8
    
    9
    
    10
    
    11
    
    12
    
    13
    
    14
    
    15
    
    16
    
    17
    
    18
    
    19
    
    20
    
    21
    
    22
    
    23
    
    24
    
    25
    
    26

|

    
    
    # -*- coding: utf-8 -*-
    
    import urllib
    
    from io import BytesIO
    
    from PIL import Image, ImageDraw, ImageFont
    
    PIC_URL = "http://pic1.zhimg.com/3676e9bd6_l.jpg"
    
    DRAW_WORD = u"①"
    
    TRANSPARENT = (255, 255, 255, 0)
    
    SOFT_RED = (243, 90, 74, 255)
    
    rsp = urllib.urlopen(PIC_URL)
    
    data = rsp.read()
    
    fp = BytesIO()
    
    fp.write(data)
    
    fp.seek(0, 0)
    
    base_image = Image.open(fp).convert('RGBA')
    
    fnt = ImageFont.truetype('CALIBRI.TTF', base_image.size[0] / 4)  # FreeTypeFont
    
    fnt_size = fnt.getsize(DRAW_WORD)
    
    txt_image = Image.new('RGBA', base_image.size, TRANSPARENT)
    
    ImageDraw.Draw(txt_image).text((base_image.size[0] - fnt_size[0], 10), DRAW_WORD, fill=SOFT_RED, font=fnt)
    
    out = Image.alpha_composite(base_image, txt_image)
    
    out.show()  
  
---|---  
  
效果图：

![](http://endless.qiniudn.com/blogpillow.bmp)

参考资料：

  1. 图片来自 [ 知乎 ](http://zhuanlan.zhihu.com/zhihu-product)
  2. [ RGBA color space ](http://en.wikipedia.org/wiki/RGBA_color_space)
  3. [ Python 练习册，每天一个小程序 ](https://github.com/Show-Me-the-Code/show-me-the-code)

附上最近发现的一个好网站： [ Adobe Color CC ](https://color.adobe.com/zh/explore/most-
popular/?time=all)

[ Pillow ](/tags/Pillow/) [ PIL ](/tags/PIL/) [ Python ](/tags/Python/)

[ ** 上一篇： **  
如何在 SAE 上正确地设置 Django 静态文件  ](/2014/12/29/how-to-properly-configure-the-
django-static-files-on-sae/)

[ ** 下一篇： **  
如何写一个无 bug 的 min/max 宏？  ](/2014/11/01/how-to-write-a-bug-free-min-max-macro/)

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

