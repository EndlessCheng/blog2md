#  [ [Linux]在Mac下配置Linux服务器并安装Nginx+PHP ](/pleasecallmewhy/article/details/32104157)

##  ** _ Linux _ **

  * ###  安装Debian系统 

我安装的是 _ Debian _ 7.5的系统， _ Debian _ 的软件包管理和升级十分方便，而且系统也很稳定。   
安装盘可以去 [ 华中科技大学镜像 ](http://mirrors.hust.edu.cn/) 、 [ 网易开源镜像站 ](http://mirrors.163.com/) 或者 [ 中国科技大学镜像 ](http://mirrors.ustc.edu.cn/) 下载，和官网一样，一般下载的时候会提供 _ DVD-1 _ 、 _ DVD-2 _ 和 _ DVD-3 _ 的下载，后面二者均是一些不太流行的软件，只需要下载安装 _ DVD-1 _ 即可。 

  * ###  修改sources.list 

装好系统之后的第一件事情就是修改 _ Debian _ 的源，因为默认的配置会访问镜像介质，修改源可以直接联网通过 ` apt-get ` 获取并安装软件包，可以使用： [ 网易 _ Debian _ 镜像源 ](http://mirrors.163.com/.help/debian.html) 。使用 _ vi _ 编辑保存即可，编辑完毕记得更新软件包。 
    
    
    vi /etc/apt/sources.list    //编辑软件源
    apt-get update              //更新软件包列表
    apt-get upgrade             //更新所有已安装的软件包
    apt-get dist-upgrade        //将系统升级到新版本
    

  * ###  安装 _ SSH _

_ SSH _ 是每一台Linux电脑的标准配置，简单来说，它是一种网络协议，可以用于计算机之间的加密登录。如果对 _ SSH _ 不太熟悉，可以阅读阮一峰老师的 [ SSH原理与运用（一）：远程登录 ](http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)
    
    
    apt-get install openssh-server   
    apt-get install ssh  
    

##  ** _ Mac _ **

  * ###  _ Root _ 远程登录 

使用 _ root _ 用户登录前面配置好的远程 _ Linux _ 主机，更详细的操作建议阅读 [ Linux服务器的初步配置流程 ](http://www.ruanyifeng.com/blog/2014/03/server_setup.html)
    
    
    ssh root@xxx.xxx.xxx.xxx
    

  * ###  配置 _ SSH _

为了避免每次都要输入 _ ip _ 地址，在 ` ~/.ssh ` 目录下创建 ` config ` 文件，以后可以直接用 ` ssh host1 ` 连接远程服务器。 
    
    
    Host host1
    HostName 222.222.222.22  
    User why  
    Port 1223
    

##  ** _ Nginx _ **

配置好了服务器并用 _ SSH _ 远程连接之后，安装 _ Nginx _ 就很简单了。 这里我参考的是 _ binarytides _ 上的一篇文章： [ Setup Nginx + php-FPM + apc + MariaDB on Debian 7 ](http://www.binarytides.com/install-nginx-php-fpm-mariadb-debian/) 首先是安装 _ Nginx _ ： 
    
    
    apt-get install nginx
    

运行如下命令可以启动 _ Nginx _ 服务器： 
    
    
    service nginx start
    

访问一下 ` localhost ` 便会看见 _ Welcome to nginx! _ 说明安装成功。 

接下来就是安装 _ PHP _ 和 _ PHP-fpm _ ： 
    
    
    apt-get install PHP5 PHP5-fpm
    

然后，修改 _ Nginx _ 的配置文件： 
    
    
    vi /etc/nginx/sites-available/default
    

具体的配置内容的意义请查阅官网： [ Nginx Configuration ](http://wiki.nginx.org/Configuration) 。 将和 _ PHP _ 相关的内容改成下面这样： 
    
    
    location ~ \.php$ {
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
    #   # NOTE: You should have "cgi.fix_pathinfo = 0;" in php.ini
    
    #   # With php5-cgi alone:
    #   fastcgi_pass 127.0.0.1:9000;
        # With php5-fpm:
        fastcgi_pass unix:/var/run/php5-fpm.sock;
        fastcgi_index index.php;
        include fastcgi_params;
    }
    

然后在根目录下创建 ` index.php ` 里面写上如下内容： 
    
    
    <?php
        phpinfo();
    ?>
    

再访问本地的地址就可以看到查看PHP属性的页面了。 

##  ** _ Other _ **

  * ###  设置Debian下默认文本编辑器为VIM 
    
    
    apt-get install vim
    update-alternatives --config editor
    

  * ###  使用 _ SSH _ 密钥登陆 

1.如果电脑没有配置过 _ SSH _ ，输入下面这条命令生成密钥： 
    
    
    ssh-keygen  
    

2.多谢二楼朋友 _ 带着石头奔跑 _ 提醒，使用homebrew给Mac电脑添加 ` ssh-copy-id ` 命令： 
    
    
    brew install ssh-copy-id
    

3.将生成的公钥上传到服务器： 
    
    
    ssh-copy-id whyadmin@222.22.222.222  
    

* * *

参考资料： 

  * [ Linux服务器初步配置流程 ](http://www.ruanyifeng.com/blog/2014/03/server_setup.html)
  * [ SSH原理与应用（SSH原理与运用（一）：远程登录） ](http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)
  * [ PostgreSQL新手入门 ](http://www.ruanyifeng.com/blog/2013/12/getting_started_with_postgresql.html)
  * [ Debian Manual Howto ](https://wiki.debian.org/zh_CN/Manual-Howto)
  * [ Nginx Beginner's Guide ](http://nginx.org/en/docs/beginners_guide.html)
  * [ Setup Nginx + php-FPM + apc + MariaDB on Debian 7 ](http://www.binarytides.com/install-nginx-php-fpm-mariadb-debian/)
  * [ What is SFTP ](https://kb.iu.edu/d/akqg)
  * [ ](https://kb.iu.edu/d/akqg)
  * [ ](https://kb.iu.edu/d/akqg)
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/32104157](http://blog.csdn.net/pleasecallmewhy/article/details/32104157)