#  [ [Node]npm的那些事儿：最好别用sudo进行-g安装 ](/pleasecallmewhy/article/details/35987757)

今天看到how to node 上的一篇文章： [ http://howtonode.org/introduction-to-npm ](http://howtonode.org/introduction-to-npm) ，其中关于sudo的一段深有体会，分享给大家。 

  


简单翻译关键的一段： 

我强力的建议不要使用sudo进行包管理！ 

安装包可能会运行一些自己的脚本，会导致 sudo操作 像用电锯剪头发一样不安全。 

建议使用如下命令修改usr/local的权限： 
    
    
    sudo chown -R $USER /usr/local
    

  
  


这样就再也不需要sudo命令了。 
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/35987757](http://blog.csdn.net/pleasecallmewhy/article/details/35987757)