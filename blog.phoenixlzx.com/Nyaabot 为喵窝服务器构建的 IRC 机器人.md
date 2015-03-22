title: Nyaabot 为喵窝服务器构建的 IRC 机器人

date: 2014-02-16T11:19:34.000Z

tags: [Node.js, Minecraft, ]

description: 

---
第一次写 IRC 机器人。之前已经看到仙子酱等等菊苣们写了好多种 IRC 机器人，但是都是 Python 写的。倒不是歧视 Python 啊什么的… 主要是咱服务器上木有方便的环境跑，而且也有需要自己做的功能。正好在逛 NPM 的时候发现了 [ node-irc ](https://npmjs.org/node-irc) 这个包，于是折腾一下午搞出来一个机器人程序。 

目前主要纠结的问题是 IRC 没有类似 HTTP Status code 或者类似的指示代码，所以我能想到的处理办法就是验证字符串。好吧我承认这种方法很不靠谱，但是… 各种求靠谱方法啊… 

###  客户端配置 

专门写了一个 ` config.js ` 来保存客户端的配置。根据 [ node-irc 的文档 ](https://node-irc.readthedocs.org/en/latest/index.html) ，在程序中做如下参数设定。 
    
    
    serveroptions: {
    
        userName: 'nyaabot',
    
        realName: 'Nyaacat IRC Bot',
    
        port: 7000,
    
        debug: false,
    
        showErrors: false,
    
        autoRejoin: true,
    
        autoConnect: true,
    
        channels: ['#nyaacat'],
    
        secure: true,
    
        selfSigned: false,
    
        certExpired: false,
    
        floodProtection: true,
    
        floodProtectionDelay: 1000,
    
        sasl: false,
    
        stripColors: true,
    
        channelPrefixes: "",
    
        messageSplit: 512
    
    }  
  
---  
  
看起来都是很好懂的嗯。昨天在配置 CraftIRC 插件的时候撞到一个坑，NickServ 一直报错说参数不完整。调了半天发现是这里的 ` realName ` 部分没有填写，于是这次特地写上了注释要求该项必须填写。 

###  帐户验证 

之后发现木有类似验证帐号的部分。查了下找到了 [ issue #205 ](https://github.com/martynsmith/node-irc/issues/205) 。原来验证并没有在 IRC RFC 里规定，因此没有包含在库里。嘛好吧，只好自己写了。 
    
    
    nyaa.addListener("notice", function (from, to, text, message) {
    
        // console.log(from + '\n' + to + '\n' + text + '\n' + util.inspect(message, false, null));
    
        if (from === 'NickServ'
    
            && to === config.serveroptions.userName
    
            && text === 'This nickname is registered. Please choose a different nickname, or identify via /msg NickServ identify <password>.') {
    
            nyaa.say('NickServ', 'identify ' + config.password);
    
        }
    
        if (from === 'NickServ'
    
            && to === config.serveroptions.userName
    
            && text === 'You are now identified for ' + config.serveroptions.userName) {
    
            console.log('Login success.');
    
        } else if (from === 'NickServ'
    
            && to === config.serveroptions.userName
    
            && text === 'Invalid password for ' + config.serveroptions.userName) {
    
            console.log('Incorrect password. check you config!');
    
        }
    
    });  
  
---  
  
嗯现在就是验证字符串… 所以似乎只能在 freenode 上跑，其他 IRC 服务器是不是这样就不知道了。测试了下表示没问题，收到登陆成功的提示了。 

###  消息处理 

目前不准备做私信支持，所以在收到 pm 的时候直接丢一句话过去就可以了。顺便，可以做成自定义消息的说，于是加上了 ` messages.js ` 包含所有的可自定义消息。 

然后是最重要的功能之一——命令。没命令的 bot 不是好 bot 嗯。编写程序时候的想法是命令以特定字符开头，但是后面如何验证，用 Stackoverflow 上扒来的 ` startsWith ` 和 ` endsWith ` 函数似乎不能做到足够准确，所以暂且用一个字母加参数来作为命令好了。首先想到的命令功能是搜索 Wiki。毕竟 Minecraft 游戏有够复杂即便是老玩家也不一定能记住 Wiki 里的所有内容。这里想要实现的效果是，提交关键字，返回搜索到的页面链接，并发送该页面的内容总结——也就是 Mediawiki 页面的 section 0。 

这里用到了 ` request ` 模块，因为 ` http.get ` 被弃用且 ` http.request ` 说实话用起来比较不爽。 ` request ` 可以轻松得到页面内容。根据 [ Mediawiki API ](http://en.wikipedia.org/w/api.php) 确定使用如下2个请求参数： 

  * ` /api.php?action=query&format=xml&titles=[页面标题] `
  * ` /api.php?format=json&action=parse&prop=text&section=0&page=[页面标题] `

话说我倒是想都用 JSON 的，毕竟 Javascript 原生支持的东西。但是但是第一个 API 返回的 JSON 居然把页面的 pageid 作为 key 啦！你这要我如何是好，为了拿你一个 key/value 要麻烦死了哦。所以还是选择了 XML 并且使用了 [ xml2js ](https://github.com/Leonidas-from-XIV/node-xml2js) 这个库。 

第二个 API 的数据处理其实一开始也是用的 XML，因为返回的 JSON 里一个 key 是 ` * ` ，然后我就 <del> 很丢脸的 </del> 不知所错了… 问了仙子才知道这种带有特殊符号的使用方法是… 
    
    
    {
    
        "v": {
    
    	      "*":{
    
    			"key1": "value1",
    
    			"key2": "value2"
    
    		  }
    
    	  }
    
    }  
  
---  
  
这样的拿到 ` * ` 的属性值的方法是 ` v['*'] ` ……… <del> 基本功不扎实，实在是太丢脸了 >////< </del>

于是拿到了返回文章 summary 的 HTML 代码。先是用正则去掉所有的 HTML Tag 和 ` \n \r ` 等换行符，然后发现 HTML 实体没有被转换，于是偷懒用了 [ htmlstrip-native ](https://www.npmjs.org/package/htmlstrip-native) 来搞定这个问题。 

测试后发现可以正确返回得到页面的链接，但是总结发出来却是乱码。感觉应该是包含了无效的 UTF-8 编码，遂尝试使用正则 ` /\uFFFD/g ` 替换掉无效的编码但是不起作用。试图移除最后一个字符也是无用。折腾了大约有2个小时，突然发现如果不去掉换行符则消息发出来是正常的。但是不去掉的话一行只有几个字啊… 

不过还是有收获，仙子根据不移除换行符则消息正常判断是 IRC 消息长度限制导致了 UTF-8 流被截断。RFC 规定 IRC 消息长度为512，但是一个 CJK 字符通常占3位。所以 512/3 差不多是170。嘛很不爽的把消息限制改成了144。这样发出来就不乱码了，但是总结大多比较长要连续发好几条消息导致游戏端被刷屏，玩家颇有微词。 

后面就方便多了，加了一条 ` 'p' ` 命令，意为 ` play ` 即 <del> 玩坏 </del> 。在 ` messages.js ` 里设定了一个 Object 包含2个数组，对应命令消息和响应消息。程序中用 ` async ` 来实现命令匹配和回复，以及在没有找到可用命令时发送命令未知消息。还有一条 ` 'c' ` 用来执行一些真正的命令——比如退出 _ (:з」∠) _

嘛现在这 [ bot ](https://github.com/phoenixlzx/nyaabot) 已经在群里开始调(wan)戏(huai)二小姐了233 
