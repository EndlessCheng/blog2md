title: Money, Money, Money

date: 2014-10-03 11:05

tags: []

description: 

---
acdream1408: [ http://115.28.76.232/problem?pid=1408 ](http://115.28.76.232/problem?pid=1408)

题意：给你一个x，让你构造a，b，是的na+bm可以组成大于x的所有的数。a>1,b>1,但是不能组成x. 

题解：这一题一开始sb。可以想到的是，所有的数(>=2)都可以由一个2和一个奇数组成。所以2和x+2,就是一个解。并且如果x是偶数，这是无解的。 
    
    
     1 #include<iostream>
     2 #include<algorithm>
     3 #include<cstdio>
     4 #include<cstring>
     5 #include<vector>
     6 using namespace std;
     7 int main(){
     8   long long a;
     9   while(~scanf("%lld",&a)){
    10       if(a%2==0)printf("0 0\n");
    11       else{
    12         printf("%d %lld\n",2,a+2);
    13       }
    14  
    15   }
    16  
    17  
    18 }
