  * [ Mind Hacks 的含义 ](http://mindhacks.cn/about/)
  * [ 前世档案 | C++的罗浮宫 ](http://mindhacks.cn/former-life-of-mindhacks/)
  * [ 所有文章 ](http://mindhacks.cn/archives/)
  * [ TopLanguage 讨论组 ](http://mindhacks.cn/about-toplanguage/)
  * [ 价值博客们 ](http://mindhacks.cn/friend-links/)

[ 刘未鹏 | Mind Hacks ](http://mindhacks.cn) 思维改变生活

  * [ 学习方法 ](http://mindhacks.cn/topics/learning-method/)
  * [ 思维改变生活 ](http://mindhacks.cn/topics/mind/)
  * [ 算法 ](http://mindhacks.cn/topics/algorithms/)
  * [ 计算机科学 ](http://mindhacks.cn/topics/computer-science/)
  * [ 数学 ](http://mindhacks.cn/topics/math/)
  * [ 机器学习与人工智能 ](http://mindhacks.cn/topics/machine-learning/)
  * [ 编程 ](http://mindhacks.cn/topics/programming/)

  * [ RSS Feed ](http://mindhacks.cn/feed/)

#  [ Failing To See the Big Picture – Mistakes we make when learning
programming ](http://mindhacks.cn/2008/03/03/failing-to-see-the-big-picture/)

By  [ 刘未鹏 ](http://mindhacks.cn/author/pongba/)

–  March 3, 2008  ** Posted in: ** [ 学习方法 ](http://mindhacks.cn/topics
/learning-method/)

Let’s start with an obvious fact:

> ** The Inconvenient Human Nature, #1  
** _ People are inherently more easily attracted by “interesting” (as opposed to “mundane”) things. (We will define “interesting” in the later parts) _

What can we derive from this simple axiom?

A lot of things. But since we’re talking about learning programming, we shall
focus mainly on the implications it has for how we learn programming.

** Programming, the interesting and the mundane **

** The Interesting **

What was the first thing that struck you when you first learned how to
program? Wasn’t it the simple fact that you could order a computer to do stuff
by simply typing a bunch of characters (thinking of the “hello world” program
that we all have written)? But what happened then? You (hopefully) would learn
the things that happened under the hood and drove your programs, which leads
us to the first point:

> _ If it’s something under the hood, it’s interesting (therefore attracts
people).  _

People are always curious about the forces behind the phenomenons in nature
since the dawn of human civilization. There’s a need for people to seek the
reason why something happened. We call it the desire to understand.

After you’ve learned how to hack up a program, and the reason why your program
works all the way down to the bit level. What, then, would be the next thing
you do? You write programs, and in so doing discover more and more features of
your programming language, which means you get more and more familiar with
your language and you start to notice the sorts of things it can do
conveniently and those it can’t. That when language tricks step into the
picture. Language tricks are interesting in that they enable you to do
something you usually can’t do. Human beings are born problem solvers, we like
solving problems just as much as we like seek out the deep reasons why stuff
works. But sadly we’re also adept problem creators.

In program language sense, the problems of which we seek for solutions are
also the ones created by us. For example, there has recently been a remarked
theory suggesting that design patterns are missing language features. First we
create a language that – of course – has some drawbacks which we then use
language tricks (such as design patterns) to overcome, but as time goes by, we
would get to a point where all those kinds of patterns aren’t wealth anymore
but instead turn into pure burdens, which is when we build them into the
language. However, by solving the problems created by the previous language,
we often create our own new problems. For example, there’s always this “DSL &
GPL” (where GPL means general-purpose language) debate. On the one hand,
building domain specific features into a language has the obvious advantage
that it would be a lot more convenient for programmers to use when faced with
domain-specific programming tasks, but on the other hand it would also limit
the usage of the language, thus making the whole set of runtime system only
accessable by itself (yeah, of course I know there’s inter-language operation,
but that’s still another additional step don’t you think?). As to GPLs, the
main advantage of them is to use a single runtime system to serve
theoretically unlimited application areas. This isn’t without compromises,
either. The main compromise is that when faced with domain-specific problems,
a GPL only makes for a second-class language. That’s why Microsoft “invented”
the CLR system; that’s also why Martin Fowler started advocating the so-called
[ Language-Oriented Programming
](http://www.martinfowler.com/articles/languageWorkbench.html) .

So, to sum up, we created all kinds of language abstractions to make
programming easier. But, as it always has been, by solving one problem
(programming convenience) we create other ones. Our language will no doubt
have many drawbacks, that is, ones that make certain programming tasks harder
to do. That’s where language tricks step in and  [ steal our focuses
](http://www.codinghorror.com/blog/archives/001011.html) (I guess you all have
a huge stack of language “techniques” books, right?). If you don’t understand
what I’m saying, please take a look at any suggested “classic C++ books” list.

However, why on earth do we have to learn those tricks? We don’t, actually.
But we tend to. Because:

> _ We’re born problem solvers, we like solving problems; problems are
interesting, even if they’re created by ourselves.  _

So, what happens after that? We learn new “techniques”. By “techniques”, I
mean literally dozens of libraries, frameworks, APIs, and several new
languages dubbed “the next big thing” (whether or not they say that
explicitly). Again, why do we have to learn these? We don’t, really. We can
learn them on an as-needed basis. One of the main reasons we’re attracted to
them is because:

> _ We like new stuff. If it’s new, it’s interesting.  _

Another reason is that we like to ** jump on the bandwagon ** .

> ** The Inconvenient Human Nature, #2  
_ Jumping-on-the-bandwagon _ ** _ : If everyone is doing it, so should I. _ **
**

Not only do corporations use this strategy to induce us, we do it ourselves,
that is, we create our own bandwagon. When some new language or technique
comes out, we often get so excited that we blind ourselves to the problems it
has; we’re blinded by the halo created by its featured features. We often, as
a result, regard it as a panacea. We start eagerly to learn it. Programmers
are smart animals, probably too smart. They always yearn for new stuff (check
out what’s been discussed on the major programming forums and you will know
what I’m saying), just like beasts hungering for blood. You walk around on the
programming forums, you see thousands and thousands of technical details; it’s
an endless job learning all those, but programmers love that.  [
![](http://lobelia.douban.com/mpic/s2652990.jpg)
](http://www.douban.com/subject/1417047/)

** The Mundane **

On the other hand, what do (most) programmers not love? Principles, be it
coding principles in the small (e.g. “always give variables meaningful names”)
or development principles in the large (e.g. “write  tests before you write
the actual code”). They’re just dull. They’re not tricky; they’re not weird;
they’re not challenging. We can’t show the world how smart we are by complying
with some silly rules. What we do love is writing some insanely tricky code or
[ ![](http://lobelia.douban.com/mpic/s1445893.jpg)
](http://www.douban.com/subject/1432042/) using some dazzling patterns that
nobody else has a clue what we’re doing (or everybody knows what we’re doing).

Right?

** The Self-handicapped Programmers **

On the one hand, programmers are learning too fast, and learning too much (see
above). On the other hand, there’re always times when we need to learn new
things.  [ ![](http://lobelia.douban.com/mpic/s1463770.jpg)
](http://www.douban.com/subject/1451622/)

There actually are several kinds of human natures that can hinder one from
learning new things. The  one related to what we’re getting at is:

> ** The Inconvenient Human Nature, #3  
_ Self-serving bias _ ** _ : We love what we’re doing, or who we’re; we
dislike all the things that counter it. _

Admit it or not, we’ve all been through this. After we get familiar enough
with some language or  [ ![](http://lobelia.douban.com/mpic/s2547828.jpg)
](http://www.douban.com/subject/1229948/) platform, the self-serving bias will
start to affect what we like (and learn) and what we dislike (and won’t
learn). Language debates are all too common in programming community. By
blinding ourselves to the disadvantages of our languages or platforms and to
the advantages of other languages or platforms, we limit our access to new
techniques and ideas. In a sense, we limit our potentials.

** Conclusion **

Most of the times, we’re learning just a little too much. We’re attracted to
interesting stuff like a  [ ![](http://lobelia.douban.com/mpic/s2595001.jpg)
](http://www.douban.com/subject/1419359/) moth to a flame. Or oftentimes we
just learn what everybody else around us is learning or what we’re  told to
learn, not know why we should learn it. Fact is, however, after we’ve grasped
the essential knowledge, other stuff can just be learned on an as-needed
basis. Don’t fall into technical details unless they’re essential or needed
right away. There’s just unlimited number of details to follow in this area;
you can put your time to something more useful (learning the essentials,
learning the ideas, or even just another language).

On the other hand, however, we’re learning too little. We blind ourselves to
the really important  [ ![](http://lobelia.douban.com/mpic/s1642259.jpg)
](http://www.douban.com/subject/1771049/) subjects just because they look
dull. Tests? That’s like wearing condoms before having sex. Refactoring? Why
do we have to do something that’s not going to generate new functionalities
and not  shinny at all? Defensive Programming? No thanks, I know what I’m
doing here. API Design? Oh-Man, it’s just too darn hard to consider how
somebody else would be using my code when I’m writing the splendid
implementations. New Languages? What… R U saying that mine is not good enough?
Did U NOT see how I can bend the language to do whatever the heck I want it to
do?

** Tags: ** [ 学习方法 ](http://mindhacks.cn/tags/%e5%ad%a6%e4%b9%a0%e6%96%b9%e6%b3%95/) , [ 编程 ](http://mindhacks.cn/tags/%e7%bc%96%e7%a8%8b/)

[ ](http://mindhacks.cn/author/pongba/)

####  About 刘未鹏

  1. Pingback: [ 使用联想式方法解决问题 | Project Maple ](http://www.lovemaple.info/blog/2011/07/solve-problems-by-making-connections/)

  2. Pingback: [ 0aish » 翻墙种种（七）：使用联想式方法解决问题 ](http://0aish.inwtrade.com/articles/%e7%bf%bb%e5%a2%99%e7%a7%8d%e7%a7%8d%ef%bc%88%e4%b8%83%ef%bc%89%ef%bc%9a%e4%bd%bf%e7%94%a8%e8%81%94%e6%83%b3%e5%bc%8f%e6%96%b9%e6%b3%95%e8%a7%a3%e5%86%b3%e9%97%ae%e9)

  3. [ IT_xiao小巫 ](http://weibo.com/wulmaycry) on [ November 2, 2014 at 10:12 pm  ](http://mindhacks.cn/2008/03/03/failing-to-see-the-big-picture/comment-page-1/#comment-33679) said: 

表示英文渣渣

  * #####  关于 

如果你对我的文章感兴趣，那么 ** 很可能你也对我平时的阅读感兴趣 ** ，以下是一些你可以参考或订阅的资源：

    1. [ 我在豆瓣 ](http://www.douban.com/people/pongba/) 上的豆列列举了一些看过的好书： [ [只读经典]思维改变生活 ](http://www.douban.com/doulist/46003/) | [ [只读经典]思考的技术与艺术 ](http://www.douban.com/doulist/127649/) | [ 决策与判断 ](http://www.douban.com/doulist/197706/) | [ 机器学习与人工智能书籍资源导引 ](http://www.douban.com/doulist/176513/)
我翻译的书：

    1. [ 《Imperfect C++ 中文版》 ](http://book.douban.com/subject/1470838/)
    2. [ 《Exceptional C++ Style 中文版》 ](http://book.douban.com/subject/1470842/)
    3. [ 《修改代码的艺术》 ](http://book.douban.com/subject/2248759/)
我写的书：

    1. [ ![](http://img3.douban.com/mpic/s6586365.jpg) ](http://book.douban.com/subject/6709809/)

  * #####  被阅读得最多的 

    * [ 怎样花两年时间去面试一个人 ](http://mindhacks.cn/2011/11/04/how-to-interview-a-person-for-two-years/) \- 282,579 views 
    * [ 数学之美番外篇：平凡而又神奇的贝叶斯方法 ](http://mindhacks.cn/2008/09/21/the-magical-bayesian-method/) \- 272,693 views 
    * [ [BetterExplained]为什么你应该（从现在开始就）写博客 ](http://mindhacks.cn/2009/02/15/why-you-should-start-blogging-now/) \- 244,807 views 
    * [ 暗时间 ](http://mindhacks.cn/2009/12/20/dark-time/) \- 225,722 views 
    * [ 逃出你的肖申克（二）：仁者见仁智者见智？从视觉错觉到偏见 ](http://mindhacks.cn/2009/03/15/preconception-explained/) \- 212,330 views 
    * [ 我在南大的七年 ](http://mindhacks.cn/2009/05/17/seven-years-in-nju/) \- 206,471 views 
    * [ [BetterExplained]如何有效地记忆与学习 ](http://mindhacks.cn/2009/03/28/effective-learning-and-memorization/) \- 202,213 views 
    * [ 逃出你的肖申克（一）：为什么一定要亲身经历了之后才能明白？ ](http://mindhacks.cn/2009/01/18/escape-from-your-shawshank-part1/) \- 172,289 views 
    * [ 逃出你的肖申克（三）：遇见20万年前的自己 ](http://mindhacks.cn/2010/03/18/escape-from-your-shawshank-part3/) \- 148,821 views 
    * [ [BetterExplained]书写是为了更好的思考 ](http://mindhacks.cn/2009/02/09/writing-is-better-thinking/) \- 137,125 views 
  * #####  我的微博 

  * #####  你可能也会喜欢以下文章 

    * [ 方法论、方法论——程序员的阿喀琉斯之踵 ](http://mindhacks.cn/2008/10/29/methodology-for-programmers/) (32) 
    * [ C++11（及现代C++风格）和快速迭代式开发 ](http://mindhacks.cn/2012/08/27/modern-cpp-practices/) (138) 
    * [ 知其所以然（续） ](http://mindhacks.cn/2010/11/14/the-importance-of-knowing-why-part2/) (69) 
    * [ 暗时间 ](http://mindhacks.cn/2009/12/20/dark-time/) (223) 
    * [ 不是书评 ：《我是一只IT小小鸟》 ](http://mindhacks.cn/2009/10/05/im-a-tiny-bird-book-review/) (87) 
    * [ [BetterExplained]遇到问题为什么应该自己动手 ](http://mindhacks.cn/2009/07/06/why-you-should-do-it-yourself/) (81) 
    * [ 我在南大的七年 ](http://mindhacks.cn/2009/05/17/seven-years-in-nju/) (193) 
    * [ [BetterExplained]如何有效地记忆与学习 ](http://mindhacks.cn/2009/03/28/effective-learning-and-memorization/) (149) 
    * [ 编程的首要原则(s)是什么？ ](http://mindhacks.cn/2009/03/09/first-principles-of-programming/) (60) 
    * [ [BetterExplained]为什么你应该（从现在开始就）写博客 ](http://mindhacks.cn/2009/02/15/why-you-should-start-blogging-now/) (326) 

  *   * [ ** About Arras WordPress Theme ** ](http://www.arrastheme.com/)

Copyright 刘未鹏 | Mind Hacks. All Rights Reserved. [ 苏ICP备09004067号
](http://www.miibeian.gov.cn/) . Powered by [ Wordpress
](http://wordpress.org/) . Using [ Arras Theme ](http://www.arrastheme.com/) .

  *[
         March 3, 2008
        ]: 2008-03-03T15:42:00+00:00

