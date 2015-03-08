#  自定义Access-Control-Allow-Origin策略以解决字体文件跨域权限问题

[ Yuguo ](http://yuguo.us) 2012年 12月 03日

##  什么是Access-Control-Allow-Origin

Access-Control-Allow-Origin是HTML5中定义的一种服务器端返回Response
header，用来解决资源（比如字体）的跨域权限问题。

它定义了该资源允许被哪个域引用，或者被所有域引用（google字体使用*表示字体资源允许被所有域引用）。

##  什么是资源跨域权限

当两个域具有相同的协议(如http), 相同的端口(如80)，相同的host（如www.example.org)，那么我们就可以认为它们是相同的域。

比如http://www.example.org/和http://www.example.org/sub/是同域，而http://www.example.o
rg, https://www.example.org, http://www.example.org:8080,
http://sub.example.org中的任何两个都将构成 [ 跨域
](http://www.woiweb.net/tag/%E8%B7%A8%E5%9F%9F) 。

例如www.a.com对www.b.com下的asset.php发送了一个 [ 跨域
](http://www.woiweb.net/tag/%E8%B7%A8%E5%9F%9F) 的HTTP请求，那么asset.php必须加入如下的响应头：

header(“Access-Control-Allow-Origin: [ http://www.a.com ](http://www.a.com/)
”);

坑爹的是，该域值不可为正则表达式，如 [ http://*.a.com ](http://*.a.com/)
<h2>如果HTML和CSS等资源所在的CDN不一致，就会出现跨域访问，而这在大型网站中是很常见的</h2> HTML域： [
http://ctc.qzs.qq.com ](http://ctc.qzs.qq.com/) [ / ](http://ctc.qzs.qq.com/)
【等】

CSS域： [ http:// ](http://ctc.qzonestyle.gtimg.cn/) [ ctc.qzonestyle.gtimg.cn
](http://ctc.qzonestyle.gtimg.cn/) 【等】

字体与CSS是相对路径所以同域： [ http:// ](http://ctc.qzonestyle.gtimg.cn/) [
ctc.qzonestyle.gtimg.cn ](http://ctc.qzonestyle.gtimg.cn/) 但是HTML与字体是跨域！

高级浏览器访问html页面的时候，对于CSS文件中使用的字体文件的请求，会带一个origin:头，这个头就是html页面所在的域。 [
![](http://yuguo.us/files/2012/12/1.png)
](http://yuguo.us/files/2012/12/1.png) 高级浏览器（Firefox，IE9+）会对比自己发出的Request
header中的Origin:和返回字体文件的Response header的Access-Control-Allow-Origin:域

  * 若相同，则表示该网站有权限使用该字体，浏览器显示字体 
  * 若不同，则表示该网站无权使用该字体，浏览器虽然下载了该字体，但拒绝显示 

###  解决办法1

  * 对于字体文件的Request，全部在返回头中加入： 
  * Access-Control-Allow-Origin:* 
  * 缺点：安全性问题 

###  解决办法2

根据Request Headers的内容，决定一些需要的Response Headers的内容，这里定义规则如下：

根据Request的Origin: 进行决策，

在Origin来自

*.qq.com（包括  [ www.qq.com ](http://www.qq.com/) ; qq.com;）时; 

Response Header中增加Access-Control-Allow-Origin:头

头的内容保持和Requset Headers中的Origin: 头URI中的protocol, domainname, port内容，并一致

[ 香港设计营商周论坛 → ](/weblog/bodw-2012/) [ ←
《众妙之门3》——第九章：移动用户体验设计考虑的因素：“是Web，还是原生？” ](/weblog/web-or-native-2/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

