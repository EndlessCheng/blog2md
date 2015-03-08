#  [ [Java]知乎下巴第4集：再把抓到篮子里的知乎塞到硬盘里吧 ](/pleasecallmewhy/article/details/17720641)

[ Java ](http://www.csdn.net/tag/Java) [ 爬虫 ](http://www.csdn.net/tag/%e7%88%ac%e8%99%ab)

上一回我们说到了如何把知乎的某些内容爬取出来，那么这一回我们就说说怎么把这些内容存储到本地吧。 

  


说到Java的本地存储，肯定使用IO流进行操作。 

首先，我们需要一个创建文件的函数createNewFile： 
    
    
    public static boolean createNewFile(String filePath) {
    		boolean isSuccess = true;
    		// 如有则将"\\"转为"/",没有则不产生任何变化
    		String filePathTurn = filePath.replaceAll("\\\\", "/");
    		// 先过滤掉文件名
    		int index = filePathTurn.lastIndexOf("/");
    		String dir = filePathTurn.substring(0, index);
    		// 再创建文件夹
    		File fileDir = new File(dir);
    		isSuccess = fileDir.mkdirs();
    		// 创建文件
    		File file = new File(filePathTurn);
    		try {
    			isSuccess = file.createNewFile();
    		} catch (IOException e) {
    			isSuccess = false;
    			e.printStackTrace();
    		}
    		return isSuccess;
    	}

  
然后，我们需要一个写入文件的函数： 
    
    
    public static boolean writeIntoFile(String content, String filePath,
    			boolean isAppend) {
    		boolean isSuccess = true;
    		// 先过滤掉文件名
    		int index = filePath.lastIndexOf("/");
    		String dir = filePath.substring(0, index);
    		// 创建除文件的路径
    		File fileDir = new File(dir);
    		fileDir.mkdirs();
    		// 再创建路径下的文件
    		File file = null;
    		try {
    			file = new File(filePath);
    			file.createNewFile();
    		} catch (IOException e) {
    			isSuccess = false;
    			e.printStackTrace();
    		}
    		// 写入文件
    		FileWriter fileWriter = null;
    		try {
    			fileWriter = new FileWriter(file, isAppend);
    			fileWriter.write(content);
    			fileWriter.flush();
    		} catch (IOException e) {
    			isSuccess = false;
    			e.printStackTrace();
    		} finally {
    			try {
    				if (fileWriter != null)
    					fileWriter.close();
    			} catch (IOException e) {
    				e.printStackTrace();
    			}
    		}
    
    		return isSuccess;
    	}

  
我们把这两个函数封装到一个FileReaderWriter.java文件中以便后续使用。 

接着我们回到知乎爬虫中。 

我们需要给知乎的Zhihu封装类加个函数，用来格式化写入到本地时的排版。 
    
    
    public String writeString() {
            String result = "";
            result += "问题：" + question + "\r\n";
            result += "描述：" + questionDescription + "\r\n";
            result += "链接：" + zhihuUrl + "\r\n";
            for (int i = 0; i < answers.size(); i++) {
                result += "回答" + i + "：" + answers.get(i) + "\r\n";
            }
            result += "\r\n\r\n";
            return result;
    }

  
OK，这样就差不多了，接下来吧mian方法中的System.out.println改成    

    
    
    // 写入本地
    		for (Zhihu zhihu : myZhihu) {
    			FileReaderWriter.writeIntoFile(zhihu.writeString(),
    					"D:/知乎_编辑推荐.txt", true);
    		}

  
运行，便可以看到本来在控制台看到的内容已经被写到了本地的txt文件里： 

![](http://img.blog.csdn.net/20131231205728765?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  


大体一看没什么问题，仔细看看发现问题：存在太多的html标签，主要是<b>和<br>。 

我们可以在输出的时候对这些标记进行处理。 

先把<br>换成io流里面的\r\n，再把所有的html标签都删除，这样看起来便会清晰很多。 
    
    
    	public String writeString() {
    		// 拼接写入本地的字符串
    		String result = "";
    		result += "问题：" + question + "\r\n";
    		result += "描述：" + questionDescription + "\r\n";
    		result += "链接：" + zhihuUrl + "\r\n";
    		for (int i = 0; i < answers.size(); i++) {
    			result += "回答" + i + "：" + answers.get(i) + "\r\n\r\n";
    		}
    		result += "\r\n\r\n\r\n\r\n";
    		// 将其中的html标签进行筛选
    		result = result.replaceAll("<br>", "\r\n");
    		result = result.replaceAll("<.*?>", "");
    		return result;
    	}

  
  


这里的replaceAll函数可以使用正则，于是所有的<>标签在最后就都被删除了。 

改进之后的效果明显好了很多，可惜CSDN的图突然挂了。。 

  


目前的项目托管在了CSDN的CODE上面（类似于GitHub）： 

[ https://code.csdn.net/wxg694175346/zhihudown ](https://code.csdn.net/wxg694175346/zhihudown)   

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/17720641](http://blog.csdn.net/pleasecallmewhy/article/details/17720641)