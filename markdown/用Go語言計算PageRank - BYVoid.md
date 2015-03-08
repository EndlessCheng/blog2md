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

四月  ** 25 ** 2013

  * 作者:  byvoid 
  * 閱讀: 5482 
  *     * [ PageRank ](/blog/tag/PageRank)
    * [ Go ](/blog/tag/Go)
    * [ 語言 ](/blog/tag/語言)
    * [ 圖輪 ](/blog/tag/圖輪)
    * [ 計算機科學 ](/blog/tag/計算機科學)
    * [ SEO ](/blog/tag/SEO)
    * [ 搜索引擎 ](/blog/tag/搜索引擎)
    * [ 齊普夫分佈 ](/blog/tag/齊普夫分佈)
    * [ Zipf ](/blog/tag/Zipf)
    * [ 返回值 ](/blog/tag/返回值)
    * [ 錯誤處理 ](/blog/tag/錯誤處理)
    * [ 異常 ](/blog/tag/異常)
    * [ 一等函數 ](/blog/tag/一等函數)
    * [ 閉包 ](/blog/tag/閉包)
    * [ 指針 ](/blog/tag/指針)
    * [ 垃圾回收 ](/blog/tag/垃圾回收)

#  [ 用Go語言計算PageRank ](/blog/pagerank-go)

PageRank是搜索引擎結果排序的重要算法，其依賴的方式是鏈接結構分析，大致解釋就是一個網頁A有一個指向另一個網頁B的鏈接，就相當於A給B投票，獲得投票越
多的網頁的PageRank值越高。並不是每個網頁的投票權重都是一樣的，自己PageRank越大的網頁投票權重越大，所以PageRank的計算公式是遞歸的，需
要迭代計算，直到結果收斂。

我使用Go語言對真實網頁的數據 [ WT2g
](http://ir.dcs.gla.ac.uk/test_collections/access_to_data.html)
進行了PageRank的計算，計算出的結果分佈如下圖：

[ ![PageRank Distribution](/upload/blog/pagerank-go/pagerank_thumb.png)
](/upload/blog/pagerank-go/pagerank.png)

觀察發現，PageRank的分佈服從齊普夫分佈(Zipf Distribution)，其中32%的網頁的PageRank爲最小值9.459×10^-7，超過
一半的網頁的PageRank的值小於6.600×10^-6，而PageRank的最大值爲1.885×10^-3。

值得一提的是 [ Go語言 ](http://golang.org/) ，推薦一個對Go語言特性的介紹： [ Go在Google：以軟件工程爲目的的語言設計
](http://www.oschina.net/translate/go-at-google-language-design-in-the-
service-of-software-engineering)
。使用Go語言最大的感受是它的函數可以有多返回值，而且在各種API中這個特性被大量使用，而且約定多返回值的最後一個參數是 ` error ` 類型，表示是否
有錯誤發生。這種錯誤處理的方法和C++、Java、Python、JavaScript使用的異常不同，倒是與C語言的錯誤處理相似。C語言習慣於把函數的返回值作
爲「是否有錯誤發生」的標記，如果有錯誤再通過其他的手段（如全局變量 ` error `
）來獲取，Go語言直接把錯誤作爲了一個返回值。Go語言還支持一等函數(First Class Function)和閉包，因此方便用來實現 ` yield `
功能，下面代碼中的 ` lineReader ` 函數就是返回了一個生成器，用來按行讀取文件，每調用一次讀取一行，讀完以後釋放內存。Go語言還是一個顯式有指
針的語言，同時也提供了垃圾回收，省去了手動維護內存的麻煩。

以下是用Go語言計算PageRank的代碼：

    
    
    package main
    
    import (
        "bufio"
        "errors"
        "fmt"
        "io"
        "math"
        "os"
        "strings"
    )
    
    type vertex struct {
        inDegree  int
        outDegree int
        pagerank  float64
    }
    
    type edge struct {
        start int
        end   int
    }
    
    var vertexs []vertex
    var edges []edge
    var vertexID map[string]int = make(map[string]int)
    var numVertex int = 0
    
    func lineReader(filename string) (func() (string, error), error) {
        f, err := os.Open(filename)
        if err != nil {
            return nil, err
        }
        buf := bufio.NewReaderSize(f, 64)
        return func() (string, error) {
            line, isPrefix, err := buf.ReadLine()
            if err != nil {
                if err == io.EOF {
                    if err := f.Close(); err != nil {
                        return "", err
                    }
                }
                return "", err
            }
            if isPrefix {
                return "", errors.New("buffer size to small")
            }
            return string(line), nil
        }, nil
    }
    
    func addVertex(vertexName string) int {
        var ID int
        var ok bool
        if ID, ok = vertexID[vertexName]; !ok {
            ID = numVertex
            vertexID[vertexName] = ID
            vertexs = append(vertexs, vertex{})
            numVertex++
        }
        return ID
    }
    
    func read() {
        readline, err := lineReader("wt2g_inlinks.source")
        if err != nil {
            panic(err)
        }
        for {
            line, err := readline()
            if err != nil {
                if err == io.EOF {
                    break
                }
                panic(err)
            }
            // Line format is like "ID1\tID2"
            sections := strings.Split(line, "\t")
            if len(sections) != 2 {
                panic(errors.New("Illegal line format"))
            }
            start := addVertex(sections[0])
            end := addVertex(sections[1])
            edges = append(edges, edge{start, end})
        }
    }
    
    func calcPagerank(alpha float64, numIterations int) {
        // Initialize out degree of every vertex
        for i := range edges {
            edge := &edges[i]
            vertexs[edge.start].outDegree++
            vertexs[edge.end].inDegree++
        }
        var I = make([]float64, numVertex)
        var S float64
        for i := 0; i < numVertex; i++ {
            vertexs[i].pagerank = 1 / float64(numVertex)
            I[i] = alpha / float64(numVertex)
        }
        // Calculate pagerank repeatedly until converge (numIterations times)
        for k := 0; k < numIterations; k++ {
            for i := range edges {
                edge := &edges[i]
                I[edge.end] += (1 - alpha) * vertexs[edge.start].pagerank / float64(vertexs[edge.start].outDegree)
            }
            S = 0
            for i := 0; i < numVertex; i++ {
                if vertexs[i].outDegree == 0 {
                    S += (1 - alpha) * vertexs[i].pagerank / float64(numVertex)
                }
            }
            for i := 0; i < numVertex; i++ {
                vertexs[i].pagerank = I[i] + S
                I[i] = alpha / float64(numVertex)
            }
        }
    }
    
    func main() {
        read()
        calcPagerank(0.15, 30)
        fmt.Println("Done")
    }

[ BYVNotes ](https://github.com/byvoid/byvnotes)
是一個我用Go語言實現的簡單在線記事本網站，使用了Revel框架。

##  相關日誌

  * [ 二分图带权匹配 KM算法与费用流模型建立 ](/blog/match-km)
  * [ 基於統計語言模型的拼音輸入法 ](/blog/slm_based_pinyin_ime)
  * [ 各种字符串Hash函数比较 ](/blog/string-hash-compare)
  * [ 如何處理C++構造函數中的錯誤——兼談不同語言的錯誤處理 ](/blog/cpp-constructor-exception)
  * [ 左偏树 ](/blog/leftist-tree)
  * [ 川滇瀕危少數民族語言田野調查之旅 ](/blog/southwest-minority-linguistic-fieldwork)
  * [ 次短路径与次小生成树问题的简单解法 ](/blog/2-sp-mst)
  * [ APIO讲稿——函数式编程 ](/blog/apio-fp)
  * [ Treap ](/blog/treap)
  * [ 树状数组 ](/blog/binary-index-tree)

Search for:

####  語言

  * [ 原文 ](/blog/pagerank-go)
  * [ 正體中文 ](/zht/blog/pagerank-go)
  * [ 簡體中文 ](/zhs/blog/pagerank-go)
  * [ English ](/en/blog/pagerank-go)

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
  * [ 海外實習面試記 ](/blog/oversea-internship-interviews) \- 47495 
  * [ 這一年來 ](/blog/recent-one-year) \- 47077 
  * [ 各种字符串Hash函数比较 ](/blog/string-hash-compare) \- 46351 
  * [ 關於阿里巴巴面試結果信息泄漏的一點說明 ](/blog/alibaba-interview-feedback-clarification) \- 45354 
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

