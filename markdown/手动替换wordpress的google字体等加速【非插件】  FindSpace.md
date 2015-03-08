#  手动替换wordpress的google字体等加速【非插件】 

[ Find ](http://www.findspace.name/author/find) |  2015年3月4日  |  [ Linux ](http://www.findspace.name/category/easycoding/linux) , [ 随意Coding ](http://www.findspace.name/category/easycoding) |  [ 2条评论  ](http://www.findspace.name/easycoding/1132#comments)

#  查找需要替换的地方 

Linux下，在网站文件夹中，用grep命令查找： 
    
    
    grep -rn "googleapis"
    

也可以将结果输出到文件： 
    
    
    grep -rn "googleapis" >> ans.txt
    

从ans.txt中查看都是哪些文件有googleapis，这个文件的格式是： 

> 文件的相对路径： 第多少行引用的： 该行的内容 

![grep结果](http://bcs.duapp.com/findspace//blog/201503//grepans1.png)

#  替换 

##  手动 

找到并用任意的文本编辑器替换googleapis为useso 

** Warning: **

> 主要是替换ajax.googleapis和fonts.googleapis，www.googleapis不要替换。 

##  命令 

Linux下使用 
    
    
    //这是格式
    sed -i "s/原字符串/新字符串/g" `grep 原字符串 -rl 所在目录`
    //这是替换ajax和fonts
    sed -i "s/ajax.googleapis/ajax.useso/g" `grep ajax.googleapis -rl /home/find/down/780309/wwwroot`
     sed -i "s/fonts.googleapis/fonts.useso/g" `grep fonts.googleapis -rl /home/find/down/780309/wwwroot`
    

** Warning: **

> 在上面的两条语句中，grep 前面的符号`是键盘1前面的那个，不是单引号。 

批量替换结束以后，再使用查找命令检查下是否找不到fonts.googleapis和ajax.googleapis，然后把文件全部传回ftp即可（因为这里你就不知道替换的哪些文件，所以直接全部传回即可）。 

Tags:  [ Linux ](http://www.findspace.name/tag/linux) , [ Ubuntu ](http://www.findspace.name/tag/ubuntu) , [ wordpress ](http://www.findspace.name/tag/wordpress)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/easycoding/1132](http://www.findspace.name/easycoding/1132)