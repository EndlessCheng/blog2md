#  [ [Python]计算闰年时候出现的and和or优先级的问题以及短路逻辑 ](/pleasecallmewhy/article/details/26133025)

好吧题目很简单，但是有些细节还是挺有意思的。 

  


题目是：计算今年是否是闰年，判断闰年条件，满足年份模400为0，或者模4为0但是模100不为0 

  


答案是这样的： 
    
    
    import time
    
    #计算今年是否是闰年，判断闰年条件，满足年份模400为0，或者模4为0但是模100不为0
    
    
    thisyear = time.localtime()[0] #获取年份
    
    if thisyear%400==0 or thisyear%4==0 and thisyear%100<>0:
    	print 'this year is a leap year'
    else:
    	print 'this yeat is not a leap year'

  
很简单的源码，在此来记录其中的一些细节。 

  


先回顾一下Python中的数组，Python的数组分三种类型：   
(1) list 普通的链表，初始化后可以通过特定方法动态增加元素。   
定义方式：arr = [元素]   
  
(2) Tuple 固定的数组，一旦定义后，其元素个数是不能再改变的。   
定义方式：arr = (元素)   
  
(2) Dictionary 词典类型， 即是Hash数组。   
定义方式：arr = {元素k:v}    


  


接下来看看源码。   


首先是time模块，localtime()返回的是一个tuple，也就是一个固定大小的数组，数组里是当前时间的一些数据 ： 

localtime([seconds]) -> (tm_year,tm_mon,tm_day,tm_hour,tm_min,tm_sec,tm_wday,tm_yday,tm_isdst) 

  


然后是if判断里面的 or 和 and ， 

Python的逻辑运算符里没有“!(非)，&&(与)，||(或)“， 

这三个表示符号(完全是英文上的表示)，即 not，and，or。 

  


但是看源码，判断是否闰年应该是： 

1.如果被400整除那就是闰年 

2.如果能被4整除且不能被100整除 

  


那if判断不应该是： 

if thisyear%400==0 or (thisyear%4==0 and thisyear%100<>0): 

这样的吗？ 

  


实际上确实是这样的，但是在Python中，and的优先级要高于or。 

  


我们可以来看一个小例子： 
    
    
    >>> if 1 or 1 and not 1:
    ...     print 'OK'
    ...
    OK

  
如果优先级相等应该是不会输出，其实上面的判断相当于： 
    
    
    if 1 or (1 and not 1):

也就是说， 

True or True and not True  仅仅表示  (True) or (True and False) 

  


  


说到这里可以再看一个有意思的东西，来看看Python里面的短路机制： 
    
    
    def a():
        print 'this is A!'
        return 1
    
    def b():
        print 'this is B!'
        return 1
    
    def c():
        print 'this is C!'
        return 1
    
    if a() or b() and not c():
        print 'OK!'

  
如果说and的优先级要高于or，那么岂不是应该先B再C再A，怎么直接就输出了A呢？ 

  


其实在其他语言中也有这样的情况，只是当时没有在意，这是  布尔运算符  的一个有趣的特性。 

  


布尔运算符有个有趣的特性：只有在需要求值时才进行求值。 

举例来说，表达式x and y需要两个变量都为真时才为真， 

所以如果x为假，表达式就会立刻返回false，而不管y的值（事实上各个语言都有这个特性）。 

实际上，如果x为假，表达式会返回x得值----否则它就返回y的值。 

这种行为被称为短路逻辑（short-circuit logic）或惰性求值（lazy evaluaion）： 

布尔运算符通常被称为逻辑运算符，就像你看到的那样第2个值有时“被短路了”。 

这种行为对于or来说也同样适用。 

在表达式x or y中，x为真时，它直接返回x的值，否则返回y值。 

注意，这意味着在布尔运算符之后的所有代码都不会执行。   


  


  


再看看刚刚的那个例子，and优先级高，表明最靠近它两边的表达式是与的关系，这样的组合是优先的。 

很明显，遇到第一个True，就没必要再计算or后面的东西了，结果已经是True了。 

  


  


在Python中运用and 和 or可以实现三元运算，比如在JS中的一个函数： 
    
    
    function trans(v) {  
        return (v==0)?1:v;  
    } 

  
在Python中可以有以下两种替换方案： 
    
    
    def trans(v):  
            return 1 if v==0 else v 

  
或者： 
    
    
    def trans(v):  
            return v==0 and 1 or v  

  
解释一下： 

如果v等于0，则跟1做与运算，为true，则不进行后面的或运算，直接返回1； 

如果v等于0为false，则跟1做与运算，为false，继续进行或运算，返回v。   


  


  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/26133025](http://blog.csdn.net/pleasecallmewhy/article/details/26133025)