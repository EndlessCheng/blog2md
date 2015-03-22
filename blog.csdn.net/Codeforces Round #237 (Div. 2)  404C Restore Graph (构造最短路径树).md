title: Codeforces Round #237 (Div. 2)  404C Restore Graph (构造最短路径树)

date: 2014-03-20 09:28

tags: [ACM, C++, codeforces, 算法, 图论, ]

description: 

---
[ http://codeforces.com/contest/404/problem/C ](http://codeforces.com/contest/404/problem/C)

  


思路：我们构造一颗最短路径树就行了。 

若能够构造，边数必然为n-1（样例1的边数可以是两条）。 

如何构造？从距离为1的点开始，逐渐往下加边，生成一颗k叉树。若在中间生成了大于k的叉，则输出-1。 

  


完整代码：   

    
    
    /*265ms,4436KB*/
    
    #include<bits/stdc++.h>
    using namespace std;
    
    vector<int> dis[100005];
    vector<pair<int, int> > ans;
    
    int main()
    {
    	int n, k, d, m = 0;
    	cin >> n >> k;
    	for (int i = 1; i <= n; i++)
    	{
    		cin >> d;
    		dis[d].push_back(i); ///统计距离
    		m = max(m, d);
    	}
    	if (dis[0].size() != 1)
    	{
    		cout << "-1";
    		return 0;
    	}
    	for (int i = 1; i <= m; i++)
    	{
    		int edge = (i != 1), cnt = 0;
    		for (int j = 0; j < dis[i].size(); j++)
    		{
    			if (edge == k)
    			{
    				edge = (i != 1);
    				cnt++; ///换另一个点，即以后的边加到下一个点
    			}
    			if (cnt == dis[i - 1].size())
    			{
    				cout << "-1";
    				return 0;
    			}
    			ans.push_back(make_pair(dis[i - 1][cnt], dis[i][j])); ///按距离逐渐加边
    			edge++;
    		}
    	}
    	cout << n - 1 << endl; ///由于构造的是一颗树(最短路径树)，所以边数必然为点数-1
    	for (int i = 0; i < ans.size(); i++)
    		cout << ans[i].first << " " << ans[i].second << endl;
    	return 0;
    }
    

  

