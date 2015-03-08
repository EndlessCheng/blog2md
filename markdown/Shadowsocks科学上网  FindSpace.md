#  Shadowsocks科学上网 

[ Find ](http://www.findspace.name/author/find) |  2014年12月3日  |  [ 推荐阅读 ](http://www.findspace.name/category/recommend) , [ 网络文摘 ](http://www.findspace.name/category/res/fromweb) , [ 资源 ](http://www.findspace.name/category/res) |  [ 7条评论  ](http://www.findspace.name/res/956#comments)

自己配了下试了试，发现速度比goagent快了不止一点，当然和hosts相比，有些hosts的ip飞速，有些龟速，但是hosts一般是没法观看youtube的。 

###  配置环境准备 

一台vps， [ 可以从这里申请一个免费的vps ](http://pan.baidu.com/s/1o6FRxR8) 。里面的操作系统可以选择，这里以ubuntu为例。 

###  服务器配置 

####  首先确保安装了python2.6或者2.7： 

检查版本： 

> python –version 

####  安装软件包（这里是两条命令，记得一条一条跑） 

> apt-get install build-essential python-pip python-m2crypto python-dev   
pip install gevent shadowsocks 

####  创建一个配置文件： 

> /etc/shadowsocks.json 

创建文件的命令： 

> touch shadowsocks.json 

编辑文件命令 nano shadowsocks.json 或者vi   
这里关于linux的命令不再赘述。如果实在不熟悉，可以百度   
文件内容： 
    
    
    {
    "server":"服务器 IP 地址", #VPS的IP地址
    "server_port":8388, #监听的端口
    "local_address": "127.0.0.1", #本地监听的IP地址，默认为主机
    "local_port":1080, #本地监听的端口
    "password":"mypassword", #服务密码
    "timeout":300, #用于加密的密码
    "method":"aes-256-cfb", #加密方法，推荐 "aes-256-cfb"
    "fast_open": false, #是否使用 TCP_FASTOPEN, true / false
    "workers": 1 #worker 数量，Unix/Linux 可用，如果不理解含义请不要改
    }
    

在实际配置的时候，记得把注释都删掉。 

####  配置完毕后 

如果为了让后台程序一直运行，可以用nohup命令 

> nohup ssserver -c /etc/shadowsocks.json &

单纯运行则是 

> ssserver -c /etc/shadowsocks.json 

服务器已经配置好了 

###  客户端配置 

####  linux（以ubuntu为例）： 

各发行版linux shadowsocks安装方法找官网的说明，这里说下配置方法：   
在自己喜欢的地方新建一个配置文件：   
文件内容 
    
    
    {
    "server":"服务器 IP 地址", #VPS的IP地址
    "server_port":8388, #监听的端口
    "local_address": "127.0.0.1", #本地监听的IP地址，默认为主机
    "local_port":1080, #本地监听的端口
    "password":"mypassword", #服务密码
    "timeout":300, #超时设置
    "method":"aes-256-cfb" #加密方法，推荐 "aes-256-cfb"
    }
    

同样，记得把注释删掉   
然后 

> sslocal -c ./shadowsocks.json 

####  win和mac下可以找个shadowsocks的客户端，会有设置的地方，设置的参数同上面linux的参数相同 

####  android和ios则需要去应用市场搜索shadowsocks，安装即可。或者用fqrouter2。 

###  桌面浏览器配置 

（移动端当然不用配置浏览器）以chrome为例：   
先去chrome应用商店搜索这个拓展Proxy SwitchySharp，如果上不去，可以先试试我博客的hosts，或者从这里[离线下载][2]。安装成功以后，在它的配置里，新建情景模式，shadowsocks（名字随意，自己可以分辨出来就可以），然后在手动配置这里，取消“对所有协议均使用相同的代理服务器”，有些默认这个选项是勾选的。 

** 在下面的socks代理里填入：127.0.0.1，端口保持和上面的远程端口一致，默认是1080，下面选择socks v5 **   
保存，然后选择这个情景模式，快去访问那些“倒闭了的网站”吧～ 

* * *

###  Update 

####  update:12.4 

浏览器插件切换规则的地址： 

> http://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt 

在切换规则–》在线规则列表中填入这个，并选择情景模式为shadowsocks（这是你建立的情景模式的名字），然后就可以有选择地fq了。 

####  update:12.10 

ubuntu添加启动项：   
修改/etc/rc.local在exit0之前添加 

> /usr/local/bin/sslocal -c /home/find/Dropbox/other/shadowsocks.json 

后面是你写的配置文件的地址，注意，这里都用的绝对地址。 

####  update 2015.2.5 

linux下可以用 ** proxychains ** 来对某个命令进行单独翻墙。   
比如 

> proxychains git push origin master 

win下的gui客户端可以直接设置全局翻。 

Tags:  [ Chrome ](http://www.findspace.name/tag/chrome) , [ google ](http://www.findspace.name/tag/google) , [ Linux ](http://www.findspace.name/tag/linux) , [ SSH ](http://www.findspace.name/tag/ssh) , [ Ubuntu ](http://www.findspace.name/tag/ubuntu) , [ 树莓派 ](http://www.findspace.name/tag/%e6%a0%91%e8%8e%93%e6%b4%be) , [ 网络资源 ](http://www.findspace.name/tag/websource)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/res/956](http://www.findspace.name/res/956)