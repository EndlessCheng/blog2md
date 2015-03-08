[ 2014-02-06 ](/2014/02/06/directshare-a-simple-file-sharing-using-direct-http-links/)

#  Directshare - 一个简单的HTTP直链文件分享工具 

嘛… 最近真心补番补多了智商降得有点厉害.. 直到我发现自己已经看不懂别人的 js 代码，却还会手贱点开 bilibili 之后才 [ 立下军令状 ](https://plus.google.com/107142103119739092775/posts/M2LA33yfdRG) ，再不开新坑再不敲代码就敲不出来啦！ 

一直很纠结再写点啥。之前财务管理系统的坑估计要弃，因为实在一个人填不完…然后 NAE 一直没计划好，估计这个坑会更巨。之前 luke 酱说发现了一个不错的东方音乐站，想要个桌面端。咱之前有试着学Qt但是一直没有方便的文档而且..终归是咱能力不行吧，Qt估计是一时半会搞不定了。写桌面端的话，似乎只有 node-webkit 了.. 然后看了一下午的文档只有一个感觉——我要死了。 

<del> Intel开发的东西和红帽一样蛋疼 </del>

桌面端什么的…. 所以就放着吧… 随便搞个东西练练手算了。想想看还没有练习过文件上传 <del> 真丢人啊都不会写文件上传 </del> 于是来写一个上传文件并分享的东西好了w 

于是老样子.. ` express -e ` 新建一个项目模板，初始化git仓库… 诶似乎有什么东西不对？ 

` express.bodyParser() ` 没了… 

先不管这些，基本的路由和功能堆起来，打印出结果来看看能不能正确获取文件信息。然后… 当然失败了。 

没有 ` bodyParser ` 之后，带有文件上传的表单无法被处理了， ` req.files ` 是 ` undefined ` ， ` req.body ` 里也是空的.. 

一阵 Google 之后表示，泥煤的 express 3.4.x 又改了… ` bodyParser ` 已经被 [ 弃用 ](https://groups.google.com/forum/#!topic/express-js/iP2VyhkypHo) ，原因是存在 [ 可能占满磁盘的漏洞 ](http://andrewkelley.me/post/do-not-use-bodyparser-with-express-js.html) 。目前推荐的方式是直接使用 ` multiparty ` 。于是又去翻这货的文档，表示要蛋疼许多… 纠结了一会觉得还是先用回 3.3.4 之后慢慢折腾下 multiparty。 

Directshare 使用 HTTP 直链文件，看起来似乎有点危险，不过毕竟可以拿来做图床、临时的文件共享或者在没有FTP/SSH的情况下把文件上传到服务器什么的.. 最重要的是， <del> 我只是想练练手而已搞那么复杂干嘛.. </del>

基本思路：整个程序分为负责接收文件的master和负责分发文件的cluster。客户端使用浏览器POST方法上传文件 => master得到文件后计算SHA256并把文件从临时目录移动到保存文件的目录，文件名是SHA256值，不带有后缀。接下来通知所有cluster来拖。这里要有一个验证，暂且用 POST accesskey 之类的东西来做好了。因为似乎没找到啥能通过 http 同步的 node 包，所以简单的双向 POST 数据基本上也没问题。本来想在cluster接收到文件后再计算一次hash值.. 不过这个后面再说。通知所有 cluster 用了一个 forEach，虽然是阻塞的方法不过发几个post请求应该是相当快的。接下来把从cluster下载文件的地址返回给客户端浏览器。这个时候cluster应该已经收到post请求，过来拖文件了。 

文件 ` master.js `
    
    
    /**
    
     * Module dependencies.
    
     */
    
    var express = require('express');
    
    var http = require('http');
    
    var path = require('path');
    
    var config = require('./config.js');
    
    var crypto = require('crypto');
    
    var fs = require('fs');
    
    var querystring = require('querystring');
    
    var app = express();
    
    // all environments
    
    app.set('port', config.port || 3000);
    
    app.set('views', path.join(__dirname, 'views'));
    
    app.set('view engine', 'ejs');
    
    app.use(express.favicon());
    
    app.use(express.logger('dev'));
    
    app.use(express.json());
    
    app.use(express.bodyParser({
    
        keepExtensions: false,
    
        uploadDir: "tmpdata"
    
    }));
    
    app.use(express.methodOverride());
    
    // app.use(app.router);
    
    app.use(express.static(path.join(__dirname, 'public')));
    
    // development only
    
    if ('development' == app.get('env')) {
    
      app.use(express.errorHandler());
    
    }
    
    app.get('/', function(req, res) {
    
        res.render('index', {
    
            siteName: config.siteName
    
        });
    
    });
    
    app.post('/', function(req, res) {
    
        // console.log(req.files.uploadfile);
    
        // hash file with sha256
    
        var sha256sum = crypto.createHash('sha256');
    
        var filehash = fs.ReadStream(req.files.uploadfile.path);
    
        filehash.on('data', function(d) {
    
            sha256sum.update(d);
    
        });
    
        filehash.on('end', function() {
    
            var d = sha256sum.digest('hex');
    
            console.log(d + ' ' + req.files.uploadfile.name);
    
            // move file to storage location
    
            fs.rename(req.files.uploadfile.path, 'files/' + d, function() {
    
                // notify clusters to fetch file
    
                config.clusters.forEach(function(cluster) {
    
                    var post_data = querystring.stringify({
    
                        clusterkey: config.clusterkey,
    
                        filename: req.files.uploadfile.name,
    
                        filehash: d
    
                    });
    
                    var post_options = {
    
                        hostname: cluster,
    
                        port: config.clustersport,
    
                        path: '/syncfile',
    
                        method: 'POST',
    
                        headers: {
    
                            'Content-Type': 'application/x-www-form-urlencoded',
    
                            'Content-Length': post_data.length
    
                        }
    
                    }
    
                    // Set up the request
    
                    console.log('syncing with ' + cluster);
    
                    var post_req = http.request(post_options);
    
                    // post the data
    
                    post_req.write(post_data);
    
                    post_req.end();
    
                });
    
                // return client with download path
    
                res.send(200, config.clusterurl + d);
    
            });
    
        });
    
    });
    
    app.post('/syncfile', function(req, res) {
    
        if (req.body.clusterkey != config.clusterkey) {
    
            return res.send(401);
    
        } else {
    
            res.sendfile('files/' + req.body.filehash);
    
        }
    
    });
    
    // handle 404
    
    app.use(function(req, res) {
    
        res.send(404, 'My files gone?! :-O');
    
    });
    
    http.createServer(app).listen(app.get('port'), function(){
    
      console.log('Express server listening on port ' + app.get('port'));
    
    });  
  
---  
  
然后是 ` cluster.js `
    
    
    /**
    
     * Module dependencies.
    
     */
    
    var express = require('express');
    
    var http = require('http');
    
    var path = require('path');
    
    var config = require('./config.js');
    
    var fs = require('fs');
    
    var querystring = require('querystring');
    
    var app = express();
    
    // all environments
    
    app.set('port', config.port || 3000);
    
    app.use(express.favicon());app.use(express.logger('dev'));
    
    app.use(express.json());
    
    app.use(express.methodOverride());
    
    app.use(express.bodyParser());
    
    app.use(app.router);
    
    app.use(express.static(path.join(__dirname, 'public')));
    
    // development only
    
    if ('development' == app.get('env')) {
    
      app.use(express.errorHandler());
    
    }
    
    app.get('/', function(req, res) {
    
        res.send(400, 'Bad request');
    
    });
    
    app.get('/:hash', function(req, res) {
    
        fs.readFile('files/' + req.params.hash + '.json', 'utf8', function(err, filedata) {
    
            if (err) {
    
                if (err.code === 'ENOENT') {
    
                    res.send(404, 'File not found. :-(');
    
                } else {
    
                    console.log(err);
    
                }
    
            } else {
    
                var filedata = JSON.parse(filedata);
    
                res.download('files/' + req.params.hash, filedata.filename);
    
            }
    
        })
    
    });
    
    app.post('/syncfile', function(req, res) {
    
        if (req.body.clusterkey != config.clusterkey) {
    
            return res.send(401);
    
        } else {
    
            res.send(200);
    
            var post_data = querystring.stringify({
    
                clusterkey: config.clusterkey,
    
                filehash: req.body.filehash
    
            });
    
            var post_options = {
    
                hostname: config.master,
    
                port: config.masterport,
    
                path: '/syncfile',
    
                method: 'POST',
    
                headers: {
    
                    'Content-Type': 'application/x-www-form-urlencoded',
    
                    'Content-Length': post_data.length
    
                }
    
            }
    
            // Set up the request
    
            console.log('Getting file with SHA256 ' + req.body.filehash);
    
            var post_req = http.request(post_options, function(res) {
    
                var file = fs.createWriteStream('files/' + req.body.filehash);
    
                res.pipe(file);
    
            });
    
            // post the data
    
            post_req.write(post_data);
    
            post_req.end();
    
            fs.appendFile('files/' + req.body.filehash + '.json', JSON.stringify({
    
                "filename": req.body.filename
    
            }), function() {
    
                console.log('Saved file ' + req.body.filename + ' with hash ' + req.body.filehash);
    
            });
    
        }
    
    });
    
    http.createServer(app).listen(app.get('port'), function(){
    
      console.log('Express server listening on port ' + app.get('port'));
    
    });  
  
---  
  
这样程序应该就相当清晰了。在 cluster 端使用了SHA256值作为文件名的 json 作为文件信息存储，当前只保存了对应的文件名。至于重复文件啊什么的.. 暂时没想好怎么做，不过拿sha256做文件名本来就有这个功能的想法。本地测试完成，commit # [ ` f6365cfcbd ` ](https://github.com/phoenixlzx/directshare/commit/f6365cfcbd18536f226da1e4fe633ece665b6ec2)

当我发军令状的时候是昨晚9点，第一个可用版本提交是今天2点左右，5个小时开新坑再填上… 不过这坑有点小所以好填… 所以5个小时不算什么了吧就… 嘛至少不用改名BAKA了～ 

[ Node.js ](/categories/Node-js/)

[ Node.js ](/tags/Node-js/) , [ Practise ](/tags/Practise/)
#### 原文：[https://blog.phoenixlzx.com/2014/02/06/directshare-a-simple-file-sharing-using-direct-http-links/](https://blog.phoenixlzx.com/2014/02/06/directshare-a-simple-file-sharing-using-direct-http-links/)