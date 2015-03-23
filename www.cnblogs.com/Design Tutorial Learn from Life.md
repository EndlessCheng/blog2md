title: Design Tutorial Learn from Life

date: 2014-10-06 18:01:00

tags: []

description: 

---
[Codeforces Round #270](http://codeforces.com/contest/472) B:<http://codeforces.com/contest/472/problem/B>

题意：n个人在1楼，想要做电梯上楼，只有1个电梯，每次只能运k个人，每移动一层需要1秒。问最小的是时间把所有人送到想去的楼层。

题解：贪心，每次选择楼层数最大k个人，用优先队列维护一下即可。
    
    
     1 #include<iostream>
     2 #include<cstdio>
     3 #include<cstring>
     4 #include<algorithm>
     5 #include<queue>
     6 using namespace std;
     7 const int N=2004;
     8 int n,k,temp;
     9 int main(){
    10    scanf("%d%d",&n,&k);
    11      priority_queue<int>Q;
    12    for(int i=1;i<=n;i++){
    13       scanf("%d",&temp);
    14       Q.push(temp);
    15    }
    16    int ans=0,tt=k;
    17    while(Q.size()>k){
    18         tt=k;
    19       ans+=(Q.top()-1);
    20       while(tt--)
    21         Q.pop();
    22    }
    23    if(Q.size()>0)
    24      ans+=(Q.top()-1);
    25    printf("%d\n",ans*2);
    26 }

 
