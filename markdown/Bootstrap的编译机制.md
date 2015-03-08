#  Bootstrap的编译机制

[ Yuguo ](http://yuguo.us) 2013年 01月 14日

从开源代码中总是能找到无数的智慧。

因为在构建自己的CSS框架，所以我想搞清楚的一个问题是 [ Bootstrap
](https://github.com/twitter/bootstrap) 的doc文档，也就是gh-pages分支是如何创建的。

有一个同事的观点是手写文档，文档和组件分别维护。这里的组件是指CSS、图片，以及html页。html页即单独某个组件的html，而文档页指类似 [ Base
CSS ](http://twitter.github.com/bootstrap/base-css.html)
的页面。我的观点不一样，我相信文档页应该是通过一些自动化的工具，Shell脚本来实现的，但具体还是要看看代码。项目应该使用大量的开源工具开源，就像 [
Linux哲学 ](http://yuguo.us/weblog/linux-philosophy/) 中说到的：“ _
把不同的程序链接在一起完成复杂任务。 _ ”

我研究了下Bootstrap的编译机制，在说明中有写到：

> 我们有一个makefile文件，以方便开发Bootstrap库。

>

> _ dependencies _ ： 我们的makefile依赖这几个库： recess, connect, uglify.js, 和 jshint
。要安装，只需要运行以下命令:

>  
>  
>     $ npm install recess connect uglify-js jshint -g

>  
>

> _ build _ \- ` make ` 命令会运行recess编译器来把/less文件编译成css文件，然后生成docs页面。
需要recess和uglify.js。

>

> _ test _ \- ` make test ` 命令会运行jslint和qunit。

>

> _ watch _ \- ` make watch `
命令会启动watch来监视Less文件的变动，然后自动的编译成css。需要Watchr（是一个Ruby程序）。

##  关于Makefile

GNU make是一个方便的工具，目的是把大量的shell 命令组合起来完成一个任务。这些命令之所以能组合起来，跟Linux哲学是息息相关的：

> 程序要能协作。程序要能处理文本流，因为这是最通用的接口。

举个例子，在 [ makefile ](https://github.com/twitter/bootstrap/blob/master/Makefile)
的74-78行：

    
    
    # 把前面这么多所有的js的源码都拷贝到bootstrap/js/bootstrap.js中去
    cat js/bootstrap-transition.js js/bootstrap-alert.js js/bootstrap-button.js js/bootstrap-carousel.js js/bootstrap-collapse.js js/bootstrap-dropdown.js js/bootstrap-modal.js js/bootstrap-tooltip.js js/bootstrap-popover.js js/bootstrap-scrollspy.js js/bootstrap-tab.js js/bootstrap-typeahead.js js/bootstrap-affix.js > bootstrap/js/bootstrap.js
    # 通过开源的uglifyjs压缩混淆，保存到一个临时文件bootstrap.min.tmp.js中去
    uglifyjs bootstrap/js/bootstrap.js -nc > bootstrap/js/bootstrap.min.tmp.js
    # 创建一个临时的copyright.js作为版权
    echo "/*!\n* Bootstrap.js by @fat & @mdo\n* Copyright 2012 Twitter, Inc.\n* http://www.apache.org/licenses/LICENSE-2.0.txt\n*/" > bootstrap/js/copyright.js
    # 把版权放在压缩文件的头部
    cat bootstrap/js/copyright.js bootstrap/js/bootstrap.min.tmp.js > bootstrap/js/bootstrap.min.js
    # 把临时文件干掉
    rm bootstrap/js/copyright.js bootstrap/js/bootstrap.min.tmp.js
    

关于makefile依赖

make是Unix下的历史最悠久的一个程序，它能很好地解决任务之间的依赖问题。

还是以 [ Bootstrap makefile
](https://github.com/twitter/bootstrap/blob/master/Makefile) 为例。第84行：

    
    
    gh-pages: bootstrap docs
    	rm -f docs/assets/bootstrap.zip
    	zip -r docs/assets/bootstrap.zip bootstrap
    	rm -r bootstrap
    	rm -f ../bootstrap-gh-pages/assets/bootstrap.zip
    	node docs/build production
    	cp -r docs/* ../bootstrap-gh-pages
    

  * gh-pages是工作目标； 
  * bootstrap docs是必要条件； 
  * 以后的6行是命令 

代码的意思是说，目标是gh-
pages，需要的依赖是bootstrap和docs，即在创建目标之前，一定要存在的文件，那么make会先完成bootstrap和docs文件。

最后补充一下，对于Linux来说，文件夹也是文件。

##  基本Shell命令

Shell命令，或者SSH命令，常用的可以参考大猫这篇文章 [ SSH 入门教程(常用命令) ](http://ooxx.me/common-ssh-
commands.orz)

但是那篇文章没有说明的一个是关于输入和输出，比如

    
    
    echo 'hello world!'
    

会把hello world!输出到屏幕命令行中，但如果用

    
    
    echo 'hello world!' > hello.txt
    

那么就不会显示在命令行中，而是输出到hello.txt中，因为Linux哲学就是一切皆文件，显示器这样的硬件也是文件，硬盘里的文件也是文件，只有输入和输出的
概念，而不关心命令和文件从哪里来，到哪里去。

##  关于nodejs

Nodejs社区有大量工具来方便我们的工作，在bootstrap中它主要起到了编译doc（也就是gh-pages分支）的作用。

    
    
    node docs/build production
    

这时候node会去找 [ docs/build
](https://github.com/twitter/bootstrap/tree/master/docs/build) 文件夹下的 [
index.js
](https://github.com/twitter/bootstrap/blob/master/docs/build/index.js)
，参数为“production”。

nodejs的理念跟make是很像的。npm（Node Package Manager）是管理nodejs包的公共平台。对于服务器，只要服务器能连接外网，就
可以通过SSH来安装nodejs程序；对于Linux或者Mac本机，就更方便了。

上面的例子中提到的uglifyjs就是Bootstrap的编译所依赖的一个js压缩库，通过NPM安装非常简单：

    
    
    npm install uglify-js@1
    

` @1 ` 是让npm下载版本1的意思。

##  关于node.js依赖

很多时候，我们的nodejs程序需要调用第三方的nodejs代码，这时候需要声明并且引用这些代码进来。

声明依赖，在 [ package.json
](https://github.com/twitter/bootstrap/blob/master/docs/build/package.json) 中：

    
    
    {
      "name": "bootstrap-doc-builder"
    , "version": "0.0.1"
    , "description": "build bootstrap docs"
    , "dependencies": { "hogan.js": "1.0.5-dev" }
    }
    

就是说我们的nodejs需要hogan.js。

然后在index.js中：

    
    
    var hogan = require('hogan.js')
      , fs    = require('fs')
      , prod  = process.argv[2] == 'production'
      , title = 'Bootstrap'
    

这时候 ` hogan ` 就是一个可以直接使用的对象了。

##  关于watch

如果觉得每次修改了一份代码都要重新编译十分麻烦，可以用 [ watchr ](https://github.com/mynyml/watchr)
来侦测文件修改，如果有修改则自动编译。它可以监视文档变动，然后自动执行响应的工作。

Watchr是一个用Ruby编写的工具，如果安装了RubyGems，那安只需要

    
    
    sudo gem install watchr
    

就可以安装成功。

安装成功之后使用Shell命令运行：

    
    
    make watch
    

就会自动执行这样一句简单的命令：

    
    
    watch:
    	echo "Watching less files..."; \
    	watchr -e "watch('less/.*\.less') { system 'make' }"
    

##  尾声

Linux/Mac开发环境是web开发者的好朋友，安装好nodejs、rubyGem之后，熟悉makefile、shell命令，然后就多多了解、调用第三方库
，来共同完成自己的需求。

[ 听Nico讲故事 → ](/weblog/nico-story/) [ ← Clash of Clans ](/weblog/clash-of-
clans/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

