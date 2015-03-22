title: 使用 FFmpeg 制作 GIF

date: 2014-02-19T06:03:05.000Z

tags: [FFmpeg, Anime, Multimedia, ]

description: 

---
貌似好久之前秋水学姐就问过如何制作 GIF，回想当时制作境界の彼方中「約束の絆」的 [ GIF动画 ](https://plus.google.com/u/0/+PhoenixNemo/posts/RqPTgGrksLV) ，现在也已经把命令忘光了。所以觉得还是稍微做个笔记。 

只需要用到 FFmpeg。绝大多数发行版都已经将它收录官方仓库，通过包管理器就可以安装。 

假设我们需要转换的视频文件是 ` input.ogg ` ，输出的GIF文件是 ` output.gif ` 。这里不讨论如何截取视频中的段落(因为命令太繁 <del> 烦 </del> 琐了)等视频剪辑的问题，需要转换的视频已经经过简单处理，可以直接使用。 

基本命令： 
    
    
    ffmpeg -i input.ogg output.gif  
  
---  
  
第一次制作的gif就是这么来的。然后当我试图上传到 Google+ 的时候发现… 

** 区区几百KB的视频片段制作出来的GIF竟然有20M之巨啊！ ** <del> 原视频是1080p 50fps的 flv </del>

于是需要两个参数，一个是缩小分辨率一个是减少帧数。50帧确实少见，但是一般来讲 gif 有15帧左右就比较流畅了。命令 
    
    
    ffmpeg -i input.ogg -s 640x320 -r 15 output.gif  
  
---  
  
很多人喜欢把 ` -r ` 选项放在前面… 按照某个早就忘记在哪的邮件列表里的说法， ` -r ` 放在 _ 输入文件 _ 的 ** 后面 ** 才是输出文件的效果。上面的命令出来的结果就是分辨率为 ` 640×320 ` ，帧率为15的gif了。 ` 640x320 ` 中间是小写字母 ` x ` <del> 别像某人一样特地复制了一份 ` × ` 进去… </del>
