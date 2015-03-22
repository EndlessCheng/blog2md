title: UVa 11178 Morley's Theorem (向量旋转)

date: 2014-03-27 16:35

tags: [ACM, C++, 算法, 计算几何, uva, ]

description: 

---
[ http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2119 ](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2119)

  

    
    
    /*0.025s*/
    
    #include<cstdio>
    #include<cmath>
    
    struct P
    {
    	double x, y;
    	P(double x = 0.0, double y = 0.0): x(x), y(y) {}
    	void read() {scanf("%lf%lf", &x, &y);}
    	void output() {printf("%f %f", x, y);}
    };
    typedef P Vector;
    
    Vector operator + (const Vector &A, const Vector &B) {return Vector(A.x + B.x, A.y + B.y);}
    Vector operator - (const P &A, const P &B) {return Vector(A.x - B.x, A.y - B.y);}
    Vector operator * (const Vector &A, double p) {return Vector(A.x * p, A.y * p);}
    Vector Rotate(const Vector &A, double rad) {return Vector(A.x * cos(rad) - A.y * sin(rad), A.x * sin(rad) + A.y * cos(rad));}
    inline double Dot(const Vector &A, const Vector &B) {return A.x * B.x + A.y * B.y;}
    inline double Cross(const Vector &A, const Vector &B) {return A.x * B.y - A.y * B.x;}
    inline double Length(const Vector &A) {return hypot(A.x, A.y);}
    inline double Angle(const Vector &A, const Vector &B) {return acos(Dot(A, B) / Length(A) / Length(B));}
    
    inline P GetLineIntersection(const P &p1, const Vector &s1, const P &p2, const Vector &s2)
    {
    	return p1 + s1 * (Cross(s2, p1 - p2) / Cross(s1, s2));
    }
    
    P getP(P A, P B, P C)
    {
    	Vector v1 = Rotate(C - B, Angle(A - B, C - B) / 3);
    	Vector v2 = Rotate(B - C, -Angle(A - C, B - C) / 3); /// 负数表示顺时针旋转
    	return GetLineIntersection(B, v1, C, v2);
    }
    
    int main()
    {
    	int T;
    	P A, B, C;
    	scanf("%d", &T);
    	while (T--)
    	{
    		A.read(), B.read(), C.read();
    		getP(A, B, C).output(), putchar(32);
    		getP(B, C, A).output(), putchar(32);
    		getP(C, A, B).output(), putchar(10);
    	}
    	return 0;
    }
    

  

