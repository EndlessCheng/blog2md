#  [ [PHP]移动端网页如何使用JqueryMobile+PHP实现上传图片的功能 ](/pleasecallmewhy/article/details/18147507)

[ 图片 ](http://www.csdn.net/tag/%e5%9b%be%e7%89%87) [ php ](http://www.csdn.net/tag/php) [ 移动设备 ](http://www.csdn.net/tag/%e7%a7%bb%e5%8a%a8%e8%ae%be%e5%a4%87) [ jQueryMobile ](http://www.csdn.net/tag/jQueryMobile) [ JQM ](http://www.csdn.net/tag/JQM)

首先，实现上传功能。上传功能是利用PHP实现的： 

##  创建一个文件上传表单 
    
    
    <html>
    <body>
    
    <form action="upload_file.php" method="post"
    enctype="multipart/form-data">
    <label for="file">Filename:</label>
    <input type="file" name="file" id="file" /> 
    <br />
    <input type="submit" name="submit" value="Submit" />
    </form>
    
    </body>
    </html>

其中，<form> 标签的 enctype 属性规定了在提交表单时要使用哪种内容类型。在表单需要二进制数据时，比如文件内容，请使用 "multipart/form-data"。 

<input> 标签的 type="file" 属性规定了应该把输入作为文件来处理。当在浏览器中预览时，会看到输入框旁边有一个浏览按钮。 

  


  


  


##  创建上传脚本 

"upload_file.php" 文件含有供上传文件的代码： 
    
    
    <?php
    if ($_FILES["file"]["error"] > 0)
      {
      echo "Error: " . $_FILES["file"]["error"] . "<br />";
      }
    else
      {
      echo "Upload: " . $_FILES["file"]["name"] . "<br />";
      echo "Type: " . $_FILES["file"]["type"] . "<br />";
      echo "Size: " . ($_FILES["file"]["size"] / 1024) . " Kb<br />";
      echo "Stored in: " . $_FILES["file"]["tmp_name"];
      }
    ?>

  
  


通过使用 PHP 的全局数组 $_FILES，你可以从客户计算机向远程服务器上传文件。 

第一个参数是表单的 input name，第二个下标可以是 "name", "type", "size", "tmp_name" 或 "error"。就像这样： 

  * $_FILES["file"]["name"] - 被上传文件的名称 
  * $_FILES["file"]["type"] - 被上传文件的类型 
  * $_FILES["file"]["size"] - 被上传文件的大小，以字节计 
  * $_FILES["file"]["tmp_name"] - 存储在服务器的文件的临时副本的名称 
  * $_FILES["file"]["error"] - 由文件上传导致的错误代码 

  


  


##  上传限制 

在这个脚本中，增加对文件上传的限制。用户只能上传 .gif 或 .jpeg 文件，文件大小必须小于 20 kb： 
    
    
    <?php
    
    if ((($_FILES["file"]["type"] == "image/gif")
    || ($_FILES["file"]["type"] == "image/jpeg")
    || ($_FILES["file"]["type"] == "image/pjpeg"))
    && ($_FILES["file"]["size"] < 20000))
      {
      if ($_FILES["file"]["error"] > 0)
        {
        echo "Error: " . $_FILES["file"]["error"] . "<br />";
        }
      else
        {
        echo "Upload: " . $_FILES["file"]["name"] . "<br />";
        echo "Type: " . $_FILES["file"]["type"] . "<br />";
        echo "Size: " . ($_FILES["file"]["size"] / 1024) . " Kb<br />";
        echo "Stored in: " . $_FILES["file"]["tmp_name"];
        }
      }
    else
      {
      echo "Invalid file";
      }
    
    ?>

  
注释：对于 IE，识别 jpg 文件的类型必须是 pjpeg，对于 FireFox，必须是 jpeg。 

  


  


##  保存被上传的文件 

上面的例子在服务器的 PHP 临时文件夹创建了一个被上传文件的临时副本。 

这个临时的复制文件会在脚本结束时消失。要保存被上传的文件，我们需要把它拷贝到另外的位置： 
    
    
    <?php
    if ((($_FILES["file"]["type"] == "image/gif")
    || ($_FILES["file"]["type"] == "image/jpeg")
    || ($_FILES["file"]["type"] == "image/pjpeg"))
    && ($_FILES["file"]["size"] < 20000))
      {
      if ($_FILES["file"]["error"] > 0)
        {
        echo "Return Code: " . $_FILES["file"]["error"] . "<br />";
        }
      else
        {
        echo "Upload: " . $_FILES["file"]["name"] . "<br />";
        echo "Type: " . $_FILES["file"]["type"] . "<br />";
        echo "Size: " . ($_FILES["file"]["size"] / 1024) . " Kb<br />";
        echo "Temp file: " . $_FILES["file"]["tmp_name"] . "<br />";
    
        if (file_exists("upload/" . $_FILES["file"]["name"]))
          {
          echo $_FILES["file"]["name"] . " already exists. ";
          }
        else
          {
          move_uploaded_file($_FILES["file"]["tmp_name"],
          "upload/" . $_FILES["file"]["name"]);
          echo "Stored in: " . "upload/" . $_FILES["file"]["name"];
          }
        }
      }
    else
      {
      echo "Invalid file";
      }
    ?>

  
  


上面的脚本检测了是否已存在此文件，如果不存在，则把文件拷贝到指定的文件夹。 

注意，要在目录下创建 "upload"文件夹要不然会出现错误。 

  


  


前面这些内容在W3C中都可以找到相应的介绍，接下来就是把PHP和JqueryMobile结合起来实现图片上传了。 

本以为简单的加上Mobile的东西就行了，但是问题出现了：使用了JqueryMobile之后出现了无限Loading的情况、 

原因是JQM把表单提交做成了异步，只需要在form中加上 data-ajax="false" 即可。 

  


** 完整步骤如下： **   


先是用户页面index.php： 
    
    
    <!DOCTYPE HTML>
    
    <html>
    
    <head>
    	<meta  http-equiv="Content-Type"  content="text/html;  charset=utf-8"  />
    	<meta name="viewport" content="width=device-width, minimum-scale=1, maximum-scale=1">
    	<link rel="stylesheet" href="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.css">
    	<script src="http://code.jquery.com/jquery-1.5.min.js"></script>
    	<script src="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.js"></script>
    </head>
    
    <body>
    
    <div data-role="page">
    
    	<div data-role="header">
    		<h1>演示PHP上传文件</h1>
    	</div><!-- /header -->
    
    	<div data-role="content">
    		<form action="upload_file.php" method="post" enctype="multipart/form-data" data-ajax="false">
    		<label for="file">文件名称</label>
    		<input type="file" name="file" id="file" /> 
    		<br />
    		<input type="submit" name="submit" value="上传！" />
    		</form>
    	</div><!-- /content -->
    
    	<div data-role="footer">
    		<h4>存到upload文件夹</h4>
    	</div><!-- /footer -->
    
    </div><!-- /page -->
    </body>
    
    </body>
    </html>

  
接着是上传处理的页面upload_file.php： 
    
    
    <!DOCTYPE HTML>
    
    <html>
    
    <head>
    	<meta  http-equiv="Content-Type"  content="text/html;  charset=utf-8"  />
    	<meta name="viewport" content="width=device-width, minimum-scale=1, maximum-scale=1">
    	<link rel="stylesheet" href="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.css">
    	<script src="http://code.jquery.com/jquery-1.5.min.js"></script>
    	<script src="http://code.jquery.com/mobile/1.0a4.1/jquery.mobile-1.0a4.1.min.js"></script>
    </head>
    
    <body>
    
    <!-- 显示图片信息 -->
    <div data-role="page">
    
    	<div data-role="header">
    		<h1>显示PHP上传的文件信息</h1>
    	</div><!-- /header -->
    
    	<div data-role="content">
    		<?php
    			if ($_FILES["file"]["error"] > 0)
    			{
    				echo "错误代码: " . $_FILES["file"]["error"] . "<br />";
    			}
    			else
    			{
    				echo "文件名称: " . $_FILES["file"]["name"] . "<br />";
    				echo "文件类型: " . $_FILES["file"]["type"] . "<br />";
    				echo "文件大小: " . ($_FILES["file"]["size"] / 1024) . " Kb<br />";
    				echo "临时路径: " . $_FILES["file"]["tmp_name"] . "<br />";
    				if (file_exists("upload/" . $_FILES["file"]["name"]))
    				{
    					echo "该文件已经存在";
    				}
    				else
    				{
    					move_uploaded_file($_FILES["file"]["tmp_name"],"upload/" . $_FILES["file"]["name"]);
    					echo "存储路径: " . "upload/" . $_FILES["file"]["name"];
    				}
    			}
    		?>
    	</div><!-- /content -->
    
    	<div data-role="footer">
    		<a href="#myimage">点击查看图片</a>
    	</div><!-- /footer -->
    
    </div><!-- /page -->
    
    
    <!-- 显示图片的div -->
    <div data-role="page" id="myimage">
    	<img src="<?php echo "upload/".$_FILES["file"]["name"]?>"/>
    </div><!-- /page -->
    
    
    </body>
    
    </body>
    </html>

  


  


在虚拟机的浏览器地址栏输入10.0.2.2或者在同一个局域网下的移动设备中输入192.168.1.101访问页面： 

  


![](http://img.blog.csdn.net/20140111210909484?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/18147507](http://blog.csdn.net/pleasecallmewhy/article/details/18147507)