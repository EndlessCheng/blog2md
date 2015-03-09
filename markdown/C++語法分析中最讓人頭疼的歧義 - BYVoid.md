五月  ** 22 ** 2013 

  *   *   *     * [ C++ ](/blog/tag/C++)
    * [ 語法分析 ](/blog/tag/語法分析)
    * [ 編譯 ](/blog/tag/編譯)
    * [ 編譯器 ](/blog/tag/編譯器)
    * [ C++11 ](/blog/tag/C++11)
    * [ 歧義 ](/blog/tag/歧義)
    * [ 函數聲明 ](/blog/tag/函數聲明)

#  [ C++語法分析中最讓人頭疼的歧義 ](/blog/cpp-most-vexing-parse)

C++是個特別複雜的語言，其複雜性不僅體現在開發模式上，也體現在語法分析上。許多人都遇到過嵌套模板參數的歧義問題，如 ` vector<vector<int>> v ` ，在有些編譯器上會被解析爲 ` vector < vector < int >> v ` ，但新的編譯器都已經解決了。而最讓人頭疼的歧義則是 [ Most vexing parse ](http://en.wikipedia.org/wiki/Most_vexing_parse) ： 
    
    
    class Timer {
     public:
      Timer() {}
    };
    
    class TimeKeeper {
     public:
      TimeKeeper(const Timer& t) {}
      int get_time() {return 0;}
    };
    
    int main() {
      TimeKeeper time_keeper(Timer());
      return time_keeper.get_time();
    }

以上代碼中出現歧義的是 ` TimeKeeper time_keeper(Timer()); ` ，因爲它有兩種理解方式： 

  1. 定義一個 ` TimeKeeper ` 類型的對象，並用 ` Timer() ` 作爲初始化參數。 
  2. 聲明一個名叫 ` time_keeper ` 的函數，它的返回值類型是 ` TimeKeeper ` ，參數是一個函數指針，這個函數指針指向的函數的返回值是 ` Timer ` ，無參數。 

很明顯我們想要表達的是第一種意思，但很不幸編譯器會默認理解爲第二種。Clang++會給出以下錯誤： 
    
    
    timekeeper.cc:15:21: error: member reference base type 'TimeKeeper (Timer (*)())' is not a
          structure or union
      return time_keeper.get_time();
              ~~~~~~~~~~~^~~~~~~~~

之所以產生這種歧義，是因爲這幾個原因： 

  1. C++的函數在使用前需要聲明，定義和聲明是可以分離的。 
  2. C++的函數聲明的參數可以只有類型，沒有名稱，如 ` int max(int, int); ` 。 
  3. C++的函數聲明的參數名在類型名後可以加 ` () ` ，如 ` int max(int (a), int()) ` 。 
  4. C++的函數聲明可以在函數體中。 

最優美的解決方案是使用C++11的統一初始化語法： 
    
    
    TimeKeeper time_keeper{Timer()};
#### 原文：[https://www.byvoid.com/blog/cpp-most-vexing-parse](https://www.byvoid.com/blog/cpp-most-vexing-parse)