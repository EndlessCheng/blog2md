title: 使用 iptables 过滤 DNS 放大攻击

date: 2014-05-23 20:52:59

tags: [iptables, DNS, Network, ]

description: 

---
昨晚开始我们的 DNS 日志中出现大量的针对`wradish.com`的`ANY`记录请求，导致大量正常解析请求超时。今天上午到中午时分再次出现流量更大、针对`ping.zong.co.ua`的`ANY`记录请求，导致整个 DNS 服务瘫痪，完全无法响应正常解析请求。

检查后发现 `wradish.com` 早已因多次 DNS 放大攻击而被列入开放 DNS 服务器黑名单，网络上也有大量的针对该域名攻击请求包的过滤方法。`ping.zong.co.ua` 却完全没有任何搜索记录。

DNS 放大攻击 (DNS Amplification Attack) 即通过向多台 DNS 开放服务器发送无意义的 recursive 解析请求，从而使得根域名服务器遭到超大流量的解析请求包，无暇顾及正常的解析请求，由此实现分布式拒绝服务攻击 (Distributed Denial of Service)。我们的 DNS 服务器在这里既是攻击者，也是受害者。

DNSMasq 默认允许 recursive 请求，且似乎本身就没有设计为开放 DNS 服务，所以貌似也没有办法禁用掉 recursive 请求。因此我们使用 [iptables 规则](http://blog.dataforce.org.uk/2013/08/limiting-the-effectiveness-of-dns-amplification/)来过滤掉这些请求。
    
    
    # Create a chain to store block rules in
    
    iptables -N BADDNS 
    
    # Match all "IN ANY" DNS Queries, and run them past the BADDNS chain.
    
    iptables -A INPUT -p udp --dport 53 -m string --hex-string "|00 00 ff 00 01|" --to 255 --algo bm -m comment --comment "IN ANY?" -j BADDNS
    
    iptables -A FORWARD -p udp --dport 53 -m string --hex-string "|00 00 ff 00 01|" --to 255 --algo bm -m comment --comment "IN ANY?" -j BADDNS
    
    # Block domains that are being used for DNS Amplification...
    
    iptables -A BADDNS -m string --hex-string "|04 72 69 70 65 03 6e 65 74 00|" --algo bm -j DROP --to 255 -m comment --comment "ripe.net"
    
    iptables -A BADDNS -m string --hex-string "|03 69 73 63 03 6f 72 67 00|" --algo bm -j DROP --to 255 -m comment --comment "isc.org"
    
    iptables -A BADDNS -m string --hex-string "|04 73 65 6d 61 02 63 7a 00|" --algo bm -j DROP --to 255 -m comment --comment "sema.cz"
    
    iptables -A BADDNS -m string --hex-string "|09 68 69 7a 62 75 6c 6c 61 68 02 6d 65 00|" --algo bm -j DROP --to 255 -m comment --comment "hizbullah.me"
    
    # Rate limit the rest.
    
    iptables -A BADDNS -m recent --set --name DNSQF --rsource
    
    iptables -A BADDNS -m recent --update --seconds 10 --hitcount 1 --name DNSQF --rsource -j DROP  
  
---  
  
添加以上规则后执行 `iptables-save` 来使更改生效。

目前为止似乎没有报告出现了明显规模的 DNS 放大攻击征兆，攻击者针对我们防火墙封锁的反应速度、攻击所用的记录以及从日志中发现的大量不同请求源也暗示着我们的服务器可能是最终攻击目标，用攻击流量消耗尽服务器带宽而导致服务瘫痪。至于原因，我也没有想明白为何会有攻击者对一个小型私用服务器感兴趣。

PS. 到本文发表时，攻击依旧在继续，且流量越来越大。目前阿里云的云盾设置可以说无力，只能依靠 iptables 暂时缓解。后续的应对计划仍在制定中。

=== 2014-05-24 更新 ===

Aveline 菊苣给出了一个[DNS Amplification IPTABLES block lists](https://github.com/smurfmonitor/dns-iptables-rules) 给点128个赞！
