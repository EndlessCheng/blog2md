#  自定义wordpress翻页

[ Yuguo ](http://yuguo.us) 2011年 08月 25日

##  起因

我的博客下面有这样的翻页条，它是基于一个叫做PageNavi的插件生成的。
![](http://yuguo.us/files/2011/08/pagenav_1.png)
插件很复杂，有语言设置，还能在后台由用户设置具体条目或者显示信息。

[ ![](http://yuguo.us/files/2011/08/pagenav_2.png)
](http://yuguo.us/files/2011/08/pagenav_2.png)
虽然它很强大，但我如果想把我的博客主题开源发布出去，那么要求用户全都下载这个插件不是一个很好的选择。而且这么多自定义项并不是每个用户都需要的。
所以我决定把它整合到主题中去。步骤如下：

  1. 创建函数 
  2. 在index.php中插入调用代码 
  3. 定义样式 

##  1.创建函数

打开functions.php，创建我们的函数如下：

    
    
    function yuguo_navi() {
    
      global $wp_query, $wp_rewrite;
    
      $pages = '';
    
      $max = $wp_query->max_num_pages;
    
      if (!$current = get_query_var('paged')) $current = 1;
    
      $a['base'] = ($wp_rewrite->using_permalinks()) ? user_trailingslashit( trailingslashit( remove_query_arg( 's', get_pagenum_link( 1 ) ) ) . 'page/%#%/', 'paged' ) : @add_query_arg('paged','%#%');
    
      if( !empty($wp_query->query_vars['s']) ) $a['add_args'] = array( 's' => get_query_var( 's' ) );
    
      $a['total'] = $max;
    
      $a['current'] = $current;
    
      //请配置下面的参数，用来设置页面的pagenav
    
      $total = 0; //1 - display the text "Page N of N", 0 - not display
    
      $a['mid_size'] = 2; //how many links to show on the left and right of the current
    
      $a['end_size'] = 1; //how many links to show in the beginning and end
    
      $a['prev_text'] = '«'; //text of the "Previous page" link
    
      $a['next_text'] = '»'; //text of the "Next page" link
    
      $a['type'] = 'plain';
    
      if ($max > 1) echo '<div class="yuguo-pagenavi">';
    
      if ($total == 1 && $max > 1) $pages = '<span class="pages">Page ' . $current . ' of ' . $max . '</span>'."\r\n";
    
      echo $pages . paginate_links($a);
    
      if ($max > 1) echo '</div>';
    
    }

其中数组参数$a的一些数据是根据我自己的需求来配置的，参考自这里（ [ wordpress pagination without a plugin
](http://dimox.net/wordpress-pagination-without-a-plugin-wp-pagenavi-
alternative/) ），还有参考一个重要的函数 [ paginate_links()
](http://codex.wordpress.org/Function_Reference/paginate_links) 的官方API。

##  2.在index.php中插入调用代码

在你的index.php中（一般是index.php，除非你想单独在某个页面使用）找到翻页代码：

    
    
    <div>
    
     <div><?php next_posts_link( __( '<span>&larr;</span> Older posts', 'twentyten' ) ); ?></div>
    
     <div><?php previous_posts_link( __( 'Newer posts <span>&rarr;</span>', 'twentyten' ) ); ?></div>
    
    </div>

替换如下：

    
    
    <?php if (function_exists('yuguo_navi')) yuguo_navi(); ?>

##  3.定义样式

在style.css中加入如下代码：

    
    
    /*
    
    yuguo-pagenavi 在function里定义的导航
    
    */
    
    .yuguo-pagenavi {clear: both;text-align:center;}
    
    .yuguo-pagenavi a, .yuguo-pagenavi span {display:inline-block;*display:inline;zoom:1;text-decoration: none;text-align:center;width:60px;color:#999;font-weight:bold;border-right:1px solid #bbb;}
    
    .yuguo-pagenavi .next {border-right:0 none;}
    
    .yuguo-pagenavi a {margin-left:-4px;}
    
    .yuguo-pagenavi a:hover {color:#222;}
    
    .yuguo-pagenavi span.current {background-color:#fff;color:#222;}
    
    .yuguo-pagenavi span.current {font-weight: bold;}

OK，你的页面应该就跟我一样了。一个缺陷就是我无法通过API来控制a标签输出不带空格，而我的设计中导航间是没有间隙的，所以我只好用了-
4px的负边距来解决。不是最好的解决办法，希望哪位有更好的建议。

[ 学用代码片段 → ](/weblog/some-snippet/) [ ← 避免figure元素的错误用法 ](/weblog/common-
mistakes-with-the-figure-element/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

