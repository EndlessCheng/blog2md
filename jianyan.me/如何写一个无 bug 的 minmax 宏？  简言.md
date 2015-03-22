#  [ 如何写一个无 bug 的 min/max 宏？ ](/2014/11/01/how-to-write-a-bug-free-min-max-macro/)

今天看了下 GHC 的源码，在 [ Rts.h ](https://github.com/ghc/ghc/blob/master/includes/Rts.h) 中，有如下宏定义： 
    
    
    #if defined(SUPPORTS_TYPEOF)
    
    #define stg_min(a,b) ({typeof(a) _a = (a), _b = (b); _a <= _b ? _a : _b; })
    
    #define stg_max(a,b) ({typeof(a) _a = (a), _b = (b); _a <= _b ? _b : _a; })
    
    #else
    
    #define stg_min(a,b) ((a) <= (b) ? (a) : (b))
    
    #define stg_max(a,b) ((a) <= (b) ? (b) : (a))
    
    #endif  
  
---  
  
那么问题来了：为什么不直接定义下面那种宏？   
原因在于传入的 a,b 可能是一个有副作用的表达式，比如 ` ++a ` ，使用下面这种宏会产生一个及其隐秘的 bug（谁知道哪天程序出错了 bug 会在这里）。   
个人觉得这真的是一个 GHC 的 bug..   
替代方案就正如源码中写的，使用 ` typeof ` ，不过这需要 C 扩展支持。   
参考： 

  1. [ macros - MIN and MAX in C - Stack Overflow ](http://stackoverflow.com/questions/3437404/min-and-max-in-c)
  2. [ Typeof - Using the GNU Compiler Collection (GCC) ](https://gcc.gnu.org/onlinedocs/gcc/Typeof.html#Typeof)
#### 原文：[http://jianyan.me/2014/11/01/how-to-write-a-bug-free-min-max-macro/](http://jianyan.me/2014/11/01/how-to-write-a-bug-free-min-max-macro/)