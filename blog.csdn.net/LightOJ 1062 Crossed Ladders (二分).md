title: LightOJ 1062 Crossed Ladders (二分)

date: 2014-03-26 18:57:00

tags: [ACM, C++, 二分, 算法, lightoj, ]

description: 

---
<http://lightoj.com/volume_showproblem.php?problem=1062>

  

    
    
    /*0.000s,1700KB*/
    
    #include<bits/stdc++.h>
    using namespace std;
    double EPS = 1e-8;
    
    int main()
    {
    	double a, b, c, j, c1, h, k, x;
    	int T, cas = 0;
    	scanf("%d", &T);
    	while (T--)
    	{
    		scanf("%lf%lf%lf", &a, &b, &c);
    		h = k = x = 0;
    		double lo = 0, hi = max(a, b);
    		while (fabs(lo - hi) > EPS)
    		{
    			x = (lo + hi) / 2;
    			h = sqrt(a * a - x * x);
    			k = sqrt(b * b - x * x);
    			c1 = (k * h) / (k + h);
    			if (fabs(c1 - c) <= EPS) break;
    			else if (c1 > c)lo = x + EPS;
    			else hi = x - EPS;
    		}
    		printf("Case %d: %.7f\n", ++cas, x);
    	}
    	return 0;
    }
    

  

