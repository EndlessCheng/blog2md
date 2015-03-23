title: 制作更好的 GIF 另一种更好的办法

date: 2014-03-25 11:11:46

tags: [FFmpeg, ImageMagick, Anime, Multimedia, ]

description: 

---
之前使用 [FFmpeg 制作 GIF](http://blog.phoenixlzx.com/2014/02/19/make-gif-with-ffmpeg/) 被 zyo 吐槽 [明显的网纹](https://plus.google.com/107142103119739092775/posts/asBTCqCnP9A)，于是找到了更好的办法。

需要：FFmpeg 以及 ImageMagick。

依旧不讨论如何截取/剪裁视频文件的问题。例如我们这里要转换的视频文件为 `clip.mp4`，首先使用 ffmpeg 转换成一个个的 PNG 文件，保持纵横比，宽为320像素，帧率为20。为防止文件名混乱，先建立一个 `png` 目录。
    
    
    mkdir -p png
    
    ffmpeg -i clip.mp4 -vf scale=320:-1 -r 20 png/output%05d.png  
  
---  
  
接下来使用 ImageMagick 的 `convert` 工具来把 png 连接成 gif。顺便做优化来缩小文件体积。
    
    
    convert -layers Optimize png/output*.png clip.gif  
  
---  
  
这样就得到了图象效果更好的 `clip.gif` 文件了。不过还有一个问题，不管是本地图象查看器还是浏览器里，这gif都像幻灯片似的。本来觉得是帧率的问题，但是就算是尝试了原帧率一样不行。[Google 之发现了问题…](http://superuser.com/questions/569924/why-is-the-gif-i-created-so-slow)

解决方案在[这里](http://humpy77.deviantart.com/journal/Frame-Delay-Times-for-Animated-GIFs-214150546)。不使用 `-delay 0` 或者是大于 `6/100` 的值。

所以刚才的命令可以稍微修改下。几次测试后发现对于我的原视频(23fps)，`4/100` 最合适。
    
    
    convert -layers Optimize -delay 4/100 png/output*.png clip.gif  
  
---  
  
这样制作出来的 gif 效果就非常赞啦。虽然比之前多了一个步骤，但是确实是制作了更好的gif，是更好的方法。
