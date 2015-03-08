#  [ [Python]一起来写一个Python爬虫工具类whyspider ](/pleasecallmewhy/article/details/24021695)

很高兴在GITCAFE遇到了志同道合的人发送了合并请求^_^希望更多的人可以参与进来   


写了很多简单的Python爬虫的小例子，今天突然想做个开源的工具包，在gitcafe上和大家一起分享源码。 

  


  


项目源地址： 

[ https://gitcafe.com/callmewhy/whyspider ](https://gitcafe.com/callmewhy/whyspider)   


  


  


  


今天写了个最简单的功能：GET和POST方法。 

其他功能会在gitcafe上陆陆续续的继续完善， 

下一步的计划是完成正则匹配的封装和模拟header这些常见的功能   


  


因为最近在学安卓，所以更新的进度可能会慢一点=。= 

如果有什么想法，比如觉得希望这个里面添加什么功能，欢迎评论或者在gitcafe中提交ticket~ 

  


目前刚完成了0.2版本： 
    
    
    # -*- coding: utf-8 -*-
    #---------------------------------------
    #   程序：whyspider.py
    #   版本：0.2
    #   作者：why
    #   日期：2014-04-18
    #   语言：Python 2.7.5
    #
    #   版本列表：
    #   0.1：添加GET和POST
    #   0.2：添加模拟头的功能
    #---------------------------------------
    
    import urllib  
    import urllib2
    import cookielib
    import re
    import string
    
    class WhySpider:
        
        # 初始化爬虫  
        def __init__(self):
            self.cookie_jar = cookielib.CookieJar()
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie_jar))
            self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'}
    
        # 发送GET请求
        def send_get(self,get_url):
            result = ""
            try:
                my_request = urllib2.Request(url = get_url, headers = self.headers)
                result = self.opener.open(my_request).read()
            except Exception,e:
                print "Exception : ",e
            return result
    
        # 发送POST请求
        def send_post(self,post_url,post_data):
            result = ""
            try:
                my_request = urllib2.Request(url = post_url,data = post_data, headers = self.headers)
                result = self.opener.open(my_request).read()
            except Exception,e:
                print "Exception : ",e
            return result
    
        # 模拟电脑
        def set_computer(self):
            user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'
            self.headers = { 'User-Agent' : user_agent }    
            
        # 模拟手机
        def set_mobile(self):
            user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25'
            self.headers = { 'User-Agent' : user_agent }    
    

  
  


  
  


调用方法很简单： 
    
    
    # -*- coding: utf-8 -*-
    import whyspider
    
    # 初始化爬虫对象
    my_spider = whyspider.WhySpider()
    
    # 模拟GET操作
    print my_spider.send_get('http://3.apitool.sinaapp.com/?why=GetString2333')  
    
    # 模拟POST操作
    print my_spider.send_post('http://3.apitool.sinaapp.com/','why=PostString2333')  
    
    # 模拟GET操作
    print my_spider.send_get('http://www.baidu.com/')  
    
    # 切换到手机模式
    my_spider.set_mobile()
    
    # 模拟GET操作
    print my_spider.send_get('http://www.baidu.com/')  
    

  
  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/24021695](http://blog.csdn.net/pleasecallmewhy/article/details/24021695)