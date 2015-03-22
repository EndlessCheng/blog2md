title: Word Puzzles

date: 2014-09-10 22:17

tags: []

description: 

---
poj1204: [ http://poj.org/problem?id=1204 ](http://poj.org/problem?id=1204)

题意：给你n*m的字符串矩阵，然后p个查询，每个查询会给出一个字符串，然后问你在矩阵中能否通过8个方向搜索到这个字符串，输出地点以及搜索的方向。 

题解：这里的思想真的很好。离线，把要查询的字符串插入trie树中，然后在矩阵中暴力查询查询。 
    
    
     1 #include<iostream>
     2 #include<cstdio>
     3 #include<cstring>
     4 #include<algorithm>
     5 #define maxn 1100000
     6 using namespace std;
     7 const char BASE='A';
     8 char str[1002][1002];
     9 int len,n,m,p,stx,sty;
    10 int as1[1002],as2[1002],as3[1003];
    11 int dir[8][2]={{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1}};
    12 bool vis[maxn];
    13 int head[maxn]; // head[i]为第i个结点的左儿子编号
    14 int next[maxn]; // next[i]为第i个结点的右兄弟编号
    15 int id[maxn];
    16 char ch[maxn];  // ch[i]为第i个结点上的字符
    17 int sz; // 结点总数
    18 void init(){
    19     sz = 1;
    20     memset(head,0,sizeof(head));
    21     memset(next,0,sizeof(next));
    22  }
    23   void insert(const char *s,int to,int num) {
    24     int u = 1, v;
    25     for(int i =0; i <to; i++) {
    26       bool found = false;
    27       for(v = head[u]; v != 0; v = next[v])
    28         if(ch[v] == s[i]) { // 找到了
    29           found = true;
    30           break;
    31         }
    32       if(!found) {
    33          v = ++sz; // 新建结点
    34         ch[v] = s[i];
    35         next[v] = head[u];
    36         head[u] = v; // 插入到链表的首部
    37         head[v] = 0;
    38       }
    39       u = v;
    40     }
    41     id[sz]=num;
    42 }
    43 void DFS(int u,int x,int y,int num){
    44     if(!u||x<0||x>=n||y<0||y>=m)return;
    45     int v=0;
    46     for(v=head[u]; v!= 0; v = next[v])
    47       if(ch[v] == str[x][y]) { // 找到了
    48           break;
    49     }
    50     if(id[v]){
    51        int tt=id[v];
    52         as1[tt]=stx,as2[tt]=sty,as3[tt]=num;
    53         id[v]=0;
    54     }
    55     DFS(v,x+dir[num][0],y+dir[num][1],num);
    56 }
    57 char temp[1002];
    58 int main(){
    59     while(~scanf("%d%d%d",&n,&m,&p)){
    60         for(int i=0;i<n;i++){
    61             scanf("%s",str[i]);
    62         }
    63         init();
    64         memset(vis,0,sizeof(vis));
    65         memset(id,0,sizeof(id));
    66         for(int i=1;i<=p;i++){
    67             scanf("%s",temp);
    68             vis[temp[0]-BASE]=1;
    69             insert(temp,strlen(temp),i);
    70         }
    71         for(int i=0;i<n;i++){
    72             for(int j=0;j<m;j++){
    73                 if(vis[str[i][j]-BASE]){
    74                 for(int k=0;k<8;k++){
    75                    stx=i,sty=j;
    76                    DFS(1,i,j,k);
    77                 }
    78               }
    79             }
    80         }
    81         for(int i=1;i<=p;i++){
    82             printf("%d %d %c\n",as1[i],as2[i],as3[i]+'A');
    83         }
    84     }
    85 }
