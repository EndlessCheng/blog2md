title: POJ 2932 Coneology (扫描线判断最外面的圆&set维护最近的圆)

date: 2014-03-20 15:08

tags: [ACM, C++, codeforces, 扫描线, 计算几何, ]

description: 

---
[ http://poj.org/problem?id=2932 ](http://poj.org/problem?id=2932)

  


先给圆的最左端和最右端的点排个序，当两点x相同时，左端点排在前面。 

然后就是扫描了， 

若扫描到的是圆的左端点，就判断圆心(y坐标)在其上方且离其最近的圆是否包含此圆，以及圆心(y坐标)在其下方且离其最近的圆是否包含此圆，若包含就continue，不包含就insert到set中； 

若扫描到的是圆的右端点，就从set中erase此圆(erase操作考虑了圆不在set中的情况) 

  


完整代码：   

    
    
    /*2282ms,5064KB*/
    
    #include<cstdio>
    #include<set>
    #include<vector>
    #include<utility>
    #include<algorithm>
    using namespace std;
    const int mx = 40005;
    
    int n;
    double x[mx], y[mx], r[mx];
    pair<double, int> px[mx * 2];
    vector<int> res; ///答案
    set<pair<double, int> > out; ///最外层的圆的集合(维护圆心纵坐标)
    set<pair<double, int> >::iterator it;
    
    ///判断圆i是否在圆j内部
    inline bool inside(int i, int j)
    {
    	return (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]) <= r[j] * r[j];
    }
    
    void solve()
    {
    	for (int i = 0, j = 0; i < n; ++i)
    	{
    		px[j++] = make_pair(x[i] - r[i], i);
    		px[j++] = make_pair(x[i] + r[i], i + n);
    	}
    	int m = n * 2;
    	sort(px, px + m);
    	for (int i = 0; i < m; ++i)
    	{
    		int id = px[i].second % n;
    		if (px[i].second < n) ///扫描到左端
    		{
    			it = out.lower_bound(make_pair(y[id], id));
    			if (it != out.end() && inside(id, it->second) ||
    					it != out.begin() && inside(id, (--it)->second)) continue;
    			res.push_back(id);
    			out.insert(make_pair(y[id], id));
    		}
    		else out.erase(make_pair(y[id], id)); ///扫描到右端
    	}
    	sort(res.begin(), res.end());
    	printf("%d\n", res.size());
    	printf("%d", res[0] + 1);
    	for (int i = 1; i < res.size(); ++i) printf(" %d", res[i] + 1);
    }
    
    int main()
    {
    	scanf("%d", &n);
    	for (int i = 0; i < n; ++i) scanf("%lf%lf%lf", &r[i], &x[i], &y[i]);
    	solve();
    	return 0;
    }
    

  

