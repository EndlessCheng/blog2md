#  Linux socket编程学习笔记（一）：socket()函数详解 

_ _ [ zxy_snow ](http://www.xysay.com/author/zxy_snow) _ _ [ 学习笔记 ](http://www.xysay.com/category/%e5%ad%a6%e4%b9%a0%e7%ac%94%e8%ae%b0) _ _ 围观 _ 503 _ 次  _ _ [ 7 条评论 ](http://www.xysay.com/linux-socket-133.html#comments) _ _ 编辑日期：  2014-07-01  _ _ 字体： [ 大 ](javascript:;) [ 中 ](javascript:;) [ 小 ](javascript:;)

_ ** 开始学socket编程哈，写笔记吧~这些都是从网上整理+实践来的，嘿嘿 ** _   
#include <sys/types.h>   
#include <sys/socket.h>   
函数原型 int socket(int domain, int type, int protocol);   
应用程序调用socket函数来创建一个能够进行网络通信的套接字。   
第一个参数指定应用程序使用的通信协议的协议族，对于TCP/IP协议族，该参数置AF_INET;   
第二个参数指定要创建的套接字类型，流套接字类型为SOCK_STREAM、数据报套接字类型为SOCK_DGRAM、原始套接字SOCK_RAW(WinSock接口并不适用某种特定的协议去封装它，而是由程序自行处理数据包以及协议首部）；   
第三个参数指定应用程序所使用的通信协议。    
该函数如果调用成功就返回新创建的套接字的描述符，如果失败就返回INVALID_SOCKET。套接字描述符是一个整数类型的值。每个进程的进程空间里都有一个套接字描述符表，该表中存放着套接字描述符和套接字数据结构的对应关系。该表中有一个字段存放新创建的套接字的描述符，另一个字段存放套接字数据结构的地址，因此根据套接字描述符就可以找到其对应的套接字数据结构。每个进程在自己的进程空间里都有一个套接字描述符表但是套接字数据结构都是在操作系统的内核缓冲里。 

_ ** 以上摘自百度百科，下面对上面进行补充。 ** _   


  * domain：指定使用何种的地址类型，比较常用的有： 

PF_INET, AF_INET： Ipv4网络协议；   
PF_INET6, AF_INET6： Ipv6网络协议。   
其中AF 表示ADDRESS FAMILY 地址族   
PF 表示PROTOCOL FAMILY 协议族   
经测试，linux下： 

/usr/include/i386-linux-gnu/bits/socket.h:#define PF_INET 2 /* IP protocol family. */ /usr/include/i386-linux-gnu/bits/socket.h:#define PF_INET6 10 /* IP version 6. */ /usr/include/i386-linux-gnu/bits/socket.h:#define AF_INET PF_INET /usr/include/i386-linux-gnu/bits/socket.h:#define AF_INET6 PF_INET6 

1 

2 

3 

4 

| 

/  usr  /  include  /  i386  \-  linux  \-  gnu  /  bits  /  socket  .  h  :  #define PF_INET 2 /* IP protocol family.  */ 

/  usr  /  include  /  i386  \-  linux  \-  gnu  /  bits  /  socket  .  h  :  #define PF_INET6 10 /* IP version 6.  */ 

/  usr  /  include  /  i386  \-  linux  \-  gnu  /  bits  /  socket  .  h  :  #define AF_INET PF_INET 

/  usr  /  include  /  i386  \-  linux  \-  gnu  /  bits  /  socket  .  h  :  #define AF_INET6 PF_INET6   
  
---|---  
  
  * type: 

SOCK_STREAM： 提供面向连接的稳定数据传输，即TCP协议。   
OOB： 在所有数据传送前必须使用connect()来建立连接状态。   
SOCK_DGRAM： 使用不连续不可靠的数据包连接。   
SOCK_SEQPACKET： 提供连续可靠的数据包连接。   
SOCK_RAW： 提供原始网络协议存取。   
SOCK_RDM： 提供可靠的数据包连接。   
SOCK_PACKET： 与网络驱动程序直接通信。   


  * protocal: 

用来指定socket所使用的传输协议编号。这一参数通常不具体设置，一般设置为0即可。    
/span 

  * 本文固定链接: [ http://www.xysay.com/linux-socket-133.html ](http://www.xysay.com/linux-socket-133.html)
  * 转载请注明: [ zxy_snow ](http://www.xysay.com/author/zxy_snow) 2012年03月21日  于 [ 小媛在努力 ](http://www.xysay.com/) 发表 

_ _ [ linux ](http://www.xysay.com/tag/linux) ， [ socket ](http://www.xysay.com/tag/socket)

  

#### 原文：[http://www.xysay.com/linux-socket-133.html](http://www.xysay.com/linux-socket-133.html)