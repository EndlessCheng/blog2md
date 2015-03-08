[ ![简言](/img/logo.png) ](/)

#  [ 简言 ](/)

##  言简意赅，技术远没那么复杂

    * [ Home ](/)
    * [ Archives ](/archives)
    * [ About ](/about)
    * Search 

#  [ Python 爬虫学习——收集「有趣」信息（8月16日更新） ](/2014/06/24/learning-python-crawler-
gathering-interesting-information/)

By [ 简言 ](https://plus.google.com/103441795113657293146?rel=author)

Published Jun 24 2014

** Contents **

我们使用 urllib2 这个组件来抓取网页，这是 Python 的一个获取 URLs (Uniform Resource Locators)的组件，它以
urlopen 函数的形式提供了一个非常简单的接口。

以获取某 <del> id 为 EndlessCheng </del> 用户的 repository 列表为例：

（阅读下面代码之前建议先看看 [ 该页面 ](https://github.com/EndlessCheng?tab=repositories) 的源码）

    
    
    1
    
    2
    
    3
    
    4
    
    5
    
    6
    
    7
    
    8
    
    9
    
    10
    
    11
    
    12
    
    13
    
    14
    
    15
    
    16
    
    17
    
    18

|

    
    
    # -*- coding: UTF-8 -*-
    
    import urllib2
    
    USERNAME = 'EndlessCheng'
    
    response = urllib2.urlopen('https://github.com/' + USERNAME + '?tab=repositories')  
    
    html = response.read()  
    
    STEP = 20
    
    cnt = next = 1
    
    while True:
    
        end = html.find('</h3>', next, len(html))  # 获取 repolist-name 尾位置
    
        if end == -1:
    
            break
    
        next = end + STEP
    
        end = html.rfind('</a>', 0, end) 
    
        begin = html.rfind('>', 0, end) + 1
    
        print "%3d  %s" % (cnt, html[begin:end])
    
        cnt += 1  
  
---|---  
  
源网页：

![](http://endless.qiniudn.com/blogrepo.png)

输出结果：

![](http://endless.qiniudn.com/blogoutput.png)

出于项目维护的需要，写了一个获取 Commits 列表的爬虫：  
（晕，代码中的 EscapeCharacterDict 的转义字符被直接转换了，可以去 [ 原项目
](https://github.com/EndlessCheng/Commits-Crawler/blob/master/Core.py) 查看）

    
    
    1
    
    2
    
    3
    
    4
    
    5
    
    6
    
    7
    
    8
    
    9
    
    10
    
    11
    
    12
    
    13
    
    14
    
    15
    
    16
    
    17
    
    18
    
    19
    
    20
    
    21
    
    22
    
    23
    
    24
    
    25
    
    26
    
    27
    
    28
    
    29
    
    30
    
    31
    
    32
    
    33
    
    34
    
    35
    
    36
    
    37
    
    38
    
    39
    
    40
    
    41
    
    42
    
    43
    
    44
    
    45
    
    46
    
    47

|

    
    
    # -*- coding: UTF-8 -*-
    
    import urllib2
    
    EscapeCharacterDict = {'&': '&', '<': '<', '>': '>', '"': '"', ''': '\''}
    
    def deal(response):
    
        html = response.read()
    
        global cnt
    
        global fp
    
        step = 24
    
        end = 1000
    
        while True:
    
            begin = html.find('data-pjax="true" title=', end, len(html))  # 获取 commit 首位置
    
            if begin == -1:
    
                break
    
            begin += step
    
            keywords = '">' if html[begin - 1] == '"' else '\'>'
    
            end = html.find(keywords, begin, len(html))
    
            s = html[begin:end]
    
            for k, v in EscapeCharacterDict.iteritems():
    
                s = s.replace(k, v)
    
            fp.write("%3d  %s\n" % (cnt, s))
    
            cnt += 1
    
    USERNAME = 'rogerwang' # 修改这里
    
    REPONAME = 'node-webkit' # 修改这里
    
    fp = open(USERNAME + '#' + REPONAME + '#commits.txt', 'w')
    
    cnt = 1
    
    i = 1
    
    while True:
    
        try:
    
            response = urllib2.urlopen('https://github.com/' + USERNAME + '/' + REPONAME + '/commits?page=' + str(i))
    
            deal(response)
    
            print 'Cheaked', i, 'page(s).'
    
            i += 1
    
        except urllib2.HTTPError, err:
    
            if err.code == 404:
    
                print ''
    
                print 'Cheaked', i - 1, 'page(s),', cnt - 1, 'commit(s) found.'
    
                break
    
            else:
    
                raise  
  
---|---  
  
[ Python ](/tags/Python/) [ 爬虫 ](/tags/爬虫/) [ GitHub ](/tags/GitHub/)

[ ** 上一篇： **  
Git 用的越早，你就活得越久  ](/2014/07/04/earlier-for-git-youll-live-longer/)

[ ** 下一篇： **  
Java 与 C++ 混合编程——JNI 学习小记  ](/2014/06/21/notes-on-java-and-c-programming-jni-
blended-learning/)

Please enable JavaScript to view the [ comments powered by Disqus.
](//disqus.com/?ref_noscript)

** Contents **

Tag Cloud

[ Android ](/tags/Android/) [ C ](/tags/C/) [ Django ](/tags/Django/) [ GHC
](/tags/GHC/) [ Git ](/tags/Git/) [ GitHub ](/tags/GitHub/) [ Hexo
](/tags/Hexo/) [ JNI ](/tags/JNI/) [ Jacman ](/tags/Jacman/) [ Java
](/tags/Java/) [ Markdown ](/tags/Markdown/) [ PIL ](/tags/PIL/) [ Pillow
](/tags/Pillow/) [ Python ](/tags/Python/) [ SAE ](/tags/SAE/) [ macro
](/tags/macro/) [ 「Hello World」 ](/tags/「Hello-World」/) [ 杂谈 ](/tags/杂谈/) [
混合编程 ](/tags/混合编程/) [ 爬虫 ](/tags/爬虫/) [ 网络传输协议 ](/tags/网络传输协议/)

Links

  * [ Logdown 博客 ](http://endless.logdown.com/)
  * [ CSDN 博客 ](http://blog.csdn.net/synapse7?viewmode=list)
  * [ GitHub ](https://github.com/EndlessCheng)

[ RSS ](/atom.xml)

[ ](https://github.com/EndlessCheng) [
](http://stackoverflow.com/users/3208881) [
](https://www.douban.com/people/52879216) [
](https://www.zhihu.com/people/endlesscheng) [
](https://plus.google.com/103441795113657293146?rel=author) [
](mailto:loli.con@qq.com)

Powered by [ hexo ](http://zespia.tw/hexo/) and Theme by [ Jacman
](https://github.com/wuchong/jacman) © 2015 [ 简言 ](http://jianyan.me/about)

![](/img/scrollup.png)

