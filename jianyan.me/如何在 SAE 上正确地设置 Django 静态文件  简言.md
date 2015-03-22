#  [ 如何在 SAE 上正确地设置 Django 静态文件 ](/2014/12/29/how-to-properly-configure-the-django-static-files-on-sae/)

1.目录结构如下：（请无视 ` .idea ` 文件夹） 

![](http://endless.qiniudn.com/blogsae-django-static.png)

2\. ` config.yaml ` 只需要两行： 
    
    
    libraries:
    
    - name: "django"
    
      version: "1.5"  
  
---  
  
3\. ` settings.py ` 里面这样写： 
    
    
    STATIC_ROOT = ''
    
    STATIC_URL = '/static/'
    
    STATICFILES_DIRS = (
    
        os.path.join('static'),
    
    )  
  
---  
  
4\. ` urls.py ` 只需要加上你的 view 就行。 

5.模板里面这样写： 

![](http://endless.qiniudn.com/blogsae-django-static2.png)

搞定。 

PS： ` USE_TZ ` 要设置成 ` False ` ，否则插入时间到数据库的时候会变成 UTC 时间而不是北京时间。 

参考资料： 

  1. [ Managing static files (CSS, images) ](https://docs.djangoproject.com/en/dev/howto/static-files/)
  2. [ The staticfiles app ](https://docs.djangoproject.com/en/1.5/ref/contrib/staticfiles/)
  3. [ Settings Documentation ](https://docs.djangoproject.com/en/1.5/ref/settings/)
#### 原文：[http://jianyan.me/2014/12/29/how-to-properly-configure-the-django-static-files-on-sae/](http://jianyan.me/2014/12/29/how-to-properly-configure-the-django-static-files-on-sae/)