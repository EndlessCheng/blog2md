#  [ [Hexo]通过别名快速执行Hexo的命令 ](/pleasecallmewhy/article/details/38460601)

Hexo的命令说多也不多，但是每次部署都需要cd到目录然后发布也是蛮烦人的。 

  


可以在终端的配置文件中加入别名： 

  

    
    
    alias blogd="cd ~/workspace/callmewhy/blog/ && hexo clean && hexo d -g"
    alias blogu="cd ~/workspace/callmewhy/blog/ && git add . --all && git commit -m 'add new post' && git push -u origin master"

  
这样只需要blogd就能发布，blogu就能add变动commit并且将博客源码上传到服务器上。 
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/38460601](http://blog.csdn.net/pleasecallmewhy/article/details/38460601)