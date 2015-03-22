title: Colored Sticks

date: 2014-09-17 09:00

tags: []

description: 

---
poj2513: [ http://poj.org/problem?id=2513 ](http://poj.org/problem?id=2513)

题意：就是求一个欧拉回路。 

题解：本题是判断欧拉通路是否存在，但是如果是用map的话就会超时，这里采用了trie树，有发现trie树的一种用法。神奇 啊 
    
    
      1 #include<iostream>
      2 #include<cstdio>
      3 #include<cstring>
      4 #include<algorithm>
      5 #define maxn 1100000
      6 using namespace std;
      7 const int N=3e5+100;
      8 int head[N],cnt,num,vis[N],deg[N];
      9 struct Node{
     10   int v;
     11   int next;
     12 }edge[N*3];
     13 void init(){
     14   memset(head,-1,sizeof(head));
     15   cnt=num=0;
     16   memset(vis,0,sizeof(vis));
     17   memset(deg,0,sizeof(deg));
     18 }
     19 
     20 void add(int u,int v){
     21     edge[cnt].v=v;
     22     edge[cnt].next=head[u];
     23     head[u]=cnt++;
     24     edge[cnt].v=u;
     25     edge[cnt].next=head[v];
     26     head[v]=cnt++;
     27 }
     28 void DFS(int u){
     29     if(vis[u])return;
     30     vis[u]=1;
     31     for(int i=head[u];i!=-1;i=edge[i].next){
     32         DFS(edge[i].v);
     33     }
     34 }
     35 struct Nod {        //0为无效值
     36     int lnk[26], val;
     37     void init() {
     38         memset(lnk, 0, sizeof(lnk));
     39         val = 0;
     40     }
     41 };
     42 const char BASE = 'a';
     43 struct Trie {
     44     Nod buf[maxn];
     45     int len;
     46     void init() {
     47         buf[len=0].init();
     48     }
     49     int insert(char * str, int val) {
     50         int now = 0;
     51         for(int i = 0; str[i]; i ++) {
     52             int & nxt = buf[now].lnk[str[i]-BASE];
     53             if(!nxt)    buf[nxt=++len].init();
     54             now = nxt;
     55         }
     56         buf[now].val = val;
     57         return now;
     58     }
     59     int search(char * str) {
     60         int now = 0;
     61         for(int i = 0; str[i]; i ++) {
     62             int & nxt = buf[now].lnk[str[i]-BASE];
     63             if(!nxt)    return 0;
     64             now = nxt;
     65         }
     66         return buf[now].val;
     67     }
     68 } trie;
     69 char s1[100],s2[100];
     70 int main(){
     71    trie.init();
     72    init();
     73    while(~scanf("%s%s",&s1,&s2)){
     74       if(trie.search(s1)==0)trie.insert(s1,++num);
     75       if(trie.search(s2)==0)trie.insert(s2,++num);
     76       int c1=trie.search(s1),c2=trie.search(s2);
     77       add(c1,c2);
     78       deg[c1]++;
     79       deg[c2]++;
     80    }
     81    bool flag=true;
     82    int ct=0;
     83     DFS(1);
     84     for(int i=1;i<=num;i++){
     85         if(!vis[i]){
     86             flag=false;
     87             break;
     88         }
     89     }
     90     for(int i=1;i<=num;i++){
     91         if(deg[i]%2==1)
     92             ct++;
     93     }
     94     if(flag){
     95         if(ct==0||ct==2){
     96             printf("Possible\n");
     97         }
     98         else
     99             printf("Impossible\n");
    100     }
    101     else
    102             printf("Impossible\n");
    103 
    104 }
