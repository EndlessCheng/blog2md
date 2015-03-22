title: HDU 4741 Save Labman No.004 (异面直线距离&直线与平面的交点)

date: 2014-03-16 19:20

tags: [C++, ACM, 算法, HDU, 计算几何, ]

description: 

---
[ http://acm.hdu.edu.cn/showproblem.php?pid=4741 ](http://acm.hdu.edu.cn/showproblem.php?pid=4741)

  


模板题。 

理论知识见代码注释。 

<del> 这题背景居然是命运石之门。。 </del>
    
    
    /*218ms,276KB*/
    
    #include<cstdio>
    #include<cmath>
    const double eps = 1e-9;
    
    struct P3
    {
    	double x, y, z;
    	P3(double x = 0.0, double y = 0.0, double z = 0.0): x(x), y(y), z(z) {}
    	void read()
    	{
    		scanf("%lf%lf%lf", &x, &y, &z);
    	}
    	void output()
    	{
    		printf("%f %f %f", x, y, z);
    	}
    	P3 operator + (P3 p)
    	{
    		return P3(x + p.x, y + p.y, z + p.z);
    	}
    	P3 operator - (P3 p)
    	{
    		return P3(x - p.x, y - p.y, z - p.z);
    	}
    	double dot(P3 p)
    	{
    		return x * p.x + y * p.y + z * p.z;
    	}
    	P3 det(P3 p)
    	{
    		return P3(y * p.z - z * p.y, z * p.x - x * p.z, x * p.y - y * p.x);
    	}
    	double length() ///向量的模
    	{
    		return sqrt(x * x + y * y + z * z);
    	}
    };
    
    struct L3
    {
    	P3 a, b;
    	L3() {}
    	L3(P3 a, P3 b): a(a), b(b) {}
    	void read()
    	{
    		a.read(), b.read();
    	}
    };
    
    struct plane
    {
    	P3 a, b, c;
    	plane() {}
    	plane(P3 a, P3 b, P3 c): a(a), b(b), c(c) {}
    	P3 normal_vector() ///法向量(ab x ac)
    	{
    		return (b - a).det(c - a);
    	}
    };
    
    ///空间两点距离
    inline double TwoPointsDistance(P3 &p1, P3 &p2)
    {
    	return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y) + (p1.z - p2.z) * (p1.z - p2.z));
    }
    
    ///空间直线距离，等价于UaVa在公垂线上的投影
    ///参见 http://219.218.160.73:8000/jxjh/kc/fla/jhlw/gn/7.pdf 图1
    inline double LineToLine(L3 u, L3 v, P3 &cross)
    {
    	cross = (u.b - u.a).det(v.b - v.a);
    	return fabs((u.a - v.a).dot(cross)) / cross.length(); ///UaVa在公垂线上的投影
    }
    
    ///空间线面交点
    ///解法参见 http://blog.csdn.net/abcjennifer/article/details/6688080
    inline P3 Intersection(L3 l, plane s)
    {
    	P3 ret = s.normal_vector();
    	double t = (ret.x * (s.a.x - l.a.x) + ret.y * (s.a.y - l.a.y) + ret.z * (s.a.z - l.a.z)) / (ret.x * (l.b.x - l.a.x) + ret.y * (l.b.y - l.a.y) + ret.z * (l.b.z - l.a.z));
    	ret.x = l.a.x + (l.b.x - l.a.x) * t;
    	ret.y = l.a.y + (l.b.y - l.a.y) * t;
    	ret.z = l.a.z + (l.b.z - l.a.z) * t; ///将t带入直线参数方程
    	return ret;
    }
    
    /************以上模板*************/
    
    void solve(L3 l1, L3 l2)
    {
    	P3 s; ///两直线公垂线的方向向量
    	printf("%f\n", LineToLine(l1, l2, s));
    	Intersection(l1, plane(l2.a, l2.b, l2.a + s)).output();///构造直线与公垂线所构成的平面
    	putchar(32);
    	Intersection(l2, plane(l1.a, l1.b, l1.a + s)).output();
    	putchar(10);
    }
    
    int main()
    {
    	int T;
    	L3 l1, l2;
    	scanf("%d", &T);
    	while (T--)
    	{
    		l1.read(), l2.read();
    		solve(l1, l2);
    	}
    	return 0;
    }
    

  


附题： [ UVa 10794 The Deadly Olympic Returns!!!  ](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1735)
