title: Html5 Web Socket

date: 2013-03-29 22:33:28

tags: []

description: 

---
一、出身

HTML5

二、使命

HTML5 Web Socket并不是像Ajax那样用来增强传统HTTP协议的功能，而是由w3c带来的全新的改变，尤其适用于在需要_实时通信（real-time）和 事件驱动（event-drive）_的web程序中。

：扫盲real-time和event-drive

real-time 即时消息，就类似于在线炒股，监控系统（如电厂即时电压，电流稳定性等），这类事务一般都需要实时而且可靠的消息，通常哪怕几秒的延迟都是难以忍受的。

event-drive 事件驱动，就类似于当你按下 Alt+F4 的键盘组合键，浏览器会把这个当成一个关闭事件处理，在web中，就类似于新浪微博的私信提醒一样，有消息到来会通知浏览器弹出消息框。

现在网页通常使用ajax来实现此类架构，浏览器按一定的时间间隔不断请求服务器看有没有新消息到来，服务器不断做查询处理，而后返回相应数据，这是一种单通道式的响应（就好比一条单向公路），即客户浏览器只能通过HTTP协议主动联系服务器而后在建立的一个HTTP链接中服务器做出响应，随后该链接被中断，服务器无法主动联系用户浏览器建立连接做出改变或传递信息。

这样很多情况下，即便传递一个1byte的数据，都需要经过一段复杂的流程（各种协议头包装），而且会使实际的数据包变大很多。HTTP的设计本身就不是Real-time和Full-duplex（全双工）的。

html5 Web Socket就将这条通道打通，能双向的交换信息（全双工），并且减少了数据包大小。

因而优势如下

三、优势

  1. _Reducing kilobytes of data to 2 bytes （数据减少到2bytes）_
  2. __Reducing latency from 150ms to 50ms (延迟从150毫秒减少到50毫秒)__

四、Web Socket出现前的尝试方案和解决方案

  1. Polling （轮询）:  浏览器按一定间隔发送http请求，服务器做出响应，类ajax。最好的情形就是服务器端新消息到来的间隔是已知的，不然会做出很多无意义的查询或处理行为。
  2. Long-Polling （长轮询）:  浏览器发送一个请求给服务器端，服务器端做出响应建立连接，并且保持一段时间的连接（通过阻塞来实现），在这一段时间内，如果服务器端收到与你相关的消息，就会给你发个response回来。如果在这一段时间内没有消息，则会主动断开连接。这个看似解决了问题，但是考虑一下，如果你的消息非常多，而且此时同时使用此服务的其他人消息也非常多，服务器是没法保证能够及时给你发回response，因为后台实现只能通过循环来处理。
  3. Streaming （流）: 在介绍这种解决方案之前，先要介绍一下 流 。最长接触到的 流 方式就是在线听歌的方式传递数据。将streaming 封装在 http协议中，浏览器首先请求服务器端，服务器建立连接，并且不再切断该连接，用类似传送音乐的形式远远不断的发送当前消息状态。 这种方式会使得IE永远显示网页未加载完成(不过可以解决)… 而且会加重服务器端的负载，极大的浪费服务器资源。在有防火墙或者代理环境下，防火墙会对数据进行buffering，并且扫描安全性，无疑又增加了延迟。

具体可以看以下链接：

[IBM Developer](http://www.ibm.com/developerworks/cn/web/wa-lo-comet/)

四、如今有了web socket

  1. 数据头被简化
  2. 数据可双向发送
  3. 文本和二进制帧均可发送，并且最小帧只有2bytes  Note:虽然可以发送2进制数据，但是由于javasccript不支持，所以客户端会忽略此种数据。不过可以在其他支持平台发送。

五、支持情况

  * IE 10+
  * Chrome 4+
  * Safari 5+
  * Firefox 4+
  * Opera 11+

更多详细支持情况在[WikiPedia](http://en.wikipedia.org/wiki/WebSocket#Browser_support)上。

六、相关开源库/产品

  * [SocketIO](http://socket.io/)
  * [Sails](https://github.com/balderdashy/sails)
  * [Meteor](http://meteor.com/)
  * [PeerCDN](http://peercdn.com/)
  * [FireBase](https://www.firebase.com/)
