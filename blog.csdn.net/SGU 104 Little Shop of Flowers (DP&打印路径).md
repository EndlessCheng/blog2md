title: SGU 104 Little Shop of Flowers (DP&打印路径)

date: 2014-03-23 18:35

tags: [ACM, C++, sgu, DP, 算法, ]

description: 

---
[ http://acm.sgu.ru/problem.php?contest=0&problem=104 ](http://acm.sgu.ru/problem.php?contest=0&problem=104)

  

    
    
    /*15ms,142KB*/
    
    #include<bits/stdc++.h>
    using namespace std;
    const int mx = 105;
    
    int a[mx][mx], dp[mx][mx], f;
    
    void print(int i, int j)
    {
    	if (i == 0) return;
    	for (; dp[i][j] == dp[i][j - 1]; --j)
    		;
    	print(i - 1, j - 1);
    	printf("%d", j);
    	if (i < f) putchar(' ');
    }
    
    void solve(int f, int v)
    {
    	int i, j;
    	for (i = 1; i <= f; ++i)
    		for (j = i; j <= v - f + i; ++j)
    			dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + a[i][j]);
    	printf("%d\n", dp[f][v] - f * 100);
    	print(f, v);
    }
    
    int main()
    {
    	int v, i, j;
    	scanf("%d%d", &f, &v);
    	for (i = 1; i <= f; ++i)
    		for (j = 1; j <= v; ++j)
    			scanf("%d", &a[i][j]), a[i][j] += 100;
    	solve(f, v);
    	return 0;
    }
    

  

