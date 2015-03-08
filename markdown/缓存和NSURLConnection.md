#  缓存和NSURLConnection

[ Yuguo ](http://yuguo.us) 2013年 01月 21日

创建NSURLConnection的时候，如果没有选择缓存策略，就会使用默认的缓存策略 `
NSURLRequestUseProtocolCachePolicy ` ，即使用协议的缓存策略。

也就是说在你的APP中的连接所请求的Web内容会根据协议（HTTP）头来进行缓存：

  * 如果你的HTTP头中带了 ` Expires ` 字段，APP会认为不需要在时间到期之前向服务器请求文件是否合法，它直接调用缓存的内容； 
  * 如果你的HTTP头中带了 ` Cache-Control: max-age ` ，APP会在每次请求内容之前询问服务器内容是否修改，如果修改了，APP重新请求内容，如果没有修改，APP调用缓存里的内容； 
  * 如果你的HTTP头中没有 ` Expires ` 和 ` Cache-Control: max-age ` ，APP会 _ 自动把内容缓存相当长的时间 _

所以最佳实践是：

  * 如果你可以控制HTTP头，那么请使用HTTP头来控制APP中Web内容的缓存策略，这是最好的方法； 
  * 如果你不可以控制HTTP头，比如第三方的API等，那么你可能会被默认的超长缓存时间困扰，解决办法是在APP中进行条件判断，具体代码见参考资料中最后一节。 

顺便说下，github pages并不能很好地进行API托管，因为没有办法控制HTTP头。基于同样的原因， [ 它也不适合做CDN
](http://stackoverflow.com/questions/5502540/should-github-be-used-as-a-cdn-
for-javascript-libraries) 。

参考资料： [ Caching and NSURLConnection ](http://blackpixel.com/blog/2012/05
/caching-and-nsurlconnection.html)

[ 从Github Pages搬家到Amazon S3 → ](/weblog/github-page-to-amazon-s3/) [ ← LESS in
Action ](/weblog/less/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

