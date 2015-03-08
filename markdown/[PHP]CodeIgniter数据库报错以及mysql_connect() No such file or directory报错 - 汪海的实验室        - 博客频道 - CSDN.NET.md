#  [ [PHP]CodeIgniter数据库报错以及mysql_connect(): No such file or directory报错 ](/pleasecallmewhy/article/details/39099093)

首先CodeIgniter连接数据库连不上，总是显示连接错误，但是又没有error信息，难以debug。 

  


解决方案是：在application/config/database.php文件的最后加上这一段代码： 
    
    
    echo '<pre>';
    print_r($db['default']);
    echo '</pre>';
    
    echo 'Trying to connect to database: ' .$db['default']['database'];
    $dbh=mysql_connect
    (
        $db['default']['hostname'],
        $db['default']['username'],
        $db['default']['password'])
    or die('Cannot connect to the database because: ' . mysql_error());
    mysql_select_db ($db['default']['database']);
    
    echo '<br />   Connected OK:'  ;
    die( 'file: ' .__FILE__ . '--> Line: ' .__LINE__);
    

  
  


  


显示报错，问题是mysql_connect(): No such file or directory报错。 

因为以前也有用过CI都没有这个错误，谷歌一下发现是因为MySQL是brew安装的，因为路径问题导致PHP无法获取相关数据。 

  


解决方案： 

如果你已经有了 /tmp/mysql.sock 但是没有  /var/mysql/mysql.sock 你应该： 

  

    
    
    cd /var 
    mkdir mysql
    cd mysql
    ln -s /tmp/mysql.sock mysql.sock

  
  


  


  


  


如果你有了 /var/mysql/mysql.sock   但是没有  mysql.sock name： 

  

    
    
    cd /tmp
    ln -s /var/mysql/mysql.sock mysql.sock

  
  


  


  


原回答地址： [ http://stackoverflow.com/questions/12584762/mysql-connect-no-such-file-or-directory ](http://stackoverflow.com/questions/12584762/mysql-connect-no-such-file-or-directory)

  


  


  


  


  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/39099093](http://blog.csdn.net/pleasecallmewhy/article/details/39099093)