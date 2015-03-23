title: 为 Linux 服务器编写的 BDRip 脚本

date: 2014-04-07 20:54:18

tags: [Multimedia, Anime, FFmpeg, ]

description: 

---
最近状态比较不好… 所以准备拿学校的服务器撒撒气_(:з」∠)_

吐槽：学校个大土豪，居然用双路 E5-2620 + 16G 内存的服务器，强烈怀疑这服务器上的站加起来不如这俩CPU贵… 另外机器上只有一块 300G 的硬盘 (SAS?) 是什么情况… 以及盗版的 RHEL5 是什么情况… 以及 /opt 分了 236G，rootfs 只有 19G 是要闹哪样…

于是进入正题。Linux 服务器一般都不安装图形界面，更加节省资源。同时现在也能以每月数十美元的价格租到足够性能和带宽的独立服务器，更何况把任务丢给服务器自动化操作，人的时间便可以节省下来做更重要的事情。

脚本需要如下软件包：

  * ffmpeg
  * mencoder
  * x264
  * mkvtoolnix

学校的服务器是 RHEL5 还没给激活，没办法换了 CentOS 的源，上面的一些软件包需要从 repoforge 获得。Ubuntu/Debian 的话，一般启用专有软件仓库就可以了。

下面贴脚本。
    
    
    #!/bin/bash
    
    # $1 = origin file
    
    # $2 = output file
    
    # $3 = quality
    
    # $4 = threads
    
    # The crf option controls encoding quality, and indirectly the final
    
    # filesize. The higher the value, the more compression and thus smaller
    
    # file size. Reduce the value and file size will go up. A value of 21
    
    # should produce a file of approximately 4GB in size for a typical movie.
    
    # Encode the video using x264, ignore the audio for now.
    
    mencoder $1.m2ts \
    
    -ovc x264 -x264encopts \
    
    crf=$3:frameref=3:bframes=3:direct_pred=auto:weight_b:partitions=all:8x8dct:me=umh:mixed_refs:trellis=1:nopsnr:nossim:subq=6:level_idc=41:threads=$4 \
    
    -nosound \
    
    -of rawvideo \
    
    -o $2.x264
    
    # Extract first sound track, normally stream 0:1 in BDs.
    
    ffmpeg -i $1.m2ts -map 0:1 -acodec flac $2.flac
    
    # Convert raw x264 video to MP4
    
    ffmpeg -i $2.x264 -vcodec copy $2.mp4
    
    # Finally, merge everything into a single MKV file
    
    mkvmerge -o $2.mkv $2.mp4 --track-name 0:Jpn $2.flac
    
    # Uncomment if you want to clean up your working environment.
    
    # rm $2.x264 $2.flac $2.mp4
    
    # Tell the user we're done.
    
    echo "Rip complete. Output file is $2.mkv"  
  
---  
  
保存为 `transcode.sh` 并赋予可执行权限：
    
    
    $ chmod +x transcode.sh  
  
---  
  
脚本基本上是从下面的参考链接里抄来的，但是做了一些更改以适合我目前的需求。脚本接受 4 个参数，分别为输入文件(不含扩展名)、输出文件(不含扩展名)、质量、线程数。我在服务器上 Rip 的文件是 zyo 买的「未確認で進行形」第一卷OVA，命令如下：
    
    
    $ ./transcode.sh 00004 4 18 20  
  
---  
  
`transcode.sh` 是当前目录下的脚本文件，`00004` 代表当前目录下的 `00004.m2ts` 片源，输出文件将是 `4.mkv`，压缩质量为 `18`，编码过程使用 20 个线程(服务器一共 12 个核心 24 个线程么我就不客气啦。

OVA压缩大约使用了不到 20 分钟的时间，最终文件大小不到 500M。看起来效果还可以嗯…

参考：

  * [FFmpeg - Extract Blu-Ray Audio - Gentoo Wiki](http://wiki.gentoo.org/wiki/FFmpeg_-_Extract_Blu-Ray_Audio)
  * [HowTo: Encode a Blu-ray rip into a smaller format without losing quality](http://www.rcomputer.eu/21-zoznam/operacne-systemy/linux/157-howto-encode-a-blu-ray-rip-into-a-smaller-format-without-losing-quality)
