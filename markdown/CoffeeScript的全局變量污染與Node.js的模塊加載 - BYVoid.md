六月  ** 29 ** 2013 

  *   *   *     * [ JavaScript ](/blog/tag/JavaScript)
    * [ CoffeeScript ](/blog/tag/CoffeeScript)
    * [ Continuation.js ](/blog/tag/Continuation.js)
    * [ 命名空間 ](/blog/tag/命名空間)
    * [ 全局變量 ](/blog/tag/全局變量)
    * [ 編譯 ](/blog/tag/編譯)
    * [ JIT ](/blog/tag/JIT)
    * [ Node.js ](/blog/tag/Node.js)
    * [ 模塊 ](/blog/tag/模塊)
    * [ 加載 ](/blog/tag/加載)
    * [ 設計開發 ](/blog/tag/設計開發)

#  [ CoffeeScript的全局變量污染與Node.js的模塊加載 ](/blog/coffee-script-global-variable-pollution)

最近發現 [ Continuation.js ](/project/continuation) 的一個Bug：命令行使用 ` -c ` 開啓緩存模式的時候，有時候更新了代碼緩存不會更新，這個Bug時隱時現，難以捕捉。今天發現這個Bug升級了，不僅僅是在緩存模式的時候會有問題，即時沒有開啓 ` -c ` 一樣會發生這個問題。再到後來發現這個Bug只在CoffeeScript代碼中出現，於是就鎖定了目標開始調試。 

[ Continuation.js ](/project/continuation) 和CoffeeScript一樣支持動態加載編譯，就是可以在Node.js中使用 ` require ` 的方法加載原始代碼，運行時編譯。這樣的好處不言而喻，給用戶提供了一致而透明的接口，無需事先編譯好再加載。具體的實現方法是，修改 ` require.extensions ` 下面的回調函數，把加載定向到自定義的函數來處理，最後再調用 ` require.main.compile ` 運行編譯後的代碼。 

` require ` 和 ` module ` 是Node.js運行時的兩個重要變量，所有模塊的運行其實都是在一個這樣的函數中的： 
    
    
    function(module, require) {
      // Your code
    }

所以 ` require ` 和 ` module ` 是模塊內的全局變量。 ` require.extensions ` 是一個對象，用於根據擴展名註冊 ` require ` 的回調函數，默認情況下， ` require.extensions ` 是這樣的（Node.js 0.10.12）： 
    
    
    {
      '.js': function (module, filename) {
        var content = NativeModule.require('fs').readFileSync(filename, 'utf8');
        module._compile(stripBOM(content), filename);
      },
      '.json': function (module, filename) {
        var content = NativeModule.require('fs').readFileSync(filename, 'utf8');
        try {
          module.exports = JSON.parse(stripBOM(content));
        } catch (err) {
          err.message = filename + ': ' + err.message;
          throw err;
        }
      },
      '.node': function () { [native code] }
    }

在Node.js代碼中使用 ` require(filename) ` 時，實際上會根據 ` filename ` 的後綴擴展名依次來選擇加載的回調函數，例如我想增加一種自定義的自動加載類型 ` .byv ` ，只需設置 ` require.extensions['.byv'] ` 即可。同理，也可以修改已有的後綴的加載函數， [ Continuation.js ](/project/continuation) 就是這麼做的（修改了 ` .js ` 文件的加載函數）。 

爲了透明支持CoffeeScript， [ Continuation.js ](/project/continuation) 修改了 ` .coffee ` 的加載函數，在自定義的回調函數中調用CoffeeScript模塊，調用CoffeeScript編譯，然後再使用Continuation.js編譯。問題就在這裏，是加載CoffeeScript的時候 ` require.extensions['.coffee'] ` 被修改了。閱讀CoffeeScript的代碼（版本1.6.3），發現在 ` 'coffee-script' ` 模塊中，有這麼幾行代碼： 
    
    
    if require.extensions
      for ext in ['.coffee', '.litcoffee', '.coffee.md']
        require.extensions[ext] = loadFile

這段代碼不應該在加載CoffeeScript模塊中運行，而應該在通過命令行運行 ` coffee ` 命令的時候運行，可惜CoffeeScript沒有注意到這一點，應該算是一個Bug吧。給CoffeeScript提交了一個推送請求 [ https://github.com/jashkenas/coffee-script/pull/3054 ](https://github.com/jashkenas/coffee-script/pull/3054) ，等待審覈中。 

更新：這個issue被標註爲重複，已經在 [ https://github.com/jashkenas/coffee-script/issues/2323 ](https://github.com/jashkenas/coffee-script/issues/2323) 合併了，CoffeeScript 2.0.0（未發佈）以後默認已經取消這個特性了。 
#### 原文：[https://www.byvoid.com/blog/coffee-script-global-variable-pollution](https://www.byvoid.com/blog/coffee-script-global-variable-pollution)