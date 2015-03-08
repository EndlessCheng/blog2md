#  Python监视网站是否宕机get和post方式 

[ Find ](http://www.findspace.name/author/find) |  2014年11月27日  |  [ Python ](http://www.findspace.name/category/easycoding/python) , [ 小工具 ](http://www.findspace.name/category/easycoding/tools) , [ 随意Coding ](http://www.findspace.name/category/easycoding) |  [ 没有评论  ](http://www.findspace.name/easycoding/946#comments)

利用python写的简单的脚本，用来检测自己的博客是否宕机，如果宕机了，就短信通知自己。 

其中涉及了get和post两种访问网页的方式。 
    
    
    #coding:utf-8
    #author Find
    #date:2014-11-27
    import httplib
    import urllib
    
    httpclient=None
    try:
        #监视的网站
        httpclient=httplib.HTTPConnection('www.findspace.name',80,timeout=3)
        #get方式访问
        httpclient.request('GET','')
        response=httpclient.getresponse()
        #如果网站不可访问，则飞信发短信通知自己
        if (response.status>=300 and response.status<200):
            #post参数表，这个api的使用可以参照另一篇博客
            params=urllib.urlencode({'user':'18366111234', 'key':'','number':'18366111234','text':'Findspaec.name crashed!'})
            headers={'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
            httpclient=httplib.HTTPConnection('openfetionapi.sinaapp.com')
            httpclient.request('POST', '/fetion.php', params, headers)
            response=httpclient.getresponse()
            if(response.status>=300 and response.status<200):
                print('Sending Fetion Message Failed')
            else:
                print(response.read())
    #最后要关闭httpclient
    finally:
        if httpclient:
            httpclient.close()
    

这个脚本最好结合linux的cron服务来定时启动， [ 关于linux的定时任务参考这篇博客 ](http://www.findspace.name/res/902) ，其中利用飞信api发短信的部分可以参考： [ 飞信开放api ](http://openfetionapi.sinaapp.com)

顺便写上python添加中文注释时，注意在Python脚本文件的第一行或第二行添加一句： 

** #coding:gbk ** 或 ** #coding:utf-8 ** 或 ** ##-*- coding : gbk -*- **

Tags:  [ Linux ](http://www.findspace.name/tag/linux) , [ python ](http://www.findspace.name/tag/python-2) , [ 小工具 ](http://www.findspace.name/tag/%e5%b0%8f%e5%b7%a5%e5%85%b7)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/easycoding/946](http://www.findspace.name/easycoding/946)