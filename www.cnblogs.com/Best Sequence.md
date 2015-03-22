title: Best Sequence

date: 2014-09-19 18:25

tags: []

description: 

---
poj1699: [ http://poj.org/problem?id=1699 ](http://poj.org/problem?id=1699)

题意：给你nge串，让你求出这些串组成的最小的串重叠部分只算一次。 

题解：我的做法是DFS，因为数据范围只有10，就算是n！也只有300多万，加上剪枝，就可以过了。 
    
    
     1 #include<iostream>
     2 #include<cstdio>
     3 #include<cstring>
     4 #include<algorithm>
     5 using namespace std;
     6 int n;
     7 char str[100][100],s[10000];
     8 int ans;
     9 bool vis[100];
    10 int getlen(char s1[],char s2[],int l1,int l2){
    11       int ans;//表示重叠部分的长度
    12       if(l1>=l2){
    13          for(ans=l2;ans>=0;ans--){
    14              bool flag=true;
    15            for(int i=0;i<ans;i++){
    16                 if(s2[i]!=s1[l1-(ans-i)]){
    17                     flag=false;
    18                     break;
    19                 }
    20           }
    21           if(flag)return ans;
    22       }
    23     }
    24     else{
    25      for(ans=l1;ans>=0;ans--){
    26              bool flag=true;
    27            for(int i=0;i<ans;i++){
    28                 if(s2[i]!=s1[l1-(ans-i)]){
    29                     flag=false;
    30                     break;
    31                 }
    32 
    33           }
    34           if(flag)return ans;
    35       }
    36     }
    37 }
    38 void DFS(char fa[],int ll,int dep){
    39       if(ll>=ans)return;
    40       if(dep==n){
    41         ans=min(ll,ans);
    42         return;
    43       }
    44       for(int i=1;i<=n;i++){
    45           if(vis[i])continue;
    46           int tt=strlen(str[i]);
    47           int temp=getlen(fa,str[i],ll,tt);
    48           for(int j=ll;j<ll+(tt-temp);j++){
    49             fa[j]=str[i][temp+(j-ll)];
    50           }
    51           vis[i]=1;
    52           DFS(fa,ll+tt-temp,dep+1);
    53           vis[i]=0;
    54       }
    55 }
    56 int main(){
    57   int T;
    58   scanf("%d",&T);
    59   while(T--){
    60     scanf("%d",&n);
    61     memset(str,0,sizeof(str));
    62     memset(s,0,sizeof(s));
    63     memset(vis,0,sizeof(vis));
    64     ans=10000000;
    65     for(int i=1;i<=n;i++){
    66         scanf("%s",str[i]);
    67     }
    68     for(int i=1;i<=n;i++){
    69       memset(s,0,sizeof(s));
    70        strcpy(s,str[i]);
    71         vis[i]=1;
    72         DFS(s,strlen(str[i]),1);
    73         vis[i]=0;
    74     }
    75     printf("%d\n",ans);
    76   }
    77 
    78 }
