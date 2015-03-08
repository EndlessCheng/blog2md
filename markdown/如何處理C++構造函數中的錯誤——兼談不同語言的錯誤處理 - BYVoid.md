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

五月  ** 8 ** 2013

  * 作者:  byvoid 
  * 閱讀: 6884 
  *     * [ C++ ](/blog/tag/C++)
    * [ 錯誤處理 ](/blog/tag/錯誤處理)
    * [ 異常 ](/blog/tag/異常)
    * [ 返回值 ](/blog/tag/返回值)
    * [ ABI ](/blog/tag/ABI)
    * [ 控制流 ](/blog/tag/控制流)
    * [ 構造函數 ](/blog/tag/構造函數)
    * [ 析構函數 ](/blog/tag/析構函數)
    * [ 初始化列表 ](/blog/tag/初始化列表)
    * [ Python ](/blog/tag/Python)
    * [ Go ](/blog/tag/Go)
    * [ panic ](/blog/tag/panic)
    * [ recover ](/blog/tag/recover)
    * [ defer ](/blog/tag/defer)
    * [ Basic ](/blog/tag/Basic)
    * [ Visual Basic ](/blog/tag/Visual Basic)
    * [ Java ](/blog/tag/Java)
    * [ 檢查型異常 ](/blog/tag/檢查型異常)
    * [ 非檢查型異常 ](/blog/tag/非檢查型異常)

#  [ 如何處理C++構造函數中的錯誤——兼談不同語言的錯誤處理 ](/blog/cpp-constructor-exception)

用C++寫代碼的時候總是避免不了處理錯誤，一般來說有兩種方式，通過函數的返回值或者拋出異常。C語言的錯誤處理一律是通過函數的返回值來判斷的，一般是返回 `
0 ` 、 ` NULL ` 或者 ` -1 ` 表示錯誤，或者直接返回錯誤代碼，具體是哪種方式沒有統一的規定，各種API也各有各的偏好。譬如 `
fopen ` 函數，當成功時返回文件指針，失敗時返回 ` NULL ` ，而POSIX標準的 ` open ` 函數則在成功時返回 ` 0 `
或者正數，失敗時返回 ` -1 ` ，然後需要再通過全局變量 ` errno ` 來判斷具體錯誤是什麼，配套的還有一系列 ` perror ` 、 `
strerror ` 這樣的函數。

##  C++的錯誤處理方式

C++號稱向下兼容C語言，於是就將C語言通過返回值的錯誤處理方式也搬了進來。但C++最大的不同是引入了異常機制，可以用 ` throw `
產生一個異常，並通過 ` try ` 和 ` catch `
來捕獲。於是就混亂了，到底是什麼時候使用返回值表示錯誤，什麼時候使用異常呢？首先簡單談論一下異常和返回值的特點。

###  異常的優點

  1. 錯誤信息豐富，便於獲得錯誤現場 
  2. 代碼相對簡短，不需要判斷每個函數的返回值 

###  異常的缺點

  1. 使控制流變得複雜，難以追蹤 
  2. 開銷相對較大 

###  返回值的優點

  1. 性能開銷相對小 
  2. 避免定義異常類 

###  返回值的缺點

  1. 程序員經常「忘記」處理錯誤返回值 
  2. 每個可能產生錯誤的函數在調用後都需要判斷是否有錯誤 
  3. 與「真正的」返回值混用，需要規定一個錯誤代碼（通常是 ` 0 ` 、 ` -1 ` 或 ` NULL ` ） 

##  使用異常還是返回值

我的觀點是，用異常來表示真正的、而且不太可能發生的錯誤。所謂不太可能發生的錯誤，指的是真正難以預料，但發生了卻又不得不單獨處理的，譬如內存耗盡、讀文件發生故
障。而在一個字符串中查找一個子串，如果沒有找到顯然應該是用一個特殊的返回值（如 ` -1 ` ），而不應該拋出一個異常。

一句話來概況就是 ** 不要用異常代替正常的控制流 ** ，只有當程序真的「不正常」的時候，纔使用異常。反過來說，當程序真正發生錯誤了，一定要使用異常而不是
返回一個錯誤代碼，因爲錯誤代碼總是傾向於被忽略。如果要保證一個以返回值來表示錯誤代碼的函數的錯誤正確地向上傳遞，需要在每個調用了可能產生錯誤的函數後面都判斷
一下是否發生了錯誤，一旦發生了不可解決的錯誤，就要終止當前函數（並釋放當前函數申請的資源），然後向上傳遞錯誤。這樣一來錯誤處理代碼會被重複地寫好幾遍，十分冗
雜，譬如下面代碼：

    
    
    int func(int n) {
      int fd = open("path/to/file", O_RDONLY);
      if (fd == -1) {
         return ERROR_OPEN;
      }
      int* array = new[n];
      int err;
      err = do_something(fd, array);
      if (err != SUCCESS) {
         delete[] array;
         return err;
      }
      err = do_other_thing();
      if (err != SUCCESS) {
         delete[] array;
         return err;
      }
      err = do_more_thing();
      if (err != SUCCESS) {
         delete[] array;
         return err;
      }
      delete[] array;
      return SUCCESS;
    }

對使用異常容易增加函數出口的指控其實是不成立的，因爲即使使用返回值，這些出口也是免不了的，除非程序員有意或無意忽略掉，但異常是不可忽略的。如果你認爲可以把判
斷錯誤的 ` if ` 語句縮寫到一行使代碼變得「更清晰」，那麼我只能說是自欺欺人。

有些錯誤幾乎總是可以被立即恢復（譬如前面所說的查找一個字符串不存在的子串，甚至都不能說這是一個「錯誤」），而且返回值本身就傳遞一定信息，就不需要使用異常了。

鑑於C++沒有統一的ABI，並不建議在模塊的接口上使用異常。如果要使用，就要把可能曝露給用戶的異常全部聲明出來，不要把其他類型的異常丟給用戶去處理，尤其是內
部狀態——模塊的使用者通常也不會關心模塊內部具體是哪條語句發生錯誤了。

##  構造函數中的錯誤

有一個相當實際的問題是，如何處理構造函數的錯誤？我們都知道構造函數是沒有返回值的，怎麼辦呢？通常有三種常見的處理方法， ** 標記錯誤狀態 ** 、 **
使用一個額外的 ` initialize ` 函數來初始化 ** ，或者直接 ** 拋出異常 ** 。

合格的C++程序員都知道C++的析構函數中不應該拋出異常，一旦析構函數中的異常沒有被捕獲，整個程序都要被中止掉。於是許多人就對在構造函數中拋出異常也產生了對
等的恐懼，寧可使用一個額外的初始化函數在裏面初始化對象的狀態並拋出異常（或者返回錯誤代碼）。這樣做違背了對象產生和初始化要在一起的原則，強迫用戶記住調用一個
額外的初始化函數，一旦沒有調用直接使用了其他函數，其行爲很可能是未定義的。

使用初始化函數的惟一好處可能是避免了手動釋放資源（釋放資源的操作交給析構函數來做），因爲C++的一個特點是構造函數拋出異常以後析構函數是不會被調用的，所以如
果你在構造函數裏面申請了內存或者打開了資源，需要在異常產生時關閉。但想想看其實並不能完全避免，因爲有些資源可能是要在可能產生錯誤的函數調用過後纔被申請的，還
是無法完全避免手工的釋放。

標記錯誤狀態也是一種常見的形式，譬如STL中的 ` ifstream `
類，當構造時傳入一個無法訪問的文件作爲參數，它不會返回任何錯誤，而是標記的內部狀態爲不可用，用戶需要手工通過 ` is_open() `
函數來判斷是否打開成功了。同時它還有 ` good() ` 、 ` fail() ` 兩個函數，同時也重載了 ` bool ` 類型轉換運算符用於在 `
if ` 語句中判斷。標記狀態的方法在實踐中相當醜陋，因爲在使用前總是需要判斷它是否「真的創建成功了」。

最直接的方法還是在構造函數中拋出異常，它並不會向析構函數中拋出異常那樣有嚴重的後果，只是需要注意的是拋出異常以後對象沒有被創建成功，析構函數也不會被調用，所
以應該自行把申請的資源全部都釋放掉。

##  如何在構造函數中捕獲異常

構造函數與普通函數有一個很不一樣特性，就是構造函數可以有初始化列表，例如下面的代碼：

    
    
    class B {
     public:
      B(int val) : val_(val * val) {
      }
     private:
      int val_;
    };
    
    class A {
     public:
      A(int val) : b_(val) {
        a_ = val;
      }
     private:
      int a_;
      B b_;
    };

以上的代碼中 ` A ` 的構造函數的函數體的語句在執行之前會先調用 ` B ` 的構造函數，這時候問題在於，如果 ` B ` 的構造函數拋出了異常， `
A ` 該如何捕獲呢？一個迂迴的做法是在 ` A ` 中把 ` B ` 的實例聲明爲指針，在構造函數和析構函數中分別創建和刪除，這樣就能捕獲到異常了。不過，
實際上是有更簡單的做法的。下面我要介紹一個C++的很不常見的語法：函數作用域級別的異常捕獲。

    
    
    class B {
     public:
      B(int val) : val_(val * val) {
        throw runtime_error("wtf from B");
      }
     private:
      int val_;
    };
    
    class A {
     public:
      A(int val) try : b_(val) {
        a_ = val;
      } catch (runtime_error& e) {
        cerr << e.what() << endl;
        throw runtime_error("wtf from A");
      }
     private:
      int a_;
      B b_;
    };

注意上面 ` A ` 的構造函數，在參數列表後和初始化列表前增加了 ` try `
關鍵字，然後構造函數就被分割爲了兩部分，前面是初始化，後面是初始化時的錯誤處理。需要指出的是， ` catch ` 塊裏面捕獲到的異常不能被忽略，即 `
catch ` 塊中必須有一個 ` throw `
語句重新拋出異常，如果沒有，則默認會將原來捕獲到的異常重新拋出，這和一般的行爲是不同的。例如下面代碼運行可以發現 ` A ` 會將捕獲到的異常原封不動拋出：

    
    
    class A {
     public:
      A(int val) try : b_(val) {
        a_ = val;
      } catch (runtime_error& e) {
        cerr << e.what() << endl;
      }
     private:
      int a_;
      B b_;
    };

這種語法是C++的標準，而且目前已經被所有的主流C++編譯器支持（VS2010、g++ 4.2、clang
3.1），所以幾乎不存在兼容性問題，大可放心使用。

##  其他語言中的錯誤處理

Java傾向於大量使用異常，而且還把異常分爲了兩類分別是檢查型異常(Checked Exception)和非檢查型異常(Unchecked
Exception)，檢查型異常就是 ` java.lang.Exception ` 的子類，用於報告需要檢查的錯誤，也就是正常的業務邏輯，錯誤主要是由用戶
產生的，方便恢復或給出提示，譬如打開不存在的文件。而非檢查型異常則是真正的系統異常，通常由軟件缺陷導致，如數組下標越界、錯誤的類型轉換等，這類異常繼承於 `
java.lang.RuntimeException ` 或 ` java.lang.Error ` 。

Python和Java一樣也傾向於使用異常，並不一定真的發生故障纔拋出異常，譬如字符串轉換爲整數，如果字符串不合法，Python會拋出一個 `
ValueError ` 異常。甚至Python的迭代器在調用 ` next() ` 時沒有更多的結果時會拋出 ` StopIteration ` 異常。這
是典型的用異常來處理正常控制流的方法，在Python中被廣泛使用。按照優秀C++代碼的標準來看，這是典型的對異常的濫用，既複雜又有額外開銷，不推薦使用，但在
Python中這是一個廣泛遵循的約定。

相較於Java和Python，Go的錯誤處理是另一個極端，Go語言則根本沒有異常的概念，而是普遍採用返回值的方式來表示錯誤，同時還提供了 ` panic `
和 ` recover ` 語法。由於Go有多返回值的特性，避免了錯誤代碼佔用返回結果的弊端，所以你可以經常看到函數的最後一個返回值是 ` error `
類型。由於總是用返回值傳遞錯誤，你可以看到Go代碼中耦合了大量的錯誤處理，幾乎再每條函數調用語句之後都有一個判斷錯誤是否發生的語句。 ` panic ` 和
` recover ` 機制十分類似於異常，程序在遇到 ` panic ` 時會一層一層退出調用棧，直到遇到 ` recover ` 。不過 `
recover ` 只在 ` defer ` 中定義，相當於一個函數只有一個 ` recover ` ，而且被 ` recover `
恢復後會回到錯誤發生處繼續向下執行代碼。Go語言傾向於把一般錯誤都作爲返回值傳遞，除非是非常可怕的、除了重置狀態幾乎無法恢復錯誤纔會被 ` panic `
語句拋出。

Go語言的 ` recover ` 機制和異常比起來，反倒更像Visual Basic語言中的 ` On Error GoTo label ` 及 `
Resume ` 語法。這是一種非結構化的錯誤處理方式，具體是當聲明有 ` On Error GoTo label `
的函數發生錯誤以後，會調轉到對應的行號，如果再遇到了 ` Resume ` 語句就會返回發生錯誤的語句後面的一條繼續執行，例如下面這段代碼：

    
    
    Sub ErrorDemo
        On Error GoTo ErrorHandler
        Dim a as Integer
        a = 1/0 ' An error occurs.
        Print a ' Go back here
        Exit Sub
    
    ErrorHandler:
        ' Code that handles errors.
        Resume
    End Sub

Visual Basic中還有 ` On Error Resume Next `
這樣的萬能錯誤處理語句，即遇到錯誤以後直接忽略並繼續執行，這是一種非常危險而且不負責任的做法，但卻可以在早期的Visual
Basic代碼中到處看到。事實上用返回值傳遞錯誤代碼的時候許多人也並不處理而是直接忽略，這跟 ` On Error Resume Next `
本質上沒有什麼區別，卻比 ` On Error Resume Next ` 危害更大——因爲 ` On Error Resume Next `
至少還有個標記說明「老子就是這麼不負責任」，但忽略錯誤返回值就難以被一眼發現了。

##  參考閱讀

  * [ Exceptions vs. status returns ](http://nedbatchelder.com/text/exceptions-vs-status.html)
  * [ “拥抱”异常，还是，“固守”返回值？ ](http://blog.dccmx.com/2011/11/raise-exception-or-return-status/)
  * [ How can I handle a constructor that fails? ](http://www.parashift.com/c++-faq-lite/ctors-can-throw.html)
  * [ Constructors and Exception in C++ ](http://www.cs.technion.ac.il/~imaman/programs/throwingctor.html)
  * [ 如何设计一门语言（三）——什么是坑(面向对象和异常处理) ](http://www.cppblog.com/vczh/archive/2013/05/05/199974.html)
  * [ Why does Go not have exceptions? ](http://golang.org/doc/faq#exceptions)
  * [ Defer, Panic, and Recover ](http://blog.golang.org/2010/08/defer-panic-and-recover.html)
  * [ Unstructured Exception Handling Overview ](http://msdn.microsoft.com/en-US/library/sf1hwa21.aspx)

##  相關日誌

  * [ C++中fstream的用法 ](/blog/cpp-fstream)
  * [ Topcoder Arena 居然与 Scim 冲突 ](/blog/topcoder-arena-scim-conflict)
  * [ Linux C语言编程学习笔记 (1)进程控制入门 ](/blog/linux-c-1)
  * [ C语言字符串函数大全 ](/blog/c-string)
  * [ Thinking in Delphi：语言的变革 ](/blog/thinking-in-delphi)
  * [ 省队培训日志3 ](/blog/noi2008-province-3)
  * [ 探寻C++最快的读取文件的方案 ](/blog/fast-readfile)
  * [ 小话随机数 ](/blog/crand)
  * [ C++ string 用法详解 ](/blog/cpp-string)
  * [ C/C++的64位整型 ](/blog/c-int64)

Search for:

####  語言

  * [ 原文 ](/blog/cpp-constructor-exception)
  * [ 正體中文 ](/zht/blog/cpp-constructor-exception)
  * [ 簡體中文 ](/zhs/blog/cpp-constructor-exception)
  * [ English ](/en/blog/cpp-constructor-exception)

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

