#  [ [PHP]如何在SAE的CodeIgniter项目中隐藏掉index.php ](/pleasecallmewhy/article/details/25257515)

第一步：修改项目根目录的config.yaml文件，添加如下内容： 
    
    
    handle:
    	- rewrite: if(!is_dir() && !is_file() && path~"/") goto "/index.php/%{QUERY_STRING}"

  
第二步：将application/config/config.php中的$config['index_page']设置为''： 
    
    
    $config['index_page'] = '';
    

  
OK，搞定。    

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/25257515](http://blog.csdn.net/pleasecallmewhy/article/details/25257515)