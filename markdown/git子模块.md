#  git子模块

[ Yuguo ](http://yuguo.us) 2013年 01月 28日

经常有这样的事情，当你在一个项目上工作时， _ 你需要在其中使用另外一个项目 _ 。也许它是一个第三方开发的库或者是你独立开发和并在多个父项目中使用的。这个
场景下一个常见的问题产生了：你想将两个项目单独处理但是又需要在其中一个中使用另外一个。

这里有一个例子。我在做http://font.isux.us的时候，需要用到第三方地字体，还有可能其他人维护的会更新的字体。这些字体属于单独的库，如果我只是
简单地把代码拷贝到自己的项目，带来的问题是，当上游被修改时，任何你进行的定制化的修改都很难归并。

Git 通过子模块处理这个问题。子模块允许你将一个 Git仓库当作另外一个Git仓库的子目录。这允许你克隆另外一个仓库到你的项目中并且保持你的提交相对独立。

##  子模块相关操作：

** 添加子模块 ** ： ` $ git submodule add [url] [path] `

如：

    
    
    $ git submodule add git://github.com/soberh/ui-libs.git src/main/webapp/ui-libs
    

新增之后，查看了当前的状态发现添加了一个新文件( ` .gitmodules ` )和一个文件夹( ` src/main/webapp/ui-libs `
；那么新增的 ` .gitmodules ` 文件是做什么用的呢？ ` .gitmodules `
记录了每个submodule的引用信息，知道在当前项目的位置以及仓库的所在。

** 查看子模块 ** ： ` $ git submodule ` —-查看当前项目用到的子模块 

![image](http://yuguo.us/files/2013/01/submodule.png)

可以看到图中子模块前面有一个 ` \- ` ，说明子模块文件还未检入（空文件夹）

** 初始化子模块 ** ： ` $ git submodule init ` —-只在首次检出仓库时运行一次就行 

![image](http://yuguo.us/files/2013/01/submodule-init.png)

** 更新子模块 ** ： ` $ git submodule update ` —-每次更新或切换分支后都需要运行一下 

![image](http://yuguo.us/files/2013/01/submodule-update.png)

现在子模块文件夹是检入OK的状态了。

** 删除子模块 ** ：（这一步比较麻烦，只是简单rm的话，可能会出现难以定位的bug） 

  1. ` $ git rm --cached [path] `
  2. 编辑 ` .gitmodules ` 文件，将子模块的相关配置节点删除掉 
  3. 编辑 ` .git/config ` 文件，将子模块的相关配置节点删除掉[这一步好像很不科学，为什么信息要保存两份？] 
  4. 手动删除子模块残留的目录 

[ 关于favicon的思考 → ](/weblog/favicon/) [ ← 残忍的COC哲学 ](/weblog/coc-and-life/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

