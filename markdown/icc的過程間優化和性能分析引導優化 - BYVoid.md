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

六月  ** 3 ** 2014

  * 作者:  byvoid 
  * 閱讀: 5102 
  *     * [ 編譯 ](/blog/tag/編譯)
    * [ 鏈接 ](/blog/tag/鏈接)
    * [ 優化 ](/blog/tag/優化)
    * [ 全局優化 ](/blog/tag/全局優化)
    * [ 過程間優化 ](/blog/tag/過程間優化)
    * [ 性能分析引導優化 ](/blog/tag/性能分析引導優化)
    * [ 彙編 ](/blog/tag/彙編)
    * [ 代碼生成 ](/blog/tag/代碼生成)
    * [ icc ](/blog/tag/icc)
    * [ gcc ](/blog/tag/gcc)
    * [ llvm ](/blog/tag/llvm)

#  [ icc的過程間優化和性能分析引導優化 ](/blog/icc-ipo-pgo)

icc（ [ Intel C++ Compiler ](https://software.intel.com/en-us/c-compilers)
）是一個非常厲害的編譯器，對優化計算密集型的程序遠超其他任何編譯器，如gcc、llvm、Visual C++。

icc提供了 ** 過程間優化(Interprocedural Optimization) ** 技術，可以幫助編譯器在不同的目標文件之間進行全局優化。傳統
的編譯器的編譯過程是編譯每個源文件到獨立的目標文件，然後再通過鏈接器將目標文件鏈接成可執行文件。傳統的編譯器的編譯優化主要集中在每個源文件內部，鏈接過程比較
簡單，因此每個文件都是獨立的，而icc提供的過程間優化打破了這一限制。

過程間優化可以對整個程序進行全局優化，而不是僅僅在單個文件、單個函數或者單個代碼塊內部優化。過程間優化可以減少過程之間重複計算、內存的低效訪問以及簡化迭代過
程，通常會採用內聯函數的方式。過程間優化還可以重排代碼的順序以優化內存的分配方式和局部性。

通過指定編譯參數 ` -ipo `
，icc可以開啓過程間優化，icc將在編譯時生成特殊格式的目標文件（中間語言），並在鏈接時進行進一步的編譯和過程間優化，如圖所示：

![](https://www.byvoid.com/upload/blog/icc-ipo-pgo/ipo.png)

使用icc啓動過程間優化的方式是在編譯參數中加上 ` -ipo ` 參數，還要設置環境變量 ` AR=xiar ` ，使用Intel的版本代替默認的 `
ar ` 。

** 性能分析引導優化(Profile Guided Optimization) ** 通過分析程序運行時的實際行爲，將結果反饋給編譯器，使得編譯器可以重新安排代碼以減少指令緩存問題和分支預測誤判，從而獲得性能的提升。性能分析引導優化通過實際執行代碼統計出運行頻率最高的部分，編譯器通過這些信息可以更加針對地優化代碼。性能分析引導優化分爲三個階段： 

  1. 第一步是生成分析程序。在這個階段，編譯器創建一個有采樣注入的可執行程序。在icc中使用的編譯指令是 ` -prog-gen ` ，以及 ` -prof-dir=[dir] ` 。 
  2. 第二步是運行第一步生成的被注入採樣分析的程序，每次運行這個程序，都會生成 ` -prof-dir ` 指定的目錄下生成一個動態信息文件(dynamic information file)，將會被最終編譯時使用。 
  3. 第三步是最終編譯的步驟。第二次編譯的時候，動態信息文件會合併成一個彙總文件。通過彙總文件，編譯器會嘗試將最常使用的執行路徑優化。 

![](https://www.byvoid.com/upload/blog/icc-ipo-pgo/pgo.png)

過程間優化和性能分析引導優化可能會相互影響，性能分析引導優化通常會幫助編譯器生成內聯函數，這會幫助過程間優化的效率。性能分析引導優化對分支預測效率的提升最有
效果，許多分支執行的可能性無法在編譯時判斷，而通過性能分析引導優化，編譯器可以針對經常執行的分支（熱代碼）和不經常執行的分支（冷代碼）生成高效的彙編代碼。

使用性能分析引導優化的方法如下：

  * 第一階段：編譯參數中加上： ` -prof-gen=srcpos -prof-dir=/tmp/profdata ` 。其中 ` -prof-dir ` 是存儲性能分析文件的目錄。 
  * 第二階段：運行編譯好的程序，然後運行 ` profmerge -prof_dir /tmp/profdata ` 生成彙總文件。 
  * 第三階段：重新編譯程序，使用參數： ` -prof-use=nomerge -prof-func-groups -prof-dir=/tmp/profdata ` 。 

這樣最終生成的代碼就是經過性能分析優化過後的了。

以上方法在icc 14.0.2上試驗通過。

##  參考

  * [ Intel® C++ Compiler XE 13.1 User and Reference Guide ](https://software.intel.com/sites/products/documentation/doclib/iss/2013/compiler/cpp-lin/index.htm)
  * [ Intel® C++ Optimizing Applications ](http://www.ucl.ac.uk/isd/staff/research_services/research-computing/services/unity/environment/intel_cc___optimizing_applications.pdf)

##  相關日誌

  * [ 探寻C++最快的读取文件的方案 ](/blog/fast-readfile)
  * [ Vakuum开发笔记02 核心与安全问题 ](/blog/vakuum-dev-note-02)
  * [ NOI 1997 解题报告 ](/blog/noi-1997-solution)
  * [ NOI 2009 诗人小G ](/blog/noi-2009-poet)
  * [ NOI 2008 设计路线 design ](/blog/noi-2008-design)
  * [ USACO 5.4.4 Betsy's Tour 漫游小镇 betsy ](/blog/usaco-544-betsys-tour)
  * [ USACO 5.3.1 Milk Measuring 量取牛奶 milk4 ](/blog/usaco-531-milk-measuring)
  * [ CoffeeScript的全局變量污染與Node.js的模塊加載 ](/blog/coffee-script-global-variable-pollution)
  * [ C++語法分析中最讓人頭疼的歧義 ](/blog/cpp-most-vexing-parse)
  * [ C语言中跨文件的全局变量 ](/blog/c-global-variables-in-multiple-files)

Search for:

####  語言

  * [ 原文 ](/blog/icc-ipo-pgo)
  * [ 正體中文 ](/zht/blog/icc-ipo-pgo)
  * [ 簡體中文 ](/zhs/blog/icc-ipo-pgo)
  * [ English ](/en/blog/icc-ipo-pgo)

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

