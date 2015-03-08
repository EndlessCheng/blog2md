[ Home ](http://blog.cee.moe) [ Subscribe ](http://blog.cee.moe/rss/)

#  Cisco IPSec VPN 配置小记

09 April 2014

咳咳。部署团委的 [ 创青春网站 ](http://www.njucqc.com) (Under Construction 2333)，顺便弄了一下
Cisco 的 VPN。

比想像中容易配置，主要参考了 [ MartianZ 菊苣 ](https://plus.google.com/+MartianZ) 的 [ blog
](http://blog.martianz.cn/article/2014-02-14-centos-cisco-ipsec) 和 [ 另一篇博文
](http://blog.wellsgz.info/?p=1964) 。

* * *

1.安装 IPSec-Tools Racoon

    
    
    # apt-get install ipsec-tools
    # apt-get install racoon
    

2.配置 IPSec-tools Racoon

######  /etc/racoon/racoon.conf

    
    
    path pre_shared_key "/etc/racoon/psk.txt";
    path certificate "/etc/racoon/certs";
    
    listen {
        isakmp YOUR.IP.ADDRESS [500];
        isakmp_natt YOUR.IP.ADDRESS [4500];
        #上两行 YOUR.IP.ADDRESS 改为 VPS 的外网地址
    }
    
    remote anonymous {
        exchange_mode aggressive, main, base;
        mode_cfg on;
        proposal_check obey;
        nat_traversal on;
        generate_policy unique;
        ike_frag on;
        passive on;
        dpd_delay 30;
    
        proposal {
               lifetime time 28800 sec;
               encryption_algorithm 3des;
            hash_algorithm md5;
            authentication_method xauth_psk_server;
            dh_group 2;
        }
    }
    
    sainfo anonymous {
        encryption_algorithm aes, 3des, blowfish;
        authentication_algorithm hmac_sha1, hmac_md5;
        compression_algorithm deflate;
    }
    
    mode_cfg {
        auth_source system;
        dns4 8.8.8.8;
        banner "/etc/racoon/motd";
        save_passwd on;
        network4 10.1.1.100;#客户端获得的 IP 起始地址
        netmask4 255.255.255.0;#客户端获得的地址的掩码
        pool_size 100;#最大客户端数量
        pfs_group 2;
    }
    

######  /etc/racoon/psk.txt

    
    
    YOUR.GROUP.NAME YOUR.GROUP.SECRET 
    #前面是 Group Name，或者 vpnc 里配置的 IPSec ID
    #后面是 Secret，或者 vpnc 里的 IPSec secret
    

######  /etc/racoon/motd

    
    
    Fuck GFW!
    #欢迎信息，貌似一定要填写？
    

3.添加用户名和密码

    
    
    # useradd -MN -b /tmp -s /sbin/nologin YOUR.USERNAME 
    # passwd YOUR.USERNAME
    

4.设置 iptables 的规则和 IPv4 forward

    
    
    # iptables -A INPUT -p udp --dport 500 -j ACCEPT
    # iptables -A INPUT -p udp --dport 4500 -j ACCEPT
    # iptables -t nat -A POSTROUTING -s 10.1.1.0/24 -o eth0 -j MASQUERADE
    # iptables -A FORWARD -s 10.1.1.0/24 -j ACCEPT
    # iptables-save
    

######  /etc/sysctl.conf

    
    
    net.ipv4.ip_forward = 1
    sysctl -p
    

5.最后启动><

    
    
    # service racoon start
    # chkconfig racoon on
    

[ Cee's Picture  ](/author/cee/)

####  [ Cee ](/author/cee/)

Read [ more posts ](/author/cee/) by this author.

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

####  Share this post

[ Twitter  ](https://twitter.com/share?text=Cisco%20IPSec%20VPN%20%E9%85%8D%E7
%BD%AE%E5%B0%8F%E8%AE%B0&url=http://blog.cee.moe/cisco-ipsec-vpn/) [ Facebook
](https://www.facebook.com/sharer/sharer.php?u=http://blog.cee.moe/cisco-
ipsec-vpn/) [ Google+  ](https://plus.google.com/share?url=http://blog.cee.moe
/cisco-ipsec-vpn/) [ Cee's Home ](http://blog.cee.moe) © 2015  Proudly
published with [ Ghost ](https://ghost.org)

