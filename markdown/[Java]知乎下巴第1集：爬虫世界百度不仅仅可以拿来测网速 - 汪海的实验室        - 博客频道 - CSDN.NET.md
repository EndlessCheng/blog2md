#  [ [Java]知乎下巴第1集：爬虫世界百度不仅仅可以拿来测网速 ](/pleasecallmewhy/article/details/17594303)

[ Java ](http://www.csdn.net/tag/Java) [ 爬虫 ](http://www.csdn.net/tag/%e7%88%ac%e8%99%ab) [ 正则表达式 ](http://www.csdn.net/tag/%e6%ad%a3%e5%88%99%e8%a1%a8%e8%be%be%e5%bc%8f) [ 网络爬虫 ](http://www.csdn.net/tag/%e7%bd%91%e7%bb%9c%e7%88%ac%e8%99%ab)

上一集中我们说到需要用Java来制作一个知乎爬虫，那么这一次，我们就来研究一下如何使用代码获取到网页的内容。 

  


首先，没有HTML和CSS和JS和AJAX经验的建议先去W3C（ [ 点我点我 ](http://www.w3school.com.cn/h.asp) ）小小的了解一下。 

  


说到HTML，这里就涉及到一个GET访问和POST访问的问题。 

如果对这个方面缺乏了解可以阅读W3C的这篇： [ 《GET对比POST》 ](http://www.w3school.com.cn/tags/html_ref_httpmethods.asp) 。   


啊哈，在此不再赘述。 

  


然后咧，接下来我们需要用Java来爬取一个网页的内容。 

这时候，我们的百度就要派上用场了。 

没错，他不再是那个默默无闻的网速测试器了，他即将成为我们的爬虫小白鼠！~ 

  


我们先来看看百度的首页： 

![](http://img.blog.csdn.net/20131227222939015?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

相信大家都知道，现在这样的一个页面，是HTML和CSS共同工作的结果。 

我们在浏览器中右击页面，选择“查看页面源代码”： 

![](http://img.blog.csdn.net/20131227223148125?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

没错，就是这一坨翔一样的东西。这就是百度页面的源代码。 

接下来我们的任务，就是使用我们的爬虫也获取到一样的东西。   


  


  


先来看一段简单的源码： 
    
    
    import java.io.*;
    import java.net.*;
    
    public class Main {
    	public static void main(String[] args) {
    		// 定义即将访问的链接
    		String url = "http://www.baidu.com";
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
    				//遍历抓取到的每一行并将其存储到result里面
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
    		System.out.println(result);
    	}
    }
    

  
以上就是Java模拟Get访问百度的Main方法， 

可以运行一下看看结果： 

![](http://img.blog.csdn.net/20131227223500828?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


啊哈，和我们前面用浏览器看到的一模一样。至此，一个最最简单的爬虫就算是做好了。 

  


但是这么一大坨东西未必都是我想要的啊，怎么从中抓取出我想要的东西呢？ 

以百度的大爪子Logo为例。 

  


临时需求： 

获取百度Logo的大爪子的图片链接。 

  


  


先说一下浏览器的查看方法。 

鼠标对图片右击，选择审查元素（火狐，谷歌，IE11，均有此功能，只是名字不太一样）： 

![](http://img.blog.csdn.net/20131227224302140?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

啊哈，可以看到在一大堆div的围攻下的可怜的img标签。 

这个src就是图像的链接了。 

  


那么在java中我们怎么搞呢？ 

事先说明，为了方便演示代码，所有代码均未作类封装，还请谅解。 

我们先把前面的代码封装成一个  sendGet  函数： 
    
    
    import java.io.*;
    import java.net.*;
    
    public class Main {
    	static String sendGet(String url) {
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
    
    	public static void main(String[] args) {
    		// 定义即将访问的链接
    		String url = "http://www.baidu.com";
    		// 访问链接并获取页面内容
    		String result = sendGet(url);
    		System.out.println(result);
    	}
    }
    

  
这样看起来稍微整洁了一点，请原谅我这个强迫症。 

  


接下来的任务，就是从获取到的一大堆东西里面找到那个图片的链接。 

  


我们首先可以想到的方法，是对页面源码的字符串result使用indexof函数进行String的子串搜索。 

没错这个方法是可以慢慢解决这个问题，比如直接indexOf("src")找到开始的序号，然后再稀里哗啦的搞到结束的序号。 

  


不过我们不能一直使用这种方法，毕竟草鞋只适合出门走走，后期还是需要切假腿来拿人头的。 

请原谅我的乱入，继续。   


  


那么我们用什么方式来寻找这张图片的src呢？ 

没错，正如下面观众所说，正则匹配。 

如果有同学不太清楚正则，可以参照这篇文章：  [ [Python]网络爬虫（七）：Python中的正则表达式教程 ](http://blog.csdn.net/pleasecallmewhy/article/details/8929576) 。 

简单来说，正则就像是匹配。 

  


比如三个胖子站在这里，分别穿着红衣服，蓝衣服，绿衣服。 

正则就是：抓住那个穿绿衣服的！ 

然后把绿胖子单独抓了出来。 

就是这么简单。 

但是正则的语法却还是博大精深的，刚接触的时候难免有点摸不着头脑， 

向大家推荐一个正则的在线测试工具： [ 正则表达式在线测试 ](http://tool.chinaz.com/regex/) 。   


  


有了正则这个神兵利器，那么怎么在java里面使用正则呢？ 

先来看个简单的小李子吧。 

啊错了，小栗子。 
    
    
    		// 定义一个样式模板，此中使用正则表达式，括号中是要抓的内容
    		// 相当于埋好了陷阱匹配的地方就会掉下去
    		Pattern pattern = Pattern.compile("href=\"(.+?)\"");
    		// 定义一个matcher用来做匹配
    		Matcher matcher = pattern.matcher("＜a href=\"index.html\"＞我的主页＜/a＞");
    		// 如果找到了
    		if (matcher.find()) {
    			// 打印出结果
    			System.out.println(matcher.group(1));
    		}

  
  


  


运行结果： 

** ** ** index.html **   
  


  


没错，这就是我们的第一个正则代码。 

这样应用的抓取图片的链接想必也是信手拈来了。 

  


我们将正则匹配封装成一个函数，然后将代码作如下修改： 
    
    
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
    		return "";
    	}
    
    	public static void main(String[] args) {
    
    		// 定义即将访问的链接
    		String url = "http://www.baidu.com";
    		// 访问链接并获取页面内容
    		String result = SendGet(url);
    		// 使用正则匹配图片的src内容
    		String imgSrc = RegexString(result, "即将的正则语法");
    		// 打印结果
    		System.out.println(imgSrc);
    	}
    }
    

  
  


  


  


好的，现在万事俱备，只差一个正则语法了！ 

那么用什么正则语句比较合适呢？ 

我们发现只要抓住了src="xxxxxx"这个字符串，就能抓出整个src链接， 

所以简单的正则语句：src=\"(.+?)\" 

  


完整代码如下： 
    
    
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
    		String url = "http://www.baidu.com";
    		// 访问链接并获取页面内容
    		String result = SendGet(url);
    		// 使用正则匹配图片的src内容
    		String imgSrc = RegexString(result, "src=\"(.+?)\"");
    		// 打印结果
    		System.out.println(imgSrc);
    	}
    }
    

  
这样我们就能用java抓出百度LOGO的链接了。 

好吧虽然花了很多时间讲百度，但是基础要打扎实啦，下次我们正式开始抓知乎咯！~   

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/17594303](http://blog.csdn.net/pleasecallmewhy/article/details/17594303)