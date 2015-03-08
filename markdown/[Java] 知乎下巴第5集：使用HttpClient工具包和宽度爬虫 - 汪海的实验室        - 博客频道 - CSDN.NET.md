#  [ [Java] 知乎下巴第5集：使用HttpClient工具包和宽度爬虫 ](/pleasecallmewhy/article/details/18010015)

[ Java ](http://www.csdn.net/tag/Java) [ 爬虫 ](http://www.csdn.net/tag/%e7%88%ac%e8%99%ab)

下载地址： [ https://code.csdn.net/wxg694175346/zhihudown ](https://code.csdn.net/wxg694175346/zhihudown)

  


说到爬虫，使用Java本身自带的  URLConnection  可以实现一些基本的抓取页面的功能，但是对于一些比较高级的功能，比如重定向的处理，HTML标记的去除，仅仅使用  URLConnection  还是不够的。 

在这里我们可以使用HttpClient这个第三方jar包，下载地址 [ 点击这里 ](http://download.csdn.net/detail/fangqingan_java/2341792) 。 

接下来我们使用HttpClient简单的写一个爬去百度的Demo： 
    
    
    import java.io.FileOutputStream;
    import java.io.InputStream;
    import java.io.OutputStream;
    import org.apache.commons.httpclient.HttpClient;
    import org.apache.commons.httpclient.HttpStatus;
    import org.apache.commons.httpclient.methods.GetMethod;
    
    /**
     * 
     * @author CallMeWhy
     * 
     */
    public class Spider {
    	private static HttpClient httpClient = new HttpClient();
    
    	/**
    	 * @param path
    	 *            目标网页的链接
    	 * @return 返回布尔值，表示是否正常下载目标页面
    	 * @throws Exception
    	 *             读取网页流或写入本地文件流的IO异常
    	 */
    	public static boolean downloadPage(String path) throws Exception {
    		// 定义输入输出流
    		InputStream input = null;
    		OutputStream output = null;
    		// 得到 post 方法
    		GetMethod getMethod = new GetMethod(path);
    		// 执行，返回状态码
    		int statusCode = httpClient.executeMethod(getMethod);
    		// 针对状态码进行处理
    		// 简单起见，只处理返回值为 200 的状态码
    		if (statusCode == HttpStatus.SC_OK) {
    			input = getMethod.getResponseBodyAsStream();
    			// 通过对URL的得到文件名
    			String filename = path.substring(path.lastIndexOf('/') + 1)
    					+ ".html";
    			// 获得文件输出流
    			output = new FileOutputStream(filename);
    			// 输出到文件
    			int tempByte = -1;
    			while ((tempByte = input.read()) > 0) {
    				output.write(tempByte);
    			}
    			// 关闭输入流
    			if (input != null) {
    				input.close();
    			}
    			// 关闭输出流
    			if (output != null) {
    				output.close();
    			}
    			return true;
    		}
    		return false;
    	}
    
    	public static void main(String[] args) {
    		try {
    			// 抓取百度首页，输出
    			Spider.downloadPage("http://www.baidu.com");
    		} catch (Exception e) {
    			e.printStackTrace();
    		}
    	}
    }

  
但是这样基本的爬虫是不能满足各色各样的爬虫需求的。 

  


先来介绍宽度优先爬虫。 

宽度优先相信大家都不陌生，简单说来可以这样理解宽度优先爬虫。 

我们把互联网看作一张超级大的有向图，每一个网页上的链接都是一个有向边，每一个文件或没有链接的纯页面则是图中的终点： 

![](http://img.blog.csdn.net/20140106235958984?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


宽度优先爬虫就是这样一个爬虫，爬走在这个有向图上，从根节点开始一层一层往外爬取新的节点的数据。 

宽度遍历算法如下所示： 

(1) 顶点 V 入队列。   
(2) 当队列非空时继续执行，否则算法为空。   
(3) 出队列，获得队头节点 V，访问顶点 V 并标记 V 已经被访问。   
(4) 查找顶点 V 的第一个邻接顶点 col。   
(5) 若 V 的邻接顶点 col 未被访问过，则 col 进队列。   
(6) 继续查找 V 的其他邻接顶点 col，转到步骤(5)，若 V 的所有邻接顶点都已经被访问过，则转到步骤(2)。 

  


按照宽度遍历算法，上图的遍历顺序为：A->B->C->D->E->F->H->G->I，这样一层一层的遍历下去。 

而宽度优先爬虫其实爬取的是一系列的种子节点，和图的遍历基本相同。 

我们可以把需要爬取页面的URL都放在一个TODO表中，将已经访问的页面放在一个Visited表中： 

![](http://img.blog.csdn.net/20140107000848281?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


则宽度优先爬虫的基本流程如下： 

(1) 把解析出的链接和 Visited 表中的链接进行比较，若 Visited 表中不存在此链接， 表示其未被访问过。   
(2) 把链接放入 TODO 表中。   
(3) 处理完毕后，从 TODO 表中取得一条链接，直接放入 Visited 表中。   
(4) 针对这个链接所表示的网页，继续上述过程。如此循环往复。 

  


下面我们就来一步一步制作一个宽度优先的爬虫。 

首先，对于先设计一个数据结构用来存储TODO表， 考虑到需要先进先出所以采用队列，自定义一个Quere类： 
    
    
    import java.util.LinkedList;
    
    /**
     * 自定义队列类 保存TODO表
     */
    public class Queue {
    
    	/**
    	 * 定义一个队列，使用LinkedList实现
    	 */
    	private LinkedList<Object> queue = new LinkedList<Object>(); // 入队列
    
    	/**
    	 * 将t加入到队列中
    	 */
    	public void enQueue(Object t) {
    		queue.addLast(t);
    	}
    
    	/**
    	 * 移除队列中的第一项并将其返回
    	 */
    	public Object deQueue() {
    		return queue.removeFirst();
    	}
    
    	/**
    	 * 返回队列是否为空
    	 */
    	public boolean isQueueEmpty() {
    		return queue.isEmpty();
    	}
    
    	/**
    	 * 判断并返回队列是否包含t
    	 */
    	public boolean contians(Object t) {
    		return queue.contains(t);
    	}
    
    	/**
    	 * 判断并返回队列是否为空
    	 */
    	public boolean empty() {
    		return queue.isEmpty();
    	}
    
    }
    

  
  


  


还需要一个数据结构来记录已经访问过的 URL，即Visited表。 

考虑到这个表的作用，每当要访问一个 URL 的时候，首先在这个数据结构中进行查找，如果当前的 URL 已经存在，则丢弃这个URL任务。 

这个数据结构需要不重复并且能快速查找，所以选择HashSet来存储。 

综上，我们另建一个SpiderQueue类来保存Visited表和TODO表： 
    
    
    import java.util.HashSet;
    import java.util.Set;
    
    /**
     * 自定义类 保存Visited表和unVisited表
     */
    public class SpiderQueue {
    
    	/**
    	 * 已访问的url集合，即Visited表
    	 */
    	private static Set<Object> visitedUrl = new HashSet<>();
    
    	/**
    	 * 添加到访问过的 URL 队列中
    	 */
    	public static void addVisitedUrl(String url) {
    		visitedUrl.add(url);
    	}
    
    	/**
    	 * 移除访问过的 URL
    	 */
    	public static void removeVisitedUrl(String url) {
    		visitedUrl.remove(url);
    	}
    
    	/**
    	 * 获得已经访问的 URL 数目
    	 */
    	public static int getVisitedUrlNum() {
    		return visitedUrl.size();
    	}
    
    	/**
    	 * 待访问的url集合，即unVisited表
    	 */
    	private static Queue unVisitedUrl = new Queue();
    
    	/**
    	 * 获得UnVisited队列
    	 */
    	public static Queue getUnVisitedUrl() {
    		return unVisitedUrl;
    	}
    
    	/**
    	 * 未访问的unVisitedUrl出队列
    	 */
    	public static Object unVisitedUrlDeQueue() {
    		return unVisitedUrl.deQueue();
    	}
    
    	/**
    	 * 保证添加url到unVisitedUrl的时候每个 URL只被访问一次
    	 */
    	public static void addUnvisitedUrl(String url) {
    		if (url != null && !url.trim().equals("") && !visitedUrl.contains(url)
    				&& !unVisitedUrl.contians(url))
    			unVisitedUrl.enQueue(url);
    	}
    
    	/**
    	 * 判断未访问的 URL队列中是否为空
    	 */
    	public static boolean unVisitedUrlsEmpty() {
    		return unVisitedUrl.empty();
    	}
    }

  
  


上面是一些自定义类的封装，接下来就是一个定义一个用来下载网页的工具类，我们将其定义为DownTool类： 
    
    
    package controller;
    
    import java.io.*;
    import org.apache.commons.httpclient.*;
    import org.apache.commons.httpclient.methods.*;
    import org.apache.commons.httpclient.params.*;
    
    public class DownTool {
    	/**
    	 * 根据 URL 和网页类型生成需要保存的网页的文件名，去除 URL 中的非文件名字符
    	 */
    	private String getFileNameByUrl(String url, String contentType) {
    		// 移除 "http://" 这七个字符
    		url = url.substring(7);
    		// 确认抓取到的页面为 text/html 类型
    		if (contentType.indexOf("html") != -1) {
    			// 把所有的url中的特殊符号转化成下划线
    			url = url.replaceAll("[\\?/:*|<>\"]", "_") + ".html";
    		} else {
    			url = url.replaceAll("[\\?/:*|<>\"]", "_") + "."
    					+ contentType.substring(contentType.lastIndexOf("/") + 1);
    		}
    		return url;
    	}
    
    	/**
    	 * 保存网页字节数组到本地文件，filePath 为要保存的文件的相对地址
    	 */
    	private void saveToLocal(byte[] data, String filePath) {
    		try {
    			DataOutputStream out = new DataOutputStream(new FileOutputStream(
    					new File(filePath)));
    			for (int i = 0; i < data.length; i++)
    				out.write(data[i]);
    			out.flush();
    			out.close();
    		} catch (IOException e) {
    			e.printStackTrace();
    		}
    	}
    
    	// 下载 URL 指向的网页
    	public String downloadFile(String url) {
    		String filePath = null;
    		// 1.生成 HttpClinet对象并设置参数
    		HttpClient httpClient = new HttpClient();
    		// 设置 HTTP连接超时 5s
    		httpClient.getHttpConnectionManager().getParams()
    				.setConnectionTimeout(5000);
    		// 2.生成 GetMethod对象并设置参数
    		GetMethod getMethod = new GetMethod(url);
    		// 设置 get请求超时 5s
    		getMethod.getParams().setParameter(HttpMethodParams.SO_TIMEOUT, 5000);
    		// 设置请求重试处理
    		getMethod.getParams().setParameter(HttpMethodParams.RETRY_HANDLER,
    				new DefaultHttpMethodRetryHandler());
    		// 3.执行GET请求
    		try {
    			int statusCode = httpClient.executeMethod(getMethod);
    			// 判断访问的状态码
    			if (statusCode != HttpStatus.SC_OK) {
    				System.err.println("Method failed: "
    						+ getMethod.getStatusLine());
    				filePath = null;
    			}
    			// 4.处理 HTTP 响应内容
    			byte[] responseBody = getMethod.getResponseBody();// 读取为字节数组
    			// 根据网页 url 生成保存时的文件名
    			filePath = "temp\\"
    					+ getFileNameByUrl(url,
    							getMethod.getResponseHeader("Content-Type")
    									.getValue());
    			saveToLocal(responseBody, filePath);
    		} catch (HttpException e) {
    			// 发生致命的异常，可能是协议不对或者返回的内容有问题
    			System.out.println("请检查你的http地址是否正确");
    			e.printStackTrace();
    		} catch (IOException e) {
    			// 发生网络异常
    			e.printStackTrace();
    		} finally {
    			// 释放连接
    			getMethod.releaseConnection();
    		}
    		return filePath;
    	}
    }
    

  
在这里我们需要一个HtmlParserTool类来处理Html标记： 
    
    
    package controller;
    
    import java.util.HashSet;
    import java.util.Set;
    import org.htmlparser.Node;
    import org.htmlparser.NodeFilter;
    import org.htmlparser.Parser;
    import org.htmlparser.filters.NodeClassFilter;
    import org.htmlparser.filters.OrFilter;
    import org.htmlparser.tags.LinkTag;
    import org.htmlparser.util.NodeList;
    import org.htmlparser.util.ParserException;
    
    import model.LinkFilter;
    
    public class HtmlParserTool {
    	// 获取一个网站上的链接，filter 用来过滤链接
    	public static Set<String> extracLinks(String url, LinkFilter filter) {
    		Set<String> links = new HashSet<String>();
    		try {
    			Parser parser = new Parser(url);
    			parser.setEncoding("gb2312");
    
    			// 过滤 <frame >标签的 filter，用来提取 frame 标签里的 src 属性
    			NodeFilter frameFilter = new NodeFilter() {
    				private static final long serialVersionUID = 1L;
    
    				@Override
    				public boolean accept(Node node) {
    					if (node.getText().startsWith("frame src=")) {
    						return true;
    					} else {
    						return false;
    					}
    				}
    			};
    			// OrFilter 来设置过滤 <a> 标签和 <frame> 标签
    			OrFilter linkFilter = new OrFilter(new NodeClassFilter(
    					LinkTag.class), frameFilter);
    			// 得到所有经过过滤的标签
    			NodeList list = parser.extractAllNodesThatMatch(linkFilter);
    			for (int i = 0; i < list.size(); i++) {
    				Node tag = list.elementAt(i);
    				if (tag instanceof LinkTag)// <a> 标签
    				{
    					LinkTag link = (LinkTag) tag;
    					String linkUrl = link.getLink();// URL
    					if (filter.accept(linkUrl))
    						links.add(linkUrl);
    				} else// <frame> 标签
    				{
    					// 提取 frame 里 src 属性的链接， 如 <frame src="test.html"/>
    					String frame = tag.getText();
    					int start = frame.indexOf("src=");
    					frame = frame.substring(start);
    					int end = frame.indexOf(" ");
    					if (end == -1)
    						end = frame.indexOf(">");
    					String frameUrl = frame.substring(5, end - 1);
    					if (filter.accept(frameUrl))
    						links.add(frameUrl);
    				}
    			}
    		} catch (ParserException e) {
    			e.printStackTrace();
    		}
    		return links;
    	}
    }

  
最后我们来写个爬虫类调用前面的封装类和函数： 
    
    
    package controller;
    import java.util.Set;
    
    import model.LinkFilter;
    import model.SpiderQueue;
    
    public class BfsSpider {
    	/**
    	 * 使用种子初始化URL队列
    	 */
    	private void initCrawlerWithSeeds(String[] seeds) {
    		for (int i = 0; i < seeds.length; i++)
    			SpiderQueue.addUnvisitedUrl(seeds[i]);
    	}
    
    	// 定义过滤器，提取以 http://www.xxxx.com开头的链接
    	public void crawling(String[] seeds) {
    		LinkFilter filter = new LinkFilter() {
    			public boolean accept(String url) {
    				if (url.startsWith("http://www.baidu.com"))
    					return true;
    				else
    					return false;
    			}
    		};
    		// 初始化 URL 队列
    		initCrawlerWithSeeds(seeds);
    		// 循环条件：待抓取的链接不空且抓取的网页不多于 1000
    		while (!SpiderQueue.unVisitedUrlsEmpty()
    				&& SpiderQueue.getVisitedUrlNum() <= 1000) {
    			// 队头 URL 出队列
    			String visitUrl = (String) SpiderQueue.unVisitedUrlDeQueue();
    			if (visitUrl == null)
    				continue;
    			DownTool downLoader = new DownTool();
    			// 下载网页
    			downLoader.downloadFile(visitUrl);
    			// 该 URL 放入已访问的 URL 中
    			SpiderQueue.addVisitedUrl(visitUrl);
    			// 提取出下载网页中的 URL
    			Set<String> links = HtmlParserTool.extracLinks(visitUrl, filter);
    			// 新的未访问的 URL 入队
    			for (String link : links) {
    				SpiderQueue.addUnvisitedUrl(link);
    			}
    		}
    	}
    
    	// main 方法入口
    	public static void main(String[] args) {
    		BfsSpider crawler = new BfsSpider();
    		crawler.crawling(new String[] { "http://www.baidu.com" });
    	}
    }

  
运行可以看到，爬虫已经把百度网页下所有的页面都抓取出来了： 

![](http://img.blog.csdn.net/20140109231152906?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/18010015](http://blog.csdn.net/pleasecallmewhy/article/details/18010015)