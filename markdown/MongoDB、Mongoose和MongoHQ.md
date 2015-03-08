#  MongoDB、Mongoose和MongoHQ 

[ Yuguo ](http://yuguo.us) 2013年 02月 20日 

我在我最新的App中使用了nodejs+MongoDB来作为服务器端，同时把代码部署在 [ Heroku ](http://heroku.com) 上面。好处就是方便扩展，在app发布初期可能没什么用户（也许一直都不会有啊囧），这时候我可以免费使用云平台（PaaS）的资源，而不必花钱购买昂贵的VPS，同时浪费VPS的CPU和内存，以及带宽。而幸运地话，如果用户增加，我也可以方便地在云平台上扩容。 

![image](/files/2013/02/heroku.png)

我尝试了在AppFog上搭建我的nodejs应用，但因为我依赖了jQuery，而jQuery总是报错（http://lol.ap01.aws.af.cm/）。现在部署在Heroku上，没有任何问题。应用还需要完善，所以我就不贴出地址了，大概还需要两周时间完成。 

本文主要介绍数据库相关的3个名词：MongoDB，Mongoose，MongoHQ。 

##  MongoDB 

什么是MongoDB？ 

[ MongoDB ](http://www.mongodb.org/) 是一个开源的 NoSQL 数据库，相比 MySQL 那样的关系型数据库，它更为轻巧、灵活，非常适合在数据规模很大、事务性不强的场合下使用。 

什么是 NoSQL 呢？为了解释清楚，首先让我们来介绍几个概念。在传统的数据库中，数据库的格式是由表（table）、行（row）、字段（field）组成的。表有固定的结构，规定了每行有哪些字段，在创建时被定义，之后修改很困难。行的格式是相同的，由若干个固定的字段组成。每个表可能有若干个字段作为索引（index），这其中有的是主键（primary key），用于约束表中的数据，还有唯一键（unique key），确保字段中不存放重复数据。表和表之间 可能还有相互的约束，称为外键（foreign key）。对数据库的每次查询都要以行为单位，复杂的查询包括嵌套查询、连接查询和交叉表查询。 

拥有这些功能的数据库被称为关系型数据库，关系型数据库通常使用一种叫做 SQL（Structured Query Language）的查询语言作为接口，因此又称为 SQL 数据库。典型的 SQL 数据库有 MySQL、Oracle、Microsoft SQL Server、PostgreSQL、SQLite，等等。 

NoSQL 是 1998 年被提出的，它曾经是一个轻量、开源、不提供SQL功能的关系数据库。但现在 NoSQL 被认为是 Not Only SQL 的简称，主要指非关系型、分布式、不提供 ACID①的数据库系统。正如它的名称所暗示的，NoSQL 设计初衷并不是为了取代 SQL 数据库的，而是作为一个补充，它和 SQL 数据库有着各自不同的适应领域。NoSQL 不像 SQL 数据库一样都有着统一的架构和接口，不同的 NoSQL 数据库系统从里到外可能完全不同。 

** MongoDB 是一个对象数据库 ** ，它没有表、行等概念，也没有固定的模式和结构，所有的数据以文档的形式存储。所谓文档就是一个关联数组式的对象，它的内部由属性组成，一个属性对应的值可能是一个数、字符串、日期、数组，甚至是一个嵌套的文档。 

MongoDB 的数据格式就是 JSON（准确地说，MongoDB 的数据格式是 BSON （Binary JSON） ，它是 JSON 的一个扩展。）因此与 JavaScript 的亲和性很强。这是我在开发nodejs的App的时候就采用了MongoDB作为数据库的原因。 

##  Mongoose 

Mongoose是封装了MongoDB的操作的一个对象模型库，为nodejs而生。就好像我们嫌原生javascript难写，代码量多，于是用jQuery库一样，因为MongoDB的操作接口复杂，不人性，所以有了Mongoose。这个库完全是可选的。 

Mongoose的使用非常简单，在App的package.js中的dependence中加入mongoose，然后 ` npm install ` 即可。 

  * [ Github ](https://github.com/LearnBoost/mongoose)
  * [ Mongoose官网 ](http://mongoosejs.com/)

##  MongoHQ 

[ MongoHQ ](https://www.mongohq.com/home) 是一个托管MongoDB的第三方平台，它的客户包括appfog和heroku这种PaaS提供商。它的最大优点就是能提供稳定、可扩展的MongoDB数据库服务。更细的分工应该是未来的一个趋势，就好像这种PaaS提供商很多都会用Amazon S3作为静态文件托管商。大家通过API来低耦合地合作在一起。 

在heroku中使用MongoHQ非常方便，只需要在Add on中选择MongoHQ，然后就会自动创建一个数据库url，提供了host、url、端口、用户名、密码。这些数据可以直接在我的App中使用，配合Mongoose，只需要一句代码就可以连接数据库。 

![image](/files/2013/02/mongohq.png)

虽然我一直在说各种云服务的无缝连接是多么简单，但实际上我第一次走通整个流程还是费了不少劲。我相信云服务是未来主流，所以多花一点时间去学习，以后会一直受益。 
#### 原文：[http://yuguo.us/weblog/mongodb-and-mongoose-and-mongohq/](http://yuguo.us/weblog/mongodb-and-mongoose-and-mongohq/)