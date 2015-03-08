[ 2014-02-23 ](/2014/02/23/kernel-hook-auto-build-dkms-modules/)

#  自动编译 DKMS 模组的内核 HOOK 

[ DKMS ](http://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support) 是个好东西，像我们这些喜欢自定义内核的家伙有了 DKMS 之后就不用为各种第三方的内核模组发愁了～ 

于是也没看是不是有人做过了(基本上是有人做了吧…) 于是参照 [ nvidia-hook ](https://aur.archlinux.org/packages/nvidia-hook/) 做了一个 [ autodkms ](https://aur.archlinux.org/packages/autodkms/) 。 

按照 [ ArchWiki ](https://wiki.archlinux.org/index.php/Dynamic_Kernel_Module_Support) ，自动编译所有模组的命令是： 
    
    
    dkms autoinstall -k NEW_KERNEL_VERSION  
  
---  
  
于是照葫芦画瓢写的 hook 文件 ` /usr/lib/initcpio/install/autodkms `
    
    
    build ()
    
    {
    
      echo "Building dkms modules for ${KERNELVERSION} kernel..."
    
      dkms autoinstall -k ${KERNELVERSION}
    
      echo "Build complete."
    
    }
    
    help ()
    
    {
    
    cat<<HELPEOF
    
        This hook rebuilds all dkms modules for new kernel.
    
    HELPEOF
    
    }  
  
---  
  
全部源码在 [ 这里 ](https://github.com/phoenixlzx/autodkms) <del> 其实一共就几行… </del>

打包好之后在 ` /etc/mkinitcpio.conf ` 的 ` HOOKS ` 最后加上 ` autodkms ` 就可以在更新内核的时候重新编译所有模组啦。 

=== 2014-03-10 更新 === 

在没有装对应内核的 headers 之前脚本执行会出错—— 
    
    
    Building dkms modules for 3.10.33-1-lts kernel...
    
    Error! echo
    
    Your kernel headers for kernel 3.10.33-1-lts cannot be found at
    
    /usr/lib/modules/3.10.33-1-lts/build or /usr/lib/modules/3.10.33-1-lts/source.
    
    Error! echo
    
    Your kernel headers for kernel 3.10.33-1-lts cannot be found at
    
    /usr/lib/modules/3.10.33-1-lts/build or /usr/lib/modules/3.10.33-1-lts/source.
    
    Build complete.  
  
---  
  
但是一般升级的时候都是先装内核再装 headers 所以脚本可以完善下： 
    
    
    build ()
    
    {
    
      if [ ! -d "/usr/lib/modules/${KERNELVERSION}/build" ]; then
    
        echo "You need to install or update ${KERNELVERSION} headers before build kernel image."
    
        exit 1
    
      fi
    
      echo "Building dkms modules for ${KERNELVERSION} kernel..."
    
      dkms autoinstall -k ${KERNELVERSION}
    
      echo "Build complete."
    
    }
    
    help ()
    
    {
    
    cat<<HELPEOF
    
        This hook rebuilds all dkms modules for new kernel.
    
    HELPEOF  
  
---  
  
[ Linux ](/categories/Linux/)

[ Linux ](/tags/Linux/) , [ Kernel ](/tags/Kernel/) , [ DKMS ](/tags/DKMS/)
#### 原文：[https://blog.phoenixlzx.com/2014/02/23/kernel-hook-auto-build-dkms-modules/](https://blog.phoenixlzx.com/2014/02/23/kernel-hook-auto-build-dkms-modules/)