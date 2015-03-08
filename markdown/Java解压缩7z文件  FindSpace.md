#  Java解压缩7z文件 

[ Find ](http://www.findspace.name/author/find) |  2015年1月28日  |  [ Java ](http://www.findspace.name/category/easycoding/java) , [ 随意Coding ](http://www.findspace.name/category/easycoding) |  [ 没有评论  ](http://www.findspace.name/easycoding/1057#comments)

  * Java解压缩7z文件 
    * 介绍 
    * 代码示例 

##  介绍 

利用7-zip的开源项目7-zip-JBinding来解压缩多种压缩文件，而不是调用外部命令（比如win下调用winrar）。 

java自带的解压模块可解压缩的压缩类型有限。 

[ 项目地址（sourceforge） ](http://sourceforge.net/projects/sevenzipjbind/)

##  代码示例 
    
    
    package core;
    
    import java.io.File;
    import java.io.FileNotFoundException;
    import java.io.FileOutputStream;
    import java.io.IOException;
    import java.io.RandomAccessFile;
    import java.util.Arrays;
    
    import net.sf.sevenzipjbinding.ExtractOperationResult;
    import net.sf.sevenzipjbinding.ISequentialOutStream;
    import net.sf.sevenzipjbinding.ISevenZipInArchive;
    import net.sf.sevenzipjbinding.SevenZip;
    import net.sf.sevenzipjbinding.SevenZipException;
    import net.sf.sevenzipjbinding.impl.RandomAccessFileInStream;
    import net.sf.sevenzipjbinding.simple.ISimpleInArchive;
    import net.sf.sevenzipjbinding.simple.ISimpleInArchiveItem;
    /**利用7zbinding*/
    public class UnZip {
    
    
        void extractile(String filepath){
             RandomAccessFile randomAccessFile = null;
                ISevenZipInArchive inArchive = null;
    
                try {
                    randomAccessFile = new RandomAccessFile(filepath, "r");
                    inArchive = SevenZip.openInArchive(null, // autodetect archive type
                            new RandomAccessFileInStream(randomAccessFile));
    
                    // Getting simple interface of the archive inArchive
                    ISimpleInArchive simpleInArchive = inArchive.getSimpleInterface();
    
                    System.out.println("   Hash   |    Size    | Filename");
                    System.out.println("----------+------------+---------");
    
                    for (final ISimpleInArchiveItem item : simpleInArchive.getArchiveItems()) {
                        final int[] hash = new int[] { 0 };
                        if (!item.isFolder()) {
                            ExtractOperationResult result;
    
                            final long[] sizeArray = new long[1];
                            result = item.extractSlow(new ISequentialOutStream() {
                                public int write(byte[] data) throws SevenZipException {
    
                                    //Write to file
                                    FileOutputStream fos;
                                    try {
                                        File file = new File(item.getPath());
                                        //error occours below
    //                                  file.getParentFile().mkdirs();
                                        fos = new FileOutputStream(file);
                                        fos.write(data);
                                        fos.close();
    
                                    } catch (FileNotFoundException e) {
                                        // TODO Auto-generated catch block
                                        e.printStackTrace();
                                    } catch (IOException e) {
                                        // TODO Auto-generated catch block
                                        e.printStackTrace();
                                    }
    
                                    hash[0] ^= Arrays.hashCode(data); // Consume data
                                    sizeArray[0] += data.length;
                                    return data.length; // Return amount of consumed data
                                }
                            });
                            if (result == ExtractOperationResult.OK) {
                                System.out.println(String.format("%9X | %10s | %s", // 
                                        hash[0], sizeArray[0], item.getPath()));
                            } else {
                                System.err.println("Error extracting item: " + result);
                            }
                        }
                    }
                } catch (Exception e) {
                    System.err.println("Error occurs: " + e);
                    e.printStackTrace();
                    System.exit(1);
                } finally {
                    if (inArchive != null) {
                        try {
                            inArchive.close();
                        } catch (SevenZipException e) {
                            System.err.println("Error closing archive: " + e);
                        }
                    }
                    if (randomAccessFile != null) {
                        try {
                            randomAccessFile.close();
                        } catch (IOException e) {
                            System.err.println("Error closing file: " + e);
                        }
                    }
                }
        }
    }

调用的时候： 
    
    
    unzip=new UnZip();
    unzip.extractile("a.7z");

会自动解压缩压缩包里的文件到当前目录下，当然可以更改设置，到特定的目录。代码简单明确。有问题可以到上面的sourceforge项目地址下的discuss搜索。 

Tags:  [ Java ](http://www.findspace.name/tag/java)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/easycoding/1057](http://www.findspace.name/easycoding/1057)