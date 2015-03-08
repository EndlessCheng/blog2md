#  [ [Grails]使用Grails的Console执行简单的CRUD操作 ](/pleasecallmewhy/article/details/18778097)

[ Grails ](http://www.csdn.net/tag/Grails) [ groovy ](http://www.csdn.net/tag/groovy)

Grails中可以使用Groovy脚本实现一些基本的操作测试，比如对数据库的CRUD操作。 

只需要在网站根目录下按住shift键右击，选择在当前位置打开命令行，然后输入grails console即可。 

  


先说一下基本的结构，主要是两个域类。 

Bookmark.groovy是书签类，主要是链接标题和创建日期，对于Tag有一对多的映射关系： 
    
    
    package com.why.bookmarks
    
    class Bookmark {
        static hasMany = [tags : Tag]//每个Bookmark有很多Tag
            
        URL url             //书签链接
        String title        //书签标题
        Date dateCreated    //创建日期
    
        static optionals = ['notes']    //可选的备注
        
        static constraints = {
        }
    }
    

  
Tag.groovy是一个标签类，主要包含了标签的名字，归属于一个bookmark对象： 
    
    
    package com.why.bookmarks
    
    class Tag {
        static belongsTo = Bookmark     //每个Tag属于一个Bookmark
        Bookmark bookmark               //所归属的Bookmark
        String name                     //Tag的名字
        
        static constraints = {
        }
        
    }
    

  
在控制台输入grails console打开Grails的控制台，然后可以使用一下代码进行CRUD的测试。 

创建书签：    

    
    
    //创建书签
    def aMark = new Bookmark(url:new URL('http://www.baidu.com'),title:'Grails Title',notes:'Grrovy-based web framework')
    aMark.addToTags(new Tag(name:'Grails'))
    aMark.addToTags(new Tag(name:'Web Framework'))
    aMark.tags.each{println it.name}
    aMark.save()

  
读取书签： 
    
    
    //读取书签
    def aMark = Bookmark.get(1)
    println aMark.url

  
修改书签： 
    
    
    def aMark = Bookmark.get(1)
    aMark.url = new URL("http://google.com")
    aMark.save()

  
删除书签： 
    
    
    //删除书签
    def aMark = Bookmark.get(1)
    aMark.delete()

  
  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/18778097](http://blog.csdn.net/pleasecallmewhy/article/details/18778097)