[ Home ](http://blog.cee.moe) [ Subscribe ](http://blog.cee.moe/rss/)

#  Dear Assembly(1)

26 July 2014

苦逼的暑假开始了。

在......

###  [ lcb大神 ](http://www.binarythink.net/)

（我特意加了链接！）

的推荐下，毫不犹豫地在六月份就选了Coursera上的CSAPP(Computer Systems: A Programmer's
Perspective)。一方面正好自己操作系统也学得很烂，所以趁这个暑假充实一下自己的暑假生活；另一方面，这CSAPP的课机会难得，不容错过啊。

这篇文章的话，主要还是讲一下Lab2的拆炸弹作业。俗话说：

> DDL是第一生产力！

赶在DDL前两天，晚上花了5个小时终于做完了！

本文分上下两篇，主要介绍一下Assembly、gdb的使用，还有拆炸弹的解题过程/w\

* * *

###  Phase_1

反编译phase_1的代码 ` disassemble phase_1 ` ，得到：

除去1，7，8行，关注剩下的2到6行。

程序调用了 ` strings_not_equal() ` 函数，比较输入字符串与 ` 0x401af8 ` 指向的字符串是否相等。使用 ` x /sb
0x401af8 ` 查看 ` 0x401af8 ` 指向的字符串，就得到了第一个答案：

> Science isn't about why, it's about why not?

phase_1结束！

###  Phase_2

进入phase_2， ` disassemble phase_2 ` 得到：

第七行调用 ` read_six_numbers ` 函数， ` disassemble read_six_numbers ` ：

` read_six_numbers ` 调用了 ` sscanf ` ，格式字符串由地址为 ` 0x401eb2 ` 中的格式解析。查看 `
0x401eb2 ` 地址中的格式字符串，使用 ` x /sb 0x401eb2 ` ：

> 0x401eb2: "%d %d %d %d %d %d"

回到phase _ 2中，我们要知道读完六个数之后做了什么，继续看第8行开始的代码。第8行让 ` rbp = rsp ` 并且注意到第⑨行中 ` r13 `
寄存器保存了 ` rsp + 12 ` （即 ` rbp + 12 ` ）的地址，以及第12、13行的 ` eax ` 取出了 ` rbp + 12 `
的数并且用 ` eax ` 和 ` rbp ` 两个寄存器之间的书比较是否相等。之后的第17行， ` rbp = rbp + 4 ` ，让指针往后走一个 `
int ` 的大小。看到这里也就知道了phase _ 2的含义：

> 输入数组 ` a[6] ` 后，比较是否是一个长度为3的循环数组。即是否满足 ` a[0] = a[3] ` ， ` a[1] = a[4] ` 和 `
a[2] = a[5] `

输入符合条件的六个数即可~难度也不是很大(｢･ω･)｢

###  Phase_3

开始进入比较有挑战性的phase_3，同样使用 ` disassenmble phase_3 ` ：

比之前更长了，不是么？

观察一下函数的特征，尤其是14-27行， ` Switch/Case ` 的跳转表，非常的明显！

查看 ` sscanf ` 的格式字符串， ` x /sb 0x401ebe ` ：

> 0x401ebe: "%d %d"

输入两个数，第一个数用于 ` Switch/Case ` 分支判断，第二个数字则用于和 ` eax ` 的比较。注意到11行的 ` cmpl `
（每次都是你！）判断了 ` rsp + 12 ` 中的数是否大于7，也就是输入的第一个数是否大于7（ ` default `
分支）：如果大于就引爆了炸弹，否则就进入不同的 ` case ` 。通过计算不同的组合我们可以很轻松的得到这道题的不同的7个解（一行一个解）：

> 0 535

>

> 1 926

>

> 2 214

>

> 3 339

>

> 4 119

>

> 5 352

>

> 6 919

>

> 7 412

当屏幕显示 ` Phase 3 cleared! ` 的时候，我们已经解决了一半的问题了！

###  Phase_4

Move on, 进入到phase_4， ` disassemble phase_4 ` ：

第3行查看 ` sscanf ` 的格式字符串， ` x /sb 0x401ec1 ` ：

> 0x401ec1: "%d"

即输入一个数。将这个输入的数放入 ` edi ` 中调用了函数 ` func4 ` 。 ` func4 ` 的代码如下：

7-13行的主要说明了递归函数目的 ` f(x) = f(x-1) + f(x-2) ` ，边际条件在第5和6行 ` f(1) = 1 `
（Fibbonacci数列)。

回到原函数，14行的 ` cmp ` 使用了返回值 ` eax ` 和 ` 0x37 = 55 ` 比较，题目意图也很明显了： ` n ` 等于几时，有 `
f(n) = 55 ` 。答案就是：

> <del> ⑨（这么写当然是错的） </del>

>

> 9

###  Phase_5

同样地先观察格式字符串， ` x /sb 0x401ebe ` ：

> 0x401ebe: "%d %d"

格式输入正确后跳转到第10行执行函数，这里一行一行解释。

第10行， ` eax ` 存入地址为 ` rsp + 12 ` 中的数，也就是第二个参数。11-12行用这个数和 ` 0xf `
做了与操作，取出了最后两位并重新保存到 ` rsp + 12 ` 中。13行判断了这个数是不是 ` 0xf `
，若是就引爆了炸弹，否则接下来进入循环。15-16行的两个计数器 ` ecx ` 和 ` edx ` 清零。

17到22行由 ` jne ` 判断出这是一个循环。17行的作用让 ` edx = edx + 1 ` ，马上18行 ` cltq ` 对 ` eax `
进行符号扩展，在19行加载 ` rax * 4 + 0x401ba0 ` 这个地址中的数到 ` eax ` 中。20行 ` ecx ` 作为累加器加上 `
eax ` 中的数。21行依旧判断 ` eax ` 这个数是不是 ` 0xf ` ，不是则进行循环。

比较难理解的是19行 ` eax = *(rax * 4 + 0x401ba0) ` 即取出了起始地址为 ` 0x401ba0 ` 的数组中序号为 `
eax ` 的数放入 ` eax ` 中。根据21行判断数组大小，用 ` x /16wd 0x401ba0 ` 查看一下 ` 0x401ba0 `
开始的数组：

> 0x401ba0  : 10 2 14 7

>

> 0x401bb0  : 8 12 15 11

>

> 0x401bc0  : 0 4 1 13

>

> 0x401bd0  : 3 9 6 5

整理一下：

> 10 2 14 7 8 12 15 11 0 4 1 13 3 9 6 5

跳出循环，第24行，判断 ` edx ` 即函数的循环次数是不是 ` 0xc = 12 ` ；第26行判断了第二个参数是否等于 ` ecx `
中的数。phase_5也就被我们转化成了一道数组倒推问题。计算后得到答案：

> 7 93

至此，作业要求的5个函数已经完成！（撒花）

* * *

###  What's Next

> Phase 6, Secret Phase还有Gdb Guide见 [ 下一篇 ](https://blog.cee.moe/dear-
assembly-2) /w\

[ Cee's Picture  ](/author/cee/)

####  [ Cee ](/author/cee/)

Read [ more posts ](/author/cee/) by this author.

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

####  Share this post

[ Twitter
](https://twitter.com/share?text=Dear%20Assembly\(1\)&url=http://blog.cee.moe
/dear-assembly-1/) [ Facebook
](https://www.facebook.com/sharer/sharer.php?u=http://blog.cee.moe/dear-
assembly-1/) [ Google+
](https://plus.google.com/share?url=http://blog.cee.moe/dear-assembly-1/) [
Cee's Home ](http://blog.cee.moe) © 2015  Proudly published with [ Ghost
](https://ghost.org)

