title: Rotate

date: 2014-09-13 19:55

tags: []

description: 

---
hdu4998: [ http://acm.hdu.edu.cn/showproblem.php?pid=4998 ](http://acm.hdu.edu.cn/showproblem.php?pid=4998)

题意：给你n个点，以及绕每个点旋转的弧度。然后，问你经过这n次旋转，平面中的点总的效果是相当于哪个点旋转了多少弧度。 

题解：我的第一道计算几何。可以选两个点，求出旋转之后的对应点，然后分别求出这两个点的中垂线，中垂线的交点就是要求的点，弧度就是所有弧度之和mod（2*pi） 
    
    
     1 #include<iostream>
     2 #include<cstdio>
     3 #include<cstring>
     4 #include<algorithm>
     5 #include<cmath>
     6 const double pi=3.14159265;
     7 using namespace std;
     8 int n;
     9 struct Point{
    10   double x;
    11   double y;
    12   double s;
    13 }num[20];
    14 struct LINE{
    15    double a,b,c;
    16    Point s;
    17 };
    18 Point HHH(Point o,double alpha,Point p) {//点p绕着o旋转alpha弧度
    19     Point tp;
    20     p.x-=o.x;
    21     p.y-=o.y;
    22     tp.x=p.x*cos(alpha)-p.y*sin(alpha)+o.x;
    23     tp.y=p.y*cos(alpha)+p.x*sin(alpha)+o.y;
    24     return tp;
    25  }
    26 bool CCC(LINE l1,LINE l2,Point&p){//两条直线是否相交，如果相交，则交点为p
    27   double d=l1.a*l2.b-l2.a*l1.b;
    28     if(abs(d)<1e-6)    return false;
    29     p.x = (l2.c*l1.b-l1.c*l2.b)/d;
    30     p.y = (l2.a*l1.c-l1.a*l2.c)/d;
    31     return true;
    32 }
    33 LINE DDD(const Point &_a, const Point &_b){//求两点之间垂直平分线
    34         LINE ret;
    35         ret.s.x = (_a.x + _b.x)/2;
    36         ret.s.y = (_a.y + _b.y)/2;
    37         ret.a = _b.x - _a.x;
    38         ret.b = _b.y - _a.y;
    39         ret.c = (_a.y - _b.y) * ret.s.y + (_a.x - _b.x) * ret.s.x;
    40         return ret;
    41 }
    42 
    43 LINE EEE(Point a,Point b){//求经过两点的中垂线
    44     LINE ret;
    45     if(abs(a.x-b.x)<1e-6){
    46         ret.a=1;
    47         ret.b=0;
    48         ret.c=-a.x;
    49         return ret;
    50     }
    51     ret.a=a.y-b.y;
    52     ret.b=b.x-a.x;
    53     ret.c=a.x*b.y-a.y*b.x;
    54     return ret;
    55 }
    56 int main(){
    57    int T;
    58    scanf("%d",&T);
    59    while(T--){
    60       scanf("%d",&n);
    61       double sum=0;
    62       for(int i=1;i<=n;i++){
    63          scanf("%lf%lf%lf",&num[i].x,&num[i].y,&num[i].s);
    64          sum+=num[i].s;
    65       }
    66       Point s1,s2;
    67       s1.x=2.345,s1.y=4.123;
    68       s2.x=11.345,s2.y=12.123;
    69       Point t1=s1,t2=s2;
    70       for(int i=1;i<=n;i++){
    71          Point temp=HHH(num[i],num[i].s,t1);
    72          t1=temp;
    73       }
    74        for(int i=1;i<=n;i++){
    75          Point temp=HHH(num[i],num[i].s,t2);
    76          t2=temp;
    77       }
    78       LINE one1=DDD(s1,t1);
    79       LINE one2=DDD(s2,t2);
    80       Point a;
    81       if(CCC(one1,one2,a)){
    82         if(sum>2*pi)
    83         sum-=2*pi;
    84         printf("%lf %lf %lf\n",a.x,a.y,sum);
    85       }
    86       else{
    87           LINE ttt=EEE(s1,s2);
    88           CCC(one1,ttt,a);
    89         if(sum>2*pi)
    90          sum-=2*pi;
    91          printf("%lf %lf %lf\n",a.x,a.y,sum);
    92       }
    93    }
    94 }
