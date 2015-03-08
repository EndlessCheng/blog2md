##  [ No Pain No Game ](http://www.cnblogs.com/chujian123/p/4004793.html)

hdu4630: [ http://acm.hdu.edu.cn/showproblem.php?pid=4630 ](http://acm.hdu.edu.cn/showproblem.php?pid=4630)

题意：给定一个排序，求区间最大GCD。 

题解：离散树状数组。首先把查询按左端点从大到小排序。然后用树状数组来维护每个位置出现的最大的公约数。枚举每个数的约数，记录到当前位置为止，上一个x的倍数出现的位置b[x]; 
    
    
     1 #include<iostream>
     2 #include<algorithm>
     3 #include<cstdio>
     4 #include<cstring>
     5 #include<vector>
     6 using namespace std;
     7 const int N=5e4+19;
     8 int a[N],c[N],b[N],ans[N];
     9 int n,m;
    10 int lowbit(int x){
    11    return x&(-x);
    12 }
    13 void add(int x,int val){
    14     while(x<=n){
    15         c[x]=max(c[x],val);
    16         x+=lowbit(x);
    17     }
    18 }
    19 int getsum(int x){
    20    int sum=0;
    21    while(x>0){
    22      sum=max(sum,c[x]);
    23      x-=lowbit(x);
    24    }
    25    return sum;
    26 }
    27 struct Node{
    28   int l,r;
    29   int id;
    30   bool operator<(const Node a)const{
    31     return l>a.l;
    32   }
    33 }num[N];
    34 int main(){
    35     int T;
    36     scanf("%d",&T);
    37     while(T--){
    38         scanf("%d",&n);
    39         memset(a,0,sizeof(a));
    40         memset(c,0,sizeof(c));
    41         memset(b,0,sizeof(b));
    42         for(int i=1;i<=n;i++)
    43           scanf("%d",&a[i]);
    44           scanf("%d",&m);
    45           for(int i=1;i<=m;i++){
    46             scanf("%d%d",&num[i].l,&num[i].r);
    47             num[i].id=i;
    48           }
    49         sort(num+1,num+m+1);
    50         int j=n;
    51         for(int i=1;i<=m;i++){
    52             for(;j>=num[i].l;j--){
    53                for(int k=1;k*k<=a[j];k++){
    54                    if(a[j]%k==0){
    55                        if(b[k]){
    56                         add(b[k],k);
    57                        }
    58                         b[k]=j;
    59                       if(k*k!=a[j]){
    60                          if(b[a[j]/k]){
    61                             add(b[a[j]/k],a[j]/k);
    62                          }
    63                          b[a[j]/k]=j;
    64                       }
    65                    }
    66                }
    67              }
    68            ans[num[i].id]=getsum(num[i].r);
    69          }
    70      for(int i=1;i<=m;i++)
    71         printf("%d\n",ans[i]);
    72     }
    73 }
#### 原文：[http://www.cnblogs.com/chujian123/p/4004793.html](http://www.cnblogs.com/chujian123/p/4004793.html)