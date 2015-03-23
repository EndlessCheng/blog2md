title: MUH and Cube Walls

date: 2014-10-08 22:25:00

tags: []

description: 

---
[Codeforces Round #269 (Div. 2)](http://codeforces.com/contest/471) D:<http://codeforces.com/problemset/problem/471/D>

题意：给定两个序列a ,b, 如果在a中存在一段连续的序列使得a[i]-b[0]==k, a[i+1]-b[1]==k.... a[i+n-1]-b[n-1]==k,就说b串在a串中出现过！最后输出b串在a串中出现几次！

题解：把两个串进行处理，相邻项之间做差，然后就很容易想到用KMP来搞，然后注意几个特判就行。
    
    
     1 #include<cstdio>
     2 #include<cstdlib>
     3 #include<cstring>
     4 #define N 1000005
     5 using namespace std;
     6 long long  next[N];
     7 long long s1[N];//模板串
     8 long long  s2[N];//主串
     9 int len1,len2,ans;
    10 long long a[N],b[N];
    11 void getnext(int plen){
    12     int i = 0,j = -1;
    13     next[0] = -1;
    14     while( i<plen ){
    15         if(j==-1||s1[i]==s1[j]){
    16             ++i;++j;
    17           //if(s1[i]!=s1[j] )这里别隐去的的部分，也可以不划去
    18             next[i] = j;
    19         //  else
    20            // next[i] = next[j];
    21         }
    22         else
    23             j = next[j];
    24     }
    25 }
    26 void  KMP(){
    27     getnext(len1);
    28     int i = 0,j = 0;
    29     while (i<len2&&j<len1){
    30         if( j == -1 || s2[i] == s1[j] ){
    31             ++i;
    32             ++j;
    33         }
    34         else {
    35             j = next[j];
    36 
    37         }
    38         if( j==len1 ){//找到一个匹配串之后，不是在原来串中往后移动一位，而是移动i-(j-next[j]);
    39             ans++;
    40             j=next[j];
    41          }
    42     }
    43 }
    44 int n,m;
    45 int main(){
    46     scanf("%d%d",&n,&m);
    47      ans=0;
    48      for(int i=1;i<=n;i++){
    49         scanf("%I64d",&a[i]);
    50      }
    51       for(int j=1;j<=m;j++){
    52           scanf("%I64d",&b[j]);
    53       }
    54       for(int i=2;i<=n;i++){
    55         a[i-1]=a[i]-a[i-1]+1e9;
    56         s2[i-2]=a[i-1];
    57        // printf("%I64d " ,s2[i-2]);
    58       }
    59       //puts("");
    60       for(int i=2;i<=m;i++){
    61          b[i-1]=b[i]-b[i-1]+1e9;
    62          s1[i-2]=b[i-1];
    63          //printf("%I64d " ,s1[i-2]);
    64       }
    65       if(n==1&&m==1)puts("1");
    66       else if(n==1&&m!=1)puts("0");
    67       else if(m==1&&n!=1)printf("%d\n",n);
    68       else{
    69       len2=n-1;
    70       len1=m-1;
    71       getnext(m-1);
    72       KMP();
    73       printf("%d\n",ans);
    74       }
    75 }

 
