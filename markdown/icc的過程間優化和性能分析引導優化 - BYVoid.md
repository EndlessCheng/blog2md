六月  ** 3 ** 2014 

  *   *   *     * [ 編譯 ](/blog/tag/編譯)
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

icc（ [ Intel C++ Compiler ](https://software.intel.com/en-us/c-compilers) ）是一個非常厲害的編譯器，對優化計算密集型的程序遠超其他任何編譯器，如gcc、llvm、Visual C++。 

icc提供了 ** 過程間優化(Interprocedural Optimization) ** 技術，可以幫助編譯器在不同的目標文件之間進行全局優化。傳統的編譯器的編譯過程是編譯每個源文件到獨立的目標文件，然後再通過鏈接器將目標文件鏈接成可執行文件。傳統的編譯器的編譯優化主要集中在每個源文件內部，鏈接過程比較簡單，因此每個文件都是獨立的，而icc提供的過程間優化打破了這一限制。 

過程間優化可以對整個程序進行全局優化，而不是僅僅在單個文件、單個函數或者單個代碼塊內部優化。過程間優化可以減少過程之間重複計算、內存的低效訪問以及簡化迭代過程，通常會採用內聯函數的方式。過程間優化還可以重排代碼的順序以優化內存的分配方式和局部性。 

通過指定編譯參數 ` -ipo ` ，icc可以開啓過程間優化，icc將在編譯時生成特殊格式的目標文件（中間語言），並在鏈接時進行進一步的編譯和過程間優化，如圖所示： 

![](https://www.byvoid.com/upload/blog/icc-ipo-pgo/ipo.png)

使用icc啓動過程間優化的方式是在編譯參數中加上 ` -ipo ` 參數，還要設置環境變量 ` AR=xiar ` ，使用Intel的版本代替默認的 ` ar ` 。 

** 性能分析引導優化(Profile Guided Optimization) ** 通過分析程序運行時的實際行爲，將結果反饋給編譯器，使得編譯器可以重新安排代碼以減少指令緩存問題和分支預測誤判，從而獲得性能的提升。性能分析引導優化通過實際執行代碼統計出運行頻率最高的部分，編譯器通過這些信息可以更加針對地優化代碼。性能分析引導優化分爲三個階段： 

  1. 第一步是生成分析程序。在這個階段，編譯器創建一個有采樣注入的可執行程序。在icc中使用的編譯指令是 ` -prog-gen ` ，以及 ` -prof-dir=[dir] ` 。 
  2. 第二步是運行第一步生成的被注入採樣分析的程序，每次運行這個程序，都會生成 ` -prof-dir ` 指定的目錄下生成一個動態信息文件(dynamic information file)，將會被最終編譯時使用。 
  3. 第三步是最終編譯的步驟。第二次編譯的時候，動態信息文件會合併成一個彙總文件。通過彙總文件，編譯器會嘗試將最常使用的執行路徑優化。 

![](https://www.byvoid.com/upload/blog/icc-ipo-pgo/pgo.png)

過程間優化和性能分析引導優化可能會相互影響，性能分析引導優化通常會幫助編譯器生成內聯函數，這會幫助過程間優化的效率。性能分析引導優化對分支預測效率的提升最有效果，許多分支執行的可能性無法在編譯時判斷，而通過性能分析引導優化，編譯器可以針對經常執行的分支（熱代碼）和不經常執行的分支（冷代碼）生成高效的彙編代碼。 

使用性能分析引導優化的方法如下： 

  * 第一階段：編譯參數中加上： ` -prof-gen=srcpos -prof-dir=/tmp/profdata ` 。其中 ` -prof-dir ` 是存儲性能分析文件的目錄。 
  * 第二階段：運行編譯好的程序，然後運行 ` profmerge -prof_dir /tmp/profdata ` 生成彙總文件。 
  * 第三階段：重新編譯程序，使用參數： ` -prof-use=nomerge -prof-func-groups -prof-dir=/tmp/profdata ` 。 

這樣最終生成的代碼就是經過性能分析優化過後的了。 

以上方法在icc 14.0.2上試驗通過。 

##  參考 

  * [ Intel® C++ Compiler XE 13.1 User and Reference Guide ](https://software.intel.com/sites/products/documentation/doclib/iss/2013/compiler/cpp-lin/index.htm)
  * [ Intel® C++ Optimizing Applications ](http://www.ucl.ac.uk/isd/staff/research_services/research-computing/services/unity/environment/intel_cc___optimizing_applications.pdf)
#### 原文：[https://www.byvoid.com/blog/icc-ipo-pgo](https://www.byvoid.com/blog/icc-ipo-pgo)