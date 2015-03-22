#  [ Django 中设置 css/js/images 路径的方法 ](/2014/09/18/django-sets-the-css-js-images-path/)

在 settings.py 的最后一行你可以看到 ` STATIC_URL = '/static/' ` 这句话，在其后面加上： 
    
    
    STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
    
    STATICFILES_DIRS = (
    
        ('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/') ),
    
        ('js', os.path.join(STATIC_ROOT, 'js').replace('\\', '/') ),
    
        ('images', os.path.join(STATIC_ROOT, 'images').replace('\\', '/') ),
    
    )  
  
---  
  
然后把你的 css/js/images 那些文件夹都丢进 static 文件夹中（此文件夹应建立在你的 view.py 所在目录下）   
模板里面这么写： 
    
    
    <link type="text/css" rel="stylesheet" href="/static/css/login.css">  
  
---  
  
如果设置之后出现了与 Unicode 有关的错误，打开 ` /Python27/Lib/mimetypes.py ` ，在 import 语句之后加入： 
    
    
    if sys.getdefaultencoding() != 'gbk':
    
        reload(sys)
    
        sys.setdefaultencoding('gbk')  
  
---
#### 原文：[http://jianyan.me/2014/09/18/django-sets-the-css-js-images-path/](http://jianyan.me/2014/09/18/django-sets-the-css-js-images-path/)