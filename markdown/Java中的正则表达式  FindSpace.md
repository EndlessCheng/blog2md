#  Java中的正则表达式 

[ Find ](http://www.findspace.name/author/find) |  2015年1月14日  |  [ Java ](http://www.findspace.name/category/easycoding/java) , [ 随意Coding ](http://www.findspace.name/category/easycoding) |  [ 没有评论  ](http://www.findspace.name/easycoding/1029#comments)

  * Java中的正则表达式 
    * 正则表达式 
    * Java中使用正则表达式 

##  正则表达式 

正则表达式是个很强大的工具，使用单个字符串来描述、匹配一系列符合某个句法规则的字符串。在很多文本编辑器里，正则表达式通常被用来检索、替换那些符合某个模式的文本。许多程序设计语言都支持利用正则表达式进行字符串操作。 

关于正则表达式，这里有一份 [ 入门文档 ](http://pan.baidu.com/s/1sjNnY4t) 。非常经典，而且非常详细。 

##  Java中使用正则表达式 
    
    
    //line是输入的字符串，例如 " hello 192.168.0.1 www.baidu.com"
    //writeline则是匹配之后的
        Pattern regex=Pattern.compile(".*(\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}).*");
        Matcher regexMatcher;
        regexMatcher=regex.matcher(line);
        if(regexMatcher.find()){
            writeline=regexMatcher.group();、
            ...
        }
    

以上代码是从 [ FetchUpdate ](https://git.oschina.net/findspace/FetchUpdate) 这个工具里找的，作用是读取下载的网页，从中找到含有ip地址的行。 

需要注意的地方： 

\+ java中正则表达式的 ** \ ** 在这里需要换成双斜线，再转义一次。 

\+ ** ( ) ** 的作用非常大， ` regexMatcher.group(); ` 默认是选取含有这一整行，而如果表达式中有括号，则 ` regexMatcher.group(1); ` 只返回括号里匹配的内容。例如，对于输入” hello 192.168.0.1 www.baidu.com”， ` regexMatcher.group(); ` 返回的是这一行，而 ` regexMatcher.group(1); ` 返回的是“192.168.0.1”。如果该行有多个符合的匹配，则都按先后顺序存在 ` regexMatcher.group(); ` 里。 

Tags:  [ Java ](http://www.findspace.name/tag/java) , [ 正则表达式 ](http://www.findspace.name/tag/%e6%ad%a3%e5%88%99%e8%a1%a8%e8%be%be%e5%bc%8f)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/easycoding/1029](http://www.findspace.name/easycoding/1029)