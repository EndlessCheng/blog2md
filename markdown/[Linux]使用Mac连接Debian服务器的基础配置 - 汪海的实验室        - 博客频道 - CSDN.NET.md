#  [ [Linux]使用Mac连接Debian服务器的基础配置 ](/pleasecallmewhy/article/details/26965275)

** **

> 配置连接服务器请参照： [ Linux服务器初步配置流程 ](http://www.ruanyifeng.com/blog/2014/03/server_setup.html) Debian安装软件手册： [ Debian Manual Howto ](https://wiki.debian.org/zh_CN/Manual-Howto)

###  安装Debian系统 

镜像可以去 [ 华中科技大学镜像 ](http://mirrors.hust.edu.cn/) 下载。 

###  设置Debian下默认文本编辑器为VIM： 
    
    
    aptitude update
    aptitude install vim
    update-alternatives --config editor
    

###  修改Debian的/etc/apt/sources.list如下，防止提示插入介质 
    
    
    # deb http://http.debian.net/debian/ wheezy main contrib non-free
    # deb http:ftp.jp.debian.org/debian sid main
    # deb http://security.debian.org/ wheezy/updates main contrib
    # deb http://ftp.debian.org/debian/ wheezy-updates main contrib
    # deb-src http://ftp.debian.org/debian/ wheezy-updates main contrib
    # deb-src http://security.debian.org/ wheezy/updates main contrib
    deb http://mirrors.163.com/debian/ stable main
    deb-src http://mirrors.163.com/debian/ stable main
    

###  给服务器的Debian系统安装SSH，这样其他电脑就能通过SSH连接 
    
    
    apt-get install openssh-server   
    apt-get install ssh  
    

###  使用Mac生成SSH公钥和密钥 
    
    
    ssh-keygen  
    

###  给Mac电脑添加 ` ssh-copy-id ` 命令 
    
    
    sudo curl https://raw.githubusercontent.com/beautifulcode/ssh-copy-id-for-OSX/master/ssh-copy-id.sh -o /usr/local/bin/ssh-copy-idsudo   
    chmod +x /usr/local/bin/ssh-copy-id  
    

###  将生成的公钥上传到服务器 
    
    
    ssh-copy-id whyadmin@222.22.222.222  
    

###  ssh连接Debian出现warning: Falling back to the standard locale ("C") 
    
    
    // 1.在/home/your-login/.bashrc里面添加：  
    export LC_ALL=C  
    // 2. 运行：  
    source ~/.bashrc  
    

###  配置SSH的config文件，以后直接用 ` ssh host1 ` 连接 
    
    
    Host host1
    HostName 222.222.222.22  
    User why  
    Port 1223

  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/26965275](http://blog.csdn.net/pleasecallmewhy/article/details/26965275)