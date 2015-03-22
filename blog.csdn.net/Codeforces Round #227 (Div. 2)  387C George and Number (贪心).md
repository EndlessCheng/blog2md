title: Codeforces Round #227 (Div. 2)  387C George and Number (贪心)

date: 2014-03-22 18:12

tags: [ACM, C++, codeforces, 算法, 贪心, ]

description: 

---
[ http://codeforces.com/contest/387/problem/C ](http://codeforces.com/contest/387/problem/C)

  

    
    
    /*31ms,100KB*/
    
    #include<cstdio>
    
    char str[100005];
    
    int main()
    {
    	gets(str);
    	int i, j, res = 0;
    	for (i = 0; str[i]; i = j)
    	{
    		for (j = i + 1; str[j] == '0'; j++);
    		
    		///当出现以下情况时，重置计数：
    		///右边的数长，或者在长度相等时(这时右边的数必为x000...0的形式)，右边的数大
    		if (j - i > i || j - i == i && str[0] < str[i]) res = 1;
    		else res++;
    	}
    	printf("%d", res);
    	return 0;
    }
    

  

