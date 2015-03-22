title: SGU 108 Self-numbers 2 (另一种滚动数组)

date: 2014-03-23 20:49

tags: [ACM, C++, sgu, 算法, 数学, ]

description: 

---
[ http://acm.sgu.ru/problem.php?contest=0&problem=108 ](http://acm.sgu.ru/problem.php?contest=0&problem=108)

  


我直接转的 [ http://www.cnblogs.com/staginner/archive/2011/12/24/2300689.html ](http://www.cnblogs.com/staginner/archive/2011/12/24/2300689.html)

他写得很好： 

这个题目可以直接筛出来结果，但要注意几个问题：①数组不够大，但由于推断的时候前后影响的区间并不大，因此我们可以把数组循环使用，对数组操作的时候多加一个取模运算即可。②空间不允许我们先把所有结果都处理出来，因此我们可以在筛的过程中，标记一下当前筛出的是第几个数，如果是需要输出的，再存到指定位置去即可，这样只要开出K的空间来就可以了。③由于si可能是无序的，而我们在筛的过程中只能顺序找到，而我们又不能每次都花O(K)的时间去看看当前是不是要输出的，所以需要预先按si的值排下序，为了能够方便查找、更改，我们不能直接对si排序，但可以对si的标号按si的大小进行排序，同时还要注意si有可能有相同大小的值。 

此外，取模运算的时候如果用位运算代替的话，会让效率高很多。 
    
    
    #include<cstdio>
    #include<cstring>
    #include<cstdlib>
    #define MAXD 100010
    #define MAXK 5010
    const int D = (1 << 16) - 1;
    
    int N, K, a[MAXK], r[MAXK];
    char d[MAXD];
    
    int cmp(const void *_p, const void *_q)
    {
    	int *p = (int *)_p;
    	int *q = (int *)_q;
    	return a[*p] - a[*q];
    }
    
    int get(int n)
    {
    	int res = n;
    	while (n)
    	{
    		res += n % 10;
    		n /= 10;
    	}
    	return res;
    }
    
    int main()
    {
    	scanf("%d%d", &N, &K);
    	int i, j, k, num, t;
    	for (i = 0; i < K; i ++)
    		scanf("%d", &a[i]);
    	a[K] = 0;
    	for (i = 0; i < K; i ++)
    		r[i] = i;
    	qsort(r, K, sizeof(r[0]), cmp);
    	r[K] = K;
    	memset(d, '\0', sizeof(d));
    	num = k = 0;
    	for (i = 1; i <= N; i ++)
    	{
    		if (!d[i & D])
    		{
    			++ num;
    			while (num == a[r[k]])
    				a[r[k ++]] = i;
    		}
    		t = get(i);
    		if (t <= N)
    			d[t & D] = '0';
    		d[i & D] = '\0';
    	}
    	printf("%d\n", num);
    	printf("%d", a[0]);
    	for (i = 1; i < K; i ++)
    		printf(" %d", a[i]);
    	printf("\n");
    	return 0;
    }
    

  

