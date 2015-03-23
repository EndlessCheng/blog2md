title: Ubuntu 服务器配置简易指南

date: 2014-02-01 00:37:34

tags: [Ubuntu, Server, Configuration, ]

description: 

---
之前许诺过的… 虽然像装系统一样纯体力活，靠的是经验，没啥技术含量。不过既然答应了，写出来也算是自己 Note 一下。

本文所有操作均在 Ubuntu 12.04 LTS Server 下测试通过(需要 root 权限)。或者说，已经在无数个 Ubuntu 12.04 LTS Server 下使用过了… Debian 的话，应该大差不差，有些包可能没有或者名称不一样，需要适当做调整。

**注意：如果未声明「新建文件」则只修改对应的行，并非整个配置文件内容。请使用查找功能查找对应变量或语句来完成修改。**

### Step 1. SSH 基本配置

不管是独立服务器还是 VPS，SSH 都是远程管理利器。一般 VPS 是通过操作系统模板安装，默认允许 root 帐号登录。独立服务器如果是手动安装的系统，大部分情况下禁用了 root 帐号登录。首先我们要配置使用公钥登录，并且在尽可能的情况下禁用 root 登录和密码登录。
    
    
    # 创建 RSA 密钥对 (本地)
    
    ssh-keygen -t rsa  
  
---  
  
这个过程中会需要你填写一些基本信息，照样例填写即可。完成后会在 `~/.ssh` 目录下生成 `id_rsa` 文件和 `id_rsa.pub` 文件(生成文件时用默认文件路径和文件名的话)。前者是私钥，也就是无论如何都不能让第二个人知道的东西；后者是公钥，一般来讲，只要你不让 Jeff Dean 看到，你可以把它满大街扔。

得到服务器 root 或带有管理员权限(sudo) 帐号的密码后，使用 `ssh-copy-id` 来传输公钥。

根据 ssh-copy-id 的[手册](http://linux.die.net/man/1/ssh-copy-id)，命令格式如下。
    
    
    # 发送公钥到服务器，这里服务器IP为 192.168.1.102
    
    # 格式： ssh-copy-id [-i [identity_file]] [user@]machine 
    
    ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.1.102  
  
---  
  
如果是第一次连接该服务器(大部分情况是这样)，ssh 会询问是否接受服务器指纹。一般来说如果服务器指纹改变则有可能你遇到了中间人攻击(比如你连接的服务器不是你的而是一个蜜罐等，使用IP而不是域名可以一定程度上避免该问题，但是如果有路由级劫持的话，那就不好说了。但是一般来讲，在私人网络里遇到路由级劫持的情况也只有天朝的ISP才干的出来。)，此时应停止继续连接，检查网络后再尝试。不过还有另一种情况：重装系统后指纹也会变掉。

确定没问题后敲 `yes` 来继续连接，接下来会询问帐号的密码。输入正确密码即可将公钥保存到服务器的正确位置。抑或你可以用更笨一点的方法，首先尝试ssh连接服务器并用密码登录，然后手动执行命令：
    
    
    # 保存公钥
    
    mkdir -p ~/.ssh
    
    echo 'your_public_key_here' > ~/.ssh/authorized_keys
    
    chmod 0700 ~/.ssh && chmod 0600 ~/.ssh/authorized_keys  
  
---  
  
`authorized_keys` 文件权限不正确的话是不会生效的哦。公钥保存到服务器上之后可以新开一个 ssh session 尝试连接服务器，如果密钥没有密码保护的话，应该直接就进去了。确保配置正确，再退出服务器， **尤其是禁用密码登录后应在结束最后一个 session 前检查是否可以正确登录服务器** ，不然退出来之后很可能别想再连上去了…

在进行接下来的任何操作之前，都要保证这些操作不能被中断。在天朝这种奇葩的网络中，ssh 不被中断除非你是用内网，而且就算你内网也说不定，因为没准哪个装了数字公司家产品的内网机器就会给你来个ARP攻击啊什么的把你的ssh断掉。<del>甚至把你整个网络搞瘫痪</del>

于是—— [Tmux](http://tmux.sourceforge.net/) 登场！

可以首先看一下 Tmux 的[手册](http://www.openbsd.org/cgi-bin/man.cgi?query=tmux&sektion=1) 或者简单使用的话掌握如下几个操作：

  * `tmux` # 启动新的 Tmux session
  * `tmux attach` # 连接到已存在的 Tmux session

在 Tmux 中，默认的组合键是 `CTRL+B`，配合其他键盘命令：

  * `^B+D` # 断开当前 session，session 中的程序将会继续运行
  * `^B+C` # 创建新的 console，在一个 console 正在执行任务时可以创建一个新的来执行其他任务。
  * `^B+[Number]` # 切换到对应的 console，比如 `^B+1` 切换到ID为1的 console

有了 tmux 之后，即使 ssh 断掉，也可以重新连接并使用 `tmux attach` 来恢复工作(也有很多其他类似的替代，比如 screen/byobu 等)。于是现在新建一个 tmux session 并开始后续配置步骤。
    
    
    # 新建 tmux session
    
    tmux
    
    # 安装 sshguard 防止 ssh 暴力破解
    
    apt-get install sshguard  
  
---  
  
类似 sshguard 的还有 fail2ban 等。

如果使用的是 VPS 的话，最重要的——不要忘记更改密码。命令：`passwd`

### Step 2. LNMP

很多童鞋买了 VPS 什么的就为了跑一个 WordPress，然后听信传言说什么 LAMP 啊之类的… 我的亲身体会是，在你有足够大的内存之前，Apache 这个东西真的不要碰… 就算我开一台4GB内存的VPS 一样会因为各种原因(包括内存不足) Apache 莫名挂掉。

安装 LNMP 命令：
    
    
    apt-get install php5-cgi php5-mysql php5-fpm php5-curl php5-gd php5-idn php-pear php5-imap php5-mcrypt php5-mhash php5-pspell php5-recode php5-snmp php5-sqlite php5-tidy php5-xmlrpc php5-xsl nginx mysql-server  
  
---  
  
看起来很长… 其实这一条就基本啥都搞定了的说(

另外推荐安装 PHP 字节码加速器 XCache，之前折腾 memcached 的时候被猫菊苣吐槽说这货速度不够快于是果断受诱导换了 XCache… 然后确实比 memcached 快多了。
    
    
    # 安装 XCache
    
    apt-get install php5-xcache  
  
---  
  
#### 配置 PHP

文件 `/etc/php5/fpm/php.ini`
    
    
    # 修改最大上传大小为 10M，两个位置，一个 upload_max_filesize 一个 post_max_size
    
    upload_max_filesize = 10M
    
    post_max_size = 10M
    
    # 修改最大内存使用，默认是128M，如果你内存较多又是专门跑PHP的可以适当加大，具体数值建议做压力测试。
    
    memory_limit = 128M
    
    # 修改最大执行时间，默认30，同样如果是跑PHP的服务器可以适当加大。
    
    max_execution_time = 30  
  
---  
  
文件 `/etc/php5/fpm/pool.d/www.conf`
    
    
    # 修改侦听路径为 UNIX socket
    
    listen = /var/run/php5-fpm.sock
    
    # 修改 process manager 最大请求数量限制以防服务器挂掉，默认该语句被注释掉(应该是不限制？) 一般VPS直接取消注释即可。
    
    pm.max_requests = 500  
  
---  
  
#### 配置 NGINX

文件 `/etc/nginx/nginx.conf`
    
    
    # 修改 NGINX 进程数量，根据CPU核心数而定
    
    worker_processes 4;
    
    # events 部分，修改 NGINX 进程连接数，同时打开多线程(默认被注释，取消注释即可)
    
    worker_connections 1024;
    
    multi_accept on;
    
    # http 部分，关闭服务器版本号(默认被注释，取消注释即可)
    
    server_tokens off;
    
    # 打开 GZIP 减少数据量，会稍微增加CPU负担。这些语句直接取消注释即可。
    
    gzip on;
    
    gzip_disable "msie6";
    
    gzip_vary on;
    
    gzip_proxied any;
    
    gzip_comp_level 6;
    
    gzip_buffers 16 8k;
    
    gzip_http_version 1.1;
    
    gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;  
  
---  
  
#### 安装 Postfix

如果你需要让该服务器上任何程序发邮件的话，除非使用外部SMTP服务器，否则需要一个程序来提供 Sendmail
    
    
    apt-get install postfix  
  
---  
  
安装过程中会询问 Postfix 的工作环境，这里选择「Internet site」，然后填写自己的域名地址。

### Step 3. 安装 WordPress

**这里用 WordPress 作为一个样例，其他基于PHP+MySQL的网站程序同理。**

下载最新的简体中文版 WordPress 程序到服务器网站路径(当前版本 3.8.1，网站目录为 /var/www，也可以使用其他较为安全的目录)，并为站点文件设置正确的权限。
    
    
    cd /var/www
    
    wget -c http://cn.wordpress.org/wordpress-3.8.1-zh_CN.tar.gz
    
    tar zxfv wordpress-3.8.1-zh_CN.tar.gz
    
    # 解包后网站目录即是 /var/www/wordpress
    
    rm wordpress-3.8.1-zh_CN.tar.gz
    
    chown -R www-data:www-data .
    
    find . -type f -exec chmod 644 {} \;
    
    find . -type d -exec chmod 755 {} \;  
  
---  
  
新建站点配置文件 `/etc/nginx/sites-available/wordpress.conf`
    
    
    server {
    
    	# 默认侦听所有IPv4地址，如果需要同时侦听 IPv4+IPv6 则添加：
    
    	# listen [::]:80;
    
            server_name example.com www.example.com;
    
            # 如果是二级域名则是
    
            # server_name suddomain.example.com
    
    	access_log   /var/log/nginx/example.com.access.log;
    
    	error_log    /var/log/nginx/example.com.error.log;
    
            root /var/www/wordpress;
    
            index index.php;
    
            location / {
    
                    try_files $uri $uri/ /index.php?$args; 
    
            }
    
            location ~ \.php$ {
    
                    try_files $uri =404;
    
                    include fastcgi_params;
    
                    fastcgi_pass unix:/var/run/php5-fpm.sock;
    
            }
    
    }  
  
---  
  
保存，把配置文件链接到 NGINX 的网站配置目录
    
    
    ln -s /etc/nginx/sites-available/wordpress.conf /etc/nginx/sites-enabled/  
  
---  
  
重启 NGINX
    
    
    service nginx restart  
  
---  
  
**注意** 如果是较新的 NGINX 版本，要同时侦听 IPv4 和 IPv6，需要在默认服务器配置，一般来说是在 `/etc/nginx/sites-enabled/default` 这个文件中定义的(其实就是 listen 后面带有 default_server 的站点配置文件)，`listen` 部分改为
    
    
    listen [::]:80 default_server ipv6only=off;  
  
---  
  
其他站点配置的 `listen` 部分仍为
    
    
    listen [::]:80;  
  
---  
  
即可。

连接数据库，为网站程序新建数据库和用户。
    
    
    mysql -u root -p  
  
---  
  
这会向你索要 root 密码。在安装过程中， MySQL 的 root 密码应该已经被正确设置。接下来新建用户和数据库。
    
    
    # 新建数据库
    
    create database `wordpress`;
    
    # 新建用户
    
    create user `wordpress` identified by 'YourStrongPassWordHereLoL';
    
    # 赋予权限
    
    grant all privileges on wordpress.* to wordpress@localhost identified by 'YourStrongPassWordHereLoL';
    
    # 刷新权限表
    
    flush privileges;
    
    # 退出
    
    exit  
  
---  
  
这样我们就得到了一个数据库名为 `wordpress`，以及一个拥有权限的用户 `wordpress` 及其密码 `YourStrongPassWordHereLoL`。

此时如果你的域名已经正确配置并解析，访问你的域名将看到 WordPress 的安装向导。使用上面的数据库连接信息即可完成安装。

### Step 4. 配置 Node.js

Node.js 越来越火爆了。咱也是 Node.js developer (作死自大一回..) 不过对于更多用户来讲，Node.js 的吸引力在于大量方便的Web应用。<del>比如末影袜</del>

Ubuntu 12.04 的 Node 版本还是 0.6.x 真是不能忍。
    
    
    # 安装 Git 以及其他必须的组件
    
    apt-get install git build-essential zlib1g-dev
    
    # 安装 n
    
    git clone https://github.com/visionmedia/n.git
    
    cd n && make
    
    # 安装最新版 Node.js，当前为 0.10.25
    
    n 0.10.25  
  
---  
  
然后 Node.js 环境就部署完毕啦。简单吧？

安装一个 Node 应用
    
    
    npm install -g shadowsocks  
  
---  
  
干啥的我就不多说了。嗯。 `-g` 表示全局安装，会安装到 `/usr/lib/node_modules` 下作为可执行程序。

### 完

暂时写这么多。想起来会继续更新下。

部分内容来源：

  * [Felix Wiki](http://felixc.at/) \- 有猫菊苣这个 Wiki 在真是干啥都方便啊啊哈哈哈哈。
