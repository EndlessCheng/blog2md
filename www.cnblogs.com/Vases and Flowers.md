title: Vases and Flowers

date: 2014-10-01 16:02

tags: []

description: 

---
hdu4614: [ http://acm.hdu.edu.cn/showproblem.php?pid=4614 ](http://acm.hdu.edu.cn/showproblem.php?pid=4614)

题意：给你n个花瓶，然后有两种操作：1从a开始选择b个花瓶，放进花，输出左端点，右端点 

2把a到b之间的花瓶中的花拿走，输出拿走的花的数目。 

题解：一看数据范围就知道是线段树，sum维护区间空的花瓶的个数，flag作为lazy标记，如果flag==1表示清空，flag==0表示填满。这一题重要的地方就是二分。 

二分找左边的端点，二分找右边的端点。这是这一题的关键，复杂度就是M*logN*logN.二分就是一件神器啊。注意一些细节的处理。 
    
    
      1 #include<iostream>
      2 #include<cstdio>
      3 #include<algorithm>
      4 #include<cstring>
      5 using namespace std;
      6 const int N=5e4+100;
      7 int sum[N*4],flag[N*4];
      8 int n,m;
      9 void pushup(int rt){
     10    sum[rt]=sum[rt<<1]+sum[rt<<1|1];
     11 }
     12 void build(int l,int r,int rt){
     13     sum[rt]=0;
     14     flag[rt]=-1;
     15     if(l==r){
     16         sum[rt]=1;
     17         return;
     18     }
     19   int mid=(l+r)/2;
     20   build(l,mid,rt<<1);
     21   build(mid+1,r,rt<<1|1);
     22   pushup(rt);
     23 }
     24 void pushdown(int l,int r,int rt){
     25     if(flag[rt]==1){
     26         flag[rt<<1]=flag[rt<<1|1]=1;
     27         sum[rt<<1]=l;
     28         sum[rt<<1|1]=r;
     29         flag[rt]=-1;
     30     }
     31     if(flag[rt]==0){
     32         flag[rt<<1]=flag[rt<<1|1]=0;
     33         sum[rt<<1]=0;
     34         sum[rt<<1|1]=0;
     35         flag[rt]=-1;
     36     }
     37 }
     38 int query(int l,int r,int rt,int from,int to){
     39     if(l==from&&r==to){
     40         return sum[rt];
     41     }
     42     int mid=(l+r)/2;
     43     pushdown(mid-l+1,r-mid,rt);
     44     if(mid>=to)return query(l,mid,rt<<1,from,to);
     45     else if(mid<from)return query(mid+1,r,rt<<1|1,from,to);
     46     else{
     47         return query(l,mid,rt<<1,from,mid)+query(mid+1,r,rt<<1|1,mid+1,to);
     48     }
     49 }
     50 void update(int l,int r,int rt,int from,int to,int val){
     51     if(l==from&&r==to){
     52         flag[rt]=val;
     53         sum[rt]=val*(r-l+1);
     54         return;
     55     }
     56     int mid=(l+r)/2;
     57     pushdown(mid-l+1,r-mid,rt);
     58     if(mid>=to) update(l,mid,rt<<1,from,to,val);
     59     else if(mid<from) update(mid+1,r,rt<<1|1,from,to,val);
     60     else{
     61          update(l,mid,rt<<1,from,mid,val);
     62          update(mid+1,r,rt<<1|1,mid+1,to,val);
     63     }
     64    pushup(rt);
     65 }
     66 int main(){
     67    int T,k,a,b,from,to;
     68    scanf("%d",&T);
     69    while(T--){
     70       scanf("%d%d",&n,&m);
     71       build(1,n,1);
     72       for(int i=1;i<=m;i++){
     73          scanf("%d%d%d",&k,&a,&b);
     74          if(k==1){
     75             from=a+1,to=n;
     76             int temp=query(1,n,1,a+1,n);
     77             if(temp==0){
     78                 printf("Can not put any one.\n");
     79             }
     80             else{
     81                 b=min(b,temp);
     82                 int l=a+1,r=n;
     83                 while(l<=r){
     84                     int mid=(l+r)/2;
     85                     if(query(1,n,1,a+1,mid)>0){
     86                         from=mid;
     87                         r=mid-1;
     88                     }
     89                     else{
     90                         l=mid+1;
     91                     }
     92                 }
     93                  l=from,r=n;
     94                 while(l<=r){
     95                     int mid=(l+r)/2;
     96                     if(query(1,n,1,from,mid)>=b){
     97                         to=mid;
     98                         r=mid-1;
     99                     }
    100                     else{
    101                         l=mid+1;
    102                     }
    103                 }
    104                printf("%d %d\n",from-1,to-1);
    105                update(1,n,1,from,to,0);
    106             }
    107          }
    108           else{
    109                printf("%d\n",b-a+1-query(1,n,1,a+1,b+1));
    110                update(1,n,1,a+1,b+1,1);
    111             }
    112       }
    113       puts("");
    114    }
    115 }
