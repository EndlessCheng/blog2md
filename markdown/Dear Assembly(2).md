[ Home ](http://blog.cee.moe) [ Subscribe ](http://blog.cee.moe/rss/)

#  Dear Assembly(2)

30 July 2014

> 继续我们的拆炸弹之旅~

>

> 上一篇请戳 [ 这里 ](https://blog.cee.moe/dear-assembly-1/) /w\

* * *

###  Phase_6

作业的要求也就是做到phase_5，但是很感兴趣所以继续往下做~

代码如上。

第4行的 ` strtol ` 函数：字符串按照10进制转换成长整形，这里不再赘述（就是得到输入的数）。并且第5行把它放在了 ` node0 ` 中。

目光投向第12行的 ` cmp ` （很重要啊混蛋！）， ` %edx == *(%rax) ` ，往上再看三行相当于 ` %rax = %rax + 8
` 做了3次，指针向后移动了三个address长度。再来分析 ` fun6 ` 究竟做了什么：

（ ` fun6 ` 就是长长长+看不懂！）

尽管如此还是得继续，手写一下各个寄存器的转化，分析一下 ` fun6 ` 的作用：排序。

题目就转换成对所有数排序后第四个数是否等于输入的数，观察一下 ` node1 ` 到 ` node9 ` ，答案也就出来了：

> 取600~673（分别对应 ` node8 ` 和 ` node6 ` ）中的任意一个整数

###  Secret_Phase

最好玩的莫过于做完了布置的作业继续探索了！Let's Go On！

说到Secret Phase，第一次看到是因为用 ` x /32c ` 看格式化字符串的时候发现了：

> austinpowers

后来发现在每个phase做完后的 ` phase_defused ` 有个调用：

顺藤摸瓜，看了一下地址在 ` 0x401ec4 ` 中的格式化字符串：

> %d %s

并且和 ` austinpowers ` 比较了。并且 ` 0x603030 ` 这个入口也就是第四题的输入，即在⑨后面加上 ` austinpowers
` 就进入了 ` secret_phase ` 。

最后来看一下 ` secret_phase ` 和调用的 ` fun7 ` ：

这里建立了一棵树，他的数据结构就是节点自身和左右孩子。第15行的 ` cmp ` （跟你们说了很重要！）函数要求我们 ` fun7 `
的返回值是3。画出树得到最后的答案：

> 107

撒花，成绩就是 ` 62.5/50 ` 了！

###  About GDB

关于gdb这里也想谈谈。

通过这次的lab作业提升了很多关于gdb调试的技巧。

给大家列一些常用的命令吧~

` gdb <file> ` : 开始调试><

` run ` , ` quit ` : 开始和退出

` break func/*0x804820 ` : 给 ` func ` 函数/在地址为 ` 0x804820 ` 处设置断点

` delete/disable/enable 1 ` : 删除/禁用/启用断点1（自动标号）

` stepi ` : 执行一条指令

` nexti ` : 执行一条指令，但是在函数调用中不停止

` step ` : 执行一条C指令

` disassemble func/0x804820 ` : 查看 ` func ` 函数/地址在 ` 0x804820 ` 的汇编语句

` print /x $rip ` : 16进制输出PC

` print /d $rip ` : 10进制输出PC

` print /t $rip ` : 2进制输出PC

` x /[NUM][SIZE][FORMAT] where ` : 指定格式输出， ` NUM ` 位数， ` SIZE `
代表每一位的大小（例如b=byte，w=word，g=giant）， ` FORMAT ` 代表格式（x，d，t）， ` WHERE ` 代表地址。

` info r ` : 查看寄存器

###  References

[ CSAPP Bomb Lab ](http://lifeofzjs.com/blog/2014/02/03/csapp-bomb-lab/)

* * *

###  What's Next

> 下一篇会主要介绍一下lab3的缓存区攻击的作业。敬请期待哦www

[ Cee's Picture  ](/author/cee/)

####  [ Cee ](/author/cee/)

Read [ more posts ](/author/cee/) by this author.

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

####  Share this post

[ Twitter
](https://twitter.com/share?text=Dear%20Assembly\(2\)&url=http://blog.cee.moe
/dear-assembly-2/) [ Facebook
](https://www.facebook.com/sharer/sharer.php?u=http://blog.cee.moe/dear-
assembly-2/) [ Google+
](https://plus.google.com/share?url=http://blog.cee.moe/dear-assembly-2/) [
Cee's Home ](http://blog.cee.moe) © 2015  Proudly published with [ Ghost
](https://ghost.org)

