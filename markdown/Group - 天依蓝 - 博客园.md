##  [ Group ](http://www.cnblogs.com/chujian123/p/4004164.html)

hdu4638: [ http://acm.hdu.edu.cn/showproblem.php?pid=4638 ](http://acm.hdu.edu.cn/showproblem.php?pid=4638)

题意：找到区间能，有多少组连续数字串 

题解：离线处理，从开始到1--n开始扫描，用树状数组记录每个位置构成组的情况。对于i位置上的数，一定会构成一个组，所以add(i,1),如果a[i]-1和a[i]+1在之前就已经出现，那么就可以删除了合并。add(pos[a[i]-1],-1),add(pos[a[i]+1],-1),如果有以i为右端点的查询，则该查询就是ans[id]=getsum(r)-getsum(l-1); 
    
    
     1 #include<iostream>
     2 #include<algorithm>
     3 #include<cstdio>
     4 #include<cstring>
     5 #include<vector>
     6 using namespace std;
     7 const int N=1e5+19;
     8 int c[N],a[N],ll[N],rr[N],ans[N],pos[N];
     9 bool flag[N];
    10 int n,m;
    11 vector<int>mp[N];
    12 int lowbit(int x){
    13   return x&(-x);
    14 }
    15 
    16 void add(int x,int val){
    17     while(x<=n){
    18         c[x]+=val;
    19         x+=lowbit(x);
    20     }
    21 }
    22 int getsum(int x){
    23     int sum=0;
    24     while(x>0){
    25         sum+=c[x];
    26         x-=lowbit(x);
    27     }
    28    return sum;
    29 }
    30 int main(){
    31    int T;
    32    scanf("%d",&T);
    33    while(T--){
    34        scanf("%d%d",&n,&m);
    35        for(int i=1;i<=n;i++){
    36         scanf("%d",&a[i]);
    37          pos[a[i]]=i;
    38        }
    39 
    40        memset(c,0,sizeof(c));
    41        memset(flag,0,sizeof(flag));
    42         for(int i=1;i<=n;i++)
    43            mp[i].clear();
    44         for(int i=1;i<=m;i++){
    45             scanf("%d%d",&ll[i],&rr[i]);
    46             mp[rr[i]].push_back(i);
    47         }
    48         for(int i=1;i<=n;i++){
    49             int pre=a[i]-1;
    50             int next=a[i]+1;
    51             if(pre>=1&&flag[pre]){
    52                 add(pos[pre],-1);
    53             }
    54             if(next<=n&&flag[next]){
    55                 add(pos[next],-1);
    56             }
    57              add(i,1);
    58             flag[a[i]]=1;
    59             int tt=mp[i].size();
    60            for(int j=0;j<tt;j++){
    61               int v=mp[i][j];
    62               ans[v]=getsum(i)-getsum(ll[v]-1);
    63            }
    64         }
    65          for(int i=1;i<=m;i++)
    66            printf("%d\n",ans[i]);
    67    }
    68 
    69 }
#### 原文：[http://www.cnblogs.com/chujian123/p/4004164.html](http://www.cnblogs.com/chujian123/p/4004164.html)