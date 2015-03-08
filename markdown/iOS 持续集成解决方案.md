[ Home ](http://blog.cee.moe) [ Subscribe ](http://blog.cee.moe/rss/)

#  iOS 持续集成解决方案

04 March 2015

  * Using OS X Server & Xcode Server & xcsbuildd 
  * Basic Steps: 

    1. 安裝 OS X Server，打開 Xcode 
    2. Settings 選項卡配置 Permission 
    3. 添加 SSH Key 到 Xcode Server 上： 
      * Login： ` sudo -u _xcsbuildd /bin/bash `
      * Generate SSH Key： ` ssh-keygen -t rsa -C "$your_email" `
      * Show your public key： ` cat /var/_xcsbuildd/.ssh/id_rsa.pub `
      * Put the key to github 
      * SSH your server to accept the fingerprint： ` ssh -T git@gitlab.domain.com `
    4. 配置 Workspace 

      * Build scheme：勾選 shared 
      * 添加 Server 到 Xcode 中（Preferences 裡面的 Accounts，匿名登錄） 
      * 添加 Bot，設置 SSH Key 
      * 集成日程安排：選擇一次提交更新一次 
      * Add Trigger： 
            
                        export LC_ALL="en_US.UTF-8" 
            # Put the git repo name instead of “reponame” variable
            cd reponame
            # Remove the following line if there is no submodules in the project
            git submodule update --init --recursive
            # If podfile is not in the root folder uncomment the following line
            # and replace with the real folder name
            # cd FolderName
            pod install
            

      * 報錯嘗試執行 ` pod setup `
  * References： 
    * [ http://papaanton.com/setting-up-xcode-6-and-apple-server-4-0-for-continues-integration-with-cocoapods/ ](http://papaanton.com/setting-up-xcode-6-and-apple-server-4-0-for-continues-integration-with-cocoapods/)
    * [ https://gist.github.com/mtitolo/f5283c54e300d88d9418 ](https://gist.github.com/mtitolo/f5283c54e300d88d9418)
    * [ http://stackoverflow.com/questions/26990057/cocoapods-commands-fail-due-to-no-such-file-or-directory-dir-initialize-us ](http://stackoverflow.com/questions/26990057/cocoapods-commands-fail-due-to-no-such-file-or-directory-dir-initialize-us)
    * [ http://blog.cocoapods.org/Repairing-Our-Broken-Specs-Repository/ ](http://blog.cocoapods.org/Repairing-Our-Broken-Specs-Repository/)
[ Cee's Picture  ](/author/cee/)

####  [ Cee ](/author/cee/)

Read [ more posts ](/author/cee/) by this author.

Please enable JavaScript to view the [ comments powered by Disqus.
](http://disqus.com/?ref_noscript) [ comments powered by  Disqus
](http://disqus.com)

####  Share this post

[ Twitter  ](https://twitter.com/share?text=iOS%20%E6%8C%81%E7%BB%AD%E9%9B%86%
E6%88%90%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88&url=http://blog.cee.moe/ios-
integration/) [ Facebook
](https://www.facebook.com/sharer/sharer.php?u=http://blog.cee.moe/ios-
integration/) [ Google+
](https://plus.google.com/share?url=http://blog.cee.moe/ios-integration/) [
Cee's Home ](http://blog.cee.moe) © 2015  Proudly published with [ Ghost
](https://ghost.org)

