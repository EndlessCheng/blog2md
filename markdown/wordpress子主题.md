#  wordpress子主题

[ Yuguo ](http://yuguo.us) 2010年 12月 29日

假想有如下情况：你喜欢一个别人创作的wordpress主题，它有很多自定义的功能。就像wp3.0默认的twentyten就有上传头图和背景图的功能，可以让用
户进行一些自定义的设置。在wp越来越开放，越来越多功能的今天，我们作为普通的用户已经不可能掌握那么多的动作钩子和数据过滤器（Action hook and
Filter hook）来定义后台了，所以我们就会在别人主题的基础上进行一些样式的修改或者功能的增加删除。

我们的目的是把一些更强大的主题借鉴过来，以此进行自己的修改。

而强大主题的制定者就是那些专精wp钩子的开发者，他们在一个新版本的wp出现之后迅速研究新的API并且增加新的功能，然后更新他们的主题以供用户更新下载。

问题出现了：

你修改了原始主题中的代码或者图片，但如果没有修改style.css（ _ 这个文件唯一地代表了一个主题 _ ），那么wp会认为这仍是同一个主题。那么你会在后
台看到主题有更新，你选择更新之后就会把这个主题更新到原始开发者刚发布的最新版本，而你做的所有修改全部都会丢失——你修改过的functions、在footer
添加的Analytics代码、修改的样式等。

而你如果修改了style.css，那么对于wp来说这就是另一个截然不同的主题，跟你原始主题没有任何关系，当然也就不会得知原始主题有更新，也就失去了体验新功能
的机会。

于是乎，wp推出了子主题这个概念。

##  子主题

如果你要基于一个主题来修改，那么这个主题就称为父主题，而你不应该直接修改源代码，而应该新建一个主题称之为子主题。子主题是与父主题并列的一个主题文件夹，其中的
style.css需要说明与父主题的依赖关系。

    
    
    /*
    
    Theme Name:     Twenty Ten Child
    
    Theme URI:      http: //example.com/
    
    Description:    Child theme for the Twenty Ten theme
    
    Author:         Yuguo
    
    Author URI:     http: //yuguo.us
    
    Template:       twentyten
    
    Version:        0.1.0
    
    */ 除了Theme Name和Template两个参数是必须的以外，其余均是可选。值得注意的一行是：
    
    Template:       twentyten
    

这里的twentyten是指父主题的文件夹名称，大小写敏感。

###  样式

使用子主题的时候，子主题的style.css会覆盖父主题的style.css，也就是说如果你希望继承父主题的绝大部分样式，只是进行一小部分的修改的话，就应该
如下先import父主题的style.css，用相对路径就好：

    
    
    /*
    
    Theme Name: Twenty Ten Child
    
    Description: Child theme for the Twenty Ten theme
    
    Author: Your name here
    
    Template: twentyten
    
    */
    
    @import url("../twentyten/style.css");
    
    #site-title a {
    
        color: #009900;
    
    }
    

###  模板

子主题的模板的处理上跟style.css是一样的，在子主题中任何与父主题同名的文件都会覆盖掉父主题的。比如父主题中有single.php，那么你简单地在子主
题中创建一个single.php就可以覆盖它。 在文件优先级的处理上则是跟单一主题内一致。比如tag.php是比archieve.php优先级更高的文件——
在单一主题中如果同时存在这两个文件，那么tag页就会调用前者而不是后者——所以子主题可以通过创建tag.php，来填补父主题没有单独tag.php的弊端。

###  函数

很多时候我们需要自定义函数，也就是功能和特性，在没有子主题之前我们是直接修改functions.php。现在有子主题了，我们可以在子主题中新建functio
ns.php。wp在functions.php的处理方法上跟style.css和模板是不一样的，子主题里的functions.php不会覆盖父主题的同名文件
，而是与之一起起作用，就好像一个php文件一样。

所以，如果希望增加功能，直接在子主题中新建functions.php并且输入php代码就好了。

如果希望修改父主题中已有的函数，那么根据该函数的定义方法不同或者植入主题的方法不同，有两种处理方法：

1.父主题中的函数定义是按照此种格式来定义：

    
    
    if ( ! function_exists( 'twentyten_admin_header_style' ) ) :
    
    function twentyten_admin_header_style(){
    
    //xxxxx
    
    }
    
    endif; 那么就可以直接在子主题的functions.php中声明函数：
    function twentyten_admin_header_style(){
    
    //xxxxx
    
    }
    

因为子主题的functions.php会优先引入，所以父主题就不会进入if判断。

2.父主题中的函数是通过特定钩子触发而引入主题中，那么在子主题中就应该删除这个钩子，然后定义自己的函数并绑定在特定钩子上。

    
    
    //twentyten_widgets_init是父主题调用的函数，我们首先移去它
    
    remove_action( 'widgets_init', 'twentyten_widgets_init' );
    
    //然后绑定自己的kiwi_widgets_init
    
    add_action('widgets_init','kiwi_widgets_init');
    

有些时候考虑到加载顺序，就会有稍微复杂点的代码：

    
    
    /* 去掉父主题的widget栏初始化，然后加上自己的widget初始化
    
     * 由于之后等父主题的add_action生效之后才能remove_action
    
     * 所以需要把整个动作封装在kiwi_child_theme_setup中
    
     * 然后绑定after_setup_theme动作
    
     */
    
    add_action('after_setup_theme','kiwi_child_theme_setup');
    
    function kiwi_child_theme_setup(){
    
        remove_action( 'widgets_init', 'twentyten_widgets_init' );
    
        add_action('widgets_init','kiwi_widgets_init');
    
    }
    

###  性能问题

虽然没有实测，但我觉得在内部钩子调用的过程中多多少少会耗费一些额外的时间消耗。

Any questions?

[ 挖墙脚的理论基础和解救人妻的道德讨论 → ](/weblog/wa-qiang-jiao/) [ ← 第23周周记：PC和MAC
](/weblog/week-23/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

