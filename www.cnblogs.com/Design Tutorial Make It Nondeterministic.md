title: Design Tutorial Make It Nondeterministic

date: 2014-10-06 17:31:00

tags: []

description: 

---
[Codeforces Round #270](http://codeforces.com/contest/472):C;<http://codeforces.com/contest/472>

题意：水题

题解：贪心即可。
    
    
     1 #include<iostream>
     2 #include<cstdio>
     3 #include<algorithm>
     4 #include<cstring>
     5 using  namespace std;
     6 const int N=1e5+100;
     7 int n;
     8 char str1[N][55];
     9 char str2[N][55];
    10 int a[N];
    11 int main(){
    12      scanf("%d",&n);
    13      for(int i=1;i<=n;i++){
    14         scanf("%s %s",str1[i],str2[i]);
    15      }
    16      for(int i=1;i<=n;i++){
    17         scanf("%d",&a[i]);
    18      }
    19      int temp=0;
    20      bool flag=false;
    21     if(strcmp(str1[a[1]],str2[a[1]])<0){
    22           temp=1;
    23         }
    24       else
    25         temp=2;
    26      //printf("%d\n",temp);
    27      for(int i=2;i<=n;i++){
    28          //  printf("%d %d\n",a[i-1],temp);
    29           if(strcmp(str1[a[i]],str2[a[i]])<0){
    30                 if(temp==1){
    31                if(strcmp(str1[a[i]],str1[a[i-1]])>0){
    32                    temp=1;
    33                   continue;
    34                 }
    35                if(strcmp(str2[a[i]],str1[a[i-1]])<0){
    36                 flag=true;
    37                    break;
    38                }
    39 
    40                }
    41             else{
    42                if(strcmp(str1[a[i]],str2[a[i-1]])>0){
    43                    temp=1;
    44                   continue;
    45                 }
    46                if(strcmp(str2[a[i]],str2[a[i-1]])<0){
    47                  flag=true;
    48                    break;
    49                }
    50 
    51             }
    52             temp=2;
    53 
    54           }
    55           else{
    56 
    57              if(temp==1){
    58                if(strcmp(str2[a[i]],str1[a[i-1]])>0){
    59                    temp=2;
    60                   continue;
    61                 }
    62                if(strcmp(str1[a[i]],str1[a[i-1]])<0){
    63                 flag=true;
    64                    break;
    65                }
    66 
    67                }
    68             else{
    69                if(strcmp(str2[a[i]],str2[a[i-1]])>0){
    70                    temp=2;
    71                   continue;
    72                 }
    73                if(strcmp(str1[a[i]],str2[a[i-1]])<0){
    74                 flag=true;
    75                    break;
    76                }
    77 
    78             }
    79             temp=1;
    80 
    81      }
    82      }
    83      if(flag)puts("NO");
    84      else
    85         puts("YES");
    86 
    87 }

 
