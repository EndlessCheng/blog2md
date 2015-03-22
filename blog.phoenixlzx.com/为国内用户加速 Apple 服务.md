title: 为国内用户加速 Apple 服务

date: 2014-05-15T13:57:19.000Z

tags: [Configuration, ]

description: 

---
偶然看到 [ 雅诗的po ](https://plus.google.com/105938465531761409080/posts/3EXLAUerxMD) 才发觉自己 DNS 的 Apple 服务加速已经几乎不能用了，速度非常慢。倒是挺奇怪的，因为自己做的 DNS 服务器对于整个 Apple 域的上游都是 V2EX DNS，难道是 V2EX DNS 出问题了？ 

总之先不管那些。现在来简单做一份 Apple 服务加速的配置。 

稍微 Google 下 Apple 的服务地址，目前获得的地址如下： 
    
    
    a{1-2000}.phobos.apple.com
    
    swdist.apple.com
    
    itunes.apple.com
    
    contentdelivery.itunes.apple.com  
  
---  
  
对应在国内的 CDN 地址是 
    
    
    a1-a200.phobos.apple.chinacache.net
    
    swdist.apple.ccgslb.net
    
    itunes.apple.ccgslb.com.cn
    
    (最后一个没找到CDN地址..)  
  
---  
  
然后根据 114DNS 和 Google DNS 综合查询以上地址的 IP。顺便发现地址里有 ` cnc ` , ` cncssr ` 这样的关键字，于是正好尝试把 ` cnc ` 改成 ` tel ` 于是得到了电信节点的 IP。 

现在写一个两句话的 js 脚本来生成一份针对 ` a{1-2000}.phobos.apple.com ` 的加速列表(废话这种东西能手写吗要累死啦)，以达到尽可能将电信、联通的节点混在一起，保证各个 ISP 用户的下载速度。 
    
    
    // Accelerate IPs for Apple download service.
    
    // apple-ips.js
    
    var ips = [
    
      '221.192.144.12',
    
      '182.118.46.137',
    
      '124.95.150.148',
    
      '123.235.32.2',
    
      '119.84.69.17',
    
      '122.228.85.196',
    
      '115.231.150.15',
    
      '61.164.153.7',
    
      '183.57.28.18'
    
    ]
    
    for (var i = 1; i <= 2000; i++) {
    
      console.log(ips[Math.floor(Math.random()*ips.length)] + ' a' + i + '.phobos.apple.com');
    
    }  
  
---  
  
然后 
    
    
    ~> node apple-ips.js > apple.conf  
  
---  
  
就得到一份可以直接用的加速列表啦。 
