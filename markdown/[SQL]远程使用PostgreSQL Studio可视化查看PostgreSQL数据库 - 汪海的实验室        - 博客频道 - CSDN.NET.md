#  [ [SQL]远程使用PostgreSQL Studio可视化查看PostgreSQL数据库 ](/pleasecallmewhy/article/details/32313611)

1.下载 

前往官网地址下载最新的PostgreSQL Studio，我下载的是 pgstudio_1.2-bin .zip，因为我的电脑里面没有tomcat。 

如果电脑里有配置好tomcat，可以下载pgstudio_1.2.zip，解压之后是一个war包。 

下载地址： [ http://www.postgresqlstudio.org/download/ ](http://www.postgresqlstudio.org/download/)

  


2.解压 

将压缩文件解压，可以看到如下目录： 

![](http://img.blog.csdn.net/20140619101505031?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


3.运行 

在bin目录下运行，启动tomcat： 
    
    
    ./catalina.sh run

  
  


  


4.查看 

浏览器中输入：localhost:8080就可以看到了： 

![](http://img.blog.csdn.net/20140619101630468?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


  


  


  


  


4.修改远程数据库允许访问 

编辑pg_hba.conf 文件，在文件的最下方加上下面的这句话： 
    
    
    host    all         all         0.0.0.0/0             trust 

  


  


编辑postgresql.conf文件，查找“listen_addresses ”字符串，然后修改为如下： 
    
    
    listen_addresses = '*' 

  


  


  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/32313611](http://blog.csdn.net/pleasecallmewhy/article/details/32313611)