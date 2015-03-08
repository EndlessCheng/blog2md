#  从wordpress迁移到Drupal

[ Yuguo ](http://yuguo.us) 2011年 01月 28日

##  从wordpress迁移到Drupal

从wordpress迁移到Drupal是一个相当直观的过程，你的内容和评论都能直接迁移过来。但更复杂的一些设置则需要更多手动操作了。本质上来说，Drupal
从wordpress站点的feed导入数据并生成node和词汇表。

下面是推荐的步骤：

  1. 建立一个Drupal站点 
  2. 根据需要配置你的站点 
  3. [ 安装 ](http://drupal.org/node/70151) 模块 [ Wordpress Import ](http://drupal.org/project/wordpress_import) 并且打开它 
  4. 根据 [ Wordpress Import ](http://drupal.org/project/wordpress_import) 模块的指引完成导入工作 

以下是需要考虑的问题：

  * 视觉上的布局、结构可能会跟以前不同，你可以考虑是否需要自定义内容类型模块（custom content types [ the CCK module ](http://drupal.org/project/cck) ）或者用默认的page类型来展示内容 
  * 你可能需要为从wordpress导入的node定义主题 
  * 从category到Drupal的分类学是一个信息从低级抽象到高级抽象的过程，所以在这一过程中不会损失信息，但可能需要一些手动的处理，你懂的 

[ Drupal模块 → ](/weblog/drupal-module/) [ ← 介绍Drupal ](/weblog/introducce-
drupal/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

