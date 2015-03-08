#  [ [Cocos2d-x]在Cocos2d-x 3.x版本中如何通过WebSocket连接服务器进行数据传输 ](/pleasecallmewhy/article/details/36686787)

### 

###  WebSocket 

首先新建一个空的文件夹，通过npm安装 ` nodejs-websocket ` ： 
    
    
    npm install nodejs-websocket
    

新建 ` app.js ` 文件： 
    
    
    var ws = require("nodejs-websocket");
    ws.createServer(function(conn){
        conn.on("text", function (str) {
            console.log("get the message: "+str);
            conn.sendText("the server got the message");
        })
        conn.on("close", function (code, reason) {
            console.log("connection closed");
        });
        conn.on("error", function (code, reason) {
            console.log("an error !");
        });
    }).listen(8001);
    

通过 ` node app.js ` 启动，这样服务器就搭建好了。 

###  Cocos2d-x 

  * 首先在头文件中include头文件： 
    
    
    #include "network/WebSocket.h"
    

  * 实现WebSocket的委托： 
    
    
    class HelloWorld : public cocos2d::Layer,public cocos2d::network::WebSocket::Delegate
    

  * 四个委托中定义的函数接口以及一个用来连接的socketClient对象： 
    
    
    // for virtual function in websocket delegate
    virtual void onOpen(cocos2d::network::WebSocket* ws);
    virtual void onMessage(cocos2d::network::WebSocket* ws, const cocos2d::network::WebSocket::Data& data);
    virtual void onClose(cocos2d::network::WebSocket* ws);
    virtual void onError(cocos2d::network::WebSocket* ws, const cocos2d::network::WebSocket::ErrorCode& error);
    
    // the websocket io client
    cocos2d::network::WebSocket* _wsiClient;
    

  * 初始化client： 
    
    
    _wsiClient = new cocos2d::network::WebSocket();
    _wsiClient->init(*this, "ws://localhost:8001");
    

  * 在cpp文件中实现这些函数： 
    
    
    // 开始socket连接
    void HelloWorld::onOpen(cocos2d::network::WebSocket* ws)
    {
        CCLOG("OnOpen");
    }
    
    // 接收到了消息
    void HelloWorld::onMessage(cocos2d::network::WebSocket* ws, const cocos2d::network::WebSocket::Data& data)
    {
            std::string textStr = data.bytes;
            textStr.c_str();
            CCLOG(textStr.c_str());
    }
    
    // 连接关闭
    void HelloWorld::onClose(cocos2d::network::WebSocket* ws)
    {
        if (ws == _wsiClient)
        {
            _wsiClient = NULL;
        }
        CC_SAFE_DELETE(ws);
        CCLOG("onClose");
    }
    
    // 遇到错误
    void HelloWorld::onError(cocos2d::network::WebSocket* ws, const cocos2d::network::WebSocket::ErrorCode& error)
    {
        if (ws == _wsiClient)
        {
            char buf[100] = {0};
            sprintf(buf, "an error was fired, code: %d", error);
        }
        CCLOG("Error was fired, error code: %d", error);
    }
    

还有一个使用SocketIO的方案，尚未尝试，明天测试一下： 
    
    
    // Require HTTP module (to start server) and Socket.IO
    var http = require('http'), io = require('socket.io');
    
    // Start the server at port 8080
    var server = http.createServer(function(req, res){ 
    
        // Send HTML headers and message
        res.writeHead(200,{ 'Content-Type': 'text/html' }); 
        res.end('<h1>Hello Socket Lover!</h1>');
    });
    server.listen(8080);
    
    // Create a Socket.IO instance, passing it our server
    var socket = io.listen(server);
    
    // Add a connect listener
    socket.on('connection', function(client){ 
    
        // Create periodical which ends a message to the client every 5 seconds
        var interval = setInterval(function() {
            client.send('This is a message from the server!  ' + new Date().getTime());
        },5000);
    
        // Success!  Now listen to messages to be received
        client.on('message',function(event){ 
            console.log('Received message from client!',event);
        });
        client.on('disconnect',function(){
            clearInterval(interval);
            console.log('Server has disconnected');
        });
    
    });

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/36686787](http://blog.csdn.net/pleasecallmewhy/article/details/36686787)