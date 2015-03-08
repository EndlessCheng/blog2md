#  [ [C++]四种方式求解最大子序列求和问题 ](/pleasecallmewhy/article/details/28641625)

#  问题 

给定整数:  A  1  ,  A  2  ,  …  ,  A  n  ，   
求  ∑  j  k  =  i  A  k  的最大值（为方便起见，如果所有的整数均为负数，则最大子序列和为0） 

#  例如 

对于输入：-2,11,-4,13,-5,-2，答案为20，即从  A  2  到  A  4 

#  分析 

这个问题之所以有意思，是因为存在很多求解它的算法。 

#  解法一：穷举遍历 

老老实实的穷举出所有的可能，代码如下： 
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    

| 
    
    
    //计算并返回所最大子序列的和：穷举遍历
    int maxSubSum1(const vector<int> & a)
    {
    	//用来存储最大子序列的和
    	int maxSum = 0;
    
    	//i标记子序列的头
    	for (int i = 0; i < a.size(); i++)
    	{
    		//j标记子序列的尾
    		for (int j = i; j < a.size(); j++)
    		{
    			//用来存储当前头尾计算的求和结果
    			int thisSum = 0;
    
    			//将子序列的值依次加入求和结果
    			for (int k = i; k <= j; k++)
    			{
    				thisSum += a[k];
    			}
    
    			//存储两者的最大值
    			if(thisSum > maxSum)
    				maxSum = thisSum;
    		}
    	}
    
    	return maxSum;
    }
      
  
---|---  
  
这是大多数人都会想到的方法：把所有的可能都列举出来，然后再把子序列的所有值都加起来求和。   
简单粗暴的解决了问题，而且还很好理解。   
这种算法的时间复杂度为  O  (  N  3  )  。 

#  解法二：穷举优化 

其实第三个for循环完全没有必要，在第二层for循环的时候就计算求得的和并且继续带入下一轮的for循环即可： 
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    

| 
    
    
    //计算并返回所最大子序列的和：穷举优化
    int maxSubSum2(const vector<int> & a)
    {
    	//用来存储最大子序列的和
    	int maxSum = 0;
    
    	//i标记子序列的头
    	for (int i = 0; i < a.size(); i++)
    	{
    		//用来存储当前头尾计算的求和结果
    		int thisSum = 0;
    
    		//j标记子序列的尾
    		for (int j = i; j < a.size(); j++)
    		{
    
    			//将子序列的值加入上次求和结果
    			thisSum += a[j];
    
    			//存储两者的最大值
    			if(thisSum > maxSum)
    				maxSum = thisSum;
    		}
    	}
    
    	return maxSum;
    }
      
  
---|---  
  
这种算法的时间复杂度为  O  (  N  2  )  。 

#  解法三：分而治之 

分而治之，顾名思义分为两个部分 

  * 分：把大问题分成大致相等的两个子问题，然后递归的进行求解。 
  * 治：把两个子问题的解合并到一起并再做少量的附加工作。 

在最大子序列和的问题里，最大子序列的和可能出现在三个地方： 

  * 整个出现在输入数据的左半部 
  * 整个输入数据的右半部 
  * 横跨左右两个部分 

对于前两种可以递归求解，对于第三种，可以把左右两个部分的和分别求出，然后加在一起。   
具体的代码如下： 
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    

| 
    
    
    //计算并返回所最大子序列的和：分而治之
    int maxSubSum3(const vector<int> & a,int left,int right)
    {
    	//基础情况：单个元素。直接返回这个数值或者0
    	if(left == right)
    	{
    		return a[left];
    	}
    
    	//获取中点
    	int center = (left + right) / 2;
    
    	/* 整个出现在输入数据的左半部的最大子序列求和 */
    	int leftMaxSum = maxSubSum3(a,left,center);
    
    	/* 整个出现在输入数据的右半部的最大子序列求和 */
    	int rightMaxSum = maxSubSum3(a,center+1,right);
    
    	//计算左右两个子序列求和结果的最大值
    	int lrMaxSum = max(leftMaxSum,rightMaxSum);
    
    
    	/* 横跨左右两个部分的最大子序列求和 */
    
    	//从center向左处理左半边
    	int maxLeftSum = 0;
    	int leftSum = 0;
    	for (int i = center; i >= left; i--)
    	{
    		leftSum += a[i];
    		maxLeftSum = max(maxLeftSum,leftSum);
    	}
    
    	//从center向右处理右半边
    	int maxRightSum = 0;
    	int rightSum = 0;
    	for (int j = center+1; j <= right; j++)
    	{
    		rightSum += a[j];
    		maxRightSum = max(maxRightSum,rightSum);
    	}
    
    	//返回求和和前面算出结果的最大值
    	return max( lrMaxSum, maxLeftSum+maxRightSum);
    }
      
  
---|---  
  
这种算法的时间复杂度为  O  (  N  l  o  g  N  )  。 

#  解法四：联机算法 

先来解释一下联机算法的概念： 

> ** 联机算法 ** ：在任意时刻，算法对要操作的数据只读入（扫描）一次，一旦被读入并处理，它就不需要在被记忆了。而在此处理过程中算法能对它已经读入的数据立即给出相应子序列问题的正确答案。具有这种特性的算法叫做联机算法（on-line algorithm）。 

对于这个问题，代码如下： 
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    

| 
    
    
    //计算并返回所最大子序列的和：最优算法
    int maxSubSum4(const vector<int> & a)
    {
    	//最终结果
    	int maxSum = 0;
    	//当前求和
    	int nowSum = 0;
    
    	//遍历序列的所有元素
    	for (int j = 0; j < a.size(); j++)
    	{
    		//将当前元素添加到结果中
    		nowSum += a[j];
    
    		//如果大于最大值，则存储为新的最大值
    		if(nowSum > maxSum)
    			maxSum = nowSum;
    		else if(nowSum < 0)
    			nowSum = 0;
    	}
    
    	return maxSum;
    }
      
  
---|---  
  
这种算法的时间复杂度为  O  (  N  )  。 

#  总结 

下表是统计的四种算法的运算结果： 

输入大小  |  O  (  N  3  )  |  O  (  N  2  )  |  O  (  N  l  o  g  N  )  |  O  (  N  )   
---|---|---|---|---  
N=10  |  0.000009  |  0.000004  |  0.000006  |  0.000003   
N=100  |  0.002580  |  0.000109  |  0.000045  |  0.000006   
N=1000  |  2.281013  |  0.010203  |  0.000485  |  0.000031   
N=10000  |  NA  |  1.2329  |  0.005712  |  0.000317   
N=100000  |  NA  |  135  |  0.064618  |  0.003206   
  
从表中可以看出，在数据量很小的时候（在它小时候=.=），算法在瞬间就完成了，差距也不是很明显。   
但是随着输入量的增大，一些算法的弊端逐渐显现出来，效率低的甚至在有限的时间里算不出结果来。   
对于很多高效的算法来说，读取数据往往是解决问题的瓶颈， 
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/28641625](http://blog.csdn.net/pleasecallmewhy/article/details/28641625)