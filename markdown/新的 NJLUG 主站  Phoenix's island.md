[ 2014-05-07 ](/2014/05/07/new-njlug-homepage/)

#  新的 NJLUG 主站 

南京 Linux 用户组有一段时间没有聚会了。偶然想起来之前我用 Jekyll 折腾的那个主页，随手敲了主页地址… 啊啦，还基本上没变啊… 

嘛虽然自己写了那么几个东西，不过在组里待了也有一段时间也学到了不少东西。用户对社区的回报应该就在这时候展现出来吧。 

依旧是 Express.js 框架，依旧是 Bootstrap。不过这回不想用数据库了，改用文本存储。除了主页和关于，顺便集成一个 Planet 在里面。RSS feed 的话，除了遍历一遍 upsert (不存在的添加，已存在的跳过)之外没想到什么更好的办法。实际上本来就是 RSS 没必要存储所有的文章，更何况又不是做之前想做的类似 Google Reader 的东西。 

目前的 Planet 工作方式为首先检测是否存在文章数据文件 ` posts.array ` ，如果不存在则读取 ` planet.list ` 中的订阅链接，获取到文章后 push 到一个数组中，按照发表日期排序并保存在 ` posts.array ` 里。到底是先排序再保存还是先存进去，渲染页面的时候再排序，这个稍微纠结了下。因为自己的配置文件里更新频率是 1 hour, 而且似乎每次更新到的文章数量还挺多的。所以保存时排序的话，则每天固定排序23次；如果渲染时排序的话，就看每天能有几个访问了…. 然后发现自己在这种小问题上纠结个毛毛啊啊啊啊啊。 

排序后保存进文件之前和从文件读出之后要有两个 JSON 操作。保存之前 ` JSON.stringify(posts) ` 转换成字符串再保存，否则文件里是 ` [[object Object], [object Object]] ` 。读出来之后 ` JSON.parse(posts) ` 再转换成对象数组，否则直接就一字符串没办法处理。 

接下来就是主页和关于。因为不想写用户系统了所以就不发文章了吧… 关于可以是万年不变的页面，首页的话，显示最近的公告好了。最简单的实现就是存两个 markdown 文件然后用 marked 渲染出来插在页面里。 

全部的源码在 [ 这里 ](https://github.com/phoenixlzx/NJLUG-site) 。 

目前似乎域名还没解析，田华兄也未必决定用这个.. 所以效果的话戳 [ 这里 ](http://njlug.phoenixlzx.com) 看。 

然后顺便说一句.. 现在已经健忘到我已经忘记刚刚想起来要写的东西了 _ (:з」∠) _

[ Node.js ](/categories/Node-js/)

[ Node.js ](/tags/Node-js/)
#### 原文：[https://blog.phoenixlzx.com/2014/05/07/new-njlug-homepage/](https://blog.phoenixlzx.com/2014/05/07/new-njlug-homepage/)