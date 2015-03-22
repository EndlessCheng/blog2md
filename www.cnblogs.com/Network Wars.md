title: Network Wars

date: 2014-09-08 14:33

tags: []

description: 

---
zoj2676: [ http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemId=1676 ](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemId=1676)

题意：给出一个带权无向图 ，每条边e有一个权 。求将点 和点t分开的一个边割集 ，使得该割集的平均边权最小，即最小化： 

题解：转化成求0-1分数规划，然后求最小割，注意e‘<0是直接加入割边的，对剩余边求最小割即可。 
    
    
      1 #include<iostream>
      2 #include<cstring>
      3 #include<algorithm>
      4 #include<cstdio>
      5 #include<queue>
      6 #include<cmath>
      7 #define INF 100000000
      8 using namespace std;
      9 const int N=1205;
     10 const int M=1000000;
     11 struct Node{
     12    int v;
     13    double f;
     14    int next;
     15 }edge[M];
     16 int n,m,u,v,cnt,sx,ex;
     17 int head[N],pre[N];
     18 int xx[N],yy[N];
     19 double cc[N];
     20 void init(){
     21     cnt=0;
     22     memset(head,-1,sizeof(head));
     23 }
     24 void add(int u,int v,double w){
     25     edge[cnt].v=v;
     26     edge[cnt].f=w;
     27     edge[cnt].next=head[u];
     28     head[u]=cnt++;
     29     edge[cnt].f=0;
     30     edge[cnt].v=u;
     31     edge[cnt].next=head[v];
     32     head[v]=cnt++;
     33 }
     34 bool BFS(){
     35   memset(pre,0,sizeof(pre));
     36   pre[sx]=1;
     37   queue<int>Q;
     38   Q.push(sx);
     39  while(!Q.empty()){
     40      int d=Q.front();
     41      Q.pop();
     42      for(int i=head[d];i!=-1;i=edge[i].next    ){
     43         if(edge[i].f&&!pre[edge[i].v]){
     44             pre[edge[i].v]=pre[d]+1;
     45             Q.push(edge[i].v);
     46         }
     47      }
     48   }
     49  return pre[ex]>0;
     50 }
     51 double dinic(double flow,int ps){
     52     double f=flow;
     53      if(ps==ex)return f;
     54      for(int i=head[ps];i!=-1;i=edge[i].next){
     55         if(edge[i].f&&pre[edge[i].v]==pre[ps]+1){
     56             double a=edge[i].f;
     57             double t=dinic(min(a,flow),edge[i].v);
     58               edge[i].f-=t;
     59               edge[i^1].f+=t;
     60             flow-=t;
     61              if(flow<=0)break;
     62         }
     63 
     64      }
     65       if(f-flow<=0)pre[ps]=-1;
     66       return f-flow;
     67 }
     68 double solve(){
     69     double sum=0;
     70     while(BFS())
     71         sum+=dinic(INF,sx);
     72     return sum;
     73 }
     74 bool ok(double mid){
     75     init();
     76     double flow=0;
     77     for(int i=1;i<=m;i++){
     78         if(cc[i]>mid){
     79             add(xx[i],yy[i],cc[i]-mid);
     80             add(yy[i],xx[i],cc[i]-mid);
     81         }
     82         else{
     83             flow+=cc[i]-mid;
     84         }
     85     }
     86     flow+=solve();
     87     if(flow>=0)return true;
     88     return false;
     89 }
     90 bool vis[N];
     91 void DFS(int u){
     92       for(int i=head[u];i!=-1;i=edge[i].next){
     93          int v=edge[i].v;
     94          if(!vis[v]&&edge[i].f>1e-5){
     95              vis[v]=1;
     96              DFS(v);
     97          }
     98       }
     99 }
    100 int ans[N],top;
    101 int main() {
    102     int tt=1;
    103     while(cin>>n>>m){
    104         sx=1;
    105         ex=n;
    106         if(tt>1)puts("");
    107         tt=2;
    108         for(int i=1;i<=m;i++){
    109             cin>>xx[i]>>yy[i]>>cc[i];
    110         }
    111         double l=0,r=1000000;
    112       while(abs(l-r)>1e-5){
    113           double mid=(l+r)/2;
    114           if(ok(mid)){
    115             l=mid;
    116           }
    117           else{
    118             r=mid;
    119           }
    120       }
    121         ok(r);
    122        memset(vis,0,sizeof(vis));
    123        vis[1]=1;
    124        DFS(1);
    125        top=0;
    126        for(int i=1;i<=m;i++){
    127           if(vis[xx[i]]+vis[yy[i]]==1||cc[i]<=r){
    128              ans[++top]=i;
    129           }
    130        }
    131        printf("%d\n",top);
    132        sort(ans+1,ans+top+1);
    133        for(int i=1;i<top;i++)
    134         printf("%d ",ans[i]);
    135        printf("%d\n",ans[top]);
    136 
    137     }
    138     return 0;
    139 }
