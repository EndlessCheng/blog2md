[ 2014-07-21 ](/2014/07/21/setup-openconnect-server-on-ubuntu/)

#  在 Ubuntu 服务器上搭建 OpenConnect 服务器小记 

最近猫给推荐的 Cisco AnyConnect，面基的时候也看到 Aveline 菊苣在用 AnyConnect(插嘴：正太菊苣果然好可爱！！！) 于是自己折腾了下。作为少有的能让我折腾起来的 VPN，暂且把搭建步骤简单记录下。 

AnyConnect 的好处是基于 HTTPS，证书可以申请 StartSSL 的，而且配置也不很复杂。另外配置文件里发现了很多专门为商业化/企业服务定制的选项，例如最大同时在线客户端数量，同账户最大在线设备数量等等。 

OpenConnect 是 AnyConnect 的开源实现。目前 0.8.0 版本需要 GnuTLS 3.1 以上版本，所以我们就直接在 Ubuntu 14.04 中搭建。另外 就算是基于 HTTPS，这货也是要用 TUN 设备的，所以 OpenVZ 用户们请注意。 

###  准备 

命令 
    
    
    apt-get install build-essential libwrap0-dev libpam0g-dev libdbus-1-dev \
    
      libreadline-dev libnl-route-3-dev libprotobuf-c0-dev libpcl1-dev libopts25-dev \
    
      autogen libgnutls28 libgnutls28-dev libseccomp-dev libhttp-parser-dev  
  
---  
  
###  安装 

下载源码 
    
    
    wget -c ftp://ftp.infradead.org/pub/ocserv/ocserv-0.8.0.tar.xz
    
    tar xvf ocserv-0.8.0.tar.xz
    
    cd ocserv-0.8.0  
  
---  
  
编译安装 
    
    
    ./configure --prefix=/opt/ocserv 
    
    make
    
    make install
    
    mkdir /opt/ocserv/etc/
    
    cp doc/sample.config /opt/ocserv/etc/config  
  
---  
  
###  配置 

这里只记录需要修改的重点配置，其他配置请参照样例配置文件的注释按需修改。 

文件 ` /opt/ocserv/etc/config `
    
    
    auth = "plain[/opt/ocserv/etc/passwd]"
    
    listen-host = connect.your.domain
    
    max-clients = 128
    
    max-same-clients = 4
    
    server-cert = /opt/ocserv/etc/ssl/server-cert.pem
    
    server-key = /opt/ocserv/etc/ssl/server-key.pem
    
    ca-cert = /opt/ocserv/etc/ssl/ca.pem
    
    mobile-idle-timeout = 2400
    
    ipv4-network = 192.168.1.0
    
    ipv4-netmask = 255.255.255.0
    
    dns = 8.8.8.8
    
    dns = 8.8.4.4
    
    route = 192.168.1.0/255.255.255.0
    
    route-add-cmd = "ip route add 192.168.1.0 dev tun0"
    
    route-del-cmd = "ip route delete 192.168.1.0 dev tun0"  
  
---  
  
创建用户，命令 
    
    
    /opt/ocserv/bin/ocpasswd -c /opt/ocserv/etc/passwd username  
  
---  
  
按提示输入两次密码。 

iptables 规则 
    
    
    iptables -t nat -A POSTROUTING -j SNAT --to-source <server ip> -o <nic>  
  
---  
  
记得把 ` <server ip> ` 和 ` <nic> ` 改为服务器公网 IP 和对应网卡的名称。 

###  搞定 

折腾完毕，AnyConnect 客户端可以成功使用了。 

<del> 不过呢折腾完之后发现这货其实被干扰得很厉害啊… </del>

[ Notes ](/categories/Notes/)

[ Server ](/tags/Server/) , [ Ubuntu ](/tags/Ubuntu/) , [ Linux ](/tags/Linux/) , [ Network ](/tags/Network/) , [ VPN ](/tags/VPN/) , [ iptables ](/tags/iptables/)
#### 原文：[https://blog.phoenixlzx.com/2014/07/21/setup-openconnect-server-on-ubuntu/](https://blog.phoenixlzx.com/2014/07/21/setup-openconnect-server-on-ubuntu/)