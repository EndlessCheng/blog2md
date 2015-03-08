#  Mac中创建一个SSH快捷方式

[ Yuguo ](http://yuguo.us) 2013年 01月 07日

在终端中连接SSH挺烦躁的：

    
    
    ssh -p 6851 user@servername.domain.com
    

所以我们可以创建一个快捷方式，打开终端，输入：

    
    
    nano ~/.ssh/config
    

第一次打开的话应该是一个空文件，输入以下内容：

    
    
    Host shortcutname
    HostName server.domain.com
    Port 5555
    User username
    

shortcutname就是快捷方式，HostName填域或者IP，最后是端口跟用户名。

重启终端，然后可以使用快捷命令连接服务器：

    
    
    ssh shortcutname
    

然后输入密码即可。

最后我搜索了下如何可以把密码也存在配置文件中，答案是这样会很有安全问题，如果别人侵入你的电脑，也会得到你的ssh密码，但是方法还是有的，比较麻烦。

[ http://askubuntu.com/questions/87956/can-you-set-passwords-in-ssh-config-to-
allow-automatic-login ](http://askubuntu.com/questions/87956/can-you-set-
passwords-in-ssh-config-to-allow-automatic-login)

[ 做一个框架 → ](/weblog/build-a-framework/) [ ← 那个什么都懂的家伙 ](/weblog/a-list-of-
three/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

