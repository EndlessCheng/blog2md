title: Keywords Search

date: 2014-09-12 17:45

tags: []

description: 

---
hdu2222: [ http://acm.hdu.edu.cn/showproblem.php?pid=2222 ](http://acm.hdu.edu.cn/showproblem.php?pid=2222)

题意：AC自动机模板。 

题解：一下是别人的模板。 
    
    
     1 #include<iostream>
     2 #include<cstdio>
     3 #include<cstring>
     4 #include<cstdlib>
     5 #include<queue>
     6 #define cha 26
     7 #define Root 0
     8 #define N 500001
     9 using namespace std;
    10 struct node{
    11     int data;//结点信息
    12     int count;//从根到此处是否是关键字,并且记录是多少个关键字的结尾
    13     int fail;
    14     int next[cha];
    15 }tree[N];
    16 
    17 void init(node &a,int data){
    18     a.data = data;
    19     a.count = 0;
    20     a.fail = Root;
    21     for(int i=0;i<cha;i++)
    22         a.next[i] = -1;
    23 }
    24 
    25 int k = 1;
    26 void Insert(char s[]){
    27     int p = Root;
    28     for(int i=0;s[i];i++){
    29         int data = s[i]-'a';
    30         if(tree[p].next[data]==-1){//不存在该结点
    31             init(tree[k],data);
    32             tree[p].next[data] = k;
    33             k++;
    34         }
    35         p = tree[p].next[data];
    36     }
    37     tree[p].count++;
    38 }
    39 
    40 queue<node> q;
    41 void AC_automation(){
    42     q.push(tree[Root]);
    43     while(!q.empty()){
    44         node k = q.front();
    45         q.pop();
    46         for(int j=0; j<cha;j++){
    47             if( k.next[j]!=-1 ){
    48                 if(k.data==-1)tree[k.next[j]].fail = Root;
    49                 else{
    50                     int t = k.fail;
    51                     while( t!=Root && tree[t].next[j]==-1) t = tree[t].fail;
    52                     tree[ k.next[j] ].fail = max( tree[t].next[j], Root );
    53                     //printf("%c %d %d %d\n",j+'a',k.next[j],tree[t].next[j],tree[k.next[j]].fail);
    54                 }
    55                 q.push(tree[k.next[j]]);
    56             }
    57         }
    58     }
    59 }
    60 
    61 int get_ans(char s[]){
    62     int k=Root, ans = 0;
    63     for(int i=0;s[i];i++){
    64         int t = s[i]-'a';
    65         while(tree[k].next[t]==-1&& k ) k = tree[k].fail;
    66         k = tree[k].next[t];
    67         if(k==-1){ k = Root;continue;}
    68         int j = k;
    69         while( tree[j].count ){
    70             ans += tree[j].count;
    71             tree[j].count = 0;
    72             j = tree[j].fail;
    73         }
    74         //下面两句很重要，如果走到头以后当前字母不是关键字终点然而其fail指针指向字母是关键字终点的话，
    75         //应当加入此关键值，而网上大多数程序忽视了这一点导致hdu的discuss里反例过不了
    76         ans += tree[ tree[j].fail ].count;
    77         tree[ tree[j].fail ].count = 0;
    78     }
    79     return ans;
    80 }
    81 
    82 char tar[2*N];
    83 int main(){
    84     int T,n;
    85     scanf("%d",&T);
    86     while(T--){
    87         scanf("%d",&n);
    88         init(tree[Root],-1);
    89         char a[55];
    90         while(n--){
    91             scanf("%s",a);
    92             Insert(a);
    93         }
    94         AC_automation();
    95         scanf("%s",tar);
    96         printf("%d\n",get_ans(tar));
    97     }
    98     return 0;
    99 }
