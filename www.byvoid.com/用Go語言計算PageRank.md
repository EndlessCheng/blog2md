title: 用Go語言計算PageRank

date: 2013-04-26 01:18:19

tags: [PageRank, Go, 語言, 圖輪, 計算機科學, SEO, 搜索引擎, 齊普夫分佈, Zipf, 返回值, 錯誤處理, 異常, 一等函數, 閉包, 指針, 垃圾回收, ]

description: 

---
# 

PageRank是搜索引擎結果排序的重要算法，其依賴的方式是鏈接結構分析，大致解釋就是一個網頁A有一個指向另一個網頁B的鏈接，就相當於A給B投票，獲得投票越多的網頁的PageRank值越高。並不是每個網頁的投票權重都是一樣的，自己PageRank越大的網頁投票權重越大，所以PageRank的計算公式是遞歸的，需要迭代計算，直到結果收斂。

我使用Go語言對真實網頁的數據[WT2g](http://ir.dcs.gla.ac.uk/test_collections/access_to_data.html)進行了PageRank的計算，計算出的結果分佈如下圖：

[![PageRank Distribution](/upload/blog/pagerank-go/pagerank_thumb.png)](/upload/blog/pagerank-go/pagerank.png)

觀察發現，PageRank的分佈服從齊普夫分佈(Zipf Distribution)，其中32%的網頁的PageRank爲最小值9.459×10^-7，超過一半的網頁的PageRank的值小於6.600×10^-6，而PageRank的最大值爲1.885×10^-3。

值得一提的是[Go語言](http://golang.org/)，推薦一個對Go語言特性的介紹：[Go在Google：以軟件工程爲目的的語言設計](http://www.oschina.net/translate/go-at-google-language-design-in-the-service-of-software-engineering)。使用Go語言最大的感受是它的函數可以有多返回值，而且在各種API中這個特性被大量使用，而且約定多返回值的最後一個參數是`error`類型，表示是否有錯誤發生。這種錯誤處理的方法和C++、Java、Python、JavaScript使用的異常不同，倒是與C語言的錯誤處理相似。C語言習慣於把函數的返回值作爲「是否有錯誤發生」的標記，如果有錯誤再通過其他的手段（如全局變量`error`）來獲取，Go語言直接把錯誤作爲了一個返回值。Go語言還支持一等函數(First Class Function)和閉包，因此方便用來實現`yield`功能，下面代碼中的`lineReader`函數就是返回了一個生成器，用來按行讀取文件，每調用一次讀取一行，讀完以後釋放內存。Go語言還是一個顯式有指針的語言，同時也提供了垃圾回收，省去了手動維護內存的麻煩。

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

[BYVNotes](https://github.com/byvoid/byvnotes)是一個我用Go語言實現的簡單在線記事本網站，使用了Revel框架。
