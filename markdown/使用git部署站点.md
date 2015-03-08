#  使用git部署站点

[ Yuguo ](http://yuguo.us) 2012年 08月 03日

我最开始的时候迁移站点都是傻乎乎的用FTP一个文件一个文件上传，一个wordpress需要半小时，而且容易中断，后来 [ damao
](http://ooxx.me/) 告诉我用wget这个神器，就发现其实可以通过SSH在服务器端直接做一些操作，速度非常快。

最近一段时间越来越喜欢用git来管理代码，而且代码变化越来越块越来越多，现在的工作流不再合适。因为版本管理和代码部署脱节了——使用git来管理版本，更新了代
码之后，还需要其他工具来把代码同步到服务器，这就很冗余了，所以我尝试用git直接把代码push到服务器。

##  在服务器上的设置：

首先需要一个支持SSH的服务器，比如 [ miao.in ](http://miao.in/) ，在终端中输入命令：

    
    
    cd /var/www/yoursite
    git init .
    git config receive.denyCurrentBranch ignore
    git config --bool receive.denyNonFastForwards false
    cd .git/hooks
    wget http://yuguo.us/post-update
    chmod +x post-update
    

##  在本地git中配置：

在本地git仓库对应的远程仓库中指定一个“生产仓库”，比如 ` prod ` ，对应的git命令是：

    
    
    $ git remote add prod your-ssh-username@your-host:/var/www/yoursite/.git
    

这样就算配置完成了，如果要把本地git的代码推送到服务器，命令是：

    
    
    $ git push prod master
    

master对应你自己的分支的名字就好，prod的意思是product。

##  FAQ

####  http://utsl.gen.nz/git/post-update是干嘛的？

在git的 ` hooks ` 文件夹可以配置一些钩子，这些钩子在git特定操作的时候被触发， ` post-update ` 就是这样一种钩子，当 `
push ` 发生的时候，它会在远程代码仓库执行操作。所以我们用 ` wget ` 把这个 ` post-update ` 放到本地覆盖。

####  我不用`git init`，而用git clone可以吗？

没问题，但是还是要完成接下来的配置操作。

####  为啥push成功之后，代码没有生效？

远程的git已经拥有所有的版本信息，但对应的HEAD节点还没有跟当前文档对应，你可以用SSH登录远程服务器之后 ` git checkout master
` （或者你的分支），之后就无需再次 ` checkout ` 了。

####  本地的配置文件跟服务器配置文件不一样，怎么办？

善用 ` .gitignore ` 。

####  还有问题？

多多使用以下命令来检查git状态：

    
    
    git status
    git log --pretty=oneline
    git remote
    git branch
    

还有问题请google、stackoverflow……

[ 我对SASS的看法 → ](/weblog/sass/) [ ← Git的优缺点 ](/weblog/git-feature/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

