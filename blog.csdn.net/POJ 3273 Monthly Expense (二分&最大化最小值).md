title: POJ 3273 Monthly Expense (二分&最大化最小值)

date: 2014-03-22 09:38

tags: [ACM, C++, codeforces, 二分, 算法, ]

description: 

---
[ http://poj.org/problem?id=3273 ](http://poj.org/problem?id=3273)

  


要特别注意l的初值选取，若这题输入的日开支可以是0的话，l应初始化为-1 
    
    
    /*63ms,556KB*/
    
    #include<cstdio>
    const int mx = 100005;
    
    int n, mon, a[mx];
    
    bool judge(int m)
    {
    	int sum = 0, cnt = 1;
    	for (int i = 0; i < n; ++i)
    	{
    		sum += a[i];
    		if (sum > m)
    		{
    			if (a[i] > m) return false;
    			sum = a[i];
    			++cnt;
    		}
    		if (cnt > mon) return false;
    	}
    	return true;
    }
    
    int main()
    {
    	scanf("%d%d", &n, &mon);
    	int sum = 0;
    	for (int i = 0; i < n; ++i) scanf("%d", &a[i]), sum += a[i];
    	int l = 0, r = sum, m;
    	while (l + 1 < r) judge(m = (l + r) >> 1) ? r = m : l = m;
    	printf("%d", l + 1);
    	return 0;
    }
    

  

