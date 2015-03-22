title: 关于 SSL 和 IPKVMVNC Applet 的笔记两则

date: 2014-10-13T21:03:07.000Z

tags: [SSL, NGINX, Server, Configuration, IPKVM, VNC, ]

description: 

---
虽然是没啥关系的两个东西不过最近没啥可写的所以放在一块做个笔记。 

###  COMODO SSL CA 正确的串联姿势 

有客户买了 COMODO Positive SSL 之后问我证书链变了要怎么串联。嘛确实文件变多了不过不至于这就不会了吧… 

SSL 证书串联用 ` cat ` 命令的话顺序是自下而上，也就是 自己的证书 -> 二级 Intermediate CA -> 一级 Intermediate CA -> Root CA 

所以不管文件有多少这个顺序总是有的。以 COMODO Positive SSL 为例，假设域名为 ` example.com ` ， ` cat ` 的串联命令： 
    
    
    cat example_com.crt COMODORSADomainValidationSecureServerCA.crt COMODORSAAddTrustCA.crt AddTrustExternalCARoot.crt > example_com.signed.crt  
  
---  
  
于是就可以拿着 ` example_com.signed.crt ` 和生成 CSR 时一并生成的 ` example_com.key ` 去给 NGINX 咯。 

附一份 NGINX 配置样例。 
    
    
    server {
    
          listen      80;
    
          listen      [::]:80 ipv6only=on;
    
          server_name example.com;
    
          ## redirect http to https ##
    
          rewrite        ^ https://example.com$request_uri? permanent;
    
    }
    
    server {
    
        listen 443 ssl;
    
        listen [::]:443 ssl ipv6only=on;
    
        server_name example.com;
    
        ssl                  on; 
    
        ssl_certificate      /etc/nginx/ssl/example_com.signed.crt;
    
        ssl_certificate_key  /etc/nginx/ssl/example_com.key;
    
        ssl_protocols SSLv3 TLSv1;
    
        ssl_prefer_server_ciphers   on;
    
        ssl_ciphers ALL:!aNULL:!ADH:!eNULL:!LOW:!EXP:RC4+RSA:+HIGH:+MEDIUM;
    
        keepalive_timeout    70;
    
        ssl_session_cache    shared:SSL:10m;
    
        ssl_session_timeout  10m;
    
        
    
        location / {
    
            # ...
    
        }
    
    }  
  
---  
  
最后不忘打广告： [ [ https://c.phoenixlzx.com ](https://c.phoenixlzx.com) ] 

###  === 2014-10-15 更新 === 

SSLv3 [ 再次爆出漏洞 ](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-exploiting-ssl-30.html) ，在 Google 的新草案 [ TLS_FALLBACK_SCSV ](https://tools.ietf.org/html/draft-ietf-tls-downgrade-scsv-00) 还未明朗的情况下，目前禁用 SSLv3 是一个 ** 不考虑 IE6 ** 的 workaround。 
    
    
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    
    ssl_ciphers ECDHE-RSA-AES256-SHA384:AES256-SHA256:HIGH:!RC4:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!AESGCM;
    
    ssl_prefer_server_ciphers on;
    
    ssl_session_cache shared:SSL:10m;
    
    ssl_session_timeout 10m;  
  
---  
  
###  IPKVM/VNC Applet 的使用 

从 7u45 版本之后的 Java Webstart 就不能再直接执行 Ubersmith/SolusVM/Proxmox 等等的 IPKVM/VNC Applet 了。虽然实际上是这些商业软件的错不过还是很想让人骂 Java。 

解决方案：下载一个旧版的 Java，比如 jdk6。 

但是直接安装也是不能运行的，因为实际上调用的 java executable 是最新版 Java 的，所以一样报错。 

如果是在 Linux 下，jre6 的目录在 ` $HOME/jre6/jre1.6.0_38 ` ，那么下载到 Applet 之后用下面的命令启动： 
    
    
    applet_path=/path/to/your/applet.jnlp
    
    ~/jre6/jre1.6.0_38/bin/java -verbose -Xbootclasspath/a:~/jre6/jre1.6.0_38/lib/javaws.jar:~/jre6/jre1.6.0_38/lib/deploy.jar:~/jre6/jre1.6.0_38/lib/plugin.jar -classpath ~/jre6/jre1.6.0_38/lib/deploy.jar -Djava.security.policy=file:~/jre6/jre1.6.0_38/lib/security/javaws.policy -DtrustProxy=true -Xverify:remote -Djnlpx.home=~/jre6/jre1.6.0_38/bin -Dsun.awt.warmup=true -Djnlpx.origFilenameArg=$applet_path -Djnlpx.remove=false -esa -Xnoclassgc -Djnlpx.splashport=59999 -Djnlpx.jvm=~/jre6/jre1.6.0_38/bin/java -Djnlpx.vmargs="-esa -Xnoclassgc" com.sun.javaws.Main $applet_path  
  
---
