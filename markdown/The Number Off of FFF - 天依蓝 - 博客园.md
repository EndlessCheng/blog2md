##  [ The Number Off of FFF ](http://www.cnblogs.com/chujian123/p/4006191.html)

hdu4727: [ http://acm.hdu.edu.cn/showproblem.php?pid=4727 ](http://acm.hdu.edu.cn/showproblem.php?pid=4727)

题意：给你一个序列，每个数比前面一个数大一。如果不是大一，则输出这个位子，如果都是大一，则输出1. 

题解：水题。 
    
    
     1 #include<iostream>
     2 #include<cstdio>
     3 #include<algorithm>
     4 #include<cstring>
     5 using namespace std;
     6 int n,temp,x,a[100003];
     7 int main(){
     8    int T,tt=1;
     9    scanf("%d",&T);
    10    while(T--){
    11         scanf("%d",&n);
    12         for(int i=1;i<=n;i++)
    13           scanf("%d",&a[i]);
    14           int i;
    15         for( i=1;i<n;i++){
    16             if(a[i+1]-a[i]!=1)
    17                 break;
    18         }
    19         if(i==n)printf("Case #%d: 1\n",tt++);
    20         else
    21             printf("Case #%d: %d\n",tt++,i+1);
    22    }
    23 }
#### 原文：[http://www.cnblogs.com/chujian123/p/4006191.html](http://www.cnblogs.com/chujian123/p/4006191.html)