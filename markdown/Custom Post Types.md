#  Custom Post Types

[ Yuguo ](http://yuguo.us) 2011年 08月 19日

wordpress 3.0开始引入了一个新的特性叫做Custom Post Types。

在此功能出现之前我们要实现一些区别于“普通文章”的自定义文章的时候，往往需要用到Custom
Fields。用户发表任何类型的“文章”——任何类型——都需要新建一个post，然后在Custom
Fields中填入不同的名值对来进行自定义。这对用户不是很友好的一种方式。 ![](http://yuguo.us/files/2011/08
/custom-fields.png) 今天介绍的Custom Post Types会在后台边栏生成一个开发者自定义的类型，同时还有自定义挂件哦~

###  1.什么是Custom Post Types

WordPress内置的两种文章类型： ** Post ** （文章）和 ** Page ** （页面），Post一般作为经常更新的文章使用（如博客日志），
Page一般作为静态页面使用（如网站的关于和联系页面）。那么使用WordPress自定义文章类型就可以实现除Post、Page等以外的更多自定义文章类型，而
且你可以设置各不同文章类型的诸多属性。

###  2.如何在主题中增加Custom Post Types

比如我们做一个行业年会网站，需要一种Post Type叫“事件”，比如演讲或者展会就可以在事件中发布，能包含时间、地点等信息。

    
    
    add_action( ‘init’, ‘create_events’ );//让wp初始的时候调用事件create_events
    
    function create_events() {//这就是creat_events，首先定义显示labels和需要支持什么，然后在register_post_type，大功告成
    
    $labels = array(//$labels注册Custom Post Types的一些设定
    
    ‘name’ => _x(‘Events’, ‘post type general name’),//复数名字
    
    ‘singular_name’ => _x(‘Event’, ‘post type singular name’),//单数名字
    
    ‘add_new’ => _x(‘Add New’, ‘Event’),//新建条目的标签名
    
    ‘add_new_item’ => __(‘Add New Event’),//新建条目标签页的页名
    
    ‘edit_item’ => __(‘Edit Event’),//编辑条目的标签名
    
    ‘new_item’ => __(‘New Event’),
    
    ‘view_item’ => __(‘View Event’),
    
    ‘search_items’ => __(‘Search Events’),
    
    ‘not_found’ => __(‘No Events found’),
    
    ‘not_found_in_trash’ => __(‘No Events found in Trash’),
    
    ‘parent_item_colon’ => ”
    
    );
    
    $supports = array(‘title’, ‘editor’, ‘custom-fields’, ‘revisions’, ‘excerpt’);
    
    //$supports数组告诉wordpress这个文章类型可以支持什么（比如文章摘要excerpt）
    
    register_post_type( ‘event’,
    
    array(
    
    ‘labels’ => $labels,
    
    ‘public’ => true,
    
    ‘supports’ => $supports
    
    )
    
    );
    
    }

[ register_post_type
](http://codex.wordpress.org/Function_Reference/register_post_type)
来自定义文章类型的时候还能创造更多的自由选项，比如可以修改menu_position来改变这个新文章类型菜单的位置，甚至可以高于Posts哦。

###  3.增加Custom fields box

Fields在这里不是选项，而是输入区域。我们已经知道的输入区域有标题、正文、Excerpt、分类、tag等。

对于我们刚刚创建的event来说，这些输入区域是不够的。比如我们现在想在边栏加一个Custom fields box，叫link，如下图： [
](http://yuguo.us/files/2011/08/custom-fields.png) [
![](http://yuguo.us/files/2011/08/project-options.png)
](http://yuguo.us/files/2011/08/project-options.png) 代码如下（同样是加在function.php中）：

    
    
    add_action("admin_init", "portfolio_meta_box");
    
    function portfolio_meta_box(){
    
    add_meta_box("projInfo-meta", "Project Options", "event_meta_options", "event", "side", "low");
    
    }
    
    function event_meta_options(){
    
    global $post;
    
    if ( defined('DOING_AUTOSAVE') && DOING_AUTOSAVE ) return $post_id;
    
    $custom = get_post_custom($post->ID);
    
    $link = $custom["projLink"][0];
    
    ?>
    
    <label>Link:</label><input name="projLink" value="<?php echo $link; ?>" />
    
    <?php
    
    }

首先我们通过wp钩子admin_init来调用我们自己的函数portfolio_meta_box() ，这样admin创建的时候就会创建这个box。port
folio_meta_box创建这个box的一些信息，主要来源于第三个参数event_meta_options，这是一个回调函数。

event_meta_options所做的就是创建一个表单，用来保存link值。

我们首先获取全局的$post数组，这样我们就可以获得当前编辑的文章的custom
fields。下一行我们检查确保wordpress没有保存post或者custom
fields，如果已经保存了，那就直接return出去。而如果没有保存，那么首先取得当前post的custom_field，然后创建一个表单元素。

你会注意到这个新的表单元素没有提交按钮，因为它作为一个表单被插入到整个文章的form中去了，保存或者发布的时候，会自动提交。

###  4.显示自定义文章类型

显示一个event是非常重要的一个环节，因为我们创建这个event就是希望它能以与众不同的方式来显示，而不是用默认post的方式。要完成这个任务，我们会创建
一个新的模板文件。

默认使用的模板的single.php/page.php等。如果希望自定义模板，就要新建一个single-
event.php来作为event的模板。这样wordpress就会自动调用这个文件来显示单event条目。wordpress总是会先寻找single-
event.php来显示event，如果没有，就找single.php。

类似的，如果新增一个page-event.php，那么wordpress就会调用这个文件来显示event列表。

参考资料： [ http://www.shejibox.com/wordpress-custom-post-types/
](http://www.shejibox.com/wordpress-custom-post-types/) [
http://wp.tutsplus.com/tutorials/widgets/using-custom-post-types-to-create-a
-killer-portfolio/ ](http://wp.tutsplus.com/tutorials/widgets/using-custom-
post-types-to-create-a-killer-portfolio/)

[ 避免figure元素的错误用法 → ](/weblog/common-mistakes-with-the-figure-element/) [ ←
泰国游 ](/weblog/about-thailand/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

