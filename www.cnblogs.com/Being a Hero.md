title: Being a Hero

date: 2014-09-09 14:54

tags: []

description: 

---
zoj3241: [ http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=3241 ](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=3241)

题意：一个国家的地图是一张n个点m条边的有向图。你保卫了国家成为了英雄，现在国王答应给你一些城市。国王居住在首都，编号为1，但他不想随意的到达你的领地，所以你必须破坏一些路，使得从首都到你所拥有的所有城市不连通。而破坏这些路需要花钱。国王给了你f个城市供你选择，每个城市有一个价值。你最后的总收益=你选择的城市的价值之和-破坏路花费的钱。现在让你输出最大的收益，以及完成这样的收益应该破坏哪些路。 

首先对于表示这个国家地图的有向边(u,v,cost)，直接在图中建一条一样的边(u,v,cost)。对于供你选择的城市i，假设它的价值是value，创建一个汇点T，建一条(i,T,value)的边。然后以1为源点，T为汇点，求最小割即可。 
    
    
      1 #include<iostream>
      2 #include<cstring>
      3 #include<algorithm>
      4 #include<cstdio>
      5 #include<queue>
      6 using namespace std;
      7 const int N=1205;
      8 const int INF=(1<<29);
      9 const int M=300000;
     10 struct Node{
     11    int v;
     12    int f;
     13    int next;
     14 }edge[M];
     15 int n,m,u,v,w,cnt,sx,ex,top,f;
     16 int head[N],pre[N];
     17 int xx[M],yy[M],ans[M];
     18 bool vis[N];
     19 void init(){
     20     cnt=0;
     21     memset(head,-1,sizeof(head));
     22 }
     23 void add(int u,int v,int w){
     24     edge[cnt].v=v;
     25     edge[cnt].f=w;
     26     edge[cnt].next=head[u];
     27     head[u]=cnt++;
     28     edge[cnt].f=0;
     29     edge[cnt].v=u;
     30     edge[cnt].next=head[v];
     31     head[v]=cnt++;
     32 }
     33 bool BFS(){
     34   memset(pre,0,sizeof(pre));
     35   pre[sx]=1;
     36   queue<int>Q;
     37   Q.push(sx);
     38  while(!Q.empty()){
     39      int d=Q.front();
     40      Q.pop();
     41      for(int i=head[d];i!=-1;i=edge[i].next    ){
     42         if(edge[i].f&&!pre[edge[i].v]){
     43             pre[edge[i].v]=pre[d]+1;
     44             Q.push(edge[i].v);
     45         }
     46      }
     47   }
     48  return pre[ex]>0;
     49 }
     50 int dinic(int flow,int ps){
     51     int f=flow;
     52      if(ps==ex)return f;
     53      for(int i=head[ps];i!=-1;i=edge[i].next){
     54         if(edge[i].f&&pre[edge[i].v]==pre[ps]+1){
     55             int a=edge[i].f;
     56             int t=dinic(min(a,flow),edge[i].v);
     57               edge[i].f-=t;
     58               edge[i^1].f+=t;
     59              flow-=t;
     60              if(flow<=0)break;
     61         }
     62 
     63      }
     64       if(f-flow<=0)pre[ps]=-1;
     65       return f-flow;
     66 }
     67 int solve(){
     68     int sum=0;
     69     while(BFS())
     70         sum+=dinic(INF,sx);
     71     return sum;
     72 }
     73 void DFS(int u){
     74   for(int i=head[u];i!=-1;i=edge[i].next){
     75       int v=edge[i].v;
     76       if(!vis[v]&&edge[i].f>0){
     77         vis[v]=1;
     78         DFS(v);
     79       }
     80   }
     81 }
     82 int main() {
     83     int T,sum,tt=1;
     84     scanf("%d",&T);
     85     while(T--) {
     86          scanf("%d%d%d",&n,&m,&f);
     87          sum=0;
     88          init();
     89          for(int i=1;i<=m;i++){
     90             scanf("%d%d%d",&u,&v,&w);
     91             xx[i]=u,yy[i]=v;
     92             add(u,v,w);
     93          }
     94          for(int i=1;i<=f;i++){
     95              scanf("%d%d",&u,&w);
     96              add(u,n+1,w);
     97              sum+=w;
     98          }
     99          sx=1,ex=n+1;top=0;
    100          int as=sum-solve();
    101          memset(vis,0,sizeof(vis));
    102          vis[1]=1;
    103          printf("Case %d: %d\n",tt++,as);
    104          DFS(1);
    105          for(int i=1;i<=m;i++){
    106             if(vis[xx[i]]&&!vis[yy[i]]){
    107                 ans[++top]=i;
    108             }
    109          }
    110          printf("%d",top);
    111          for(int i=1;i<=top;i++)
    112             printf(" %d",ans[i]);
    113             puts("");
    114     }
    115     return 0;
    116 }
