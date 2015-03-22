title: Desert King

date: 2014-09-08 09:39

tags: []

description: 

---
poj2728: [ http://poj.org/problem?id=2728 ](http://poj.org/problem?id=2728)

题意：给你n的点，每一个点会有一个坐标(x,y),然后还有一个z值，现在上你求一棵生成树，是的这棵生成树的所有边的费用/所有边的距离最小，其中，边费用是指两点之z差值的绝对值，边距离是指两点之间的距离。 

题解：这一题就是求最小比率生成树。采用的解法就是0-1分数规划。 

其中设最后的比率是l 

1，z(l)是单调递减的。 

2,z(max(l))=0;这可以采用反证法进行证明。 

3，因为是完全图，所以要采用prime求最小生成树。 
    
    
     1 #include<iostream>
     2 #include<cstdio>
     3 #include<cstring>
     4 #include<algorithm>
     5 #include<cmath>
     6 using namespace std;
     7 const int N=1003;
     8 const double inf=10000000000.0;
     9 double mp[N][N],cost[N][N];
    10 double dist[N];
    11 double xx[N],yy[N],zz[N];
    12 int n;
    13 bool vis[N];
    14 bool solve(double x){
    15     for(int i=1;i<=n;i++){
    16         vis[i]=0;
    17         dist[i]=cost[i][1]-mp[i][1]*x;
    18     }
    19     vis[1]=1;
    20     dist[1]=0;
    21     double cost2=0;
    22     for(int i=1;i<n;i++){
    23         double minn=inf;
    24         int k=-1;
    25         for(int j=1;j<=n;j++){
    26             if(!vis[j]&&dist[j]<minn){
    27                 minn=dist[j];
    28                 k=j;
    29             }
    30         }
    31         if(k!=-1){
    32             cost2+=dist[k];
    33             vis[k]=1;
    34             for(int j=1;j<=n;j++){
    35                 if(!vis[j]){
    36                      double tt=cost[k][j]-mp[k][j]*x;
    37                      if(dist[j]>tt){
    38                         dist[j]=tt;
    39                      }
    40                 }
    41             }
    42         }
    43     }
    44   if(cost2>=0)return true;
    45   return false;
    46 
    47 }
    48 int main(){
    49     while(~scanf("%d",&n)&&n){
    50        for(int i=1;i<=n;i++){
    51          scanf("%lf%lf%lf",&xx[i],&yy[i],&zz[i]);
    52        }
    53        for(int i=1;i<=n;i++){
    54          for(int j=i+1;j<=n;j++){
    55             double temp=(xx[i]-xx[j])*(xx[i]-xx[j])+(yy[i]-yy[j])*(yy[i]-yy[j]);
    56             mp[i][j]=mp[j][i]=sqrt(temp);
    57             cost[i][j]=cost[j][i]=abs(zz[i]-zz[j]);
    58          }
    59        }
    60       double l=0,r=100,ans=0;
    61       while(abs(r-l)>1e-4){
    62         double mid=(r+l)/2;
    63         if(solve(mid)){
    64             l=mid;
    65             ans=mid;
    66         }
    67         else
    68             r=mid;
    69       }
    70      printf("%.3f\n",ans);
    71     }
    72 }
