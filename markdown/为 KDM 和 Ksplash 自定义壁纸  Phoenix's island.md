[ 2014-02-11 ](/2014/02/11/custom-wallpaper-for-kdm-and-ksplash/)

#  为 KDM 和 Ksplash 自定义壁纸 

嘛非常简单的几个小步骤，不过KDE的KDM和启动屏幕不能直接自定义壁纸确实很讨厌。 

###  KDM 

表示 KDM 相对简单所以先说了。首先是下载对应的 KDM 主题，然后解压到一个临时目录下。 

我下载的是 Glassified，在 [ kde-look ](http://kde-look.org/content/show.php/Glassified+Splash?content=84124) 上非常受欢迎的一款玻璃效果主题。 

Glassified 主题解压后得到了 ` background.svg ` 和 ` glassfied.xml ` 等等文件。由于我的壁纸是 JPEG 格式而且本机没安装 Inkscape (放心 GIMP 不支持矢量图的…) 所以只好直接把图片切割并缩放为适合我屏幕分辨率的文件放进来，重命名为 ` background.jpg ` 。因为文件变了，所以打开 ` glassified.xml ` 文件，查找 ` background.svg ` 并全部替换成 ` background.jpg ` <del> 其实就替换了一处 </del>

接下来返回上级目录，把 ` Glassified ` 目录压缩为 ` .tar.gz ` 或 ` .tar.bz2 ` 文件，就可以直接在 KDE 系统设置里安装了。(安装KDM主题需要root权限哦) 

###  KSplash 

Ksplash 其实也不复杂，就是比较蛋疼的是目录很多，一般自己用的话… 我反正是把和我分辨率靠不着边的目录都删了。一样是下载的 Glassified 主题，解压后得到以分辨率命名的目录，扫了一眼居然没有16:9的分辨率啊啊啊啊！虽然我更喜欢16:10但是这也太蛋疼了吧！ 

在 ` 1600x1200 ` 这个目录里找到了所有的文件。其他目录里应该只有 ` background.png ` 或者类似的文件。于是进入 ` 1600x1200 ` 这个目录，用博丽灵梦的壁纸覆盖了 ` background.png ` 。需要注意一点，本本是16:9 1600×900 分辨率的(嗯就是这么奇葩又正常的分辨率) 所以灵梦的壁纸原本是 1600x900，被我缩放成 1600x1200。图片看起来是被压窄了，不过放心——KDE会自动帮你从1600x1200拉伸成适合屏幕分辨率的… 如果放的文件是1600x900或者其他16:9分辨率的话… <del> 效果非常鬼畜哦 </del>

留给自己用的，所以把其他分辨率的都删掉了。如果想要做来分享，那么还需要把图像文件放缩放成正确的比例和分辨率放在对应的目录下。完成后返回上级目录，像KDM主题一样压缩成 ` .tar.gz ` 即可。不需要root权限，可以直接在系统设置里安装。装好了记得测试下哦。 

下面上效果图。 

![KSplash - Hakurei Reimu](http://blog.phoenixlzx.com/static/img/posts/2014-02-11-ksplash.jpg)

PS. Glassifed 这款主题的链接貌似死掉好久了。于是顺便附上下载链接好了。Dropbox 访问不能的话.. 嘛我相信大家都有办法的对吧～ 

  * [ Glassifed KDM ](https://dl.dropboxusercontent.com/u/2705405/Glassified.KDM.tar.gz)
  * [ Glassifed KSplash ](https://dl.dropboxusercontent.com/u/2705405/Glassified.ksplash.tar.gz)

[ Notes ](/categories/Notes/)

[ KDE ](/tags/KDE/) , [ Artwork ](/tags/Artwork/)
#### 原文：[https://blog.phoenixlzx.com/2014/02/11/custom-wallpaper-for-kdm-and-ksplash/](https://blog.phoenixlzx.com/2014/02/11/custom-wallpaper-for-kdm-and-ksplash/)