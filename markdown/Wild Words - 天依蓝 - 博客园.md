##  [ Wild Words ](http://www.cnblogs.com/chujian123/p/3970212.html)

poj1816: [ http://poj.org/problem?id=1816 ](http://poj.org/problem?id=1816)

题意：给你n个模板串，然后每个串除了字母，还有？或者*，？可以代替任何非空单个字符，*可以替代任何长度任何串，包括空字符串。现在给以一些串，问你这些串在哪些串中出现过。 

题解：trie+DFS。首先，把n个字符串放到trie中，注意，这n个串中可能有相同的字符串。然后对于每个要查询的串，从根节点进行DFS搜索，注意一些特殊处理，例如匹配到*或者？的处理。 
    
    
     1 #include<iostream>
     2 #include<cstdio>
     3 #include<cstring>
     4 #include<algorithm>
     5 using namespace std;
     6 #define N 500001
     7 using namespace std;
     8 const int cha=28;
     9 struct node{
    10     int num;
    11     int count[30];//从根到此处是否是关键字,并且记录是多少个关键字的结尾
    12     int next[cha];
    13 }tree[N];
    14 int ans[100002],top;
    15 int n,m;
    16 void init(node &a,int data){
    17     a.num=0;
    18     for(int i=0;i<cha;i++)
    19         a.next[i] = -1;
    20 }
    21 int k = 1;
    22 void insert(char s[],int num){
    23     int p = 0;
    24     for(int i=0;s[i];i++){
    25         int data = s[i]-'a';
    26          if(s[i]=='?')data=26;
    27          if(s[i]=='*')data=27;
    28         if(tree[p].next[data]==-1){//不存在该结点
    29             init(tree[k],num);
    30             tree[p].next[data] = k;
    31             k++;
    32         }
    33         p = tree[p].next[data];
    34     }
    35     int temp=tree[p].num;
    36     tree[p].num++;
    37     tree[p].count[++temp]=num;
    38 }
    39 void DFS(node p,char *s,int len,int cur){
    40       if(cur==len){
    41          if(p.num){
    42             for(int i=1;i<=p.num;i++)
    43             ans[++top]=p.count[i];
    44          }
    45         while(p.next[27]>0&&tree[p.next[27]].num==0)
    46             p=tree[p.next[27]];
    47          if(p.next[27]>0&&tree[p.next[27]].num>0){
    48                 int tt=tree[p.next[27]].num;
    49          for(int i=1;i<=tt;i++)
    50             ans[++top]=tree[p.next[27]].count[i];
    51          }
    52            return ;
    53       }
    54       int t=s[cur]-'a';
    55       if(p.next[t]>0)
    56          DFS(tree[p.next[t]],s,len,cur+1);
    57       if(p.next[26]>0)
    58         DFS(tree[p.next[26]],s,len,cur+1);
    59       if(p.next[27]>0){
    60           int temp=cur;
    61           while(temp<=len){
    62             DFS(tree[p.next[27]],s,len,temp);
    63             temp++;
    64           }
    65       }
    66 }
    67 char str[100002];
    68 int main(){
    69   while(~scanf("%d%d",&n,&m)){
    70          init(tree[0],-1);
    71     for(int i=1;i<=n;i++){
    72         scanf("%s",str);
    73         insert(str,i-1);
    74     }
    75     for(int i=1;i<=m;i++){
    76         scanf("%s",str);
    77         top=0;
    78         DFS(tree[0],str,strlen(str),0);
    79         sort(ans+1,ans+top+1);
    80         int tt=unique(ans+1,ans+top+1)-ans-1;
    81         if(tt>0){
    82         for(int i=1;i<tt;i++)
    83             printf("%d ",ans[i]);
    84         printf("%d\n",ans[tt]);
    85         }
    86         else
    87             printf("Not match\n");
    88     }
    89   }
    90 }
#### 原文：[http://www.cnblogs.com/chujian123/p/3970212.html](http://www.cnblogs.com/chujian123/p/3970212.html)