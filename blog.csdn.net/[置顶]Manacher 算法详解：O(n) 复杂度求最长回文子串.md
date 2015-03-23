title: [置顶]Manacher 算法详解：O(n) 复杂度求最长回文子串

date: 2014-02-03 12:27:00

tags: [字符串, C++, 最长回文子串, Manacher, 算法, ]

description: 

---
先预处理下：在每个字符的两边都插入一个特殊的符号，比如abba变成#a#b#b#a#，aba变成 #a#b#a#（因为Manacher算法只能处理奇数长度的字符串）。同时，为了避免数组越界，在字符串开头添加另一特殊符号，比如$#a#b#a#。

以字符串3212343219为例，处理后变成S[] = "$#3#2#1#2#3#4#3#2#1#9#"。  
然后用一个数组Len[i]来记录以处理后的字符S[i]为中心的最长回文子串的**半长度**（包括S[i]）：
    
    
    S   # 3 # 2 # 1 # 2 # 3 # 4 # 3 # 2 # 1 # 9 #
    Len 1 2 1 2 1 6 1 2 1 2 1 8 1 2 1 2 1 2 1 2 1
    

（最终的回文子串的长度即为maxLen-1）

  


Manacher算法的核心就在于减少Len[i]的计算量，使得原来O(n^2)的算法优化为O(n)。  


下面两幅图的红框中的字符串为当前的**右边界下标最大**的回文子串，mid为其中心，right为其**最右端+1**，i'=2*mid-i为i关于mid的对称点。

现要计算Len[i]，若以i'为中心的回文串（黄框）包含在最长回文子串中，则由回文串的**对称性**，以i为中心的回文串亦在最长回文子串中，即有Len[i]=Len[2*mid-i]

![](http://img.blog.csdn.net/20140203122027250?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3luYXBzZTc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  


若以i'为中心的回文串（黄框）不包含在最长回文子串中，则以i为中心的回文串的半长度Len[i]=right-i+(之后继续判断的长度)

![](http://img.blog.csdn.net/20140203115953390?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3luYXBzZTc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  


那么，为什么复杂度是O(n)的呢？

首先，主要影响复杂度的是s[i + len[i]] == s[i - len[i]]这一判断。

由下面的代码可知，当i<right时，我们就用常数的时间计算Len[i]（此时不会执行while中的语句）；当i>=right时，我们就继续判断：while (s[i + len[i]] == s[i - len[i]]) ++len[i]; 结束后，right < i + len[i]为真，更新right值。这样，我们至多进行n次s[i + len[i]] == s[i - len[i]]判断，故复杂度为O(n)。

  


完整代码：
    
    
    #include<bits/stdc++.h>
    using namespace std;
    const int mx = 10000;
    
    char ss[mx + 5], s[(mx << 1) + 5]; /// ss为源串，s为处理后的字符串
    int len[(mx << 1) + 5];
    
    void debug()
    {
    	int i;
    	for (i = 1; s[i]; ++i) printf("%c ", s[i]);
    	puts("");
    	for (i = 1; s[i]; ++i) printf("%d ", len[i]);
    	puts("");
    }
    
    int main()
    {
    	int right, mid, i, maxlen;
    	while (gets(ss))
    	{
    		memset(s, 0, sizeof(s));
    		s[0] = '$';
    		for (i = 0; ss[i]; ++i) s[(i << 1) + 1] = '#', s[(i << 1) + 2] = ss[i];
    		s[(i << 1) + 1] = '#';
    		memset(len, 0, sizeof(len));
    		maxlen = right = mid = 0;
    		for (i = 1; s[i]; ++i)
    		{
    			len[i] = (i < right ? min(len[(mid << 1) - i], right - i) : 1);
    			/* 取min的原因：记点i关于mid的对称点为i'，
    			若以i'为中心的回文串范围超过了以mid为中心的回文串的范围
    			(此时有i + len[(mid << 1) - i] >= right，注意len是包括中心的半长度)
    			则len[i]应取right - i(总不能超过边界吧) */
    			while (s[i + len[i]] == s[i - len[i]]) ++len[i];
    			maxlen = max(maxlen, len[i]);
    			if (right < i + len[i]) mid = i, right = i + len[i];
    		}
    		printf("%d\n", maxlen - 1);
    		debug();
    	}
    	return 0;
    }
    

  


补充：使用 Manacher 算法后我们得到了一个 len 数组，利用它我们可以在 O(1) 的时间内判断该字符串的**任意子串**是不是回文串，方法如下：
    
    
    inline bool Query(int l, int r) /// 判断源串中的某一子串 ss[l...r] 是否为回文串
    {
        return len[l + r + 2] >= r - l + 1;
    }

这里必须要有等号，不过其成立的例子我并未想到，如果你找到了一个例子，欢迎在下方评论 ^_^

  


例题：

[HDU 3068 最长回文](http://acm.hdu.edu.cn/showproblem.php?pid=3068)

[POJ 3974 Palindrome](http://poj.org/problem?id=3974)

  


与 Manacher 算法思想类似的题：[CF 359D Pair of Numbers](http://codeforces.com/contest/359/problem/D)

  


代码：
    
    
    /* 124 ms, 2324 KB */
    #include<cstdio>
    
    int a[300005], w[300005];
    
    int main()
    {
    	int n, i, l, r, cnt = 0, maxd = 0;
    	scanf("%d", &n);
    	for (i = 0; i < n; i++) scanf("%d", &a[i]);
    	for (i = 0; i < n;)
    	{
    		l = r = i;
    		while (l && a[l - 1] % a[i] == 0) l--; // 向左找
    		while (r < n - 1 && a[r + 1] % a[i] == 0) r++; // 向右找
    		i = r + 1; // 关键，这样做是因为在[l,r]内的数的「边界」不会超过[l,r]（可用反证法思考），同时，每个数被找到的次数不会超过log(a[i])
    		r -= l;
    		if (r > maxd) cnt = 0, maxd = r;
    		if (r == maxd) w[cnt++] = l + 1;
    	}
    	printf("%d %d\n", cnt, maxd);
    	for (i = 0; i < cnt; ++i) printf("%d ", w[i]);
    	return 0;
    }

  
  

