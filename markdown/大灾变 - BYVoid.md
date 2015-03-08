  * [ ](https://www.facebook.com/byvoid)
  * [ ](https://twitter.com/byvoid)
  * [ ](https://plus.google.com/+CarboKuo)
  * [ ](https://www.linkedin.com/in/byvoid)
  * [ ](https://github.com/BYVoid)
  * [ ](http://www.renren.com/byvoid)
  * [ ](http://weibo.com/byvoid)
  * [ ](http://www.douban.com/people/byvoid/)
  * [ ](/feed)

#  [ ![](/images/logo.png) ](/)

  * [ 網誌 ](/blog)
  * [ 列表 ](/blog/list)
  * [ 標籤 ](/blog/tag)
  * [ 項目 ](/project)
  * [ 關於  ](/about)
    * [ Resume ](/about/resume)
    * [ Logo ](/about/logo)
    * [ Slides ](/slides/)
  * [ 聯繫 ](/contact)

![](/images/banner-bg-0.jpg)

三月  ** 29 ** 2014

  * 作者:  byvoid 
  * 閱讀: 4452 
  *     * [ 競賽題解 ](/blog/tag/競賽題解)
    * [ NOI ](/blog/tag/NOI)
    * [ 國家集訓隊 ](/blog/tag/國家集訓隊)
    * [ 冬令營 ](/blog/tag/冬令營)
    * [ 魔獸世界 ](/blog/tag/魔獸世界)
    * [ 單調性 ](/blog/tag/單調性)
    * [ 計算幾何 ](/blog/tag/計算幾何)
    * [ 半平面交 ](/blog/tag/半平面交)
    * [ 二分答案 ](/blog/tag/二分答案)

#  [ 大灾变 ](/blog/cataclysm-problem)

大灾变是我在2009年末的时候在NOI国家集训队冬令营出的题，题目背景是魔兽世界。当年出题的时候刚好听到魔兽世界第三个资料片「大灾变」的传闻，所以就以此为背
景了，之前我还出过三次魔兽世界模拟赛的题。今天回头重新来看，发现题解和数据的质量还是很高的，所以决定发布出来。有趣的是，我还给题解的每个算法起了一个名字，如
下表所示：

思路甲  |  欲窮千里目，更上一層樓  |  说明“站得越高，看得越远”的道理  
---|---|---  
算法一  |  行遠必自邇，登高必自卑  |  太高了要降低高度，说明二分的原理  
思路乙  |  不識廬山眞面目，祇緣身在此山中  |  说明可视区域在山脉上方  
算法二  |  表獨立兮山之上，云容容兮而在下  |  在山脉上空的下凸线上扫描最低点，比喻为云层  
算法三  |  刪繁就簡三秋樹，領異標新二月花  |  用“删繁就简”概括维护凸线的堆栈（单调队列）  
算法四  |  近水樓臺先得月，向陽花木易逢春  |  比喻制造单调性的优势  
思路丙  |  會當淩絕頂，一覽眾山小  |  猜想到山坡交线最高点就能看见山脉  
算法五  |  不畏浮雲遮望眼，自緣身在最高層  |  在上升线和下降线的最高点，就能一览山脉全貌  
  
##  资源链接

  * [ 问题解析 ](https://www.byvoid.com/upload/blog/cataclysm/cataclysm-solution.pdf)
  * [ 讲稿 ](https://www.byvoid.com/upload/blog/cataclysm/cataclysm-speech.pptx)
  * [ 测试数据 ](https://www.byvoid.com/upload/blog/cataclysm/cataclysm-data.zip)
  * [ 数据可视化程序 ](https://www.byvoid.com/upload/blog/cataclysm/cataclysm-GUI.zip)
  * 在线评测 
    * [ COGS ](http://cojs.tk/cogs/problem/problem.php?pid=403)
    * [ 清澄 ](http://www.tsinsen.com/A1215)

##  问题描述

艾泽拉斯世界经历一场亘古未有的地震过后，大地和海洋被完全撕裂，旧大陆残缺不全。联盟和部落各种族的居民们被迫离开了世代居住的家园，来寻找新的生存空间。原本平坦
的陆地上现在隆起了一座座山峰，暴风城的人类开始在 ** 艾尔文山脉 ** 重建家园。他们决定在山脉之中建造一座 ** 瞭望塔 ** 和一个魔法 ** 浮空岛
** ，以便于在瞭望塔和浮空岛上可以俯视艾尔文山脉的全貌。

艾尔文山脉被描述为一个折线，给定每个点的坐标（横纵坐标均不小于0），按照横坐标从小到大顺次连接起来就是就是山脉的折线。折线上所有点的横坐标均不相同。如果一个
位置与山脉任何一点的连线均不被挡住（但可以与地面相切），那么就说这一点可以望到整个艾尔文山脉。瞭望塔的塔身不会挡住视线，而且瞭望塔和浮空岛可以建造在同一位置
。为节省建筑材料，瞭望塔塔身的高度必须尽量小，即从塔顶到塔底的距离尽量小，瞭望塔可以建在山坡上。由于气候因素，浮空岛应建立在海拔尽量低的位置（甚至可以建在地
面上），海平面高度为0。如果有多个位置均满足条件，则选择横坐标最小的那个。瞭望塔和浮空岛横坐标范围应在艾尔文山脉横坐标范围之内。给定艾尔文山脉，请你求出瞭望
塔和浮空岛的位置。

###  输入文件

  * 第 ` 1 ` 行，一个整数 ` N ` ，表示描述艾尔文山脉的折线的顶点数。 
  * 第 ` 2-N+1 ` 行，每行两个整数， ` xi, yi ` 表示折线上点的坐标。 

###  输出文件

  * 第1行，两个保留3位小数的浮点数 ` x1, y1 ` ，表示瞭望塔顶端的坐标。 
  * 第2行，两个保留3位小数的浮点数 ` x2, y2 ` ，表示浮空岛的坐标。 

###  输入样例

    
    
    6
    2 2
    6 1
    8 6
    10 3
    16 5
    20 2

###  输出样例

    
    
    8.00 11.00
    9.54 9.85

###  样例说明

样例中描述的艾尔文山脉各个顶点，按照横坐标顺序顺次连接后的折线如下图所示：

![艾尔文山脉](https://www.byvoid.com/upload/blog/cataclysm/cataclysm1.png)

瞭望塔应建造在山峰 ` (8, 6) ` 处，塔顶端为 ` (8, 11) ` ，高度为 ` 5 ` ，此时瞭望塔的高度最小。

![瞭望塔](https://www.byvoid.com/upload/blog/cataclysm/cataclysm2.png)

浮空岛建立在 ` (9.54, 9.85) ` 处，海拔高度最低。

![浮空岛](https://www.byvoid.com/upload/blog/cataclysm/cataclysm3.png)

###  问题限制

  * 时间限制2000 ms 
  * 内存限制128 MB 

###  数据规模

  * 40%的数据2<=N<=10 
  * 100%的数据2<=N<=1 000 000；0<=xi,yi<=5 000 000 

###  评分方式

对于每个测试点，如果输出的结果与答案文件完全相同，得该测试点100%的分数，如果仅有一行与答案文件相同，得该测试点50%的分数，否则得0%的分数。

##  相關日誌

  * [ NOI 2007 社交网络 ](/blog/noi-2007-network)
  * [ 最长公共子串问题的后缀数组解法 ](/blog/lcs-suffix-array)
  * [ Ubuntu 一周小记 ](/blog/ubuntu-week-note)
  * [ 线性规划与网络流24题-圆桌问题 ](/blog/lpf24-5)
  * [ NOI 2009 二叉查找树 ](/blog/noi-2009-treapmod)
  * [ 线性规划与网络流24题-最小路径覆盖问题 ](/blog/lpf24-3)
  * [ NOI 2002 调皮的小孩 ](/blog/noi-2002-child)
  * [ 线性规划与网络流24题-太空飞行计划问题 ](/blog/lpf24-2)
  * [ NOI 2009 变换序列 ](/blog/noi-2009-transform)
  * [ AHOI 上学路线 ](/blog/ahoi-route)

Search for:

####  語言

  * [ 原文 ](/blog/cataclysm-problem)
  * [ 正體中文 ](/zht/blog/cataclysm-problem)
  * [ 簡體中文 ](/zhs/blog/cataclysm-problem)
  * [ English ](/en/blog/cataclysm-problem)

####  分類

  * [ 中文與漢語 ](/blog/tag/中文與漢語)
  * [ 生活點滴 ](/blog/tag/生活點滴)
  * [ 稷下學宮 ](/blog/tag/稷下學宮)
  * [ 精華轉載 ](/blog/tag/精華轉載)
  * [ 自娛自樂 ](/blog/tag/自娛自樂)
  * [ 設計開發 ](/blog/tag/設計開發)
  * [ 點滴發現 ](/blog/tag/點滴發現)
  * [ 計算機科學 ](/blog/tag/計算機科學)
  * [ 競賽題解 ](/blog/tag/競賽題解)
  * [ 競賽歷程 ](/blog/tag/競賽歷程)
  * [ JavaScript ](/blog/tag/JavaScript)

####  最熱門

  * [ 有向图强连通分量的Tarjan算法 ](/blog/scc-tarjan) \- 158282 
  * [ 推薦一個神級輸入法——Rime ](/blog/recommend-rime) \- 119439 
  * [ C++ string 用法详解 ](/blog/cpp-string) \- 102630 
  * [ 避諱借字——“屌”、“肏”、“屄” ](/blog/bh-diao-cao) \- 75103 
  * [ 『古劍奇譚』劇情梗概 ](/blog/gjqt-plot) \- 60577 
  * [ 海外實習面試記 ](/blog/oversea-internship-interviews) \- 47494 
  * [ 這一年來 ](/blog/recent-one-year) \- 47077 
  * [ 各种字符串Hash函数比较 ](/blog/string-hash-compare) \- 46351 
  * [ 關於阿里巴巴面試結果信息泄漏的一點說明 ](/blog/alibaba-interview-feedback-clarification) \- 45353 
  * [ 图的割点、桥与双连通分支 ](/blog/biconnect) \- 44832 
  * [ HTTP协议头部与Keep-Alive模式详解 ](/blog/http-keep-alive-header) \- 42370 
  * [ 探寻C++最快的读取文件的方案 ](/blog/fast-readfile) \- 39696 
  * [ C++中fstream的用法 ](/blog/cpp-fstream) \- 34519 
  * [ 匈牙利算法 ](/blog/hungary) \- 34057 
  * [ 廣韻查詢系統 ](/blog/kyonh) \- 26676 
  * [ C/C++的64位整型 ](/blog/c-int64) \- 25991 
  * [ 勸君惜取少年時 ](/blog/treasure-young-days) \- 23896 
  * [ C语言字符串函数大全 ](/blog/c-string) \- 22034 
  * [ Vim 语法高亮与自动缩进 ](/blog/vim-syntex) \- 21597 
  * [ 最长公共子串问题的后缀数组解法 ](/blog/lcs-suffix-array) \- 21444 
  * [ 线性规划与网络流24题 解题报告 ](/blog/lpf24-solution) \- 21272 
  * [ NOIP2000-2007 全部题解 ](/blog/noip-allsolutions) \- 20789 
  * [ Linux下实现自动设置SSH代理 ](/blog/linux-ssh-wall) \- 20140 
  * [ 二分图带权匹配 KM算法与费用流模型建立 ](/blog/match-km) \- 20102 
  * [ 仙劍奇俠傳五破關之談 ](/blog/pal5-comment) \- 19959 
  * [ Node.js中的child_process及進程通信 ](/blog/node-child-process-ipc) \- 19633 
  * [ 仙劍五前傳淺析 ](/blog/pal5q-comment) \- 18650 
  * [ 普通話是胡語嗎？ ](/blog/mandarin-altaic) \- 18537 
  * [ 說說「支那」 ](/blog/talk-about-cina) \- 18149 
  * [ Linux C语言编程学习笔记 (1)进程控制入门 ](/blog/linux-c-1) \- 18138 

####  存檔

  * [ 2014年九月 ](/blog/archive/2014/9) (1) 
  * [ 2014年六月 ](/blog/archive/2014/6) (3) 
  * [ 2014年五月 ](/blog/archive/2014/5) (1) 
  * [ 2014年三月 ](/blog/archive/2014/3) (6) 
  * [ 2014年一月 ](/blog/archive/2014/1) (1) 
  * [ 2013年十二月 ](/blog/archive/2013/12) (1) 
  * [ 2013年十月 ](/blog/archive/2013/10) (1) 
  * [ 2013年六月 ](/blog/archive/2013/6) (2) 
  * [ 2013年五月 ](/blog/archive/2013/5) (4) 
  * [ 2013年四月 ](/blog/archive/2013/4) (4) 
  * [ 2013年三月 ](/blog/archive/2013/3) (2) 
  * [ 2013年二月 ](/blog/archive/2013/2) (1) 
  * [ 2013年一月 ](/blog/archive/2013/1) (2) 
  * [ 2012年十二月 ](/blog/archive/2012/12) (1) 
  * [ 2012年九月 ](/blog/archive/2012/9) (1) 
  * [ 2012年八月 ](/blog/archive/2012/8) (2) 
  * [ 2012年七月 ](/blog/archive/2012/7) (3) 
  * [ 2012年六月 ](/blog/archive/2012/6) (1) 
  * [ 2012年五月 ](/blog/archive/2012/5) (1) 
  * [ 2012年四月 ](/blog/archive/2012/4) (2) 
  * [ 2012年三月 ](/blog/archive/2012/3) (1) 
  * [ 2012年二月 ](/blog/archive/2012/2) (2) 
  * [ 2012年一月 ](/blog/archive/2012/1) (8) 
  * [ 2011年十二月 ](/blog/archive/2011/12) (13) 
  * [ 2011年十一月 ](/blog/archive/2011/11) (3) 
  * [ 2011年十月 ](/blog/archive/2011/10) (2) 
  * [ 2011年九月 ](/blog/archive/2011/9) (1) 
  * [ 2011年八月 ](/blog/archive/2011/8) (3) 
  * [ 2011年七月 ](/blog/archive/2011/7) (3) 
  * [ 2011年六月 ](/blog/archive/2011/6) (6) 
  * [ 2011年五月 ](/blog/archive/2011/5) (4) 
  * [ 2011年四月 ](/blog/archive/2011/4) (2) 
  * [ 2011年二月 ](/blog/archive/2011/2) (3) 
  * [ 2010年十二月 ](/blog/archive/2010/12) (4) 
  * [ 2010年十一月 ](/blog/archive/2010/11) (2) 
  * [ 2010年十月 ](/blog/archive/2010/10) (3) 
  * [ 2010年九月 ](/blog/archive/2010/9) (3) 
  * [ 2010年八月 ](/blog/archive/2010/8) (7) 
  * [ 2010年六月 ](/blog/archive/2010/6) (5) 
  * [ 2010年五月 ](/blog/archive/2010/5) (11) 
  * [ 2010年四月 ](/blog/archive/2010/4) (10) 
  * [ 2010年三月 ](/blog/archive/2010/3) (12) 
  * [ 2010年二月 ](/blog/archive/2010/2) (1) 
  * [ 2010年一月 ](/blog/archive/2010/1) (10) 
  * [ 2009年十二月 ](/blog/archive/2009/12) (5) 
  * [ 2009年十一月 ](/blog/archive/2009/11) (11) 
  * [ 2009年十月 ](/blog/archive/2009/10) (13) 
  * [ 2009年九月 ](/blog/archive/2009/9) (6) 
  * [ 2009年八月 ](/blog/archive/2009/8) (2) 
  * [ 2009年七月 ](/blog/archive/2009/7) (9) 
  * [ 2009年六月 ](/blog/archive/2009/6) (14) 
  * [ 2009年五月 ](/blog/archive/2009/5) (16) 
  * [ 2009年四月 ](/blog/archive/2009/4) (28) 
  * [ 2009年三月 ](/blog/archive/2009/3) (21) 
  * [ 2009年二月 ](/blog/archive/2009/2) (18) 
  * [ 2009年一月 ](/blog/archive/2009/1) (6) 
  * [ 2008年十二月 ](/blog/archive/2008/12) (22) 
  * [ 2008年十一月 ](/blog/archive/2008/11) (21) 
  * [ 2008年十月 ](/blog/archive/2008/10) (24) 
  * [ 2008年九月 ](/blog/archive/2008/9) (6) 
  * [ 2008年八月 ](/blog/archive/2008/8) (12) 
  * [ 2008年七月 ](/blog/archive/2008/7) (20) 
  * [ 2008年六月 ](/blog/archive/2008/6) (23) 
  * [ 2008年四月 ](/blog/archive/2008/4) (29) 
  * [ 2008年三月 ](/blog/archive/2008/3) (8) 
  * [ 2008年二月 ](/blog/archive/2008/2) (1) 
  * [ 2008年一月 ](/blog/archive/2008/1) (6) 
  * [ 2007年十二月 ](/blog/archive/2007/12) (3) 
  * [ 2007年十一月 ](/blog/archive/2007/11) (22) 

#  Recent Posts

  * [ 橫貫西伯利亞小記 ](/blog/trans-siberia-travel-notes)
  * [ 高維世界與一維價值 ](/blog/high-dimensional-world-and-unified-value)
  * [ 誰說中國醫療差——談醫療制度 ](/blog/discussion-on-health-care-system)
  * [ icc的過程間優化和性能分析引導優化 ](/blog/icc-ipo-pgo)
  * [ 朝鮮並不封閉：《我們最幸福》札記 ](/blog/dprk-nothing-to-envy-notes)

#  Blogroll

  * [ MaskRay ](http://maskray.me/)
  * [ Yuxin's Blog ](http://ppwwyyxx.com/)
  * [ BlahGeek ](https://blog.blahgeek.com/)
  * [ Yangzhe1990's Blog ](http://yangzhe1990.wordpress.com/)
  * [ Dang Fan's Blog ](http://dangfan.me/)

#  Blogroll

  * [ Swj's Home ](http://www.curimit.com/blog/)
  * [ CS Slayer ](http://www.csslayer.info/)
  * [ Typeof.net ](http://typeof.net/)
  * [ Henry's Blog ](http://blog.henryhu.net/)
  * [ polyhedron(古韻) ](http://blog.sina.com.cn/ychromosome)

#  Blogroll

  * [ 閱微堂 ](http://zhiqiang.org/blog/)
  * [ 優哉幽齋 ](http://www.liyaos.com/)
  * [ 超越時空 ](http://www.vuryleo.com/)
  * [ 獨異誌 ](http://solog.me/)

↑  Originally designed by Site5 WordPress Themes. BYVoid refactored with
Node.js, less, jade and CoffeeScript.

