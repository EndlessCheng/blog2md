##  [ 汪海的实验室 ](http://blog.csdn.net/pleasecallmewhy)

###  一名普通小程序员的学习笔记。 博客地址：http://blog.callmewhy.com

  * [ ![](http://static.blog.csdn.net/images/ico_list.gif) 目录视图  ](http://blog.csdn.net/pleasecallmewhy?viewmode=contents)
  * [ ![](http://static.blog.csdn.net/images/ico_summary.gif) 摘要视图  ](http://blog.csdn.net/pleasecallmewhy?viewmode=list)
  * [ ![](http://static.blog.csdn.net/images/ico_rss.gif) 订阅  ](http://blog.csdn.net/pleasecallmewhy/rss/list)

[ CSDN学院讲师招募，诚邀您加入！  ](http://blog.csdn.net/csdnedu/article/details/43306129)
[ 博客Markdown编辑器上线啦
](http://blog.csdn.net/csdnproduct/article/details/43561659) [
那些年我们追过的Wrox精品红皮计算机图书
](http://blog.csdn.net/blogdevteam/article/details/42918959) [ PMBOK第五版精讲视频教程
](http://edu.csdn.net/lecturer/lecturer_detail?lecturer_id=95) [ 火星人敏捷开发1001问
](http://edu.csdn.net/course/detail/443)

#  [ [iOS] Swift的函数式API ](/pleasecallmewhy/article/details/39313843)

分类： [ iOS ](/wxg694175346/article/category/1512775) 2014-09-16 10:24  941人阅读
评论  (4)  [ 收藏 ](javascript:void\(0\);) 举报

[ iOS ](http://www.csdn.net/tag/iOS) [ Swift ](http://www.csdn.net/tag/Swift)
[ 函数式编程
](http://www.csdn.net/tag/%e5%87%bd%e6%95%b0%e5%bc%8f%e7%bc%96%e7%a8%8b)

原文地址： [ http://blog.callmewhy.com/2014/09/11/functional-swift-apis/
](http://blog.callmewhy.com/2014/09/11/functional-swift-apis/)

  

  

  

在过去的时间里，人们对于设计 API 总结了很多通用的模式和最佳实践方案。一般情况下，我们总是可以从苹果的 Foundation、Cocoa、Cocoa
Touch 和很多其他框架中总结出一些开发中的范例。毫无疑问，对于“特定情境下的 API
应该如何设计”这个问题，不同的人总是有着不同的意见，对于这个问题有很大的讨论空间。不过对于很多 Objective-C
的开发者来说，对于那些常用的模式早已习以为常。

随着 Swift 的出现，设计 API 引起了更多的问题。绝大多数情况下，我们只能继续做着手头的工作，然后把现有的方法翻译成 Swift 版本。不过，这对于
Swift 来说并不公平，因为和 Objective-C 相比，Swift 添加了很多新的特性。引用 Swift 创始人 [ Chris Lattner
](https://twitter.com/clattner_llvm) 的一段话：

> Swift 引入了泛型和函数式编程的思想，极大地扩展了设计的空间。

在这篇文章里，我们将会围绕 ` Core Image ` 进行 API 封装，以此为例，探索如何在 API 设计中使用这些新的工具。 ` Core
Image ` 是一个功能强大的图像处理框架，但是它的 API 有时有点笨重。 ` Core Image ` 的 API 是弱类型的 - 它通过键值对
(key-value) 设置图像滤镜。这样在设置参数的类型和名字时很容易失误，会导致运行时错误。新的 API
将会十分的安全和模块化，通过使用类型而不是键值对来规避这样的运行时错误。

##  目标

我们的目标是构建一个 API ，让我们可以简单安全的组装自定义滤镜。举个例子，在文章的结尾，我们可以这样写：

    
    
    let myFilter = blur(blurRadius) >|> colorOverlay(overlayColor)
    let result = myFilter(image)
    

上面构建了一个自定义的滤镜，先模糊图像，然后再添加一个颜色蒙版。为了达到这个目标，我们将充分利用 Swift 函数是一等公民这一特性。项目源码可以在
Github 上的这个 [ 示例项目 ](https://github.com/objcio/issue-16-functional-apis) 中下载。

##  Filter 类型

` CIFilter ` 是 ` Core Image ` 中的一个核心类，用来创建图像滤镜。当实例化一个 ` CIFilter ` 对象之后，你 (几乎)
总是通过 ` kCIInputImageKey ` 来输入图像，然后通过 ` kCIOutputImageKey `
获取返回的图像，返回的结果可以作为下一个滤镜的参数输入。

在我们即将开发的 API 里，我们会把这些键值对 (key-value) 对应的真实内容抽离出来，为用户提供一个安全的强类型
API。我们定义了自己的滤镜类型 ` Filter ` ，它是一个可以传入图片作为参数的函数，并且返回一个新的图片。

    
    
    typealias Filter = CIImage -> CIImage
    

这里我们用 ` typealias ` 关键字，为 ` CIImage -> CIImage `
类型定义了我们自己的名字，这个类型是一个函数，它的参数是一个 ` CIImage ` ，返回值也是 ` CIImage `
。这是我们后面开发需要的基础类型。

如果你不太熟悉函数式编程，你可能对于把一个函数类型命名为 ` Filter `
感觉有点奇怪，通常来说，我们会用这样的命名来定义一个类。如果我们很想以某种方式来表现这个类型的函数式的特性，我们可以把它命名成 `
FilterFunction ` 或者一些其他的类似的名字。但是，我们有意识的选择了 ` Filter ` 这个名字，因为在函数式编程的核心哲学里，函数就是
值，函数和结构体、整数、多元组、或者类，并没有任何区别。一开始我也不是很适应，不过一段时间之后发现，这样做确实很有意义。

##  构建滤镜

现在我们已经定义了 ` Filter ` 类型，接下来可以定义函数来构建特定的滤镜了。这些函数需要参数来设置特定的滤镜，并且返回一个类型为 ` Filter
` 的值。这些函数大概是这个样子：

    
    
    func myFilter(/* parameters */) -> Filter
    

注意返回的值 ` Filter ` 本身就是一个函数，在后面有利于我们将多个滤镜组合起来，以达到理想的处理效果。

为了让后面的开发更轻松一点，我们扩展了 ` CIFilter ` 类，添加了一个 convenience 的初始化方法，以及一个用来获取输出图像的计算属性：

    
    
    typealias Parameters = Dictionary<String, AnyObject>
    
    extension CIFilter {
    
        convenience init(name: String, parameters: Parameters) {
            self.init(name: name)
            setDefaults()
            for (key, value : AnyObject) in parameters {
                setValue(value, forKey: key)
            }
        }
    
        var outputImage: CIImage { return self.valueForKey(kCIOutputImageKey) as CIImage }
    
    }
    

这个 convenience 初始化方法有两个参数，第一个参数是滤镜的名字，第二个参数是一个字典。字典中的键值对将会被设置成新滤镜的参数。我们
convenience 初始化方法先调用了指定的初始化方法，这符合 Swift 的开发规范。

计算属性 ` outputImage ` 可以方便地从滤镜对象中获取到输出的图像。它查找 ` kCIOutputImageKey `
对应的值并且将其转换成一个 ` CIImage ` 对象。通过提供这个属性， API 的用户不再需要对返回的结果手动进行类型转换了。

##  模糊

有了这些东西，现在我们就可以定义属于自己的简单滤镜了。高斯模糊滤镜只需要一个模糊半径作为参数，我们可以非常容易的完成一个模糊滤镜：

    
    
    func blur(radius: Double) -> Filter {
        return { image in
            let parameters : Parameters = [kCIInputRadiusKey: radius, kCIInputImageKey: image]
            let filter = CIFilter(name:"CIGaussianBlur", parameters:parameters)
            return filter.outputImage
        }
    }
    

就是这么简单，这个模糊函数返回了一个函数，新的函数的参数是一个类型为 ` CIImage ` 的图片，返回值 ( ` filter.outputImage
` ) 是一个新的图片 。这个模糊函数的格式是 ` CIImage -> CIImage ` ，满足我们前面定义的 ` Filter ` 类型的格式。

这个例子只是对 ` Core Image ` 中已有滤镜的一个简单的封装，我们可以多次重复同样的模式，创建属于我们自己的滤镜函数。

##  颜色蒙版

现在让我们定义一个颜色滤镜，可以在现有的图片上面加上一层颜色蒙版。 ` Core Image ` 默认没有提供这个滤镜，不过我们可以通过已有的滤镜组装一个。

我们使用两个模块来完成这个工作，一个是颜色生成滤镜 ( ` CIConstantColorGenerator ` )，另一个是资源合成滤镜 ( `
CISourceOverCompositing ` )。让我们先定义一个生成一个常量颜色面板的滤镜：

    
    
    func colorGenerator(color: UIColor) -> Filter {
        return { _ in
            let filter = CIFilter(name:"CIConstantColorGenerator", parameters: [kCIInputColorKey: color])
            return filter.outputImage
        }
    }
    

这段代码看起来和前面的模糊滤镜差不多，不过有一个较为明显的差异：颜色生成滤镜不会检测输入的图片。所以在函数里我们不需要给传入的图片参数命名，我们使用了一个匿
名参数 ` _ ` 来强调这个 filter 的图片参数是被忽略的。

接下来，我们来定义合成滤镜：

    
    
    func compositeSourceOver(overlay: CIImage) -> Filter {
        return { image in
            let parameters : Parameters = [ 
                kCIInputBackgroundImageKey: image, 
                kCIInputImageKey: overlay
            ]
            let filter = CIFilter(name:"CISourceOverCompositing", parameters: parameters)
            return filter.outputImage.imageByCroppingToRect(image.extent())
        }
    }
    

在这里我们将输出图像裁剪到和输入大小一样。这并不是严格需要的，要取决于我们想让滤镜如何工作。不过，在后面我们的例子中我们可以看出来这是一个明智之举。

    
    
    func colorOverlay(color: UIColor) -> Filter {
        return { image in
            let overlay = colorGenerator(color)(image)
            return compositeSourceOver(overlay)(image)
        }
    }
    

我们再一次返回了一个参数为图片的函数， ` colorOverlay ` 在一开始先调用了 ` colorGenerator ` 滤镜。 `
colorGenerator ` 滤镜需要一个颜色作为参数，并且返回一个滤镜。因此 ` colorGenerator(color) ` 是 ` Filter
` 类型的。但是 ` Filter ` 类型本身是一个 ` CIImage ` 向 ` CIImage ` 转换的函数，我们可以在 `
colorGenerator(color) ` 后面加上一个类型为 ` CIImage ` 的参数，这样可以得到一个类型为 ` CIImage `
的蒙版图片。这就是在定义 ` overlay ` 的时候发生的事情：我们用 ` colorGenerator `
函数创建了一个滤镜，然后把图片作为一个参数传给了这个滤镜，从而得到了一张新的图片。返回值 `
compositeSourceOver(overlay)(image) ` 和这个基本相似，它由一个滤镜 `
compositeSourceOver(overlay) ` 和一个图片参数 ` image ` 组成。

##  组合滤镜

现在我们已经定义了一个模糊滤镜和一个颜色滤镜，我们在使用的时候可以把它们组合在一起：我们先将图片做模糊处理，然后再在上面放一个红色的蒙层。让我们先加载一张图
片：

    
    
    let url = NSURL(string: "http://tinyurl.com/m74sldb");
    let image = CIImage(contentsOfURL: url)
    

现在我们可以把滤镜组合起来，同时应用到一张图片上：

    
    
    let blurRadius = 5.0
    let overlayColor = UIColor.redColor().colorWithAlphaComponent(0.2)
    let blurredImage = blur(blurRadius)(image)
    let overlaidImage = colorOverlay(overlayColor)(blurredImage)
    

我们又一次的通过滤镜组装了图片。比如在倒数第二行，我们先得到了模糊滤镜 ` blur(blurRadius) ` ，然后再把这个滤镜应用到图片上。

##  函数组装

不过，我们可以做的比上面的更好。我们可以简单的把两行滤镜的调用组合在一起变成一行，这是我脑海中想到的第一个能改进的地方：

    
    
    let result = colorOverlay(overlayColor)(blur(blurRadius)(image))
    

不过，这些圆括号让这行代码完全不具有可读性，更好的方式是定义一个函数来完成这项任务：

    
    
    func composeFilters(filter1: Filter, filter2: Filter) -> Filter {
        return { img in filter2(filter1(img)) }
    }
    

` composeFilters ` 函数的两个参数都是 Filter ，并且返回了一个新的 Filter 滤镜。组装后的滤镜需要一个 ` CIImage
` 类型的参数，并且会把这个参数分别传给 ` filter1 ` 和 ` filter2 ` 。现在我们可以用 ` composeFilters `
来定义我们自己的组合滤镜：

    
    
    let myFilter = composeFilters(blur(blurRadius), colorOverlay(overlayColor))
    let result = myFilter(image)
    

我们还可以更进一步的定义一个滤镜运算符，让代码更具有可读性，

    
    
    infix operator >|> { associativity left }
    
    func >|> (filter1: Filter, filter2: Filter) -> Filter {
        return { img in filter2(filter1(img)) }
    }
    

运算符通过 ` infix ` 关键字定义，表明运算符具有 ` 左 ` 和 ` 右 ` 两个参数。 ` associativity left `
表明这个运算满足左结合律，即：f1 >|> f2 >|> f3 等价于 (f1 >|> f2) >|>
f3。通过使这个运算满足左结合律，再加上运算内先应用了左侧的滤镜，所以在使用的时候滤镜顺序是从左往右的，就像 Unix 管道一样。

剩余的部分是一个函数，内容和 ` composeFilters ` 基本相同，只不过函数名变成了 ` >|> ` 。

接下来我们把这个组合滤镜运算器应用到前面的例子中：

    
    
    let myFilter = blur(blurRadius) >|> colorOverlay(overlayColor)
    let result = myFilter(image)
    

运算符让代码变得更易于阅读和理解滤镜使用的顺序，调用滤镜的时候也更加的方便。就好比是 ` 1 + 2 + 3 + 4 ` 要比 `
add(add(add(1, 2), 3), 4) ` 更加清晰，更加容易理解。

##  自定义运算符

很多 Objective-C 的开发者对于自定义运算符持有怀疑态度。在 Swift 刚发布的时候，这是一个并没有很受欢迎的特性。很多人在 C++
中遭遇过自定义运算符过度使用 (甚至滥用) 的情况，有些是个人经历过的，有些是听到别人谈起的。

你可能对于前面定义的运算符 ` >|> ` 持有同样的怀疑态度，毕竟如果每个人都定义自己的运算符，那代码岂不是很难理解了？值得庆幸的是在函数式编程里有很多的
操作，为这些操作定义一个运算符并不是一件很罕见的事情。

我们定义的滤镜组合运算符是一个 [ 函数组合
](http://en.wikipedia.org/wiki/Function_composition_%28computer_science%29)
的例子，这是一个在函数式编程中广泛使用的概念。在数学里，两个函数 ` f ` 和 ` g ` 的组合有时候写做 ` f ∘ g `
，这样定义了一种全新的函数，将输入的 ` x ` 映射到 ` f(g(x)) ` 上。这恰好就是我们的 ` >|> ` 所做的工作 (除了函数的逆向调用)。

##  泛型

仔细想想，其实我们并没有必要去定义一个用来专门组装滤镜的运算符，我们可以用一个泛型的运算符来组装函数。目前我们的 ` >|> ` 是这样的：

    
    
    func >|> (filter1: Filter, filter2: Filter) -> Filter
    

这样定义之后，我们传入的参数只能是 ` Filter ` 类型的滤镜。

但是，我们可以利用 Swift 的通用特性来定义一个泛型的函数组合运算符：

    
    
    func >|> <A, B, C>(lhs: A -> B, rhs: B -> C) -> A -> C {
        return { x in rhs(lhs(x)) }
    }
    

这个一开始可能很难理解 — 至少对我来说是这样。但是分开的看了各个部分之后，一切都变得清晰起来。

首先，我们来看一下函数名后面的尖括号。尖括号定义了这个函数适用的泛型类型。在这个例子里我们定义了三个类型：A、B 和
C。因为我们并没有指定这些类型，所以它们可以代表任何东西。

接下来让我们来看看函数的参数：第一个参数：lhs (left-hand side 的缩写)，是一个类型为 A -> B 的函数。这代表一个函数的参数为
A，返回值的类型为 B。第二个参数：rhs (right-hand side 的缩写)，是一个类型为 B -> C 的函数。参数命名为 lhs 和
rhs，因为它们分别对应操作符左边和右边的值。

重写了没有 ` Filter ` 的滤镜组合运算符之后，我们很快就发现其实前面实现的组合运算符只是泛型函数中的一个特殊情况：

    
    
    func >|> (filter1: CIImage -> CIImage, filter2: CIImage -> CIImage) -> CIImage -> CIImage
    

把我们脑海中的泛型类型 A、B、C 都换成 ` CIImage ` ，这样可以清晰的理解用通用运算符的来替换滤镜组合运算符是多么的有用。

##  结论

至此，我们成功的用函数式 API 封装了 ` Core Image ` 。希望这个例子能够很好的说明，对于 Objective-C
的开发者来说，在我们所熟知的 API 的设计模式之外有一片完全不同的世界。有了 Swift，我们现在可以动手探索那些全新的领域，并且将它们充分地利用起来。

  

  * 上一篇  [ [iOS] 初探 iOS8 中的 Size Class ](/pleasecallmewhy/article/details/39295327)
  * 下一篇  [ [iOS] 用 Swift 开发一个 TODO 应用 ](/pleasecallmewhy/article/details/39321255)

顶

     2 

踩

     0 

主题推荐

     [ 函数式 ](http://www.csdn.net/tag/函数式) [ ios ](http://www.csdn.net/tag/ios) [ swift ](http://www.csdn.net/tag/swift) [ 函数式编程 ](http://www.csdn.net/tag/函数式编程) [ 设计模式 ](http://www.csdn.net/tag/设计模式)

猜你在找

查看评论

* 以上用户言论只代表其个人观点，不代表CSDN网站的观点或立场 

![快速回复](http://static.blog.csdn.net/images/blog-icon-reply.png)
![TOP](http://static.blog.csdn.net/images/top.png)

#####  [ 核心技术类目 ](http://www.csdn.net/tag/)

[ 全部主题 ](http://www.csdn.net/tag) [ Hadoop ](http://g.csdn.net/5272865) [ AWS
](http://g.csdn.net/5272866) [ 移动游戏 ](http://g.csdn.net/5272870) [ Java
](http://g.csdn.net/5272871) [ Android ](http://g.csdn.net/5272872) [ iOS
](http://g.csdn.net/5272873) [ Swift ](http://g.csdn.net/5272868) [ 智能硬件
](http://g.csdn.net/5272869) [ Docker ](http://g.csdn.net/5272867) [ OpenStack
](http://g.csdn.net/5272925) [ VPN ](http://www.csdn.net/tag/vpn) [ Spark
](http://g.csdn.net/5272924) [ ERP ](http://www.csdn.net/tag/erp) [ IE10
](http://www.csdn.net/tag/ie10) [ Eclipse ](http://www.csdn.net/tag/eclipse) [
CRM ](http://www.csdn.net/tag/crm) [ JavaScript
](http://www.csdn.net/tag/javascript) [ 数据库 ](http://www.csdn.net/tag/数据库) [
Ubuntu ](http://www.csdn.net/tag/ubuntu) [ NFC ](http://www.csdn.net/tag/nfc)
[ WAP ](http://www.csdn.net/tag/wap) [ jQuery
](http://www.csdn.net/tag/jquery) [ BI ](http://www.csdn.net/tag/bi) [ HTML5
](http://www.csdn.net/tag/html5) [ Spring ](http://www.csdn.net/tag/spring) [
Apache ](http://www.csdn.net/tag/apache) [ .NET
](http://www.csdn.net/tag/.net) [ API ](http://www.csdn.net/tag/api) [ HTML
](http://www.csdn.net/tag/html) [ SDK ](http://www.csdn.net/tag/sdk) [ IIS
](http://www.csdn.net/tag/iis) [ Fedora ](http://www.csdn.net/tag/fedora) [
XML ](http://www.csdn.net/tag/xml) [ LBS ](http://www.csdn.net/tag/lbs) [
Unity ](http://www.csdn.net/tag/unity) [ Splashtop
](http://www.csdn.net/tag/splashtop) [ UML ](http://www.csdn.net/tag/uml) [
components ](http://www.csdn.net/tag/components) [ Windows Mobile
](http://www.csdn.net/tag/windowsmobile) [ Rails
](http://www.csdn.net/tag/rails) [ QEMU ](http://www.csdn.net/tag/qemu) [ KDE
](http://www.csdn.net/tag/kde) [ Cassandra
](http://www.csdn.net/tag/cassandra) [ CloudStack
](http://www.csdn.net/tag/cloudstack) [ FTC ](http://www.csdn.net/tag/ftc) [
coremail ](http://www.csdn.net/tag/coremail) [ OPhone
](http://www.csdn.net/tag/ophone ) [ CouchBase
](http://www.csdn.net/tag/couchbase) [ 云计算 ](http://www.csdn.net/tag/云计算) [
iOS6 ](http://www.csdn.net/tag/iOS6) [ Rackspace
](http://www.csdn.net/tag/rackspace ) [ Web App
](http://www.csdn.net/tag/webapp) [ SpringSide
](http://www.csdn.net/tag/springside) [ Maemo ](http://www.csdn.net/tag/maemo)
[ Compuware ](http://www.csdn.net/tag/compuware) [ 大数据
](http://www.csdn.net/tag/大数据) [ aptech ](http://www.csdn.net/tag/aptech) [
Perl ](http://www.csdn.net/tag/perl) [ Tornado
](http://www.csdn.net/tag/tornado) [ Ruby ](http://www.csdn.net/tag/ruby) [
Hibernate ](http://www.csdn.net/hibernate) [ ThinkPHP
](http://www.csdn.net/tag/thinkphp) [ HBase ](http://www.csdn.net/tag/hbase) [
Pure ](http://www.csdn.net/tag/pure) [ Solr ](http://www.csdn.net/tag/solr) [
Angular ](http://www.csdn.net/tag/angular) [ Cloud Foundry
](http://www.csdn.net/tag/cloudfoundry) [ Redis
](http://www.csdn.net/tag/redis) [ Scala ](http://www.csdn.net/tag/scala) [
Django ](http://www.csdn.net/tag/django) [ Bootstrap
](http://www.csdn.net/tag/bootstrap)

个人资料

[ ![](http://avatar.csdn.net/5/D/9/1_wxg694175346.jpg)
](http://my.csdn.net/wxg694175346)  
[ wxg694175346 ](http://my.csdn.net/wxg694175346)

[ ](javascript:void\(0\);) [ ](javascript:void\(0\);)

![2](http://csdnimg.cn/jifen/images/xunzhang/xunzhang/zhuanlandaren.png)
![1](http://csdnimg.cn/jifen/images/xunzhang/xunzhang/chizhiyiheng.png)

    * 访问：  1035561次 
    * 积分：  12112 
    * 等级：  ![](http://csdnimg.cn/jifen/images/xunzhang/jianzhang/blog7.png)

积分：12112

    * 排名：  第390名 
    * 原创：  270篇 
    * 转载：  15篇 
    * 译文：  14篇 
    * 评论：  856条 

我的邮箱  whywanghai@gmail.com

新浪微博  [ ![](http://img.my.csdn.net/uploads/201312/15/1387088999_1404.png)
](http://weibo.com/small1030light)

文章搜索

博客专栏  [ ![](http://avatar.csdn.net/blogpic/20131003093705406.jpg)
](http://blog.csdn.net/column/details/call-me-ogre.html) |  [ 谈一谈OGRE游戏引擎
](http://blog.csdn.net/column/details/call-me-ogre.html)

文章：12篇

阅读：12540  
---|---  
[ ![](http://avatar.csdn.net/blogpic/20130515134502305.jpg)
](http://blog.csdn.net/column/details/why-bug.html) |  [ Python爬虫入门教程
](http://blog.csdn.net/column/details/why-bug.html)

文章：12篇

阅读：458675  
---|---  
[ ![](http://avatar.csdn.net/blogpic/20130208175124735.jpg)
](http://blog.csdn.net/column/details/call-me-why.html) |  [ PHP学习笔记
](http://blog.csdn.net/column/details/call-me-why.html)

文章：23篇

阅读：43213  
---|---  
[ ![](http://avatar.csdn.net/blogpic/20130107235224912.jpg)
](http://blog.csdn.net/column/details/i-am-why.html) |  [ 汪海带你做游戏--
Unity3D的开发与应用 ](http://blog.csdn.net/column/details/i-am-why.html)

文章：35篇

阅读：111909  
---|---  
  
文章分类

  * [ 计算机图形学 ](http://blog.csdn.net/wxg694175346/article/category/1278424) (32) 
  * [ 数据结构 ](http://blog.csdn.net/wxg694175346/article/category/1278425) (30) 
  * [ Linux ](http://blog.csdn.net/wxg694175346/article/category/1278588) (5) 
  * [ 数据库 ](http://blog.csdn.net/wxg694175346/article/category/1280693) (5) 
  * [ Matlab ](http://blog.csdn.net/wxg694175346/article/category/1283631) (8) 
  * [ Unity3D ](http://blog.csdn.net/wxg694175346/article/category/1302926) (35) 
  * [ C++ ](http://blog.csdn.net/wxg694175346/article/category/1303968) (38) 
  * [ 计算机组成原理 ](http://blog.csdn.net/wxg694175346/article/category/1305100) (4) 
  * [ JavaScript ](http://blog.csdn.net/wxg694175346/article/category/1335773) (9) 
  * [ Axure ](http://blog.csdn.net/wxg694175346/article/category/1338189) (2) 
  * [ SAE ](http://blog.csdn.net/wxg694175346/article/category/1338860) (4) 
  * [ PowerDesign ](http://blog.csdn.net/wxg694175346/article/category/1338951) (3) 
  * [ PHP ](http://blog.csdn.net/wxg694175346/article/category/1341271) (31) 
  * [ SVN ](http://blog.csdn.net/wxg694175346/article/category/1341321) (1) 
  * [ XML ](http://blog.csdn.net/wxg694175346/article/category/1342505) (1) 
  * [ CSS ](http://blog.csdn.net/wxg694175346/article/category/1342677) (6) 
  * [ C# ](http://blog.csdn.net/wxg694175346/article/category/1342952) (2) 
  * [ CodeIgniter ](http://blog.csdn.net/wxg694175346/article/category/1343659) (15) 
  * [ Python ](http://blog.csdn.net/wxg694175346/article/category/1344887) (27) 
  * [ jQuery ](http://blog.csdn.net/wxg694175346/article/category/1345185) (6) 
  * [ Windows8 ](http://blog.csdn.net/wxg694175346/article/category/1370237) (17) 
  * [ Java ](http://blog.csdn.net/wxg694175346/article/category/1387661) (9) 
  * [ PhotoShop ](http://blog.csdn.net/wxg694175346/article/category/1388288) (2) 
  * [ Django ](http://blog.csdn.net/wxg694175346/article/category/1413227) (5) 
  * [ SQL ](http://blog.csdn.net/wxg694175346/article/category/1416701) (1) 
  * [ 爬虫 ](http://blog.csdn.net/wxg694175346/article/category/1418998) (19) 
  * [ Ajax ](http://blog.csdn.net/wxg694175346/article/category/1430006) (1) 
  * [ 操作系统 ](http://blog.csdn.net/wxg694175346/article/category/1431103) (2) 
  * [ C ](http://blog.csdn.net/wxg694175346/article/category/1431104) (1) 
  * [ wifi ](http://blog.csdn.net/wxg694175346/article/category/1474173) (1) 
  * [ Android ](http://blog.csdn.net/wxg694175346/article/category/1494279) (1) 
  * [ iOS ](http://blog.csdn.net/wxg694175346/article/category/1512775) (29) 
  * [ Chrome ](http://blog.csdn.net/wxg694175346/article/category/1554113) (1) 
  * [ OGRE ](http://blog.csdn.net/wxg694175346/article/category/1660481) (12) 
  * [ Cocos2D-X ](http://blog.csdn.net/wxg694175346/article/category/1683931) (4) 
  * [ OpenGL ](http://blog.csdn.net/wxg694175346/article/category/1690953) (5) 
  * [ OpenCV ](http://blog.csdn.net/wxg694175346/article/category/1710675) (2) 
  * [ 数字图像处理 ](http://blog.csdn.net/wxg694175346/article/category/1824293) (1) 
  * [ Html ](http://blog.csdn.net/wxg694175346/article/category/1851815) (1) 
  * [ Grails ](http://blog.csdn.net/wxg694175346/article/category/1875691) (1) 
  * [ Groovy ](http://blog.csdn.net/wxg694175346/article/category/1875693) (1) 
  * [ MCM ](http://blog.csdn.net/wxg694175346/article/category/1882757) (1) 
  * [ Node.js ](http://blog.csdn.net/wxg694175346/article/category/2036855) (4) 
  * [ Hexo ](http://blog.csdn.net/wxg694175346/article/category/2036859) (1) 
  * [ Worktile ](http://blog.csdn.net/wxg694175346/article/category/2283405) (1) 
  * [ Git ](http://blog.csdn.net/wxg694175346/article/category/2310295) (1) 
  * [ API ](http://blog.csdn.net/wxg694175346/article/category/2316053) (1) 
  * [ PostgreSQL ](http://blog.csdn.net/wxg694175346/article/category/2343533) (1) 
  * [ Swift ](http://blog.csdn.net/wxg694175346/article/category/2582661) (4) 

文章存档

  * [ 2015年02月 ](http://blog.csdn.net/wxg694175346/article/month/2015/02) (1) 
  * [ 2015年01月 ](http://blog.csdn.net/wxg694175346/article/month/2015/01) (2) 
  * [ 2014年12月 ](http://blog.csdn.net/wxg694175346/article/month/2014/12) (2) 
  * [ 2014年11月 ](http://blog.csdn.net/wxg694175346/article/month/2014/11) (1) 
  * [ 2014年10月 ](http://blog.csdn.net/wxg694175346/article/month/2014/10) (2) 
  * [ 2014年09月 ](http://blog.csdn.net/wxg694175346/article/month/2014/09) (11) 
  * [ 2014年08月 ](http://blog.csdn.net/wxg694175346/article/month/2014/08) (3) 
  * [ 2014年07月 ](http://blog.csdn.net/wxg694175346/article/month/2014/07) (3) 
  * [ 2014年06月 ](http://blog.csdn.net/wxg694175346/article/month/2014/06) (15) 
  * [ 2014年05月 ](http://blog.csdn.net/wxg694175346/article/month/2014/05) (6) 
  * [ 2014年04月 ](http://blog.csdn.net/wxg694175346/article/month/2014/04) (2) 
  * [ 2014年03月 ](http://blog.csdn.net/wxg694175346/article/month/2014/03) (1) 
  * [ 2014年02月 ](http://blog.csdn.net/wxg694175346/article/month/2014/02) (3) 
  * [ 2014年01月 ](http://blog.csdn.net/wxg694175346/article/month/2014/01) (5) 
  * [ 2013年12月 ](http://blog.csdn.net/wxg694175346/article/month/2013/12) (15) 
  * [ 2013年10月 ](http://blog.csdn.net/wxg694175346/article/month/2013/10) (13) 
  * [ 2013年09月 ](http://blog.csdn.net/wxg694175346/article/month/2013/09) (5) 
  * [ 2013年08月 ](http://blog.csdn.net/wxg694175346/article/month/2013/08) (4) 
  * [ 2013年07月 ](http://blog.csdn.net/wxg694175346/article/month/2013/07) (4) 
  * [ 2013年06月 ](http://blog.csdn.net/wxg694175346/article/month/2013/06) (3) 
  * [ 2013年05月 ](http://blog.csdn.net/wxg694175346/article/month/2013/05) (19) 
  * [ 2013年04月 ](http://blog.csdn.net/wxg694175346/article/month/2013/04) (12) 
  * [ 2013年03月 ](http://blog.csdn.net/wxg694175346/article/month/2013/03) (26) 
  * [ 2013年02月 ](http://blog.csdn.net/wxg694175346/article/month/2013/02) (36) 
  * [ 2013年01月 ](http://blog.csdn.net/wxg694175346/article/month/2013/01) (41) 
  * [ 2012年12月 ](http://blog.csdn.net/wxg694175346/article/month/2012/12) (28) 
  * [ 2012年11月 ](http://blog.csdn.net/wxg694175346/article/month/2012/11) (38) 

阅读排行

  * [ [Python]网络爬虫（二）：利用urllib2通过指定的URL抓取网页内容 ](/pleasecallmewhy/article/details/8923067) (72317) 
  * [ [Python]网络爬虫（一）：抓取网页的含义和URL基本构成 ](/pleasecallmewhy/article/details/8922826) (61829) 
  * [ [Python]网络爬虫（三）：异常的处理和HTTP状态码的分类 ](/pleasecallmewhy/article/details/8923725) (39773) 
  * [ [Python]网络爬虫（五）：urllib2的使用细节与抓站技巧 ](/pleasecallmewhy/article/details/8925978) (39301) 
  * [ [Python]网络爬虫（七）：Python中的正则表达式教程 ](/pleasecallmewhy/article/details/8929576) (39070) 
  * [ [Python]网络爬虫（12）：爬虫框架Scrapy的第一个爬虫示例入门教程 ](/pleasecallmewhy/article/details/19642329) (36601) 
  * [ [Python]网络爬虫（六）：一个简单的百度贴吧的小爬虫 ](/pleasecallmewhy/article/details/8927832) (33369) 
  * [ [Python]网络爬虫（四）：Opener与Handler的介绍和实例应用 ](/pleasecallmewhy/article/details/8924889) (32705) 
  * [ [Python]网络爬虫（八）：糗事百科的网络爬虫（v0.3）源码及解析(简化更新) ](/pleasecallmewhy/article/details/8932310) (31985) 
  * [ [Python]网络爬虫（十）：一个爬虫的诞生全过程（以山东大学绩点运算为例） ](/pleasecallmewhy/article/details/9305229) (28040) 

评论排行

  * [ [Python]网络爬虫（八）：糗事百科的网络爬虫（v0.3）源码及解析(简化更新) ](/pleasecallmewhy/article/details/8932310) (138) 
  * [ [Python]网络爬虫（十）：一个爬虫的诞生全过程（以山东大学绩点运算为例） ](/pleasecallmewhy/article/details/9305229) (78) 
  * [ [Python]网络爬虫（二）：利用urllib2通过指定的URL抓取网页内容 ](/pleasecallmewhy/article/details/8923067) (64) 
  * [ [Python]网络爬虫（六）：一个简单的百度贴吧的小爬虫 ](/pleasecallmewhy/article/details/8927832) (56) 
  * [ [Python]网络爬虫（12）：爬虫框架Scrapy的第一个爬虫示例入门教程 ](/pleasecallmewhy/article/details/19642329) (53) 
  * [ [Python]网络爬虫（九）：百度贴吧的网络爬虫（v0.4）源码及解析 ](/pleasecallmewhy/article/details/8934726) (49) 
  * [ [Python]网络爬虫（一）：抓取网页的含义和URL基本构成 ](/pleasecallmewhy/article/details/8922826) (41) 
  * [ [Python]项目打包：5步将py文件打包成exe文件 ](/pleasecallmewhy/article/details/8935135) (26) 
  * [ [Python]网络爬虫（三）：异常的处理和HTTP状态码的分类 ](/pleasecallmewhy/article/details/8923725) (25) 
  * [ [Review]To be coder(2011.08.01~2014.01.11-Grails-ing) ](/pleasecallmewhy/article/details/8515820) (17) 

推荐文章

最新评论

  * [ [Python]网络爬虫（12）：爬虫框架Scrapy的第一个爬虫示例入门教程 ](/pleasecallmewhy/article/details/19642329#comments)

[ u014375100 ](/u014375100) :
@u012230838:http://jgjz.hzjg.gov.cn/jgjz/getMrcjAl...

  * [ [Python]网络爬虫（二）：利用urllib2通过指定的URL抓取网页内容 ](/pleasecallmewhy/article/details/8923067#comments)

[ yunixiang ](/yunixiang) :
@Tassadar_map:博主代码中这句应该删掉，否则不能运行，这句的语法相当于并列了几个查询条件...

  * [ [Python]网络爬虫（八）：糗事百科的网络爬虫（v0.3）源码及解析(简化更新) ](/pleasecallmewhy/article/details/8932310#comments)

[ lixu_puppet ](/lixu_puppet) :
我使用的linux操作系统，不管是那个代码都是无法链接。。我猜是user_agent的问题，但是我不...

  * [ [Python]网络爬虫（十）：一个爬虫的诞生全过程（以山东大学绩点运算为例） ](/pleasecallmewhy/article/details/9305229#comments)

[ oDaHua12 ](/oDaHua12) :
作者前半部分分析post的提交地址走了很多弯路，在HTTPfox抓包显示在POST那行后面的URL就...

  * [ [Python]网络爬虫（十）：一个爬虫的诞生全过程（以山东大学绩点运算为例） ](/pleasecallmewhy/article/details/9305229#comments)

[ dingding_1983 ](/dingding_1983) :
楼主你好，我是外行的。刚才试着用火狐抓取下面这个网址，http://www.sse.com.cn/d...

  * [ [Python]网络爬虫（一）：抓取网页的含义和URL基本构成 ](/pleasecallmewhy/article/details/8922826#comments)

[ colouful987 ](/colouful987) : 想学点python写个爬虫，来看看。又逛了你的各站，发现你居然也搞swift，哈哈哈 有缘啊

  * [ [Python]网络爬虫（九）：百度贴吧的网络爬虫（v0.4）源码及解析 ](/pleasecallmewhy/article/details/8934726#comments)

[ sinat_25837091 ](/sinat_25837091) :
非常感谢博主的分享，我现在正在尝试把爬虫修改之后爬tripadvisor的用户评价，但是在评论中有很...

  * [ [Python]网络爬虫（六）：一个简单的百度贴吧的小爬虫 ](/pleasecallmewhy/article/details/8927832#comments)

[ sinat_24746081 ](/sinat_24746081) :
弱弱的问一个小白问题，可以爬有css和js的网页么？如果不能顺便问一下我用模板做的H5页面，通过浏览...

  * [ [Python]网络爬虫（六）：一个简单的百度贴吧的小爬虫 ](/pleasecallmewhy/article/details/8927832#comments)

[ jiaxingpride ](/jiaxingpride) : 楼主你好！小白求教一个问题：bdurl =
str(raw_input(u'请输入贴吧的地址，去掉p...

  * [ [Python]网络爬虫（二）：利用urllib2通过指定的URL抓取网页内容 ](/pleasecallmewhy/article/details/8927832#comments)

[ Tassadar_map ](/Tassadar_map) :
name=Somebody+Here&language=Python&location=Northa...

