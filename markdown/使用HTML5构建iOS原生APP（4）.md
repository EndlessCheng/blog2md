#  使用HTML5构建iOS原生APP（4） 

[ Yuguo ](http://yuguo.us) 2013年 03月 17日 

今天要解决的问题是，当使用HTML5制作（webview）的时候，如果出现垂直滚动条时，手指滑动页面滚动之后，滚动很快停下来，好像踩着刹车在开车，有“滚动很吃力”的感觉。而原生UITableView之类的滚动非常快。 

我之前考虑的原因是，可能浏览器渲染webview的重绘非常困难，比如各种绝对定位，华丽的CSS，所以iOS系统选择了降低滚动速度以增强webview滚动时的FPS。 

实际上不是这样的，可能是由于使用场景不同，苹果认为用户浏览网页的时候，需要页面滚动不用那么快，所以对webview设置了更高的“减速率”，也就是scrollView的 ` decelerationRate ` 属性。 

当我们用HTML5制作应用程序的时候，希望模拟原生组件比如UITableView的滚动速度，所以代码就很简单了： 
    
    
    //滚动速度正常
    self.webView.scrollView.decelerationRate = UIScrollViewDecelerationRateNormal;
    

但是关于webView重绘的结论仍然是正确的，如果我们没有对页面做合理的优化，那么会出现FPS过低，页面卡顿的情况，可以参考我之前的 [ 使用Chrome的持续绘制模式侦测页面绘制时间 ](http://yuguo.us/weblog/continuous-painting-mode/) 一文。 
#### 原文：[http://yuguo.us/weblog/scroll-speed-in-uiview/](http://yuguo.us/weblog/scroll-speed-in-uiview/)