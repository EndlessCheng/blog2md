#  [ [NodeJS]使用Node.js写一个简单的在线聊天室 ](/pleasecallmewhy/article/details/24419023)

声明：教程来自《Node即学即用》。源码案例均出自此书。博文仅为个人学习笔记。 

  


第一步：创建一个聊天服务器。 

首先，我们先来写一个Server： 
    
    
    var net = require('net')
    
    var chatServer = net.createServer()
    
    chatServer.on('connection',function(client){
    	client.write('connection~~~\n')
    	client.end()
    })
    
    chatServer.listen(2333)
    
    console.log('Server')

  
可以使用telnet命令访问服务器： 

![](http://img.blog.csdn.net/20140424160808718?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


  


  


  


第二步：监听所有的连接请求 

服务器源代码： 
    
    
    var net = require('net')
    
    var chatServer = net.createServer()
    
    chatServer.on('connection',function(client){
    	client.write('Hello~~\n')
    	client.on('data',function(data){
    		console.log(data);
    	})
    })
    
    chatServer.listen(2333)
    
    console.log('Server')	

  
这里添加了一个事件监听器client.on()，每当client发送data的时候这个函数都会被调用。所以现在不论发送什么数据，服务器都会显示出来： 

![](http://img.blog.csdn.net/20140424161530890?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


但是这里有个问题：返回的内容均为乱码，因为JS不能很好的处理二进制数据，所以Node增加了一个buffer库来帮助服务器。 

打印的字符实际上是16进制的字节数据，可以保持二进制的格式，因为TCP和Telnet都能处理它们。 

  


第三步：客户端之间的通信： 
    
    
    var net = require('net')
    
    var chatServer = net.createServer()		//服务器
    var clientList = []						//客户端数组
    
    chatServer.on('connection',function(client){
    	client.write('Hello~Client~\n')
    	clientList.push(client)
    	client.on('data',function(data){
    		for (var i = 0; i < clientList.length; i++) {
    			clientList[i].write(data)
    		};
    	})
    })
    
    chatServer.listen(2333)
    
    console.log('Server')
    

  
这个就是一个最简单的聊天服务器了，可以打开多个终端，输入telnet localhost 2333访问服务器。 

![](http://img.blog.csdn.net/20140424164008281?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


下一步，改进消息发送和显示的方式，让页面更友善一些。 

我们把IP和端口号拼接作为用户名，这样可以看出来是谁发了消息。 

同时我们还需要加上异常的处理，因为在前面的程序中，如果有些客户端退出并没有在服务器的clientlist中移除。 

  


改善后的完整版本如下： 
    
    
    /*
     * A chat online server
     */
    
    var net = require('net')
    
    // server
    var chatServer = net.createServer()
    
    // clients
    var clientList = []
    
    chatServer.on('connection',function(client){
    	/*
    	//name = ip + port
    	client.name = client.remoteAddress + ":" + client.remotePort
    	*/
    	client.name = "No." + client.remotePort
    	client.write('Hello~ ' + client.name + "\n")
    
    	//add the client to list
    	clientList.push(client)	//push clients to arraylist
    
    	//when get data
    	client.on('data',function(data){
    		broadcast(data,client)
    	})
    
    	//when data end
    	client.on('end',function(){
    		clientList.splice(clientList.indexOf(client),1)
    	})
    
    	//when get error
    	client.on('error',function(e){
    		console.log(e)
    	})
    })
    
    
    //broadcast the message to the client
    function broadcast(message,client){
    	//the clients to delete
    	var cleanup = []
    
    	//check clients in clientlist
    	for (var i = 0; i < clientList.length; i++) {
    		if(client != clientList[i]){
    			if (clientList[i].writable) {
    				//write message if writable
    				clientList[i].write(client.name + " says " + message)
    			}else{
    				//add to cleanup list and destroy if not writable
    				cleanup.push(clientList[i])
    				clientList[i].destroy()
    			}
    		}
    	}
    
    	//remove the clients in clientlist according to the cleanup list
    	for (var i = 0; i < cleanup.length; i++) {
    		clientList.splice(clientList.indexOf(cleanup[i]),1)
    	};
    }
    
    //listen to 2333 port
    chatServer.listen(2333)
    
    //log the 
    console.log('Server is running')

  
  


  


  


  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/24419023](http://blog.csdn.net/pleasecallmewhy/article/details/24419023)