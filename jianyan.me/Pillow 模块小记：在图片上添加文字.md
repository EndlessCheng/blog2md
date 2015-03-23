title: Pillow 模块小记：在图片上添加文字

date: 2014-12-09T09:00:00.000Z

tags: [Pillow, PIL, Python, ]

description: 1. 图片来自 [知乎](http://zhuanlan.zhihu.com/zhihu-product) 2. 颜色参考了 [Adobe Color CC](https://color.adobe.com/zh/explore/most-popular/?time=all) 3. [RGBA color space](http://en.wikipedia.org/wiki/RGBA_color_space) 4. [Python 练习册，每天一个小程序](https://github.com/Show-Me-the-Code/show-me-the-code)

---
首先 `pip install Pillow` 安装 Pillow 模块。（这名字挺萌的）

直接上代码：
    
    
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
  
---  
  
效果图：

![](http://endless.qiniudn.com/blogpillow.bmp)

参考资料：

  1. 图片来自 [知乎](http://zhuanlan.zhihu.com/zhihu-product)
  2. [RGBA color space](http://en.wikipedia.org/wiki/RGBA_color_space)
  3. [Python 练习册，每天一个小程序](https://github.com/Show-Me-the-Code/show-me-the-code)

附上最近发现的一个好网站：[Adobe Color CC](https://color.adobe.com/zh/explore/most-popular/?time=all)
