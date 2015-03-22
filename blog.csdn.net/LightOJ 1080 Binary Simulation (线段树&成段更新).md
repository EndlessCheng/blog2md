title: LightOJ 1080 Binary Simulation (线段树&成段更新)

date: 2014-03-24 08:18

tags: [ACM, C++, lightoj, 算法, 线段树, ]

description: 

---
[ http://lightoj.com/volume_showproblem.php?problem=1080 ](http://lightoj.com/volume_showproblem.php?problem=1080)

  


模板。 
    
    
    /*0.484s,4312KB*/
    
    #include <cstdio>
    #include <cstring>
    #include <algorithm>
    using namespace std;
    #define lson l , m , rt << 1
    #define rson m + 1 , r , rt << 1 | 1
    #define root 1, N, 1
    #define LL int
    const int mx = 100000;
    
    LL sum[mx << 2], add[mx << 2];
    char s[mx + 5];
    int i;
    
    inline void pushup(int rt)
    {
    	sum[rt] = sum[rt << 1] + sum[rt << 1 | 1];
    }
    
    inline void pushdown(int rt, int m)
    {
    	if (add[rt])
    	{
    		add[rt << 1] += add[rt];
    		add[rt << 1 | 1] += add[rt];///更新左右子区间add
    		sum[rt << 1] += add[rt] * (m - (m >> 1));
    		sum[rt << 1 | 1] += add[rt] * (m >> 1);///平分父节点add，更新左右子区间和
    		add[rt] = 0;///父节点add清零
    	}
    }
    
    void build(int l, int r, int rt)
    {
    	add[rt] = 0;
    	if (l == r)
    	{
    		sum[rt] = s[i++] & 15;
    		return;
    	}
    	int m = (l + r) >> 1;
    	build(lson);
    	build(rson);
    	pushup(rt);
    }
    
    void update(int ql, int qr, int c, int l, int r, int rt)
    {
    	if (ql <= l && r <= qr)
    	{
    		add[rt] += c;///存至此，不再往下更新
    		sum[rt] += (LL)c * (r - l + 1);
    		return;
    	}
    	pushdown(rt , r - l + 1);///用父节点add往下细分计算
    	int m = (l + r) >> 1;
    	if (ql <= m) update(ql, qr, c, lson);
    	if (qr > m) update(ql, qr, c, rson);
    	pushup(rt);
    }
    
    LL query(int ql, int qr, int l, int r, int rt)
    {
    	if (ql <= l && r <= qr)
    	{
    		return sum[rt];
    	}
    	pushdown(rt , r - l + 1);///用父节点add往下细分计算
    	int m = (l + r) >> 1;
    	LL ret = 0;
    	if (ql <= m) ret += query(ql, qr, lson);
    	if (qr > m) ret += query(ql, qr, rson);
    	return ret;
    }
    
    int main()
    {
    	int t, N, m, ql, qr, pos;
    	scanf("%d", &t);
    	for (int cas = 1; cas <= t; ++cas)
    	{
    		printf("Case %d:\n", cas);
    		getchar();
    		gets(s + 1);
    		N = strlen(s + 1);
    		i = 1;
    		build(root);
    		scanf("%d", &m);
    		while (m--)
    		{
    			getchar();
    			if (getchar() == 'I')
    			{
    				scanf("%d%d", &ql, &qr);
    				update(ql, qr, 1, root);
    			}
    			else
    			{
    				scanf("%d", &pos);
    				puts(query(pos, pos, root) & 1 ? "1" : "0");
    			}
    		}
    	}
    	return 0;
    }
    

  

