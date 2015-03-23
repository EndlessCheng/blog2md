title: 【Android问题解决】The application’s PagerAdapter changed the adapter’s contents without calling PagerAdapter#notifyDataSetChanged

date: 2013-06-07 16:00:27

tags: []

description: 

---
首先不得不说，ADT22就是个大坑，一旦更新，过去稍不符合规定的代码，统统会现出原形来。（其实就是ADT22变得严格了）

> FATAL EXCEPTION: main java.lang.IllegalStateException: The application’s PagerAdapter changed the adapter’s contents without calling PagerAdapter#notifyDataSetChanged! 

出这个错，是因为你的PagerAdapter中的数据变了，但是没有调用adapter.notifyDataSetChanged方法。

如果你的代码逻辑是这样的：

> class XXX extends asynctask
> 
> …
> 
> doInBackground(…){
> 
> 1、**获取数据**
> 
> 2、**添加到数据池**
> 
> 3、**publicProgress()**
> 
> }
> 
> onPublicProgress(…){
> 
> 4、调用adapter的notifydatasetchanged方法
> 
> }

在ADT22中，上面的代码肯定会报错的。为什么？

看下官方文档对[ support/v4/view/PagerAdapter](http://developer.android.com/reference/android/support/v4/view/PagerAdapter.html) 的一个解释：

PagerAdapter supports data set changes. Data set changes must occur on the main thread and must end with a call to `[notifyDataSetChanged()](http://developer.android.com/reference/android/support/v4/view/PagerAdapter.html#notifyDataSetChanged\(\))` similar to AdapterView adapters derived from `[BaseAdapter](http://developer.android.com/reference/android/widget/BaseAdapter.html)`.

出错原因：数据更新必须在main thread进行更新！！结束前还得调用 notifyDataSetChanged() ！！

也就是说，必须得把上面的2步骤，移动到onPublicProgress中才正常。
