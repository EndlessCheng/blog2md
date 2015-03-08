#  [ [Java]知乎下巴第2集：使用爬虫来获取知乎的编辑推荐内容 ](/pleasecallmewhy/article/details/17630063)

[ Java ](http://www.csdn.net/tag/Java) [ 网络爬虫 ](http://www.csdn.net/tag/%e7%bd%91%e7%bb%9c%e7%88%ac%e8%99%ab) [ 爬虫 ](http://www.csdn.net/tag/%e7%88%ac%e8%99%ab) [ 正则 ](http://www.csdn.net/tag/%e6%ad%a3%e5%88%99)

上一回我们拿百度做了测试，那么这一次开始做知乎下巴啦。 

首先花个三五分钟设计一个Logo=。=作为一个程序员我一直有一颗做美工的心！ 

  


  


![](http://img.blog.csdn.net/20131228143452000?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


好吧做的有点小凑合，就先凑合着用咯。 

接下来呢，我们开始制作知乎的爬虫。 

  


首先，确定第一个目标：编辑推荐。 

网页链接： [ http://www.zhihu.com/explore/recommendations ](http://www.zhihu.com/explore/recommendations)

  


我们对上次的代码稍作修改，先实现能够获取该页面内容： 
    
    
    import java.io.*;
    import java.net.*;
    import java.util.regex.*;
    
    public class Main {
    	static String SendGet(String url) {
    		// 定义一个字符串用来存储网页内容
    		String result = "";
    		// 定义一个缓冲字符输入流
    		BufferedReader in = null;
    
    		try {
    			// 将string转成url对象
    			URL realUrl = new URL(url);
    			// 初始化一个链接到那个url的连接
    			URLConnection connection = realUrl.openConnection();
    			// 开始实际的连接
    			connection.connect();
    			// 初始化 BufferedReader输入流来读取URL的响应
    			in = new BufferedReader(new InputStreamReader(
    					connection.getInputStream()));
    			// 用来临时存储抓取到的每一行的数据
    			String line;
    			while ((line = in.readLine()) != null) {
    				// 遍历抓取到的每一行并将其存储到result里面
    				result += line;
    			}
    		} catch (Exception e) {
    			System.out.println("发送GET请求出现异常！" + e);
    			e.printStackTrace();
    		}
    		// 使用finally来关闭输入流
    		finally {
    			try {
    				if (in != null) {
    					in.close();
    				}
    			} catch (Exception e2) {
    				e2.printStackTrace();
    			}
    		}
    		return result;
    
    	}
    
    	static String RegexString(String targetStr, String patternStr) {
    		// 定义一个样式模板，此中使用正则表达式，括号中是要抓的内容
    		// 相当于埋好了陷阱匹配的地方就会掉下去
    		Pattern pattern = Pattern.compile(patternStr);
    		// 定义一个matcher用来做匹配
    		Matcher matcher = pattern.matcher(targetStr);
    		// 如果找到了
    		if (matcher.find()) {
    			// 打印出结果
    			return matcher.group(1);
    		}
    		return "Nothing";
    	}
    
    	public static void main(String[] args) {
    
    		// 定义即将访问的链接
    		String url = "http://www.zhihu.com/explore/recommendations";
    		// 访问链接并获取页面内容
    		String result = SendGet(url);
    		// 使用正则匹配图片的src内容
    		//String imgSrc = RegexString(result, "src=\"(.+?)\"");
    		// 打印结果
    		System.out.println(result);
    	}
    }
    

  
运行一下木有问题，接下来就是一个正则匹配的问题了。 

首先我们先来获取该页面的所有的问题。 

右击标题，审查元素： 

![](http://img.blog.csdn.net/20131228121918109?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

啊哈，可以看到标题其实是一个a标签，也就是一个超链接，而其中能够和其他超链接区分开的，应该就是那个class了，也就是类选择器。 

于是我们的正则语句就出来了：question_link.+?href=\"(.+?)\" 

调用RegexString函数，并给它传参： 
    
    
    	public static void main(String[] args) {
    
    		// 定义即将访问的链接
    		String url = "http://www.zhihu.com/explore/recommendations";
    		// 访问链接并获取页面内容
    		String result = SendGet(url);
    		// 使用正则匹配图片的src内容
    		String imgSrc = RegexString(result, "question_link.+?>(.+?)<");
    		// 打印结果
    		System.out.println(imgSrc);
    	}

  
  


啊哈，可以看到我们成功抓到了一个标题（注意，只是一个）：   


![](http://img.blog.csdn.net/20131228123821421?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

等一下啊这一大堆的乱七八糟的是什么玩意？！ 

别紧张=。=它只是字符乱码而已。 

编码问题可以参见： [ HTML字符集 ](http://www.w3school.com.cn/tags/html_ref_charactersets.asp)   


  


一般来说，对中文支持较好的主流编码是UTF-8，GB2312和GBK编码。 

网页可以通过meta标签的charset来设置网页编码，譬如： 
    
    
    <meta charset="utf-8" />

  
  


  
我们右击，查看页面源代码： 

![](http://img.blog.csdn.net/20131228124337843?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

可以看到，知乎采用的是UTF-8编码。 

在这里和大家解释一下查看页面源代码和审查元素的区别。 

查看页面源代码是显示整个页面的所有代码，没有按照HTML的标签进行排版，相当于是直接查看源码，这种方式对于查看整个网页的信息，比如meta比较有用。 

审查元素，或者有的浏览器叫查看元素，是针对你右击的元素进行查看，比如一个div或者img，比较适用于单独查看某个对象的属性和标签。 

  


好的，我们现在知道了问题出在了编码上，接下来就是对抓取到的内容进行编码转换了。 

在java中实现很简单，只需要在InputStreamReader里面指定编码方式就行： 
    
    
    // 初始化 BufferedReader输入流来读取URL的响应
    			in = new BufferedReader(new InputStreamReader(
    					connection.getInputStream(),"UTF-8"));

  
  


此时再运行程序，便会发现可以正常显示标题了： 

![](http://img.blog.csdn.net/20131228125244734?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

好的！非常好！ 

但是现在才只有一个标题，我们需要的是所有的标题。 

我们将正则稍加修改，把搜索到的结果存储到一个ArrayList里面： 
    
    
    import java.io.*;
    import java.net.*;
    import java.util.ArrayList;
    import java.util.regex.*;
    
    public class Main {
    	static String SendGet(String url) {
    		// 定义一个字符串用来存储网页内容
    		String result = "";
    		// 定义一个缓冲字符输入流
    		BufferedReader in = null;
    
    		try {
    			// 将string转成url对象
    			URL realUrl = new URL(url);
    			// 初始化一个链接到那个url的连接
    			URLConnection connection = realUrl.openConnection();
    			// 开始实际的连接
    			connection.connect();
    			// 初始化 BufferedReader输入流来读取URL的响应
    			in = new BufferedReader(new InputStreamReader(
    					connection.getInputStream(), "UTF-8"));
    			// 用来临时存储抓取到的每一行的数据
    			String line;
    			while ((line = in.readLine()) != null) {
    				// 遍历抓取到的每一行并将其存储到result里面
    				result += line;
    			}
    		} catch (Exception e) {
    			System.out.println("发送GET请求出现异常！" + e);
    			e.printStackTrace();
    		}
    		// 使用finally来关闭输入流
    		finally {
    			try {
    				if (in != null) {
    					in.close();
    				}
    			} catch (Exception e2) {
    				e2.printStackTrace();
    			}
    		}
    		return result;
    
    	}
    
    	static ArrayList<String> RegexString(String targetStr, String patternStr) {
    		// 预定义一个ArrayList来存储结果
    		ArrayList<String> results = new ArrayList<String>();
    		// 定义一个样式模板，此中使用正则表达式，括号中是要抓的内容
    		Pattern pattern = Pattern.compile(patternStr);
    		// 定义一个matcher用来做匹配
    		Matcher matcher = pattern.matcher(targetStr);
    		// 如果找到了
    		boolean isFind = matcher.find();
    		// 使用循环将句子里所有的kelvin找出并替换再将内容加到sb里
    		while (isFind) {
    			//添加成功匹配的结果
    			results.add(matcher.group(1));
    			// 继续查找下一个匹配对象
    			isFind = matcher.find();
    		}
    		return results;
    	}
    
    	public static void main(String[] args) {
    
    		// 定义即将访问的链接
    		String url = "http://www.zhihu.com/explore/recommendations";
    		// 访问链接并获取页面内容
    		String result = SendGet(url);
    		// 使用正则匹配图片的src内容
    		ArrayList<String> imgSrc = RegexString(result, "question_link.+?>(.+?)<");
    		// 打印结果
    		System.out.println(imgSrc);
    	}
    }
    

  
  


  


这样就能匹配到所有的结果了（因为直接打印了ArrayList所以会有一些中括号和逗号）： 

![](http://img.blog.csdn.net/20131228130751671?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


  


OK，这样就算是完成了知乎爬虫的第一步。 

但是我们可以看出来，用这样的方式是没有办法抓到所有的问题和回答的。 

我们需要设计一个Zhihu封装类，来存储所有抓取到的对象。 

Zhihu.java源码： 
    
    
    import java.util.ArrayList;
    
    public class Zhihu {
    	public String question;// 问题
    	public String zhihuUrl;// 网页链接
    	public ArrayList<String> answers;// 存储所有回答的数组
    
    	// 构造方法初始化数据
    	public Zhihu() {
    		question = "";
    		zhihuUrl = "";
    		answers = new ArrayList<String>();
    	}
    
    	@Override
    	public String toString() {
    		return "问题：" + question + "\n链接：" + zhihuUrl + "\n回答：" + answers + "\n";
    	}
    }
    

  
  


  


再新建一个Spider类来存放一些爬虫常用的函数。 

Spider.java源码： 
    
    
    import java.io.BufferedReader;
    import java.io.InputStreamReader;
    import java.net.URL;
    import java.net.URLConnection;
    import java.util.ArrayList;
    import java.util.regex.Matcher;
    import java.util.regex.Pattern;
    
    public class Spider {
    	static String SendGet(String url) {
    		// 定义一个字符串用来存储网页内容
    		String result = "";
    		// 定义一个缓冲字符输入流
    		BufferedReader in = null;
    
    		try {
    			// 将string转成url对象
    			URL realUrl = new URL(url);
    			// 初始化一个链接到那个url的连接
    			URLConnection connection = realUrl.openConnection();
    			// 开始实际的连接
    			connection.connect();
    			// 初始化 BufferedReader输入流来读取URL的响应
    			in = new BufferedReader(new InputStreamReader(
    					connection.getInputStream(), "UTF-8"));
    			// 用来临时存储抓取到的每一行的数据
    			String line;
    			while ((line = in.readLine()) != null) {
    				// 遍历抓取到的每一行并将其存储到result里面
    				result += line;
    			}
    		} catch (Exception e) {
    			System.out.println("发送GET请求出现异常！" + e);
    			e.printStackTrace();
    		}
    		// 使用finally来关闭输入流
    		finally {
    			try {
    				if (in != null) {
    					in.close();
    				}
    			} catch (Exception e2) {
    				e2.printStackTrace();
    			}
    		}
    		return result;
    
    	}
    
    	static ArrayList<Zhihu> GetZhihu(String content) {
    		// 预定义一个ArrayList来存储结果
    		ArrayList<Zhihu> results = new ArrayList<Zhihu>();
    		// 用来匹配标题
    		Pattern questionPattern = Pattern.compile("question_link.+?>(.+?)<");
    		Matcher questionMatcher = questionPattern.matcher(content);
    		// 用来匹配url，也就是问题的链接
    		Pattern urlPattern = Pattern.compile("question_link.+?href=\"(.+?)\"");
    		Matcher urlMatcher = urlPattern.matcher(content);
    
    		// 问题和链接要均能匹配到
    		boolean isFind = questionMatcher.find() && urlMatcher.find();
    
    		while (isFind) {
    			// 定义一个知乎对象来存储抓取到的信息
    			Zhihu zhuhuTemp = new Zhihu();
    			zhuhuTemp.question = questionMatcher.group(1);
    			zhuhuTemp.zhihuUrl = "http://www.zhihu.com" + urlMatcher.group(1);
    
    			// 添加成功匹配的结果
    			results.add(zhuhuTemp);
    			// 继续查找下一个匹配对象
    			isFind = questionMatcher.find() && urlMatcher.find();
    		}
    		return results;
    	}
    
    }
    

  
  


最后一个main方法负责调用。 
    
    
    import java.util.ArrayList;
    
    public class Main {
    
    	public static void main(String[] args) {
    		// 定义即将访问的链接
    		String url = "http://www.zhihu.com/explore/recommendations";
    		// 访问链接并获取页面内容
    		String content = Spider.SendGet(url);
    		// 获取该页面的所有的知乎对象
    		ArrayList<Zhihu> myZhihu = Spider.GetZhihu(content);
    		// 打印结果
    		System.out.println(myZhihu);
    	}
    }
    

  
Ok这样就算搞定了。运行一下看看结果： 

![](http://img.blog.csdn.net/20131228141055906?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

好的效果不错。 

接下来就是访问链接然后获取到所有的答案了。 

下一回我们再介绍。   


  


  


  


  


  


  


  


  


  


  


  


  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/17630063](http://blog.csdn.net/pleasecallmewhy/article/details/17630063)