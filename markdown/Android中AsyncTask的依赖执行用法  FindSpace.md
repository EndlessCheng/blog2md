#  Android中AsyncTask的依赖执行用法 

[ Find ](http://www.findspace.name/author/find) |  2015年1月6日  |  [ Android ](http://www.findspace.name/category/easycoding/android) , [ 随意Coding ](http://www.findspace.name/category/easycoding) |  [ 没有评论  ](http://www.findspace.name/easycoding/983#comments)

在Android中实现异步任务机制有两种方式，Handler和AsyncTask。 

Handler模式需要为每一个任务创建一个新的线程，任务完成后通过Handler实例向UI线程发送消息，完成界面的更新，这种方式对于整个过程的控制比较精细，但也是有缺点的，例如代码相对臃肿，在多个任务同时执行时，不易对线程进行精确的控制。 

为了简化操作，Android1.5提供了工具类android.os.AsyncTask，它使创建异步任务变得更加简单，不再需要编写任务线程和Handler实例即可完成相同的任务。 

先来看看AsyncTask的定义： 

> public  abstract  class  AsyncTask<Params, Progress, Result> { 

三种泛型类型分别代表“启动任务执行的输入参数”、“后台任务执行的进度”、“后台计算结果的类型”。在特定场合下，并不是所有类型都被使用，如果没有被使用，可以用java.lang.Void类型代替。 

一个异步任务的执行一般包括以下几个步骤： 

1\. ** execute(Params… params) ** ，执行一个异步任务，需要我们在代码中调用此方法，触发异步任务的执行。 

2\. ** onPreExecute() ** ，在execute(Params… params)被调用后立即执行，一般用来在执行后台任务前对UI做一些标记。 

3\. ** doInBackground(Params… params) ** ，在onPreExecute()完成后立即执行，用于执行较为费时的操作，此方法将接收输入参数和返回计算结果。在执行过程中可以调用publishProgress(Progress… values)来更新进度信息。 

4\. ** onProgressUpdate(Progress… values) ** ，在调用publishProgress(Progress… values)时，此方法被执行，直接将进度信息更新到UI组件上。 

5\. ** onPostExecute(Result result) ** ，当后台操作结束时，此方法将会被调用，计算结果将做为参数传递到此方法中，直接将结果显示到UI组件上。 

在使用的时候，有几点需要格外注意： 

1.异步任务的实例必须在UI线程中创建。 

2.execute(Params… params)方法必须在UI线程中调用。 

3.不要手动调用onPreExecute()，doInBackground(Params… params)，onProgressUpdate(Progress… values)，onPostExecute(Result result)这几个方法。 

4.不能在doInBackground(Params… params)中更改UI组件的信息。 

5.一个任务实例只能执行一次，如果执行第二次将会抛出异常。 

而如果是依赖性的asynctask，taskA，B，C，出现顺序不一定，但是都互相依赖，某种条件下，A执行的结果给B，B才执行，等等。比如我需要先抓取findspace.name的首页，抓取完成后才进行下一步。 

如果事件比较少，而且顺序基本固定，那么可以直接在onpostexecute里new新的asynctask；如果事件比较多，或者顺序不固定，那么一个很巧妙的方法就是利用queue。 

定义时间集合，然后没触发一个条件就往queue里addtask，而每个task，在onpostexecute里，最后都是queue.nexttask，这个nexttask的主要内容就是取出队列头的时间，通过switch-case来执行对应的task。 

reference： 

http://blog.csdn.net/liuhe688/article/details/6532519 

Tags:  [ Android ](http://www.findspace.name/tag/android) , [ Java ](http://www.findspace.name/tag/java)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/easycoding/983](http://www.findspace.name/easycoding/983)