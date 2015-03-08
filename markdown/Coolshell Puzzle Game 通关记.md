[ Home ](http://blog.cee.moe) [ Subscribe ](http://blog.cee.moe/rss/)

#  Coolshell Puzzle Game 通关记

21 December 2014

某日，看到 [ zyq女神 ](http://quantize.me/) 在群里发了个链接说：有没有人玩这个游戏啊...

于是...就手贱 [ 点进去了 ](http://fun.coolshell.cn) 。

（ ** 本文涉及答案，如果要看解答请主动屏蔽LZ ** ）

* * *

###  0x00 Fuck your brain

正如其名：Brainfuck。给了一段brainfuck的代码放在解释器里跑一下就得到了下一关的答案。

####  answer: welcome.html

####  keypoint:

  * [ brainfuck ](http://en.wikipedia.org/wiki/Brainfuck)

* * *

###  0x01 Multiply

乘法，求得 ` X * Y ` 就可以得到答案了。

算 ` X ` ：2, 3, 6, 18, 108, ?（1944， ` a(n) = a(n-1) * a(n-2) ` ）

算 ` Y ` ：生命、宇宙以及任何事情的终极答案——42

算 ` X * Y ` ； 1944 * 42 = 81648

####  answer: 81648.html

####  keypoint:

  * [ the answer to life, the universe and everything ](https://www.google.com.hk/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#ie=UTF-8&q=the%20answer%20to%20life%2C%20the%20universe%20and%20everything&sourceid=chrome-psyapi2) （Google Calculator Knows，出自道格拉斯·亚当斯的小说《银河系漫游指南》，值得一读哦） 

* * *

###  0x02 Keyboard

点开图是一个Wiki，讲的是Dvorak Simplified Keyboard。意思就是把下面的密文按照键盘替换。得到解密后的程序：

> main() { printf(&unix["\021%six\012\0"],(unix)["have"]+"fun"-0x60);}

Google一下：原来是C语言混乱大赛的代码。详细见keypoint，这里给出答案。

####  answer: unix.html

####  keypoint:

  * [ Dvorak Simplified Keyboard ](http://en.wikipedia.org/wiki/Dvorak_Simplified_Keyboard)
  * [ About the code ](http://blog.chinaunix.net/uid-13701930-id-336417.html)

* * *

###  0x03 QR Code

扫一下二维码，得到 ` a-z ` 的转换表 ` [abcdefghijklmnopqrstuvwxyz] <=>
[pvwdgazxubqfsnrhocitlkeymj] ` 。替换下面的乱码得到问题：

> Where there is a shell, there is a way. I expect you use the shell command
to solve this problem, now, please try using the rot13 of "shell" to enter
next level.

用Rot13加密方法替换 ` shell ` 这个单词。嘛继续Wiki。

####  answer: furyy.html

####  keypoint:

  * [ ROT13 ](http://en.wikipedia.org/wiki/Rot13)

* * *

###  0x04 Cat

（这一关卡了很久，我都快绝望的时候在v2ex上看到了用Sublime正则查找，豁然开朗）

题目中给的提示有两个，一个是标题很大的 ` Palindrome ` （回文），还有一个是 ` The answer has been lost in
the source ` 。View Source之后发现了注释掉的代码，800行。尝试用 ` cat ` 解密后发现了新的提示： ` You need
to find the pattern of "cat" ` ，告诉我们要看图片左边的那个8行的特征：

  1. 必须是Palindrome； 
  2. 一个数字，一个大写，一个小写，提取出的都是小写字母。 

打开Sublime写个正则： ` ([A-Z])([0-9])[a-z](\2)(\1)|([0-9])([A-Z])[a-z](\6)(\5) `
，得到了符合条件的表达式：

> E1v1E  
4FaF4  
9XrX9  
O3i3O  
0MaM0  
4GbG4  
M5l5M  
0WeW0  
Y0s0Y

取出小写字母。

####  answer: variables.html

####  keypoint:

  * [ Regex Expression ](http://deerchao.net/tutorials/regex/regex.htm)

* * *

###  0x05 Variables

Keep Going，点开图之后有新的网页，数字是32722。替换2014为32722，又出现了新的数字。猜测和以前的贴吧那种链接差不多，写个js搞定。

####  answer: tree.html

* * *

###  0x06 Tree

给了张图，写了一棵树的中序和后序遍历。 <del> 还好电脑里有大二上学期数据结构的求先序的C++程序就跑了一下。 </del>
得到树之后先序遍历得到数的深度最长的路径 ` zWp8LGn01wxJ7 ` 。下面有一串小字 ` openssl enc -aes-128-cbc -a
-d -pass pass:??? ` 。经过 [ Ricter菊苣 ](http://ricter.me) 指点，把 `
U2FsdGVkX1+gxunKbemS2193vhGGQ1Y8pc5gPegMAcg= ` 放入 ` test.in ` 中再用terminal执行： `
openssl enc -aes-128-cbc -a -d -pass pass:zWp8LGn01wxJ7 -in test.in -out
test.out ` 得到答案。

####  answer: nqueens.html

####  keypoint:

  * [ Tree Traversal ](http://en.wikipedia.org/wiki/Tree_traversal)
  * [ OpenSSL ](http://blog.csdn.net/as3luyuan123/article/details/14411039)

* * *

###  0x07 N Queens

给了个 ` code = 57138642 ` 发现就是图上的解答。提示要我们使用⑨皇后问题生成这个 ` code `
。写个python暴力跑一下（python技术烂到家）：

得到最后结果。

####  answer: 953172864.html

####  keypoint:

  * [ N皇后问题 ](http://blog.dayanjia.com/2012/10/solve-n-queen-puzzle-using-python-generator/)

* * *

###  0x08 Excel Column

26进制表示。求得 ` COOLSHELL = 3×(26^8)+15×(26^7)+15×(26^6)+12×(26^5)+19×(26^4)+8×(26
^3)+5×(26^2)+12×(26^1)+12 = 751743486376 ` 和 ` SHELL =
19×(26^4)+8×(26^3)+5×(26^2)+12×(26^1)+12 = 8826856 ` 。两个除一下得到答案 ` 85165 `
。结果进了这个网页还让我们再用字符表示，也是败了。

####  answer: duyo.html

####  keypoint:

  * 数的N进制表示 

* * *

###  0x09 Fraternal Organisation

Google搜索了两张图，原来是 ` Pigpen Cipher ` 。Wiki上说明这是一种加密方式（ <del> zxw大神说他给妹子写过情书
</del> ）。根据下面的一张图得到最后的破解密文。

####  answer: helloworld.html

####  keypoint:

  * [ Pigpen Cipher ](http://en.wikipedia.org/wiki/Pigpen_Cipher)

* * *

###  0x0a Congratulations!

Update：耗子说还有个迷。于是继续打开这个网页把图片down下来之后vim打开后发现了可以是一个rar <del> （感觉就是个种子） </del>
。解包之后有个txt得到了最终的答案。

####  answer: DennisRitchie.html

* * *

恭喜并不代表结束。从这次小小的活动中又一次知道了自己是如此的渣逼。(╯‵□′)╯︵┻━┻

最后的Ranking是37，前后也做了快5个小时。卡在cat那一关太久了=。=

Wiki是个好东西，也要善于搜索。更重要的还是要平时积累啊~（摔）

[ Cee's Picture  ](/author/cee/)

####  [ Cee ](/author/cee/)

Read [ more posts ](/author/cee/) by this author.

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

####  Share this post

[ Twitter  ](https://twitter.com/share?text=Coolshell%20Puzzle%20Game%20%E9%80
%9A%E5%85%B3%E8%AE%B0&url=http://blog.cee.moe/coolshell-puzzle-game-tong-guan-
ji/) [ Facebook
](https://www.facebook.com/sharer/sharer.php?u=http://blog.cee.moe/coolshell-
puzzle-game-tong-guan-ji/) [ Google+
](https://plus.google.com/share?url=http://blog.cee.moe/coolshell-puzzle-game-
tong-guan-ji/) [ Cee's Home ](http://blog.cee.moe) © 2015  Proudly published
with [ Ghost ](https://ghost.org)

