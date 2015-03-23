title: LightOJ 1258 Making Huge Palindromes (回文&KMP)

date: 2014-03-27 13:40:00

tags: [ACM, C++, lightoj, kmp, 算法, ]

description: 

---
<http://lightoj.com/volume_showproblem.php?problem=1258>

  


首先原串+翻转过来的串必然是一个回文串，但是二者在中间可以“融合”，而KMP算法恰好可以求出最大融合长度。

所以看翻转过来的串能匹配多少原串即可，答案就是len+(len-匹配个数)。

  


完整代码：  

    
    
    /*0.140s,7548KB*/
    
    #include<bits/stdc++.h>
    using namespace std;
    const int mx = 1000005;
    
    char t[mx], p[mx];
    int f[mx], len;
    
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
    	getfail();
    	int j = 0;
    	for (int i = 0; t[i]; ++i)
    	{
    		while (j && p[j] != t[i]) j = f[j];
    		if (p[j] == t[i]) ++j;
    	}
    	return (len << 1) - j;
    }
    
    int main()
    {
    	int tt;
    	scanf("%d", &tt);
    	getchar();
    	for (int cas = 1; cas <= tt; ++cas)
    	{
    		gets(t);
    		len = strlen(t);
    		reverse_copy(t, t + len, p);
    		p[len] = 0;
    		printf("Case %d: %d\n", cas, find());
    	}
    	return 0;
    }
    

  

