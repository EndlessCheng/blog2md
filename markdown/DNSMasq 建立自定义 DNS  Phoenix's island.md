[ 2014-03-11 ](/2014/03/11/setup-custom-dns-with-dnsmasq/)

#  DNSMasq 建立自定义 DNS 

一直想写的 [ 微萌DNS ](https://github.com/phoenixlzx/micromoedns) 在今天上午准备好基本架构后却在下午遇到各种各样的坑而弃掉了… 心情有够不爽。所以把自己维护的缓存DNS解决方案写出来，想要折腾类似的东西的童鞋可以试试看。 

所谓自定义DNS，这里有这么几个功能： 

  * 反DNS污染 
  * 可以直接访问部分网站 
  * 一些特定的服务加速 
  * 解决一些国外DNS被X的问题 

接下来是搭建步骤。 

###  安装基本包 

需要： ` dnsmasq ` 和 ` dnscrypt-proxy `

前者在几乎所有的发行版里都有，直接装就行了。后者需要添加第三方源。如果是 Ubuntu 的话可以添加 ` ppa:shnatsel/dnscrypt ` 仓库然后安装这个包。 

###  DNSCrypt 配置 

默认的话安装的 dnscrypt-proxy 是侦听于 ` 127.0.0.2 ` 的 ` 53 ` 端口，这里需要让 DNSMasq 来作为上游服务器所以需要修改配置。文件： ` /etc/default/dnscrypt-proxy `

修改 
    
    
    local-address=127.0.0.2:53  
  
---  
  
为 
    
    
    local-address=127.0.0.1:5301  
  
---  
  
以及默认的DNS服务器是 OpenDNS —— 和其他欧美服务一样，节点遍布欧美亚洲就那么可怜的一两个节点，甚至一个节点都没就敢叫遍布全球了呢。所以这里最好能改一下，比如选择日本的OpenNIC节点。配置文件里添加(原本是有 OpenDNS 注释的，无视即可) 
    
    
    resolver-address=106.186.17.181:2053
    
    provider-name=2.dnscrypt-cert.ns2.jp.dns.opennic.glue
    
    provider-key=8768:C3DB:F70A:FBC6:3B64:8630:8167:2FD4:EE6F:E175:ECFD:46C9:22FC:7674:A1AC:2E2A  
  
---  
  
更多可用的 DNSCrypt 服务器在 [ DNSCrypt主页 ](http://dnscrypt.org/) 可以找到。 

修改好配置文件后保存，重启 dnscrypt 服务。 

###  两个好用的配置文件 

要感谢喵菊苣的功劳，我们有两个很方便好用的配置文件来阻止一些国内ISP的DNS污染，以及部分国内站点的加速。 

配置文件地址在 [ 这里 ](https://github.com/felixonmars/dnsmasq-china-list)
    
    
    # 为了方便日后更新，把这个仓库 clone 到本地而不是直接下载。
    
    git clone https://github.com/felixonmars/dnsmasq-china-list.git
    
    cd dnsmasq-china-list
    
    # 创建到 DNSMasq 配置目录的软链接，当前该目录在 /root/dnsmasq-china-list 下。
    
    ln -s /root/dnsmasq-china-list/accelerated-domains.china.conf /etc/dnsmasq.d/
    
    ln -s /root/dnsmasq-china-list/bogus-nxdomain.china.conf /etc/dnsmasq.d/  
  
---  
  
###  一份你懂的hosts和拿来主义 

hosts 神马的最喜欢了。自从有了它，妈妈再也不用担心我上不了 Google+ ~~ 

于是这玩意到处都有，找一份你觉得靠谱的，然后保存在一个方便找的目录下。~~注意：不要放在 ` /etc/dnsmasq.d ` 下，这里文件位置在 ` /etc/dns/hosts `

实在受不了渣渣 Android 的坑爹于是换了 iPhone 之后，Apple 软件的下载速度其实不比 Android 浪费我的时间少多少。一直以来我自己写 Apple 服务加速配置，通过各种查询 Apple 在 Chinacache 的CDN IP，然后写个简单的脚本保证2000个地址能平均分配到各种线路的IP。不过后来发现这种办法开始行不通了… 于是直接拿别人的来用好了。新建文件： ` /etc/dnsmasq.d/apple.conf ` 内容只有一行： 
    
    
    server=/.apple.com/199.91.73.222  
  
---  
  
在这里要感谢 V2EX 的 DNS 啦～ 

###  调教 DNSMasq 

一切准备就绪，现在来看 DNSMasq 的配置文件—— ` /etc/dnsmasq.conf `

这里只写修改了的配置，其他的保持默认即可。 
    
    
    # 不读取 /etc/resolv.conf ，取消注释即可
    
    no-resolv
    
    no-poll
    
    # 添加上游服务器为 DNSCrypt，如果还有其他的 server= 记得取消注释。
    
    server=127.0.0.1#5301
    
    # 在所有网卡上关闭 DHCP，用不着这个功能。如果有多个网卡那么一行一个。
    
    no-dhcp-interface=eth0
    
    # 添加自定义 hosts 文件
    
    addn-hosts=/etc/dns/hosts  
  
---  
  
一共就是这些。保存配置文件并重启 dnsmasq，这样就有了一台可以给所有设备使用的、具备防污染/服务加速以及自定义地址等功能的 DNS 服务器啦～ 

[ Notes ](/categories/Notes/)

[ DNS ](/tags/DNS/) , [ Server ](/tags/Server/)
#### 原文：[https://blog.phoenixlzx.com/2014/03/11/setup-custom-dns-with-dnsmasq/](https://blog.phoenixlzx.com/2014/03/11/setup-custom-dns-with-dnsmasq/)