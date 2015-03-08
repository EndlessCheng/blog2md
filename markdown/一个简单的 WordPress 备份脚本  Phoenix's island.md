[ 2014-02-11 ](/2014/02/11/a-simple-wordpress-backup-script/)

#  一个简单的 WordPress 备份脚本 

居然会有人问我要这个东西… 我最不会写脚本了好吧呀！ 

<del> 真心觉得这货 Google 一下粗来一大坨 </del>

嘛不多说了.. 既然写了就发粗来让大家吐槽一下好了… 不光是 WordPress.. 只要是静态文件+MySQL的站都可以用。 
    
    
    #!/bin/bash
    
    # settings
    
    mysqldbuser="wordpress"
    
    mysqldbpass="YourMySQLPassword"
    
    mysqldb="wordpress"
    
    webroot="/var/www/wordpress"
    
    backuproot="/root/backup/backups"
    
    temproot="/root/backup/temp/`date +%y-%m-%d`"
    
    temp="/root/backup/temp"
    
    logfile="/root/backup/backup.log"
    
    mkdir -p $backuproot $temproot/files
    
    # backup start
    
    echo "Backup start" >> $logfile
    
    echo $(date +"%y-%m-%d %H:%M:%S") >> $logfile 
    
    echo "------------" >> $logfile
    
    # database backup
    
    echo "Dumping MySQL database..." >> $logfile
    
    mysqldump --user=$mysqldbuser --password=$mysqldbpass --databases $mysqldb > $temproot/db.$(date +"%y-%m-%d").sql
    
    echo "Done exporting database." >> $logfile
    
    # copy wordpress files
    
    echo "Copying website files..." >> $logfile
    
    cp -r $webroot $temproot/files/
    
    echo "Done copying website files." >> $logfile
    
    # Compress backup files
    
    echo "Compressing backup files..." >> $logfile
    
    cd $temp
    
    tar zcf $backuproot/backup-$(date +"%y-%m-%d").tar.gz $(date +"%y-%m-%d") >> $logfile
    
    echo "Backup complete." >> $logfile
    
    # Cleanup
    
    echo "Cleaning up..." >> $logfile
    
    rm -rf $temp/* >> $logfile
    
    echo "------------" >> $logfile
    
    echo >> $logfile  
  
---  
  
真心的没有用到任何… 高级的东西。 

保存为文件 ` /root/backup.sh ` 然后修改下前面几个变量，以 root 用户新建 cronjob 

` crontab -e ` 然后敲 

` 00 01 * * 1 /root/backup.sh `

保存。这样每周一的凌晨1点(当然是你的服务器时间..) 就会自动备份到 ` /root/backup/backups ` 下。懒得写自动删除… 于是手动删好了。 

<del> 我要是被猫菊苣笑话了某人你可死定了 </del>

[ Practise ](/categories/Practise/)

[ WordPress ](/tags/WordPress/) , [ Script ](/tags/Script/) , [ Server ](/tags/Server/)
#### 原文：[https://blog.phoenixlzx.com/2014/02/11/a-simple-wordpress-backup-script/](https://blog.phoenixlzx.com/2014/02/11/a-simple-wordpress-backup-script/)