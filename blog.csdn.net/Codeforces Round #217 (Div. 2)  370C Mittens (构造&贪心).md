title: Codeforces Round #217 (Div. 2)  370C Mittens (构造&贪心)

date: 2014-03-14 20:07

tags: [ACM, codeforces, C++, 算法, ]

description: 

---
[ http://codeforces.com/contest/370/problem/C ](http://codeforces.com/contest/370/problem/C)

  

    
    
    /*31ms,0KB*/
    
    #include<iostream>
    #include<algorithm>
    using namespace std;
    
    int C[5005];
    
    int main()
    {
    	int N, M;
    	cin >> N >> M;
    	for (int i = 0; i < N; i++) cin >> C[i];
    	sort(C, C + N);
    	int cnt = 0;
    	for (int i = 0; i < N; i++) cnt += (C[i] != C[(i + N / 2) % N]);
    	cout << cnt << endl;
    	for (int i = 0; i < N; i++) cout << C[i] << ' ' << C[(i + N / 2) % N] << endl;
    	return 0;
    }
    

  

