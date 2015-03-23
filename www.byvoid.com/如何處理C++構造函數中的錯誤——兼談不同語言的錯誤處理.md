title: 如何處理C++構造函數中的錯誤——兼談不同語言的錯誤處理

date: 2013-05-08 13:14:16

tags: [C++, 錯誤處理, 異常, 返回值, ABI, 控制流, 構造函數, 析構函數, 初始化列表, Python, Go, panic, recover, defer, Basic, Visual Basic, Java, 檢查型異常, 非檢查型異常, ]

description: 

---
# 

用C++寫代碼的時候總是避免不了處理錯誤，一般來說有兩種方式，通過函數的返回值或者拋出異常。C語言的錯誤處理一律是通過函數的返回值來判斷的，一般是返回`0`、`NULL`或者`-1`表示錯誤，或者直接返回錯誤代碼，具體是哪種方式沒有統一的規定，各種API也各有各的偏好。譬如`fopen`函數，當成功時返回文件指針，失敗時返回`NULL`，而POSIX標準的`open`函數則在成功時返回`0`或者正數，失敗時返回`-1`，然後需要再通過全局變量`errno`來判斷具體錯誤是什麼，配套的還有一系列`perror`、`strerror`這樣的函數。

## C++的錯誤處理方式

C++號稱向下兼容C語言，於是就將C語言通過返回值的錯誤處理方式也搬了進來。但C++最大的不同是引入了異常機制，可以用`throw`產生一個異常，並通過`try`和`catch`來捕獲。於是就混亂了，到底是什麼時候使用返回值表示錯誤，什麼時候使用異常呢？首先簡單談論一下異常和返回值的特點。

### 異常的優點

  1. 錯誤信息豐富，便於獲得錯誤現場
  2. 代碼相對簡短，不需要判斷每個函數的返回值

### 異常的缺點

  1. 使控制流變得複雜，難以追蹤
  2. 開銷相對較大

### 返回值的優點

  1. 性能開銷相對小
  2. 避免定義異常類

### 返回值的缺點

  1. 程序員經常「忘記」處理錯誤返回值
  2. 每個可能產生錯誤的函數在調用後都需要判斷是否有錯誤
  3. 與「真正的」返回值混用，需要規定一個錯誤代碼（通常是`0`、`-1`或`NULL`）

## 使用異常還是返回值

我的觀點是，用異常來表示真正的、而且不太可能發生的錯誤。所謂不太可能發生的錯誤，指的是真正難以預料，但發生了卻又不得不單獨處理的，譬如內存耗盡、讀文件發生故障。而在一個字符串中查找一個子串，如果沒有找到顯然應該是用一個特殊的返回值（如`-1`），而不應該拋出一個異常。

一句話來概況就是**不要用異常代替正常的控制流**，只有當程序真的「不正常」的時候，纔使用異常。反過來說，當程序真正發生錯誤了，一定要使用異常而不是返回一個錯誤代碼，因爲錯誤代碼總是傾向於被忽略。如果要保證一個以返回值來表示錯誤代碼的函數的錯誤正確地向上傳遞，需要在每個調用了可能產生錯誤的函數後面都判斷一下是否發生了錯誤，一旦發生了不可解決的錯誤，就要終止當前函數（並釋放當前函數申請的資源），然後向上傳遞錯誤。這樣一來錯誤處理代碼會被重複地寫好幾遍，十分冗雜，譬如下面代碼：
    
    
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

對使用異常容易增加函數出口的指控其實是不成立的，因爲即使使用返回值，這些出口也是免不了的，除非程序員有意或無意忽略掉，但異常是不可忽略的。如果你認爲可以把判斷錯誤的`if`語句縮寫到一行使代碼變得「更清晰」，那麼我只能說是自欺欺人。

有些錯誤幾乎總是可以被立即恢復（譬如前面所說的查找一個字符串不存在的子串，甚至都不能說這是一個「錯誤」），而且返回值本身就傳遞一定信息，就不需要使用異常了。

鑑於C++沒有統一的ABI，並不建議在模塊的接口上使用異常。如果要使用，就要把可能曝露給用戶的異常全部聲明出來，不要把其他類型的異常丟給用戶去處理，尤其是內部狀態——模塊的使用者通常也不會關心模塊內部具體是哪條語句發生錯誤了。

## 構造函數中的錯誤

有一個相當實際的問題是，如何處理構造函數的錯誤？我們都知道構造函數是沒有返回值的，怎麼辦呢？通常有三種常見的處理方法，**標記錯誤狀態**、**使用一個額外的`initialize`函數來初始化**，或者直接**拋出異常**。

合格的C++程序員都知道C++的析構函數中不應該拋出異常，一旦析構函數中的異常沒有被捕獲，整個程序都要被中止掉。於是許多人就對在構造函數中拋出異常也產生了對等的恐懼，寧可使用一個額外的初始化函數在裏面初始化對象的狀態並拋出異常（或者返回錯誤代碼）。這樣做違背了對象產生和初始化要在一起的原則，強迫用戶記住調用一個額外的初始化函數，一旦沒有調用直接使用了其他函數，其行爲很可能是未定義的。

使用初始化函數的惟一好處可能是避免了手動釋放資源（釋放資源的操作交給析構函數來做），因爲C++的一個特點是構造函數拋出異常以後析構函數是不會被調用的，所以如果你在構造函數裏面申請了內存或者打開了資源，需要在異常產生時關閉。但想想看其實並不能完全避免，因爲有些資源可能是要在可能產生錯誤的函數調用過後纔被申請的，還是無法完全避免手工的釋放。

標記錯誤狀態也是一種常見的形式，譬如STL中的`ifstream`類，當構造時傳入一個無法訪問的文件作爲參數，它不會返回任何錯誤，而是標記的內部狀態爲不可用，用戶需要手工通過`is_open()`函數來判斷是否打開成功了。同時它還有`good()`、`fail()`兩個函數，同時也重載了`bool`類型轉換運算符用於在`if`語句中判斷。標記狀態的方法在實踐中相當醜陋，因爲在使用前總是需要判斷它是否「真的創建成功了」。

最直接的方法還是在構造函數中拋出異常，它並不會向析構函數中拋出異常那樣有嚴重的後果，只是需要注意的是拋出異常以後對象沒有被創建成功，析構函數也不會被調用，所以應該自行把申請的資源全部都釋放掉。

## 如何在構造函數中捕獲異常

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

以上的代碼中`A`的構造函數的函數體的語句在執行之前會先調用`B`的構造函數，這時候問題在於，如果`B`的構造函數拋出了異常，`A`該如何捕獲呢？一個迂迴的做法是在`A`中把`B`的實例聲明爲指針，在構造函數和析構函數中分別創建和刪除，這樣就能捕獲到異常了。不過，實際上是有更簡單的做法的。下面我要介紹一個C++的很不常見的語法：函數作用域級別的異常捕獲。
    
    
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

注意上面`A`的構造函數，在參數列表後和初始化列表前增加了`try`關鍵字，然後構造函數就被分割爲了兩部分，前面是初始化，後面是初始化時的錯誤處理。需要指出的是，`catch`塊裏面捕獲到的異常不能被忽略，即`catch`塊中必須有一個`throw`語句重新拋出異常，如果沒有，則默認會將原來捕獲到的異常重新拋出，這和一般的行爲是不同的。例如下面代碼運行可以發現`A`會將捕獲到的異常原封不動拋出：
    
    
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

這種語法是C++的標準，而且目前已經被所有的主流C++編譯器支持（VS2010、g++ 4.2、clang 3.1），所以幾乎不存在兼容性問題，大可放心使用。

## 其他語言中的錯誤處理

Java傾向於大量使用異常，而且還把異常分爲了兩類分別是檢查型異常(Checked Exception)和非檢查型異常(Unchecked Exception)，檢查型異常就是`java.lang.Exception`的子類，用於報告需要檢查的錯誤，也就是正常的業務邏輯，錯誤主要是由用戶產生的，方便恢復或給出提示，譬如打開不存在的文件。而非檢查型異常則是真正的系統異常，通常由軟件缺陷導致，如數組下標越界、錯誤的類型轉換等，這類異常繼承於`java.lang.RuntimeException`或`java.lang.Error`。

Python和Java一樣也傾向於使用異常，並不一定真的發生故障纔拋出異常，譬如字符串轉換爲整數，如果字符串不合法，Python會拋出一個`ValueError`異常。甚至Python的迭代器在調用`next()`時沒有更多的結果時會拋出`StopIteration`異常。這是典型的用異常來處理正常控制流的方法，在Python中被廣泛使用。按照優秀C++代碼的標準來看，這是典型的對異常的濫用，既複雜又有額外開銷，不推薦使用，但在Python中這是一個廣泛遵循的約定。

相較於Java和Python，Go的錯誤處理是另一個極端，Go語言則根本沒有異常的概念，而是普遍採用返回值的方式來表示錯誤，同時還提供了`panic`和`recover`語法。由於Go有多返回值的特性，避免了錯誤代碼佔用返回結果的弊端，所以你可以經常看到函數的最後一個返回值是`error`類型。由於總是用返回值傳遞錯誤，你可以看到Go代碼中耦合了大量的錯誤處理，幾乎再每條函數調用語句之後都有一個判斷錯誤是否發生的語句。`panic`和`recover`機制十分類似於異常，程序在遇到`panic`時會一層一層退出調用棧，直到遇到`recover`。不過`recover`只在`defer`中定義，相當於一個函數只有一個`recover`，而且被`recover`恢復後會回到錯誤發生處繼續向下執行代碼。Go語言傾向於把一般錯誤都作爲返回值傳遞，除非是非常可怕的、除了重置狀態幾乎無法恢復錯誤纔會被`panic`語句拋出。

Go語言的`recover`機制和異常比起來，反倒更像Visual Basic語言中的`On Error GoTo label`及`Resume`語法。這是一種非結構化的錯誤處理方式，具體是當聲明有`On Error GoTo label`的函數發生錯誤以後，會調轉到對應的行號，如果再遇到了`Resume`語句就會返回發生錯誤的語句後面的一條繼續執行，例如下面這段代碼：
    
    
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

Visual Basic中還有`On Error Resume Next`這樣的萬能錯誤處理語句，即遇到錯誤以後直接忽略並繼續執行，這是一種非常危險而且不負責任的做法，但卻可以在早期的Visual Basic代碼中到處看到。事實上用返回值傳遞錯誤代碼的時候許多人也並不處理而是直接忽略，這跟`On Error Resume Next`本質上沒有什麼區別，卻比`On Error Resume Next`危害更大——因爲`On Error Resume Next`至少還有個標記說明「老子就是這麼不負責任」，但忽略錯誤返回值就難以被一眼發現了。

## 參考閱讀

  * [Exceptions vs. status returns](http://nedbatchelder.com/text/exceptions-vs-status.html)
  * [“拥抱”异常，还是，“固守”返回值？](http://blog.dccmx.com/2011/11/raise-exception-or-return-status/)
  * [How can I handle a constructor that fails?](http://www.parashift.com/c++-faq-lite/ctors-can-throw.html)
  * [Constructors and Exception in C++](http://www.cs.technion.ac.il/~imaman/programs/throwingctor.html)
  * [如何设计一门语言（三）——什么是坑(面向对象和异常处理)](http://www.cppblog.com/vczh/archive/2013/05/05/199974.html)
  * [Why does Go not have exceptions?](http://golang.org/doc/faq#exceptions)
  * [Defer, Panic, and Recover](http://blog.golang.org/2010/08/defer-panic-and-recover.html)
  * [Unstructured Exception Handling Overview](http://msdn.microsoft.com/en-US/library/sf1hwa21.aspx)
