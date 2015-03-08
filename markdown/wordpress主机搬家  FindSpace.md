#  wordpress主机搬家 

[ Find ](http://www.findspace.name/author/find) |  2015年1月13日  |  [ 其他 ](http://www.findspace.name/category/res/other) , [ 资源 ](http://www.findspace.name/category/res) |  [ 3条评论  ](http://www.findspace.name/res/1023#comments)

  * wordpress主机搬家 
    * 备份 
      *         * 备份文件 
        * 备份数据库 
    * 转移 
    * WP-SuperCache插件 
    * PS 

今天域名备案终于通过了，主机也就搬到了国内，这里简单说下搬家（域名不换，只换主机）过程和遇到的问题。 

* * *

##  备份 

####  备份文件 

首先用filezilla（一个FTP管理工具）从原主机把文件都下载下来，注意并不一定是全都下载，下载的文件夹是打开之后便是wordpress的那个文件夹，比如有些是domains/yourdomains有的是wwwroot，视情况而定。 

或者使用多备份定时备份的文件也可以。 

_ 如果你使用了wp supercache插件，请参看后面的说明 _

####  备份数据库 

: 可以利用多种途径备份：     

  * 直接从网站后台通过phpmyadmin导出 
  * 利用网站控制面板提供的备份功能 
  * 利用多备份的自动备份功能 

##  转移 

修改根目录下的wp-config.php文件把 
    
    
    define('DB_NAME', 'yourname');
    /** MySQL database username */
    define('DB_USER', 'user');
    /** MySQL database password */
    define('DB_PASSWORD', 'passwd');

这一段代码的配置和你新主机的配置同步起来。 

把备份的文件上传到新的主机空间，注意上传内容到目标文件夹。 

从新主机的后台控制面板（不是wordpress的，现在应该打开是有数据库错误的）导入备份的sql文件。 

##  WP-SuperCache插件 

如果在之前启用了这个插件，以上步骤之后主页一般会提示有错误，搬家过程需要做如下修改： 

  * 修改wp-config.php 
    
    
    define( 'WPCACHEHOME', '/home/example/wwwroot/wp-content/plugins/wp-super-cache/' ); //Added by WP-Cache Manager
    define('WP_CACHE', true); //Added by WP-Cache Manager

这两个声明应该是在最开头，删掉他们。 

  * 在wordpress后台删除wordpress插件，然后重新安装一次，当然上面这两个定义会重新加进去，但是路径会改变。 

##  PS 

[ 多备份的注册 ](http://www.dbfen.com/index.php/users/newuser_by/4DBDAFA6)

主机搬到了国内的西部数据，而且域名也注册了，正常情况下，应该再也不会宕机了～ 

买主机的时候，西部数据赠送了100元的优惠券，有效期到2015.12.31，适用的机型是： 

> b032,b064,tw003,B075,java005,ghostC,M005,B075,B071 

当然肯定不允许转赠，有需要的小伙伴可以联系我，替你买。 

Tags:  [ wordpress ](http://www.findspace.name/tag/wordpress) , [ 网络资源 ](http://www.findspace.name/tag/websource)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/res/1023](http://www.findspace.name/res/1023)