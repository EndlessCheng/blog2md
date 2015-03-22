title: Codeforces Round #183 (Div. 1)  303A Lucky Permutation Triple (强大的数学&想法题)

date: 2014-03-15 12:35

tags: [ACM, C++, codeforces, 算法, 数学, ]

description: 

---
[ http://codeforces.com/problemset/problem/303/A ](http://codeforces.com/problemset/problem/303/A)

  * when n is odd, A[i] = B[i] = i 
  * when n is even, there is no solution. 
  * why? I  f  ![](http://espresso.codeforces.com/7a993ef5fb6c3995968a2b76f1df1b5257c6c2c6.png) , then  ![](http://espresso.codeforces.com/b9cadc7df5f9446fa5653dd49910ee1e03e025bd.png) or just  ![](http://espresso.codeforces.com/4fb1e17fc3e104447f5c6303697a8f55d2eecf0f.png) , where  S  = 0 + 1 + ... + _ n _ - 1 = _ n _ ( _ n _ - 1) / 2  . So, there must be  ![](http://espresso.codeforces.com/0b6bf89cc6e463947cec28752e0a5062dbc17a91.png) . But when  n  is even,  ![](http://espresso.codeforces.com/8bcfcfd002b6a18e8c5d7bb9203a92e657d3c091.png) . 
    
    
    /*92ms,0KB*/
    
    #include <iostream>
    using namespace std;
    
    int main()
    {
    	int n;
    	cin >> n;
    	if (n & 1) 
    	{
    		for (int i = 0; i < n; i++) cout << i << " ";
    		cout << endl;
    		for (int i = 0; i < n; i++) cout << i << " ";
    		cout << endl;
    		for (int i = 0; i < n; i++) cout << (2 * i) % n << " ";
    		cout << endl;
    	}
    	else cout << -1 << endl;
    	return 0;
    }
    

  


【额外思考】 

另一种构造方法如下，并且还满足了一个要求：   


当n为奇数时，若要求AB两个排列不一样，怎么做？ 

可以把A序列设为n-1,n-2,n-3,...,1,0（公差为-1） 

然后B序列设为0,2,4,...,1,3,5,...（公差为2） 

这样C序列就是n-1,0,1,2,...（公差为1） 
