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

三月  ** 20 ** 2014

  * 作者:  byvoid 
  * 閱讀: 6308 
  *     * [ 比特幣 ](/blog/tag/比特幣)
    * [ 原理 ](/blog/tag/原理)
    * [ 挖礦 ](/blog/tag/挖礦)
    * [ 區塊 ](/blog/tag/區塊)
    * [ 區塊鏈 ](/blog/tag/區塊鏈)
    * [ 交易 ](/blog/tag/交易)
    * [ 散列 ](/blog/tag/散列)
    * [ 挖礦難度 ](/blog/tag/挖礦難度)
    * [ 私鑰 ](/blog/tag/私鑰)
    * [ 簽名 ](/blog/tag/簽名)

#  [ 一段程序看懂比特幣原理 ](/blog/bitcoin-principle-program)

自從比特幣火起來以後，網上對比特幣的解釋可謂汗牛充棟，紛繁複雜。但對於程序員來說，最直接的方式莫過於直接看程序代碼了。嫌比特幣代碼龐雜沒關係，我找到一段簡明
扼要的代碼，用來理解比特幣再好不過了。

以下這段程序轉自 [ 知乎上Wu Hao的回答
](http://www.zhihu.com/question/20941124/answer/16668373) 。

    
    
    function mine()
    {
        while(true)
        {
            longestChain = getLongestValidChain()
    
            -- A number that changes every time, so that you don't waste 
            -- time trying to calculate a valid blockHash with the same
            -- input.
            nonce = getNewNonce()
    
            currentTXs = getUnconfirmedTransactionsFromNetwork()
    
            newBlock = getNewBlock(longestChain, currentTXs, nonce)
    
            -- http://en.wikipedia.org/wiki/SHA-2
            -- and this is what all the "mining machines" are doing.
            blockHash = sha256(newBlock)
    
            if (meetReqirements(blockHash))
            {
                broadcast(newBlock)
                -- Now the height the block chain is incremented by 1
                -- (if the new block is accepted by other peers),
                -- and all the TXs in the new block are "confirmed"
            }
        }
    }
    ////////////////////////////////////////////////////////////////
    function sendBTC(amount)
    {
        sourceTXs = pickConfirmedTransactionsToBeSpent(amount)
        tx = generateTX(sourceTXs, targetAddrs, amount, fee)
        signedTx = sign(tx, privateKeysOfAllInputAddress)
        broadcast(signedTx)
    }
    ////////////////////////////////////////////////////////////////

下面是我的解釋：

挖礦過程就是不斷從比特幣網絡中獲取所有未確認交易 ` getUnconfirmedTransactionsFromNetwork() `
，把它們打包成一個區塊並掛載目前最長的區塊鏈上 ` getNewBlock(longestChain, currentTXs, nonce) `
，然後計算新的區塊的散列值 ` sha256(newBlock) ` ，如果散列值正好滿足挖礦難度了 `
meetReqirements(blockHash) `
，那麼就挖礦成功了。所謂挖礦難度，指的是要求的二進制散列值小於某個閾值，閾值越小，挖礦的難度就越大。

付款過程就是把一些有餘額的已確認交易拿出來作爲發送地址 ` pickConfirmedTransactionsToBeSpent(amount) `
，然後根據目標地址支付一定交易費生成新的交易 ` generateTX(sourceTXs, targetAddrs, amount, fee) `
，並用錢包私鑰對交易簽名 ` sign(tx, privateKeysOfAllInputAddress) ` ，然後廣播出去。

##  相關日誌

  * [ 你不知道的東西正在傷害你——淺談信息不對稱 ](/blog/information-asymmetry-hurts-you)
  * [ 萊特幣連環爆倉事件始末 ](/blog/litecoin-plummet-incident)
  * [ 比特幣的價值探討 ](/blog/bitcoin-value)
  * [ 比特幣——史上最瘋狂的虛擬貨幣 ](/blog/bitcoin-craziest-money)

Search for:

####  語言

  * [ 原文 ](/blog/bitcoin-principle-program)
  * [ 正體中文 ](/zht/blog/bitcoin-principle-program)
  * [ 簡體中文 ](/zhs/blog/bitcoin-principle-program)
  * [ English ](/en/blog/bitcoin-principle-program)

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

