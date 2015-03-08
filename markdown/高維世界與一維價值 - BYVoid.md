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

六月  ** 30 ** 2014

  * 作者:  byvoid 
  * 閱讀: 12529 
  *     * [ 德國 ](/blog/tag/德國)
    * [ 萊比錫 ](/blog/tag/萊比錫)
    * [ ISC ](/blog/tag/ISC)
    * [ 超級計算 ](/blog/tag/超級計算)
    * [ 清華 ](/blog/tag/清華)
    * [ LINPACK ](/blog/tag/LINPACK)
    * [ 浮點 ](/blog/tag/浮點)
    * [ 密碼學 ](/blog/tag/密碼學)
    * [ 高維 ](/blog/tag/高維)
    * [ 價值觀 ](/blog/tag/價值觀)
    * [ 價值 ](/blog/tag/價值)
    * [ 向量 ](/blog/tag/向量)
    * [ 標量 ](/blog/tag/標量)
    * [ 序關係 ](/blog/tag/序關係)
    * [ 價格 ](/blog/tag/價格)
    * [ 商品 ](/blog/tag/商品)
    * [ 供求 ](/blog/tag/供求)
    * [ 計劃經濟 ](/blog/tag/計劃經濟)
    * [ 價值多元化 ](/blog/tag/價值多元化)
    * [ 稷下學宮 ](/blog/tag/稷下學宮)

#  [ 高維世界與一維價值 ](/blog/high-dimensional-world-and-unified-value)

我前幾天去德國萊比錫參加了 [ ISC學生集羣大賽 ](http://hpcadvisorycouncil.com/events/2014/isc14
-student-cluster-competition/) 。這個比賽的內容是在限定功率（3000W）的條件下，優化集羣的計算性能。每個隊伍的集羣分別由贊
助商提供，清華大學隊是浪潮公司贊助的。由於硬件實在沒法和別的學校比，我們只好從軟件上來優化，比賽的程序包括了 [ LINPACK
](http://www.top500.org/project/linpack/) 、 [ HPCC
](http://icl.cs.utk.edu/hpcc/) 、 [ HPCG
](https://software.sandia.gov/hpcg/html/index.html) 、 [ Quantum ESPRESSO
](http://www.quantum-espresso.org/) 和 [ Gadget ](http://www.mpa-
garching.mpg.de/gadget/)
。最終清華隊獲得了全球第三名，也算是盡力了——畢竟我們的集羣連GPU都沒，而許多隊伍配置極盡奢華，像愛丁堡大學連液冷系統都上了。

##  世界上「最快」的超級計算機

在ISC會議期間，我們得知了中國的「天河2號」以LINPACK峯值54902.4 TFlop/S的速度保持了超級計算機 [ TOP500
](http://www.top500.org/lists/2014/06/)
榜首，全球媒體爭相報道。但是在各個媒體的報道中，我們看到的是「天河2號」成爲「全球最快的超級計算機」，如 [ Forbes
](http://www.forbes.com/sites/alexknapp/2014/06/23/chinas-tianhe-2-remains-
the-worlds-fastest-supercomputer/) 的報道，而紛紛忽略了一個重要細節，即TOP500是以LINPACK的速度來排名的。 [
LINPACK ](http://en.wikipedia.org/wiki/LINPACK_benchmarks)
基準測試求解的問題是一個稠密的線性方程組，它完全是計算密集型的應用，其內存訪問、並行通信、磁盤讀寫都不成爲瓶頸。因此 [ 有人批評
](http://opensky.library.ucar.edu/collections/TECH-NOTE-000-000-000-227) LINPA
CK提供的數值是「基本上無法到達的，卻有一小撮程序員在無聊地優化它的代碼，爲了使得他們的機器獲得更好的數值」。實際上衡量一個計算機性能的好壞，僅僅通過浮點計
算密集型的應用來估計絕對是以偏概全，真實的系統性能還取決於整數計算性能、內存訪問性能、網絡通信性能和磁盤讀寫性能等等各個方面。哪怕是僅僅在科學計算領域，許多
應用也不僅僅是在求解稠密線性方程組。許多時候可以認爲LINPACK數值完全不具備參考意義，因爲大多數科學計算應用的性能瓶頸根本不在這上面。

作爲「國家安全戰略投資」的天河2號，想必許多時候在求解的問題是破解密碼。然而一個可怕的事實是，大量密碼學算法，包括散列、非對稱加密（如MD5、RSA），都
[ 只進行整數計算 ](http://crypto.stackexchange.com/questions/2715/do-cryptographic-
hashing-algorithms-operate-only-on-integers)
，完全沒有任何浮點計算操作。如此看來，追求高LINPACK數值來提高密碼破解的性能，差不多是緣木求魚。

##  高維世界的序關係

說到CPU的性能，幾年前，大家在裝電腦的時候選購CPU只看主頻，頻率越高越好。於是英特爾爲了迎合市場，推出了奔騰四3.0GHz甚至3.6GHz主頻的CPU。
後來進入多核時代，大家就看核心數，雙核的肯定比單核的好，四核的肯定比雙核的好。殊不知CPU的性能好壞有太多的參數，盲目追求高的主頻或者核心的數量沒有意義。不
單單是CPU，想想看大家買數碼相機看什麼呢？許多人第一反應當然是像素啊。買單反鏡頭？光圈大小！買汽車？排量！買房？面積！

事實上這個道理淺顯易懂，但人們卻對它無能爲力。作爲沒有相關知識的普通消費者，面對這個世界紛繁複雜的參數真的是無能爲力，於是只好選擇一個「公認」的參數作爲基準
了。

這一切的根源在於，向量和向量是無法比較大小的，只有標量纔能比較。向量只能通過一些函數變換到標量纔能比較，如模長，或者在某個空間上的投影。世界上的任何一件東西
都可以用一個高維向量來表示，但爲了獲得序關係，我們通常只能把它映射到一個一維空間。在這個過程中，大量的信息都丟失了。對於同一組向量使用不同的函數，獲得序關係
可以是完全不一樣的。

這是一個淺顯易懂的道理，而人們卻無能爲力。因爲人們天生傾向於用一個一維的數值來比較一切同類的事物（甚至不同類的事物），但事物天生是高維的。

##  價值觀是一個從高維空間到一維空間的映射

人們經常談論價值觀，譬如價值觀不同的人不要在一起，現代社會通過價值觀把人分爲不同的羣體。價值觀實際上 ** 是一個從高維空間到一維空間的映射 ** ，也就是
一個高維向量的函數。人們面對紛繁複雜的事物，一個與生俱來的衝動就是對它進行評價，然後與其他事物相互比較。在這個過程中，不同價值觀的人使用了不同的函數，因此得
出的結果是大相徑庭的。

##  商品的價格與價值

作爲一個通用的價值衡量工具，商品的價格成爲一個被廣泛使用的尺度。價格短期看來反應的是供求的關係，但本質上反映了一個長期的、多人的價值。用數學的語言方式表示，
** 價格是一個高維的泛函（Functional） ** ，其中每一維的變量都是一個個體的價值觀函數，或者用以下代碼（OCaml）表示：

    
    
    (* 價值觀是一個從任意向量到整數的函數 *)
    type value = (anything -> int)
    
    (* 價格是一個從多個價值觀函數到一個價值觀函數的函數(泛函) *)
    val price : (values_of_all : value list) -> value
    
    (* 一個簡單實現：價格即爲所有人價值觀的平均值 *)
    let price values_of_all =
      fun thing ->
        let sum = List.fold_left (
          fun sum value_function -> sum + (value_function thing)
        ) 0 values_of_all in
        let number_of_people = (List.length values_of_all) in
        sum / number_of_people

換人話說，價格反映了全體生產者和消費者的價值觀，儘管可能各不相同，但卻用一個工具把它們統一了起來，變成了一個單一的可以衡量不同事物的價值的函數。對於一個個體
來說，商品的價格可能偏離個人對商品的價值衡量，因此會有感覺便宜或者感覺貴。根據個人是否有錢，個人對價值的衡量也會不同，個人資產可以作爲價值觀函數的一個其他參
數。

用價格衡量價值的方法看似簡單粗暴，有諸多弊端，卻也有着其他方法無可比擬的優點。其最大的優點就是簡單性，因爲人類對複雜事物的理解力實在有限。這也是爲什麼計劃經
濟無法執行的一個原因，因爲沒有一個把萬物映射到一維的函數，或者這個函數取樣過於有限，只能反應少數統治者的意願。

##  價值多元化

一元價值儘管有着便於比較排序的優點，但卻會導致優化目標的單一化。譬如超級計算機只優化LINPACK或其他某個性能，學生爲了應付高考成爲做題機器，全社會「向錢
看」道德淪喪等等。儘管着本身沒有什麼問題，卻會讓導致潛在的評估偏差風險。對此，價值多元化的主張被提了出來。價值多元化是把一維的價值標量變爲多維向量，也可以理
解爲是多個價值函數的組合。價值多元化以後，價值本身重新變得不可比較，只能按照維度比較（或者價值向量的函數）。

在我看來，價值多元化沒有解決太多的問題，反而喪失了序關係，事實上是一種掩耳盜鈴的方法。價值多元化就等於沒有價值，只是把一個高維向量映射到了另一個向量，不僅丟
失了信息，還無法比較。價值多元化可以當作進一步價值比較的「中間結果」，方便進一步計算而已，最終還是要歸結於一維。用金錢衡量一切的一元價值儘管不能解決許多問題
，卻是人類目前能想到並實踐的最有效的方法。但願會有更好的方式被發明出來。

##  相關日誌

  * [ 比特幣的價值探討 ](/blog/bitcoin-value)
  * [ 誰說中國醫療差——談醫療制度 ](/blog/discussion-on-health-care-system)
  * [ 我支持取消NOIP保送 ](/blog/noip-cu)
  * [ 過去一年的環球旅行 ](/blog/global-tour-in-the-last-year)
  * [ 哥德爾不完備性定理與不可知論 ](/blog/godel-incompleteness-theorems-agnosticism)
  * [ 清華入學總結 ](/blog/thu-3weeks-summary)
  * [ 當今世界的帝國主義 ](/blog/current-world-imperialism)
  * [ 這一年來 ](/blog/recent-one-year)
  * [ 冰雪奇緣中的左翼符號 ](/blog/frozen-leftist-symbols)
  * [ Firefox4校園推廣及小調查 ](/blog/firefox4-tsinghua)

Search for:

####  語言

  * [ 原文 ](/blog/high-dimensional-world-and-unified-value)
  * [ 正體中文 ](/zht/blog/high-dimensional-world-and-unified-value)
  * [ 簡體中文 ](/zhs/blog/high-dimensional-world-and-unified-value)
  * [ English ](/en/blog/high-dimensional-world-and-unified-value)

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
  * [ 推薦一個神級輸入法——Rime ](/blog/recommend-rime) \- 119438 
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
  * [ Linux下实现自动设置SSH代理 ](/blog/linux-ssh-wall) \- 20139 
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

