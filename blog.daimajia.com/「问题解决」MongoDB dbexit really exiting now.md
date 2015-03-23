title: 「问题解决」MongoDB dbexit really exiting now

date: 2013-07-01T07:59:41+00:00

tags: []

description: 

---
如果你在启动MongoDB的时候，出现以下错误： 

Wed Apr 27 10:02:41 [initandlisten] shutdown: going to close listening sockets…   
Wed Apr 27 10:02:41 [initandlisten] shutdown: going to flush diaglog…   
Wed Apr 27 10:02:41 [initandlisten] shutdown: going to close sockets…   
Wed Apr 27 10:02:41 [initandlisten] shutdown: waiting for fs preallocator…   
Wed Apr 27 10:02:41 [initandlisten] shutdown: closing all files…   
Wed Apr 27 10:02:41 closeAllFiles() finished   
Wed Apr 27 10:02:41 [initandlisten] shutdown: removing fs lock…   
Wed Apr 27 10:02:41 [initandlisten] couldn’t remove fs lock errno:9 Bad file descriptor   
Wed Apr 27 10:02:41  dbexit: really exiting now 

理论来说，是因为缺乏写权限，无法向/data/db/文件夹写入数据。 

修复方法： 

** sudo chown `id -u` /data/db **

** sudo mongo **

如果还有问题： 

** sudo mongo –repaire **
