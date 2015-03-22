title: Codeforces Round #206 (Div. 2)  355C (转化&枚举)

date: 2014-03-14 20:17

tags: [ACM, C++, codeforces, 算法, ]

description: 

---
[ http://codeforces.com/contest/355/problem/C ](http://codeforces.com/contest/355/problem/C)   


  


枚举i，左手操作了i次，右手操作了n-i次，然后重复次数可以直接算出来，所以答案就可以在O(n)的时间内算出来。 
    
    
    /*30ms,4000KB*/
    
    #include<bits/stdc++.h>
    using namespace std;
    
    int a[100005];
    
    int main()
    {
    	int n, l, r, q1, q2;
    	cin >> n >> l >> r >> q1 >> q2;
    	for (int i = 1; i <= n; i++) cin >> a[i], a[i] += a[i - 1];
    	int ans = INT_MAX;
    	for (int i = 0; i <= n; i++)
    	{
    		int tmp = a[i] * l + (a[n] - a[i]) * r;
    		if (2 * i > n + 1) tmp += q1 * (2 * i - n - 1);
    		else if (2 * i < n - 1) tmp += q2 * (n - 2 * i - 1);
    		ans = min(ans, tmp);
    	}
    	cout << ans << endl;
    	return 0;
    }
    

  

