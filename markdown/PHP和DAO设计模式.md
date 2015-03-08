#  PHP和DAO设计模式

[ Yuguo ](http://yuguo.us) 2012年 07月 11日

DAO（Data Access Object，数据存取对象）设计模式对于从PHP和MySQL教程一步步走过来的人来说是一个新的概念。我们的编码中的一大部分就
是用来解决数据（库）获取和操作。随着大数据的来临，和数据分析方法的进步，数据操作越来越重要。

DAO设计模式旨在解决两个问题：重复、和数据源抽象。

重复：在程序中我们一般会写一句SQL语句来在数据库中创造一个条目。之后又写一个SQL语句来更新某一栏。不断地重复写SQL既无聊又不优雅。

事实上，我们如果用DAO设计模式来实现的话，一个数据存取对象会用来封装SQL的创建过程，减少复杂性和重复性。它应该不用区分具体的表结构和数据库引擎。

数据源抽象：另一个优势就是数据层的抽象。现在你的逻辑代码不用再担心数据库引擎和表的关系。调用他们的公共方法可以返回任意类型的数据，无论底层需要怎样的SQL。

但是程序员不要过度设计DAO。简化DAO的设计就好，不要增加不需要的功能。

在github上有一些使用了DAO模式的Repo，有的简单，有的过度设计了。简单地说，实现上我们需要一个抽象类（baseDAO）和一些继承了它的实体类（比如
userDAO）。

在baseDAO中需要定义两个公共函数：fetch和update，分别获得一行数据和更新一个数组。还定义一些私有的函数比如链接数据库，还有私有的数据比如当前
表的主键和表明。

在userDAO继承baseDAO的时候，需要声明私有数据比如主键和表明，然后在baseDAO的fetch和update的基础上自定义一些新的公共函数。这样
做的好处是把生成SQL的工作全部封装在两个抽象类的公共函数之中，userDAO以及其他的更多DAO只是调用这一函数而已。

需要更多的数据存取操作的时候，我们就基于baseDAO新建一个userDAO或者itemDAO，然后实例化这一对象，这就是DAO设计模式。

[ 那么你想制作CSS3字体吗？ → ](/weblog/so-do-you-want-to-make-a-css3-font/) [ ←
现在是出版社做移动APP的最好时机 ](/weblog/the-best-time-for-press-to-build-web-app/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

