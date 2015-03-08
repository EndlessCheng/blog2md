[ ![简言](/img/logo.png) ](/)

#  [ 简言 ](/)

##  言简意赅，技术远没那么复杂

    * [ Home ](/)
    * [ Archives ](/archives)
    * [ About ](/about)
    * Search 

#  [ 如何写一个无 bug 的 min/max 宏？ ](/2014/11/01/how-to-write-a-bug-free-min-max-
macro/)

By [ 简言 ](https://plus.google.com/103441795113657293146?rel=author)

Published Nov 1 2014

** Contents **

今天看了下 GHC 的源码，在 [ Rts.h
](https://github.com/ghc/ghc/blob/master/includes/Rts.h) 中，有如下宏定义：

    
    
    1
    
    2
    
    3
    
    4
    
    5
    
    6
    
    7

|

    
    
    #if defined(SUPPORTS_TYPEOF)
    
    #define stg_min(a,b) ({typeof(a) _a = (a), _b = (b); _a <= _b ? _a : _b; })
    
    #define stg_max(a,b) ({typeof(a) _a = (a), _b = (b); _a <= _b ? _b : _a; })
    
    #else
    
    #define stg_min(a,b) ((a) <= (b) ? (a) : (b))
    
    #define stg_max(a,b) ((a) <= (b) ? (b) : (a))
    
    #endif  
  
---|---  
  
那么问题来了：为什么不直接定义下面那种宏？  
原因在于传入的 a,b 可能是一个有副作用的表达式，比如 ` ++a ` ，使用下面这种宏会产生一个及其隐秘的 bug（谁知道哪天程序出错了 bug
会在这里）。  
个人觉得这真的是一个 GHC 的 bug..  
替代方案就正如源码中写的，使用 ` typeof ` ，不过这需要 C 扩展支持。  
参考：

  1. [ macros - MIN and MAX in C - Stack Overflow ](http://stackoverflow.com/questions/3437404/min-and-max-in-c)
  2. [ Typeof - Using the GNU Compiler Collection (GCC) ](https://gcc.gnu.org/onlinedocs/gcc/Typeof.html#Typeof)

[ C ](/tags/C/) [ macro ](/tags/macro/) [ GHC ](/tags/GHC/)

[ ** 上一篇： **  
Pillow 模块小记：在图片上添加文字  ](/2014/12/09/notes-of-the-pillow-moudle-adding-text-on-
the-picture/)

[ ** 下一篇： **  
GitHub 秘籍  ](/2014/09/23/github-cheats/)

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

