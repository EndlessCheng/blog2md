#  单入口、MVC和Restful Service

[ Yuguo ](http://yuguo.us) 2012年 04月 19日

首先解释三个名词。

##  单入口web程序

在解释什么是单一入口应用程序之前，我们先来看看传统的 web 应用程序。

news.php 显示新闻列表

news_edit.php 显示新闻编辑页面

这两个页面不但分别实现了两个功能，还成为了应用程序的两个入口。

单一入口的应用程序实际上就是说用一个文件处理所有的 HTTP 请求。例如不管是新闻列表功能还是新闻编辑功能，都是从浏览器访问 index.php 文件。这个
index.php 文件就是这个应用程序的单一入口。

index.php 如何知道用户是要使用哪一个功能呢？

很简单，我们访问 index.php 时跟上一个特定的参数就行了。例如 index.php?action=news 就是显示新闻列表，而
index.php?action=news_edit 就是新闻编辑。

著名的单入口web程序有WordPress，所以用过WordPress的朋友都知道默认的post的url格式是http://yuguo.us/?p=2342
，这是index.php来处理这个请求，接收p=2342参数。

有人会问这样URL不是很不友好吗？

其实通过Apache的htaccess文件可以把URL改写，比如去掉index.php，或者把参数接收改写成字段的模式。 **
web程序是否采用单入口架构，跟用户实际看到URL是什么样子是没有关系的。 ** 单入口文件的优势是比较明显的，比如CodeIgniter对所有请求都能有效
的初始化所需资源，包括安全处理。两个独立的应用使用两个入口，设置不同的配置、使用不同的应用程序是正常的，同时也便于在未来将web应用分离到多个物理服务器上。
CI中index.php文件的第一个PHP语句设置就是当前所在的运行环境。最直接的影响就是错误提示的级别不一样，通过一个开关快速切换开发环境和生产环境。

需要说明的是单入口一般是对逻辑处理通过index.php来单入口dispatch，而js/img/css等静态文件建议丢在index.php所在的根目录，并
且使用绝对URL（变量拼接，不是hard code）。

##  MVC

MVC如今在web开发中大放异彩。虽然其中包括代码的简洁和升级的便利等原因，但是首要原因还是他 ** 提倡的开发工作流 **
。在开发团队中，MVC提供了有效的合作模式，他将各人的职责分为了三个主要的角色。 ** 开发 ** 。开发人员是指处理模型的程序员。他们通常拥有与PHP、数
据库管理、算法、构架和数据校验等方面的相关技能。这一角色通常会负责实现应用程序的编程细节，他们提供API，同时实施处理数据的策略。 ** 设计 ** 。设计
人员处理视图并负责实现应用程序的外观。他们具有如HTML、CSS、JavaScript和图形设计等方面的技能。通常，这一角色负责与外部的通信源交互以决定要开
发或者增强的应用程序的现实的业务规则。设计通常会导致原型的开发，也就是创造能够显示理想功能的模型设计。 ** 集成 ** 。集成工作存在于控制器层中。他将设
计师和开发人员的工作连在一起。集成人员的经验通常比开发人员要少，他们负责切割静态模板并且制作应用程序所需的动态区域。他们还负责代理来自请求源的数据。他们将从
表格中获取请求信息，请这些信息传递给模型，解释结果，并将结果传递给视图。

通过职责分工，开发方法的细节与开发需求的细节分开了，这使得创意学科和技术学科能够更加容易交互。

以腾讯互联网研发部的工作流为例，前端开发就是V（负责HTML/CSS/雪碧图/优化/设计稿还原），做出静态页面之后交付给C（前台开发同学，负责模板页/js/
数据整合）。与此同时后台开发也就是M可以建立模型，创建数据库等等，然后把接口也给到C。拿到两边的数据之后进行整合，把变量插入到HTML中，
并最后给出外网的URL。

##  MVC和单入口

MVC是一种普遍的软件敏捷开发模式，在许多领域特别是桌面编程领域早已经得到了广泛的应用，然而在像php一样的脚本语言中比较难以实现，特别是几年前在脚本语言中
很难看到mvc的实现，但是今年随着众多框架的涌现，mvc在各个框架中得到了初步实现。

在PHP中单入口和MVC可以很好地结合起来。

比如CodeIgniter中的 http://localhost/index.php，所有对应用程序的访问都是必须通过这个入口，正是单一入口才使得mvc模式
得以实现。因为当你访问index.php的时候，应用程序会做大量的初始化工作，调用大量的基础类库，并根据index.php后面的参数加载控制器，然后加载试图
，模型等内容信息。

简而言之，我们创建web程序的时候可以不再考虑url层级以及文件架构之间的关系， 我们专注于C层的class和function就可以生成
http://localhost/class/function这样的url。

这样能让程序代码更清晰，保证了DRY原则（Don’t Repeat Yourself，不要编写重复代码）。

##  Restful Service/URL/API

我之前写 [ CodeIgniter ](http://yuguo.us/weblog/a-introduction-to-codeigniter/)
简介的时候，有朋友留言说URL格式很Restful。

REST是目前大量的Web 2.0网站使用的一种架构方案。Web 上所有的东西（页面、图像等）本质上都是资源。而 REST
正是基于命名资源而非消息的，这就限制了底层技术的曝光，从而给应用程序设计中的松耦合提供了便利条件。例如，下面的 URL
在不暗示任何底层技术的情况下，公开了资源：http://thediscoblog.com/2008/03/20/unambiguously-
analyzing-metrics/。

REST 是一种思维方式，而非协议或标准。

三者之间没有必然联系，不是说只有MVC架构才能使用单入口模式。但是如果使用MVC分离的方法和单入口模式来开始建立应用程序，那么采用REST的方法来思考就更为
轻松了。

参考资料： [ http://www.ibm.com/developerworks/cn/education/java/j-rest/index.html
](http://www.ibm.com/developerworks/cn/education/java/j-rest/index.html) [
http://net.tutsplus.com/tutorials/php/working-with-restful-services-in-
codeigniter-2/ ](http://net.tutsplus.com/tutorials/php/working-with-restful-
services-in-codeigniter-2/)

[ jQuery要杀死js了 → ](/weblog/jquery-is-slowly-killing-javascript/) [ ←
CodeIgniter简介 ](/weblog/a-introduction-to-codeigniter/)

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

© 2009 – 2014 Yuguo. Powered by [ Jekyll ](https://github.com/mojombo/jekyll)
and host by [ Github ](https://github.com/yuguo) 。

