##  [ Design Tutorial: Inverse the Problem ](http://www.cnblogs.com/chujian123/p/4008351.html)

[ Codeforces Round #270 ](http://codeforces.com/contest/472) D: [ http://codeforces.com/contest/472/problem/D ](http://codeforces.com/contest/472/problem/D)

题意：给以一张图，用邻接矩阵表示，现在问你这张图能不能够是一棵树？(并且边权都是正的) 

题解：看了题解才知道。如果这张图是一棵树的话，那么最小生成树一定满足条件。所以可以这样解，求一颗生成树，然后在生成树每个点DFS，求出任意两点之间的距离，看看这两点之间距离在原来的矩阵中，是否一致，如果都是一致的，则说明是可以的，否则就不行。 
    
    
      1 #include<iostream>
      2 #include<cstdio>
      3 #include<algorithm>
      4 #include<cstring>
      5 #include<vector>
      6 using namespace std;
      7 const int N=2003;
      8 struct Edge{
      9   int v;
     10   long long w;
     11 };
     12 vector<Edge>mp[N];
     13 long long a[N][N];
     14 int n,m;
     15 struct Node{
     16   int u,v;
     17   long long w;
     18   bool operator<(const Node a) const {
     19     return w<a.w;
     20   }
     21 }num[N*N/2];
     22 int fa[N];
     23 void init(){
     24    for(int i=1;i<=n;i++)
     25       fa[i]=i;
     26 }
     27 int Find(int x){
     28    int s;
     29    for(s=x;s!=fa[s];s=fa[s]);
     30    while(s!=x){
     31       int temp=fa[x];
     32       fa[x]=s;
     33       x=temp;
     34    }
     35   return s;
     36 }
     37 void solve(){
     38     int cnt=0;
     39     for(int i=1;i<=m;i++){
     40 
     41         int u=num[i].u;
     42         int v=num[i].v;
     43        // printf("***%d %d\n",u,v);
     44          int r1=Find(u);
     45          int r2=Find(v);
     46          if(r1==r2)continue;
     47           fa[r1]=r2;
     48          cnt++;
     49          Edge temp;
     50          temp.v=v;temp.w=num[i].w;
     51          mp[u].push_back(temp);
     52          temp.v=u;
     53          mp[v].push_back(temp);
     54          if(cnt==n-1)break;
     55     }
     56 }
     57 long long ds[N];
     58 bool visit[N];
     59 void DFS(int u,long long w){
     60     int tt=mp[u].size();
     61     for(int i=0;i<tt;i++){
     62         int v=mp[u][i].v;
     63         if(visit[v])continue;
     64         ds[v]=w+mp[u][i].w;
     65         visit[v]=1;
     66         DFS(v,ds[v]);
     67     }
     68 }
     69 
     70 bool AC(){
     71     for(int i=1;i<=n;i++){
     72         memset(ds,-1,sizeof(ds));
     73         memset(visit,0,sizeof(visit));
     74         visit[i]=1;
     75         DFS(i,0);
     76         ds[i]=0;
     77         for(int k=1;k<=n;k++){
     78             if(ds[k]!=a[i][k])return false;
     79         }
     80     }
     81    return true;
     82 }
     83 
     84 int main(){
     85    scanf("%d",&n);
     86    memset(a,0,sizeof(a));
     87    init();
     88    m=0;
     89    for(int i=1;i<=n;i++)
     90    for(int j=1;j<=n;j++)
     91      scanf("%I64d",&a[i][j]);
     92    bool flag=false;
     93    for(int i=1;i<=n;i++){
     94       for(int j=1;j<=n;j++){
     95           if(i==j&&a[i][j]!=0)flag=true;
     96           if(i!=j&&(a[i][j]==0||a[i][j]!=a[j][i]))flag=true;
     97           if(j>i){
     98            num[++m].u=i;num[m].v=j;num[m].w=a[i][j];
     99           }
    100       }
    101    }
    102 
    103    if(!flag){
    104       sort(num+1,num+m+1);
    105    //for(int i=1;i<=m;i++)
    106       //printf("%d %d %I64d\n",num[i].u,num[i].v,num[i].w);
    107       solve();
    108       if(!AC())flag=true;
    109    }
    110     if(flag)puts("NO\n");
    111     else
    112         puts("YES\n");
    113 
    114 }
#### 原文：[http://www.cnblogs.com/chujian123/p/4008351.html](http://www.cnblogs.com/chujian123/p/4008351.html)