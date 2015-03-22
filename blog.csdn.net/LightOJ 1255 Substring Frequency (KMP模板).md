title: LightOJ 1255 Substring Frequency (KMP模板)

date: 2014-03-26 23:27

tags: [ACM, C++, lightoj, kmp, 算法, ]

description: 

---
[ http://lightoj.com/volume_showproblem.php?problem=1255 ](http://lightoj.com/volume_showproblem.php?problem=1255)

  

    
    
    /*0.068s,7548KB*/
    
    #include<bits/stdc++.h>
    using namespace std;
    const int mx = 1000005;
    
    char t[mx], p[mx];
    int f[mx];
    
    void getfail()
    {
    	f[0] = f[1] = 0;
    	for (int i = 1; p[i]; ++i)
    	{
    		int j = f[i];
    		while (j && p[i] != p[j]) j = f[j];
    		f[i + 1] = (p[i] == p[j] ? j + 1 : 0);
    	}
    }
    
    int find()
    {
    	int m = strlen(p), cnt = 0;
    	getfail();
    	int j = 0;
    	for (int i = 0; t[i]; ++i)
    	{
    		while (j && p[j] != t[i]) j = f[j];
    		if (p[j] == t[i]) ++j;
    		if (j == m) ++cnt;
    	}
    	return cnt;
    }
    
    int main()
    {
    	int tt;
    	scanf("%d", &tt);
    	getchar();
    	for (int cas = 1; cas <= tt; ++cas)
    	{
    		gets(t), gets(p);
    		printf("Case %d: %d\n", cas, find());
    	}
    	return 0;
    }
    

  

