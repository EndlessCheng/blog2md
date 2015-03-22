title: LightOJ 1085 All Possible Increasing Subsequences (DP&离散化&树状数组)

date: 2014-03-25 21:28

tags: [ACM, C++, 离散化, lightoj, 算法, ]

description: 

---
[ http://lightoj.com/volume_showproblem.php?problem=1085 ](http://lightoj.com/volume_showproblem.php?problem=1085)   


  


先说个很快的方法——二维思考，从右下往左上离散化： 
    
    
    /*0.364s,2860KB*/
    
    #include<bits/stdc++.h>
    using namespace std;
    const int mx = 100005;
    const int mod = 1000000007;
    
    int tree[mx], a[mx], dis[mx], n;
    
    ///从右下往左上“看”
    bool cmp(int x, int y)
    {
    	if (a[x] != a[y]) return a[x] < a[y];
    	return x > y;
    }
    
    void add(int pos, int x)
    {
    	for (; pos <= n; pos += pos & -pos) tree[pos] = (tree[pos] + x) % mod;
    }
    
    int sum(int pos)
    {
    	int res = 0;
    	for (; pos; pos -= pos & -pos) res = (res + tree[pos]) % mod;
    	return res;
    }
    
    int main()
    {
    	int t, cas, i;
    	scanf("%d", &t);
    	for (cas = 1; cas <= t; ++cas)
    	{
    		scanf("%d", &n);
    		for (i = 1; i <= n; ++i) scanf("%d", &a[i]), dis[i] = i;
    		sort(dis + 1, dis + n + 1, cmp);
    		memset(tree, 0, sizeof(tree));
    		for (i = 1; i <= n; i++) add(dis[i], sum(dis[i]) + 1);
    		printf("Case %d: %d\n", cas, sum(n));
    	}
    	return 0;
    }
    

  


然后是普遍的从左往右离散化的方法，但是太慢，而且还耗内存： 
    
    
    /*1.236s,7088KB*/
    
    #include<bits/stdc++.h>
    using namespace std;
    const int mx = 100005;
    const int mod = 1000000007;
    
    int tree[mx], a[mx], n;
    map<int, int> m;
    
    void add(int pos, int x)
    {
    	for (; pos <= n; pos += pos & -pos) tree[pos] = (tree[pos] + x) % mod;
    }
    
    int sum(int pos)
    {
    	int res = 0;
    	for (; pos; pos -= pos & -pos) res = (res + tree[pos]) % mod;
    	return res;
    }
    
    int main()
    {
    	int t, cas, i, cnt, pos;
    	map<int, int>::iterator it;
    	scanf("%d", &t);
    	for (cas = 1; cas <= t; ++cas)
    	{
    		scanf("%d", &n);
    		m.clear();
    		for (i = 0; i < n; ++i) scanf("%d", &a[i]), m[a[i]];
    		cnt = 0;
    		for (it = m.begin(); it != m.end(); ++it) it->second = ++cnt;
    		memset(tree, 0, sizeof(tree));
    		for (i = 0; i < n; ++i) pos = m[a[i]], add(pos, sum(pos - 1) + 1);
    		printf("Case %d: %d\n", cas, sum(cnt));
    	}
    	return 0;
    }
    

  

