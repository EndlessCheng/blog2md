title: Android 上传文件到服务器：理论与编码

date: 2015-02-01T20:10:00.000Z

tags: [Android, Django, ]

description: 手机端用户注册完成后，会需要你上传一个头像到服务器，本文就是来解决这一问题的。（内附 GitHub 源码地址）

---
本文源码地址：<https://github.com/EndlessCheng/AndroidUploadImages>

# 需求

手机端用户注册完成后，会需要你上传一个本地头像到服务器，本文就是来解决这一问题的。

我们的目标是完成这样一个方法：

`public int postFileToURL(File file, String mimeType, URL url, String fieldName);`

其中 `mimeType` 是文件的互联网媒体类型（见下面图片中的 `Content-Type: image/jpeg`），`fieldName` 是 `<input>` 标签中的 `name` 值。

返回的有上传成功（0）、上传失败（-1）和文件不存在（-2）。

# 理论

由于标准的 Android API 没有提供一个明显直接的向服务器上传文件的方法，所以还需手动设置一些 HTTP header 字段。我们先来学习下相关知识。

首先在服务器端做个实验：
    
    
    <form method="post" enctype="multipart/form-data">
    
        <p>选择一个文件</p>
    
        <p><input name="docfile" type="file"/></p>
    
        <p><input type="submit" value="上传"/></p>
    
    </form>  
  
---  
  
打开开发者工具，切换至「网络」，然后点击上传按钮，查看 POST 信息：

![](http://endless.qiniudn.com/blogupload-file.png)

注意三个地方：

  1. 由于上传文件可能会比较大，网速可能会比较慢，故采用 `Connection: keep-alive`，使客户端到服务器端的连接持续有效，避免重新建立连接。

  2. `Content-Type: multipart/form-data; boundary=--balabala` 是上传文件必须的属性

  3. multipart/form-data 的请求体也是一个字符串，不过和 post 的请求体不同的是它的构造方式，post 是简单的 name=value 值连接，multipart/form-data 则是添加了分隔符等内容的构造体。具体格式如下：
    
    
    --${bound}
    
    Content-Disposition: form-data; name="field-name"; filename="img.jpg"
    
    Content-Type: image/jpeg
    
    file content
    
    --${bound}
    
    Content-Disposition: form-data; name="field-name2"; filename="img2.jpg"
    
    Content-Type: image/jpeg
    
    file content
    
    --${bound}--  
  
---  
  
注意最后的两个连字符号。

参考：

  1. [List of HTTP header fields](http://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Request_fields)
  2. [HTTP协议头部与Keep-Alive模式详解](https://www.byvoid.com/blog/http-keep-alive-header) <\- byvoid 博客的好文之一
  3. [HTTP协议之multipart/form-data请求分析](http://blog.csdn.net/five3/article/details/7181521)
  4. [RFC 1341 7.2.1 节](http://www.w3.org/Protocols/rfc1341/7_2_Multipart.html#sec7.2.1) 中有这样一段话：「The boundary must be followed immediately either by another CRLF and the header fields for the next part, or by two CRLFs, in which case there are no header fields for the next part (and it is therefore assumed to be of Content-Type text/plain).」即再加一个换行的目的是界定请求头的末尾。

# 编码

## 选择文件

首先图片不能过大，限制在 1 Mb 内最好，这个在选择图片的时候就应该处理一下。

onClick()
    
    
    Intent intent = new Intent();
    
    intent.setType("image/*");
    
    intent.setAction(Intent.ACTION_GET_CONTENT); // 返回文件 Uri
    
    startActivityForResult(intent, RESULT_CANCELED);  
  
---  
      
    
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    
    	if (resultCode == Activity.RESULT_OK) {
    
    		Uri uri = data.getData();
    
    		String path = convertUriToPath(uri);
    
    		if (!isImageFileExtension(MimeTypeMap.getFileExtensionFromUrl(path))) {
    
    			alert("不是有效的图片文件！");
    
    			return;
    
    		}
    
    		try {
    
    			Bitmap bitmap = BitmapFactory.decodeStream(this
    
    					.getContentResolver().openInputStream(uri));
    
    			if (bitmap.getByteCount() > MAX_FILE_SIZE) { // 1024 * 1024
    
    				alert("图片文件过大！");
    
    				return;
    
    			}
    
    			mImageView.setImageBitmap(bitmap);
    
    			mPicturePath = path;
    
    		} catch (FileNotFoundException e) {
    
    			e.printStackTrace();
    
    		}
    
    	}
    
    }  
  
---  
  
`onActivityResult()` 内的几个方法见源码，此不累述。

## 上传文件

onClick()
    
    
    if (mPicturePath == null) {
    
    	alert("请选择文件！");
    
    	return;
    
    }
    
    String mimeType = MimeTypeMap.getSingleton().getMimeTypeFromExtension(
    
    				MimeTypeMap.getFileExtensionFromUrl(mPicturePath));
    
    new UploadFileTask(this).execute(mPicturePath, mimeType, REQUEST_URL, FIELD_NAME);  
  
---  
  
我们的目标方法来了：
    
    
    public static int postFileToURL(File file, String mimeType, URL url, String fieldName) {
    
    	if (file == null) // 再判断一次，因为可能在选择图片之后，该图片在上传之前被删除
    
    		return FILE_NOT_EXIST; // -2
    
    	try {
    
    		String boundary = UUID.randomUUID().toString();
    
    		HttpURLConnection conn = (HttpURLConnection) url.openConnection();
    
    		
    
    		setHttpURLConnection(conn, boundary);
    
    		writeData(conn, boundary, file, mimeType, fieldName);
    
    		int res = conn.getResponseCode();
    
    		if (res == 200)
    
    			return SUCCESS; // 0
    
    	} catch (IOException e) {
    
    		e.printStackTrace();
    
    	}
    
    	return FAILURE; // -1
    
    }
    
    private static void setHttpURLConnection(HttpURLConnection conn,
    
    		String boundary) {
    
    	conn.setConnectTimeout(TIME_OUT); // 30 * 1000 ms
    
    	conn.setReadTimeout(TIME_OUT);
    
    	conn.setDoInput(true); // 允许输入流
    
    	conn.setDoOutput(true); // 允许输出流
    
    	try {
    
    		conn.setRequestMethod("POST");
    
    	} catch (ProtocolException e) {
    
    		e.printStackTrace();
    
    	}
    
    	conn.setRequestProperty("Connection", "keep-alive");
    
    	conn.setRequestProperty("Content-Type", CONTENT_TYPE + "; boundary="
    
    			+ boundary);
    
    }
    
    private static void writeData(HttpURLConnection conn, String boundary,
    
    		File file, String mimeType, String fieldName) throws IOException {
    
    	DataOutputStream requestData = new DataOutputStream(
    
    			conn.getOutputStream());
    
    	requestData.writeBytes("--" + boundary + CRLF); // CRLF = "\r\n"
    
    	requestData.writeBytes("Content-Disposition: form-data; name=\""
    
    			+ fieldName + "\"; filename=\"" + file.getName() + "\"" + CRLF);
    
    	requestData.writeBytes("Content-Type: " + mimeType + CRLF + CRLF); // 两个回车换行
    
    	InputStream fileInput = new FileInputStream(file);
    
    	int bytesRead;
    
    	byte[] buffer = new byte[1024];
    
    	while ((bytesRead = fileInput.read(buffer)) != -1) {
    
    		requestData.write(buffer, 0, bytesRead);
    
    	}
    
    	fileInput.close();
    
    	requestData.writeBytes(CRLF);
    
    	requestData.writeBytes("--" + boundary + "--" + CRLF);
    
    	requestData.flush();
    
    }  
  
---  
  
# Django 上的处理

为了方便手机端的上传，还需要在 `view.py` 的函数定义前加上 `@csrf_exempt`：

view.py
    
    
    from django.views.decorators.csrf import csrf_exempt
    
    ...
    
    @csrf_exempt
    
    def upload_file(request):
    
    	...  
  
---
