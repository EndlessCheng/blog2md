##  [ Hard Life ](http://www.cnblogs.com/chujian123/p/3963284.html)

poj3155: [ http://poj.org/problem?id=3155 ](http://poj.org/problem?id=3155)

题意：最大密度子图的模板题。 

题解：直接看代码。 
    
    
      1 /*
      2 题意简述一个公司有n个人,给出了一些有冲突的人的对数(u,v),所有为了公司更好的发展，公司的
      3 总裁决定裁人，那么总裁现在裁要裁掉冲突率最高的哪些（冲突率=人数/在这些人中存在的冲突数
      4 分析;很明显的一个求最大密度子图的题目，求最大密度子图的方法有两种不同的模型可以求解，
      5 一种是采用了转换为最大权闭合图的模型来求解，而另一种则是通过补集转换的思想来求解，
      6 现在就最大权闭合图的模型来谈论以下：设max g = f(x)= |E‘|/|V’| ，找一个子图的边数与点数
      7 的比值达到其中的最大，我们通常都是构造一个函数max h（g）= |E'|-g*|V'|,当h(g)为0的时候，
      8 g的值即为最优（证明见Amber论文），h（g）>0 时 g<最优值， h(g)<0时，g>最优值；
      9 那么首先来解释为什么要是该函数的值尽量大？因为如果最大值大于0那么我们就可以继续增加
     10 g的值来减小h(g),若最大值都小于0了，那么g不可能增加只可能减少！
     11 注意观察h（g）,边和点有依赖关系，就边依赖点，边存在的必要条件是点的存在，那么这样以后，
     12 如果我们将边看成点，那么这不就符合最大权闭合子图了么，现在h（g）的求法就可以通过
     13 求新图的最大权闭合子图的值来求解，但是这里有个问题，建图之后你可以发现当求出来的值和
     14 h（g）原本应该为值不对应（具体为什么不怎么理解），可以这样理解，当最小的一个g使得
     15 h（g）为0的时候该解即为最优解，因为h(g)是以个单调递减函数，就该函数来看只可能存在一个
     16 g使得h（g）=0；然而通过求最大权闭合子图是子图权值和为0的有很多中g，当最小的一个g使得
     17 h（g）为0之后，如果g继续增大那么虽然通过最大权闭合子图的值求出来依旧为0，但是真正的
     18 h（g）< 0 了，所以要使得最优的一个解就是使得最大权闭合子图的权值和为0的最小的一个g值！
     19 这样求解之后从点点流到汇点为满流的边即为最大密度子图中的点
     20 注意精度的控制！
     21 
     22 ////////////
     23 第二种模型的建图： 源点到各个点连接一条有向边权值为U,各个点到汇点连接一条边权值为U+2*g-d，
     24 原来有关系的点连接两条有向边（u,v），（v,u）权值为1（U可以取m，U的目的是用来使得2*g-d的值
     25 始终为正），这样以后求最小割，那么h（g）= （U*n-mincut）/2;二分找到最优值即为mid ，
     26 但是如果要求图中的点则需要用left来从新图求最大流之后然后从源点开始dfs遍历，
     27 
     28 这里再补充一点编程时需要注意的地方：这个题目是利用分数规划进行二分求解的，但这个问题的
     29 分数规划和我之前的见过的很多分数规划是不同的，之前的分数规划表达式很多都是在给定区间
     30 内只有一个零点的单调函数。但这个题目不同，因为MiniCut=U*n-Maxmize{f(n)}，而MiniCut& lt;=U*n是
     31 恒成立的，所以Maxmize{f(n)}>=0恒成立，及Maxmize{f(n)}函数会先递减，然后一直为0，
     32 我们的目标是找出第一个零点。
     33 
     34 */
     35 #include<iostream>
     36 #include<cstring>
     37 #include<algorithm>
     38 #include<cstdio>
     39 #include<queue>
     40 #include<cmath>
     41 using namespace std;
     42 const int N=205;
     43 const double INF=1000000000.0;
     44 const int M=300000;
     45 struct Node{
     46    int v;
     47    double f;
     48    int next;
     49 }edge[M];
     50 int n,m,u,v,w,cnt,sx,ex,top;
     51 int head[N],pre[N],deg[N];
     52 int xx[M],yy[M],ans[M];
     53 bool vis[N];
     54 void init(){
     55     cnt=0;
     56     memset(head,-1,sizeof(head));
     57 }
     58 void add(int u,int v,double w){
     59     edge[cnt].v=v;
     60     edge[cnt].f=w;
     61     edge[cnt].next=head[u];
     62     head[u]=cnt++;
     63     edge[cnt].f=0;
     64     edge[cnt].v=u;
     65     edge[cnt].next=head[v];
     66     head[v]=cnt++;
     67 }
     68 bool BFS(){
     69   memset(pre,0,sizeof(pre));
     70   pre[sx]=1;
     71   queue<int>Q;
     72   Q.push(sx);
     73  while(!Q.empty()){
     74      int d=Q.front();
     75      Q.pop();
     76      for(int i=head[d];i!=-1;i=edge[i].next    ){
     77         if(edge[i].f&&!pre[edge[i].v]){
     78             pre[edge[i].v]=pre[d]+1;
     79             Q.push(edge[i].v);
     80         }
     81      }
     82   }
     83  return pre[ex]>0;
     84 }
     85 double dinic(double flow,int ps){
     86     double f=flow;
     87      if(ps==ex)return f;
     88      for(int i=head[ps];i!=-1;i=edge[i].next){
     89         if(edge[i].f&&pre[edge[i].v]==pre[ps]+1){
     90             double a=edge[i].f;
     91             double t=dinic(min(a,flow),edge[i].v);
     92               edge[i].f-=t;
     93               edge[i^1].f+=t;
     94              flow-=t;
     95              if(flow<=0)break;
     96         }
     97 
     98      }
     99       if(f-flow<=0)pre[ps]=-1;
    100       return f-flow;
    101 }
    102 double solve(){
    103     double sum=0;
    104     while(BFS())
    105         sum+=dinic(INF,sx);
    106     return sum;
    107 }
    108 double ok(double mid){
    109     init();
    110     sx=0,ex=n+1;
    111     for(int i=1;i<=n;i++){
    112         add(sx,i,m*1.0);
    113         add(i,ex,m*1.0+2*mid-1.0*deg[i]);
    114     }
    115     for(int i=1;i<=m;i++){
    116         add(xx[i],yy[i],1.0);
    117         add(yy[i],xx[i],1.0);
    118     }
    119     return solve();
    120 }
    121 
    122 void DFS(int u){
    123   for(int i=head[u];i!=-1;i=edge[i].next){
    124       int v=edge[i].v;
    125       if(!vis[v]&&edge[i].f>1e-5){
    126         vis[v]=1;
    127         DFS(v);
    128       }
    129   }
    130 }
    131 int main() {
    132     while(~scanf("%d%d",&n,&m)){
    133           memset(deg,0,sizeof(deg));
    134          for(int i=1;i<=m;i++){
    135             scanf("%d%d",&u,&v);
    136             xx[i]=u,yy[i]=v;
    137             deg[u]++;
    138             deg[v]++;
    139          }
    140          double bt=1.0/(n*1.0*n);//这是有定理得出的。
    141          double l=0,r=1000;
    142          while(abs(r-l)>=bt){
    143             double mid=(r+l)/2;
    144             double temp=(n*m*1.0-ok(mid))/2;
    145             if(temp>=1e-7){//注意这里的精度，精度小了，就会wa
    146                 l=mid;
    147             }
    148             else{
    149                 r=mid;
    150             }
    151          }
    152          if(m==0){//注意特判
    153             puts("1\n1");
    154             continue;
    155          }
    156          ok(l);
    157          memset(vis,0,sizeof(vis));
    158          vis[0]=1;
    159          DFS(0);
    160          top=0;
    161          for(int i=1;i<=n;i++){//要求是输出的点数，能够从源点访问的点都是结果集中的元素
    162             if(vis[i])
    163                 ans[++top]=i;
    164          }
    165          printf("%d\n",top);
    166          for(int i=1;i<=top;i++)
    167             printf("%d\n",ans[i]);
    168     }
    169     return 0;
    170 }
#### 原文：[http://www.cnblogs.com/chujian123/p/3963284.html](http://www.cnblogs.com/chujian123/p/3963284.html)