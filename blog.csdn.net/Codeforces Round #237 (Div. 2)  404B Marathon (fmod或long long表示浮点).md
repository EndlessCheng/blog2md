title: Codeforces Round #237 (Div. 2)  404B Marathon (fmod或long long表示浮点)

date: 2014-03-20 09:40

tags: [ACM, C++, codeforces, 算法, 精度, ]

description: 

---
[ http://codeforces.com/contest/404/problem/B ](http://codeforces.com/contest/404/problem/B)

  


这题很容易出现精度误差，解决方法有两种： 

1\. 分析知当d远大于a时，在计算除法时容易产生较大误差，故可以先用fmod把d减小。 

2\. 因为输入的小数至多到小数点后4位，故计算过程中的结果完全可以用long long存下来，这样就不用担心精度的问题了，且此法具有一定的普适性。 

  

    
    
    /*124ms,0KB*/
    
    #include<bits/stdc++.h>
    using namespace std;
    
    double a;
    
    void f(double len)
    {
    	int c = ((int)(len / a)) % 4;
    	len = fmod(len, a);
    	if (c == 0) printf("%f 0\n", len);
    	else if (c == 1) printf("%f %f\n", a, len);
    	else if (c == 2) printf("%f %f\n", a - len, a);
    	else printf("0 %f\n", a - len);
    }
    
    int main()
    {
    	double d;
    	int n;
    	scanf("%lf%lf%d", &a, &d, &n);
    	d = fmod(d, 4 * a); /// 若d远大于a，可以先 d %= 4*a
    	for (int i = 1; i <= n; ++i) f(d * i);
    	return 0;
    }
    

  

