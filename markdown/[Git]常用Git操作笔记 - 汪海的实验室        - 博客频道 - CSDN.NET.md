#  [ [Git]常用Git操作笔记 ](/pleasecallmewhy/article/details/28648949)

### 

  1. 删除Git中跟踪的文件 

在使用git之后发现某个文件不应该添加到git中。 可以在.gitignore文件中加上该文件。 但是这个文件如果之前已经被git跟踪了，这样修改是没有用的。每次修改完以后，用git status还是能看到提示它被修改了。 解决办法就是在git中删除这个文件的跟踪记录，用这个命令： 
    
    
    git rm --cached project.iws
    

这样就从git的跟踪记录中删除了这个文件的跟踪记录。 如果是文件夹可以加上-r标记，比如删除对于themes文件夹的跟踪： 
    
    
    git rm --cached themes/ -r

  


  


  


  


  


  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/28648949](http://blog.csdn.net/pleasecallmewhy/article/details/28648949)