title: LightOJ 1203 Guarding Bananas (凸包最小顶角)

date: 2014-03-26 17:52:00

tags: [ACM, C++, lightoj, 计算几何, 凸包, ]

description: 

---
<http://lightoj.com/volume_showproblem.php?problem=1203>

  

    
    
    /*0.164s,6512KB*/
    
    #include<bits/stdc++.h>
    using namespace std;
    #define sqr(x) ((x)*(x))
    const double INF = 1e100;
    const double pi = acos(-1.0);
    const double eps = 1e-9;
    
    struct POINT
    {
    	double x, y;
    } temp[100000 + 7], ch[100000 + 7], s[100000 + 7];
    
    double dist(POINT a, POINT b)
    {
    	return sqrt(sqr(a.x - b.x) + sqr(a.y - b.y));
    }
    
    double findArea(POINT o, POINT a, POINT b)
    {
    	return (a.x - o.x) * (b.y - o.y) - (b.x - o.x) * (a.y - o.y);
    }
    
    bool cmp_position(POINT a, POINT b)
    {
    	return a.y < b.y || (a.y == b.y && a.x < b.x);
    }
    
    double findAngle(POINT a, POINT b, POINT c)
    {
    	double A = sqrt(sqr(b.x - c.x) + sqr(b.y - c.y));
    	double B = sqrt(sqr(a.x - c.x) + sqr(a.y - c.y));
    	double C = sqrt(sqr(a.x - b.x) + sqr(a.y - b.y));
    	if (2 * A * C == 0) return INF;
    	double ang = acos((A * A + C * C - B * B) / (2 * A * C));
    	return (ang * 180) / pi;
    }
    
    bool cmp_angle(POINT a, POINT b)
    {
    	double temp = findArea(ch[0], a, b);
    	if (!temp) return (dist(a, ch[0]) + eps < dist(b, ch[0]));
    	else return temp > -eps;
    }
    
    void print(POINT a[], int N)
    {
    	double MIN = INF;
    	for (int i = 0; i < N - 2; i++) MIN = min(MIN, findAngle(a[i], a[i + 1], a[i + 2]));
    	MIN = min(MIN, findAngle(a[N - 2], a[N - 1], a[0]));
    	MIN = min(MIN, findAngle(a[N - 1], a[0], a[1]));
    	if (MIN == INF) MIN = 0;
    	printf("%.7f\n", MIN + eps);
    }
    
    int main()
    {
    	int P, cs = 0;
    	scanf("%d", &P);
    	while (P--)
    	{
    		int N;
    		scanf("%d", &N);
    		for (int i = 0; i < N; i++) scanf("%lf%lf", &temp[i].x, &temp[i].y);
    		printf("Case %d: ", ++cs);
    		if (N < 3) { printf("0\n"); continue; }
    		sort(temp, temp + N, cmp_position);
    		ch[0] = temp[0];
    		int K = N;
    		N = 1;
    		for (int i = 1; i < K; i++)
    		{
    			if (temp[i].x == temp[i - 1].x && temp[i].y == temp[i - 1].y) continue;
    			ch[N++] = temp[i];
    		}
    		sort(ch + 1, ch + N, cmp_angle);
    		ch[N] = ch[0];
    		int top = 2;
    		s[0] = ch[0];
    		s[1] = ch[1];
    		for (int i = 2; i <= N; i++)
    		{
    			double A;
    			while (top >= 2 && (A = findArea(s[top - 2], s[top - 1], ch[i])) < 0) top--;
    			s[top++] = ch[i];
    		}
    		top--;
    		print(s, top);
    	}
    	return 0;
    }
    

  

