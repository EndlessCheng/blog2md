#  Java的FTP上传下载 

[ Find ](http://www.findspace.name/author/find) |  2015年1月23日  |  [ Java ](http://www.findspace.name/category/easycoding/java) , [ 随意Coding ](http://www.findspace.name/category/easycoding) |  [ 没有评论  ](http://www.findspace.name/easycoding/1052#comments)

#  Java的FTP上传下载 

  * Java的FTP上传下载 
    * 介绍 
    * 代码说明 
    * 代码 

##  介绍 

利用 [ apache开源项目HttpClient ](http://hc.apache.org/httpclient-3.x/) 在java中进行ftp的上传下载，只用FTP的话，直接用从这个项目的包里面提取出的 [ common包 ](https://git.oschina.net/findspace/FetchUpdate/blob/master/libs/commons-net-3.3.jar) 就可以。 

##  代码说明 

connect(String path,String addr,int port,String username,String password ) 

传入参数就是正常ftp登陆时需要的参数，不解释。 

ftp的connect,login两个方法也很明确。 

这里说明一下reply（ftp登陆返回状态） 

简略的说，这种错误跟http协议类似，大致是： 

> 2开头－－成功 
> 
> 3开头－－权限问题 
> 
> 4开头－－文件问题 
> 
> 5开头－－服务器问题 

详细： 

返回值  |  说明   
---|---  
120  |  Service ready in NNN minutes.服务在NNN时间内可用   
125  |  Data connection already open; transfer starting.数据连接已经打开，开始传送数据.   
150  |  File status okay; about to open data connection.文件状态正确，正在打开数据连接.   
200  |  Command okay.命令执行正常结束.   
202  |  Command not implemented, superfluous at this site.命令未被执行，此站点不支持此命令.   
211  |  System status, or system help reply.系统状态或系统帮助信息回应.   
212  |  Directory status.目录状态信息.   
213  |  File status. $XrkxmL=文件状态信息.   
214  |  Help message.On how to use the server or the meaning of a particular non-standard command. This reply is useful only to the human user.帮助信息。关于如何使用本服务器或特殊的非标准命令。   
215  |  NAME system type. Where NAME is an official system name from the list in the Assigned Numbers document.NAME系统类型。   
220  |  Service ready for new user.新连接的用户的服务已就绪   
221  |  Service closing control connection.控制连接关闭   
225  |  Data connection open; no transfer in progress.数据连接已打开，没有进行中的数据传送   
150  |  File status okay; about to open data connection.文件状态正确，正在打开数据连接.   
227  |  Entering Passive Mode (h1,h2,h3,h4,p1,p2).进入被动模式   
230  |  User logged in, proceed. Logged out if appropriate.用户已登入。 如果不需要可以登出。   
250  |  Requested file action okay, completed.被请求文件操作成功完成 63   
257  |  “PATHNAME” created.路径已建立   
331  |  User name okay, need password.用户名存在，需要输入密码   
332  |  Need account for login.需要登陆的账户   
350  |  Requested file action pending further inFORMation U对被请求文件的操作需要进一步更多的信息   
421  |  Service not available, closing control connection.This may be a reply to any command if the service knows it must shut down.服务不可用，控制连接关闭。这可能是对任何命令的回应，如果服务认为它必须关闭   
425  |  Can’t open data connection.打开数据连接失败   
426  |  Connection closed; transfer aborted.连接关闭，传送中止。   
450  |  Requested file action not taken.对被请求文件的操作未被执行   
451  |  Requested action aborted. Local error in processing.请求的操作中止。处理中发生本地错误。   
452  |  Requested action not taken. Insufficient storage space in system.File unavailable (e.g., file busy).请求的操作没有被执行。系统存储空间不足。 文件不可用   
500  |  Syntax error, command unrecognized. This may include errors such as command line too long.语法错误，不可识别的命令。 这可能是命令行过长。   
501  |  Syntax error in parameters or arguments.参数错误导致的语法错误   
502  |  Command not implemented.命令未被执行   
503  |  Bad sequence of commands.命令的次序错误。   
504  |  Command not implemented for that parameter.由于参数错误，命令未被执行   
530  |  Not logged in.没有登录   
532  |  Need account for storing files.存储文件需要账户信息!   
550  |  Requested action not taken. File unavailable (e.g., file not found, no access).请求操作未被执行，文件不可用。   
551  |  Requested action aborted. Page type unknown.请求操作中止，页面类型未知   
552  |  Requested file action aborted. Exceeded storage allocation (for current directory or dataset).对请求文件的操作中止。 超出存储分配   
553  |  Requested action not taken. File name not allowed请求操作未被执行。 文件名不允许   
  
##  代码 
    
    
    package core;
    
    import java.io.File;
    import java.io.FileInputStream;
    import java.io.FileNotFoundException;
    import java.io.FileOutputStream;
    import java.io.IOException;
    import java.io.OutputStream;
    import java.net.SocketException;
    
    import org.apache.commons.net.ftp.FTPClient;
    import org.apache.commons.net.ftp.FTPFile;
    import org.apache.commons.net.ftp.FTPReply;
    
    public class FtpFileTransmit {
        private FTPClient ftp;
        /**  
         *   
         * @param path 上传到ftp服务器哪个路径下     
         * @param addr 地址  
         * @param port 端口号  
         * @param username 用户名  
         * @param password 密码  
         * @return  
         * @throws Exception  
         */    
        protected boolean connect(String path,String addr,int port,String username,String password ){
            boolean result=false;
            ftp=new FTPClient();
            int reply;
            try {
                ftp.connect(addr, port);
                ftp.login(username, password);
                reply = ftp.getReplyCode();    
                if (!FTPReply.isPositiveCompletion(reply)) {      
                    ftp.disconnect();      
                    return result;      
                }      
                ftp.changeWorkingDirectory(path);      
                result = true;      
                return result;     
            } catch (SocketException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return false;
        }
        /**  
         *   
         * @param file 上传的文件或文件夹  
         * @throws Exception  
         */    
        protected void upload(File file) {          
                FileInputStream input;
                try {
                    input = new FileInputStream(file);
                    ftp.storeFile(file.getName(), input);      
                    input.close();        
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }      
        }
        /**文件下载类
         * @param downloadPath 远程文件夹目录路径
         * @param fileName 要下载的文件名字
         * */
        protected void download(String downloadPath,String fileName){
            try {
                ftp.changeWorkingDirectory(downloadPath);
                FTPFile[] files=ftp.listFiles();
                for(FTPFile file:files){
                    if(file.getName().equals(fileName)){
                        System.out.println("Downloading "+fileName);
                        File localfile=new File(fileName);
                        OutputStream out=new FileOutputStream(localfile);
                        ftp.retrieveFile(fileName, out);
                        out.close();
                    }
                }
                
                
            } catch (IOException e) {
                System.out.println("Error in downloadfile from ftp");
    //          e.printStackTrace();
            }
        }
    }
    
    

Tags:  [ Eclipse ](http://www.findspace.name/tag/eclipse) , [ Java ](http://www.findspace.name/tag/java)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/easycoding/1052](http://www.findspace.name/easycoding/1052)