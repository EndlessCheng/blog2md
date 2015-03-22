title: 如何搭建免费静态博客——Hexo 与 GitHub 使用小记

date: 2014-06-21T13:30:00.000Z

tags: [Hexo, GitHub, Jacman, ]

description: 参考了下别人的经验，无需配置 SSH 等麻烦操作。

---
##  缘起 

把网页托管在 GitHub 上有什么好处呢？——秒开。（吐槽下某些空间服务商的速度。。）   
其次，可能你会遇到修改了某些文字之后又想改回去的情况，这时 Github 上保存的历史记录就会帮到你了。 

##  快速搭建 

1.首先参见最简单的搭建教程： [ Github+Hexo搭建静态Blog小结 ](http://wsgzao.github.io/post/hexo-guide/)

** 注意，若生成文章之后首页文章显示异常（如出现空白文章或重复文章等），请先 ` hexo clean ` 之后再 ` hexo g ` **

2.然后修改成 Jacman 主题（或者你喜欢的其他主题）：在根目录下右键选择 Git Bash 输入 
    
    
    git clone https://github.com/wuchong/jacman.git themes/jacman  
  
---  
  
3.修改 ` ./_config.yml ` 配置文件中的 ` theme ` 属性，将其设置为 ` jacman ` 。然后在 ` deploy ` 前面加入 
    
    
    stylus:
    
       compress: true  
  
---  
  
4.在 ` ./source ` 文件夹中建立 ` tags ` 、 ` categories ` 和 ` about ` 文件夹，各文件夹内部新建一个 ` index.md ` 文件。内容分别为： 
    
    
    layout: tags
    
    title: tags
    
    ---  
  
---  
      
    
    layout: categories
    
    title: categories
    
    ---  
  
---  
      
    
    title: 关于我
    
    ---
    
    <自我介绍>  
  
---  
  
如果你想让你的 tags 有标签云的效果，把 ` ./themes/<你的主题>/_config.yml中widgets ` 下的 ` tag ` 修改成 ` tagcloud `

5.完成上述步骤后在 sync 时可能会遇到 ` fancybox ` 文件夹内部的文件无法同步的问题，这时需要在 ` ./fancybox ` 下右键打开 Git Bash，输入以下内容即可： 
    
    
    git add .
    
    git commit -m "update fancybox"  
  
---  
  
6.添加 Disqus（多说明明有回复评论后邮箱提醒却不给我发邮件，差评）：点击 [ https://disqus.com/ ](https://disqus.com/) 添加站点，填完，记住 ` shortname ` 中填的名字，无视掉验证。然后打开 ` ./themes/<你的主题>/_config.yml ` ，找到 ` disqus_shortname ` ，修改如下： 
    
    
    disqus_shortname: <你填的名字>  
  
---  
  
7.添加 RSS：在根目录下运行 Git Bash，输入 
    
    
    npm install hexo-generator-feed  
  
---  
  
然后编辑 ` ./_config.yml ` ，添加如下代码： 
    
    
    plugins:
    
    - hexo-generator-feed  
  
---  
  
之后确认在 ` ./themes/<你的主题>/_config.yml ` 中有 ` rss: /atom.xml ` 这一行（Jacman 主题自带） 

8.写新文章时，建议在 ` \--- ` 上方添加 ` description: <文章纲要> `

9.添加 [ 百度统计 ](http://tongji.baidu.com/web/welcome/login) ：有两种方法, 一种是默认加载, 一种是异步加载。   
默认加载这种方式只需将代码添加至网站全部页面的 ` <body> ` 标签 ** 前 ** , 因此只需要在 ` ./themes/<你的主题>/layout/_partial/after_footer.ejs ` 里添加如下代码（这里添加的是我的代码, 请适当修改） 
    
    
    <script type="text/javascript">
    
    var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
    
    document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3Fcfedc723a9dc30bd7db67ad8e53a97fa' type='text/javascript'%3E%3C/script%3E"));
    
    </script>  
  
---  
  
百度统计异步代码是以异步加载形式加载了网站分析代码，使用该代码能够大幅提升您网站的打开速度(目前使用百度统计异步代码会导致百度统计图标和代码检查功能的失效).使用这种方式需要将代码添加至网站全部页面的标签前, 因此只需要在 ` ./themes/<你的主题>/layout/_partial/head.ejs ` 里添加如下代码（这里添加的是我的代码, 请适当修改） 
    
    
    <script>
    
    var _hmt = _hmt || [];
    
    (function() {
    
      var hm = document.createElement("script");
    
      hm.src = "//hm.baidu.com/hm.js?efd32d79f8a09abef26865f3b17a3fc7";
    
      var s = document.getElementsByTagName("script")[0]; 
    
      s.parentNode.insertBefore(hm, s);
    
    })();
    
    </script>  
  
---  
  
10.添加 sitemap：在根目录下运行 Git Bash，输入 
    
    
    npm install hexo-generator-sitemap  
  
---  
  
然后编辑 ` ./_config.yml ` ，添加如下代码： 
    
    
    plugins:
    
    - hexo-generator-sitemap  
  
---  
  
随后提交给 Google 网站站长工具即可。 
