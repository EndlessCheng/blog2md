title: POJ 3104 Drying (二分&最大化最小值)

date: 2014-03-22 10:10

tags: [ACM, C++, codeforces, 算法, 二分, ]

description: 

---
[ http://poj.org/problem?id=3104 ](http://poj.org/problem?id=3104)

  


一开始没注意k为1的情况，WA了一发。。 

加个特判就过了。 

  


完整代码：   

    
    
    /*750ms,576KB*/
    
    #include<cstdio>
    #include<cmath>
    #include<algorithm>
    using namespace std;
    const int mx = 100005;
    
    int n, k, a[mx];
    
    bool judge(int time)
    {
    	int cnt = 0;
    	for (int i = 0; i < n; ++i)
    	{
    		if (a[i] > time) cnt += ceil((double)(a[i] - time) / k);
    		if (cnt > time) return false;
    	}
    	return true;
    }
    
    int main()
    {
    	scanf("%d", &n);
    	int l = 0, r = 0, m;
    	for (int i = 0; i < n; ++i)  scanf("%d", &a[i]), r = max(r, a[i]);
    	scanf("%d", &k);
    	if (k == 1) return printf("%d", r), 0; ///要特判k为1的情况！！
    	--k;
    	while (l + 1 < r) judge(m = (l + r) >> 1) ? r = m : l = m;
    	printf("%d", l + 1);
    	return 0;
    }
    

  

