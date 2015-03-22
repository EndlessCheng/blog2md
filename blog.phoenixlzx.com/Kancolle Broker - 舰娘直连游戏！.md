title: Kancolle Broker - 舰娘直连游戏！

date: 2015-02-08T06:55:16.000Z

tags: [Node.js, Anime, ]

description: 

---
废话：啊……我终于治好了自己的拖延症。 

事情的起因，无非就是 2015 年的第一场大戏——舰娘国服。嘛。不多评论，大家心里都明白。之后用 nginx + SNI Proxy 配置了一个代理服务器方便大家在日本地区外玩舰娘。但是这种代理服务有一个很大的问题就是会引起恶意攻击，被用作 DDoS 攻击的肉鸡使用，因此日本法律也是禁止 VPN 服务器的。 

这个 idea 出现的时候还在帝都，房间里没开空调没有暖气，4M带宽20人用还有人开迅雷，无奈只好烧朋友送的 4G 流量卡来维持网络需求。完全没有力气做事情的时候偏偏看到 DMM 那个变态到极点的登录验证…… 

于是一直拖到回家之后碰上一大堆喵窝的活动… bangumi.moe 那边也在一直催着干活，直到今天我才 <del> 良心发现 </del> 用力让自己头脑清醒一点，认真分析了下 DMM 的登录验证。 

整个过程大概是这样：客户端请求登录页面，页面中包含两个 token，加载完毕后一个 token 作为 header 数据，一个作为 XHR POST 请求数据发送给服务器，获得另外两个 token。这两个 token 将作为用户登录 email 和 password 的 key。用户登录时 post 给服务器的数据大概是下面这样： 
    
    
    {
    
        "token": "11dde99d39af2287fc6eed02632ccbee",
    
        "login_id": "user@example.com",
    
        "save_login_id": 0,
    
        "password": "P@ssw0rd",
    
        "use_auto_login": 0,
    
        "dfdfa8466f24710893d99529acaaeef0": "user@example.com",
    
        "2760cb37702b03d10d92caf9daaaf675": "P@ssw0rd"
    
    }  
  
---  
  
… 好了，看晕了吧。咱就不吐槽日本人脑子里到底在想啥了。总之来看代码 -> [ Github ](https://github.com/phoenixlzx/kancolle-broker)

原理就是登录后用 cookie 拿到游戏 link 的 apptoken，而这个游戏的 link 是不会验证日本 IP 的。 

想测试效果的话，那么先关闭本地的各种舰娘代理，移除所有相关的 hosts，然后访问 [ 这里 ](https://kancolle.phoenixlzx.com) 。使用 DMM 帐号登录，成功的话会跳到舰娘的游戏页面。适用于所有在日本境外没有日本代理的情况下使用。 

问：会不会有安全问题？ 

必须的。而且比 SNI 代理更不安全。但是反过来说，也是比 SNI 更安全的。因为 DMM 登录发送密码完全没有加密，只是靠 HTTPS。所以用这个程序的话： 

  1. 密码都是可以在服务端记录的。虽然程序里完全没有记录密码相关的代码，但是要加也不是难事。 
  2. 没有 HTTPS 的情况下，你发送的所有数据都是明文的。所以我做的这个 demo 用了 HTTPS 加密链接。 

所以如果是有 HTTPS 加密且 deploy 这个程序的人比较靠谱的话，安全性还是有保障的。 

至于大家是不是相信我……嗯这个看各位如何考量啦。 

最后：我真的没玩过舰娘，我也不会去玩。 
