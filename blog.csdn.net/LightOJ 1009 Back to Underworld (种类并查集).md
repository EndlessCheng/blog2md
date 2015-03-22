title: LightOJ 1009 Back to Underworld (种类并查集)

date: 2014-03-24 16:35

tags: [ACM, C++, lightoj, 并查集, 算法, ]

description: 

---
[ http://lightoj.com/volume_showproblem.php?problem=1009 ](http://lightoj.com/volume_showproblem.php?problem=1009)   


  


种类并查集实现（当然用二分图染色也可以） 
    
    
    /*0.204s,2820KB*/
    
    #include<bits/stdc++.h>
    using namespace std;
    const int mx = 20000;
    
    int fa[mx * 2 + 5], rk[mx * 2 + 5], x[100005], y[100005];
    bool has[mx * 2 + 5];
    
    int find(int x) {return ~fa[x] ? fa[x] = find(fa[x]) : x;}
    
    void merge(int x, int y)
    {
    	x = find(x), y = find(y);
    	if (x == y) return;
    	fa[y] = x;
    	rk[x] += rk[y];
    }
    
    int main()
    {
    	int t, n, ans, cnt, u, v, fau, fav, i;
    	scanf("%d", &t);
    	for (int cas = 1; cas <= t; ++cas)
    	{
    		memset(fa, -1, sizeof(fa));
    		memset(rk, 0, sizeof(rk));
    		memset(has, 0, sizeof(has));
    		scanf("%d", &n);
    		ans = cnt = 0;
    		while (n--)
    		{
    			scanf("%d%d", &u, &v);
    			x[cnt] = u, y[cnt++] = v;
    			has[u] = has[v] = has[u + mx] = has[v + mx] = true;
    			rk[u] = rk[v] = 1;
    		}
    		while (cnt--)
    		{
    			merge(x[cnt], y[cnt] + mx);
    			merge(x[cnt] + mx, y[cnt]); ///切莫弄反
    		}
    		for (i = 1; i <= mx * 2; ++i)
    			if (has[i] && fa[i] == -1)
    			{
    				fau = i, fav = find(i + mx);
    				ans += max(rk[fau], rk[fav]);
    				fa[fau] = fa[fav] = 0; ///已访问
    			}
    		printf("Case %d: %d\n", cas, ans);
    	}
    	return 0;
    }
    

  

