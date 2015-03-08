#  HTML5拖拽文件以及显示文件

[ Yuguo ](http://yuguo.us) 2011年 03月 16日

利用支持HTML5（具体是拖拽API和File API）的浏览器拖拽图片/音频文件到浏览器窗口指定区域来看到预览（还未上传），需要了解的知识主要是拖拽API
，和通过拖拽事件获得File之后，对File进行相关信息读取。在HTML5出现之前读取文件信息操作往往是通过后台来实现，现在浏览器也具有了这样的能力，就能提
供更好的用户体验。需要的知识大概如下：

  1. (拖拽事件 API) 拖放文件到页面上的指定区域， ** [ drop事件 ](http://rebuildpattern.com/node/68) ** 发生 
  2. (拖拽事件 API) 从drop事件取得 ** [ DataTransfer ](http://rebuildpattern.com/node/64) ** 对象 
  3. (File API) 调用DataTransfer对象的files属性，得到 ** [ FileList ](http://rebuildpattern.com/node/64) ** ，它代表了拖放文件的列表。 
  4. (File API) 遍历FileList，得到每一个单独的 ** [ File对象 ](http://rebuildpattern.com/node/64) ** 。 
  5. (File API) 通过 ** [ FileReader对象 ](http://rebuildpattern.com/node/65) ** 来读取每一个File对象的内容（FileReader.readAsDataURL(file)）。然后一个新的 ** [ data URI ](http://rebuildpattern.com/node/69) ** 格式对象被创建，然后剩下的就交给onloadend回调函数来处理。 
  6. (File API) 现在我们通过对拖拽文件的处理得到了一个“data URL”，比如显示图片和MP3播放器。或者可以通过读取 ** text ** 来获得拖拽css文件的文本内容。 

[ 优秀的人就应该在优秀的地方 → ](/weblog/stay-excellent/) [ ← 写一些简短的东西 ](/weblog/write-
short/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

