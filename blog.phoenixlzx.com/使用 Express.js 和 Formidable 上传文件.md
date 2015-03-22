title: 使用 Express.js 和 Formidable 上传文件

date: 2014-02-17T11:49:22.000Z

tags: [Node.js, ]

description: 

---
写 [ 之前一篇文章 ](/2014/02/06/directshare-a-simple-file-sharing-using-direct-http-links/) 时发现 Express.js 更新到 3.4.x 了，运行的时候出现警告 
    
    
    connect.multipart() will be removed in connect 3.0
    
    visit https://github.com/senchalabs/connect/wiki/Connect-3.0 for alternatives
    
    connect.limit() will be removed in connect 3.0  
  
---  
  
按照 Wiki 的指引看了下 ` multiparty ` ， ` connect-multiparty ` 和 ` formidable ` ，最终选用了 ` formidable ` <del> 因为说明看起来很碉堡的样子 </del>

简单写了两个路由控制，按照 [ node-formidable ](https://github.com/felixge/node-formidable) 的示例加上了打印文件上传信息的几个语句，运行时发现程序 hang 了… 

Google 许久无果——找到的结果基本都是要你注释掉 ` app.use(express.bodyParser()) ` ，而我已经是 express 3.4 所以早就没有 bodyParser 了。回去又看 formidable 给的例子，于是发现自己犯二了…—— 
    
    
    <form action="/upload" enctype="multipart/form-data" method="post">  
  
---  
  
真是个バカ！ 

立马给 ` index.ejs ` 中的 form 部分加上了 ` enctype="multipart/form-data" ` ，重试，成功。 <del> 于是就这么解决了 </del> (被打飞 

主程序 
    
    
    /**
    
     * Module dependencies.
    
     */
    
    var express = require('express');
    
    var http = require('http');
    
    var path = require('path');
    
    var util = require('util');
    
    var formidable = require('formidable');
    
    var app = express();
    
    // all environments
    
    app.set('port', process.env.PORT || 3000);
    
    app.set('views', path.join(__dirname, 'views'));
    
    app.set('view engine', 'ejs');
    
    app.use(express.favicon());
    
    app.use(express.logger('dev'));
    
    app.use(express.json());
    
    app.use(express.urlencoded());
    
    app.use(express.methodOverride());
    
    app.use(app.router);
    
    app.use(express.static(path.join(__dirname, 'public')));
    
    // development only
    
    if ('development' == app.get('env')) {
    
      app.use(express.errorHandler());
    
    }
    
    app.get('/', function(req, res) {
    
        res.render('index');
    
    });
    
    app.post('/upload', function(req, res) {
    
        var form = new formidable.IncomingForm();
    
        form.parse(req, function(err, fields, files) {
    
            res.writeHead(200, {'content-type': 'text/plain'});
    
            res.write('received upload:\n\n');
    
            res.end(util.inspect({fields: fields, files: files}));
    
        });
    
    });
    
    http.createServer(app).listen(app.get('port'), function(){
    
      console.log('Express server listening on port ' + app.get('port'));
    
    });  
  
---  
  
以及一个简单的 ` index.ejs `
    
    
    <!DOCTYPE html>
    
    <html>
    
    <head>
    
        <title>Upload test</title>
    
        <link rel='stylesheet' href='/stylesheets/style.css' />
    
    </head>
    
    <body>
    
    <h1>Test formidable</h1>
    
    <form action="/upload" method="post" enctype="multipart/form-data">
    
        <input type="text" name="textfield"/>
    
        <input type="file" name="file" />
    
        <button type="submit">Upload</button>
    
    </form>
    
    </body>
    
    </html>  
  
---  
  
PS. [ 后来发现确实有人遇到这个问题了… ](http://stackoverflow.com/a/5543851)
