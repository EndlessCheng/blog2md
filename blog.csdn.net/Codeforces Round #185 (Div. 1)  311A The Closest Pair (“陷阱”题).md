title: Codeforces Round #185 (Div. 1)  311A The Closest Pair (“陷阱”题)

date: 2014-03-15 13:15

tags: [ACM, C++, codeforces, 算法, 数学, ]

description: 

---
[ http://codeforces.com/problemset/problem/311/A ](http://codeforces.com/problemset/problem/311/A)   


  


If we ignore "break",  _ tot _ will be up to ![](http://espresso.codeforces.com/66a19249b26d808e85ea349b8b84dee8a2090e0c.png) . 

Consider whether we can make such inequality  _ d _ ≤ _ p _ [ _ j _ ]. _ x _ \- _ p _ [ _ i _ ]. _ x _ is always false. The obvious way is to ** make all points' x coordinates the same ** (WTF!!!). And we can just choose  _ n _ distinct numbers to be all points' y coordinate. 

Thus the problem is solved. 

  

    
    
    #include<cstdio>
    
    int main()
    {
    	int n, k;
    	scanf("%d%d", &n, &k);
    	if (k >= n * (n - 1) / 2) puts("no solution");
    	else for (int i = 1; i <= n; i++) printf("0 %d\n", i);
    	return 0;
    }
    

  


【扩展】 

如果要求每个x的横坐标都不相同呢？ 
