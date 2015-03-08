##  [ 汪海的实验室 ](http://blog.csdn.net/pleasecallmewhy)

###  一名普通小程序员的学习笔记。 博客地址：http://blog.callmewhy.com

  * [ ![](http://static.blog.csdn.net/images/ico_list.gif) 目录视图  ](http://blog.csdn.net/pleasecallmewhy?viewmode=contents)
  * [ ![](http://static.blog.csdn.net/images/ico_summary.gif) 摘要视图  ](http://blog.csdn.net/pleasecallmewhy?viewmode=list)
  * [ ![](http://static.blog.csdn.net/images/ico_rss.gif) 订阅  ](http://blog.csdn.net/pleasecallmewhy/rss/list)

[ CSDN学院讲师招募，诚邀您加入！  ](http://blog.csdn.net/csdnedu/article/details/43306129)
[ 博客Markdown编辑器上线啦
](http://blog.csdn.net/csdnproduct/article/details/43561659) [
那些年我们追过的Wrox精品红皮计算机图书
](http://blog.csdn.net/blogdevteam/article/details/42918959) [ PMBOK第五版精讲视频教程
](http://edu.csdn.net/lecturer/lecturer_detail?lecturer_id=95) [ 火星人敏捷开发1001问
](http://edu.csdn.net/course/detail/443)

#  [ [C++]C++11 语法记录: Lambda简单入门 ](/pleasecallmewhy/article/details/34941721)

分类： [ C++ ](/wxg694175346/article/category/1303968) 2014-06-26 22:02  585人阅读
评论  (0)  [ 收藏 ](javascript:void\(0\);) 举报

一、Lambda表达式

C++ 11中的Lambda表达式用于定义并创建匿名的函数对象，以简化编程工作。Lambda的语法形式如下：  
[函数对象参数] (操作符重载函数参数) mutable或exception声明 ->返回值类型 {函数体}  
可以看到，Lambda主要分为五个部分：[函数对象参数]、(操作符重载函数参数)、mutable或exception声明、->返回值类型、{函数体}。下面分
别进行介绍。  
一、[函数对象参数]，标识一个Lambda的开始，这部分必须存在，不能省略。函数对象参数是传递给编译器自动生成的函数对象类的构造函数的。函数对象参数只能使用
那些到定义Lambda为止时Lambda所在作用范围内可见的局部变量（包括Lambda所在类的this）。函数对象参数有以下形式：  
1、空。没有使用任何函数对象参数。  
2、=。函数体内可以使用Lambda所在作用范围内所有可见的局部变量（包括Lambda所在类的this），并且是  值传递
方式（相当于编译器自动为我们按值传递了所有局部变量）。  
3、&。函数体内可以使用Lambda所在作用范围内所有可见的局部变量（包括Lambda所在类的this），并且是  引用传递
方式（相当于编译器自动为我们按引用传递了所有局部变量）。  
4、this。函数体内可以使用Lambda所在类中的成员变量。  
5、a。将a按值进行传递。按值进行传递时，函数体内不能修改传递进来的a的拷贝，因为默认情况下函数是const的。要修改传递进来的a的拷贝，可以添加mutab
le修饰符。  
6、&a。将a按引用进行传递。  
7、a, &b。将a按值进行传递，b按引用进行传递。  
8、=，&a, &b。除a和b按引用进行传递外，其他参数都按值进行传递。  
9、&, a, b。除a和b按值进行传递外，其他参数都按引用进行传递。  
二、(操作符重载函数参数)，标识重载的()操作符的参数，没有参数时，这部分可以省略。参数可以通过按值（如：(a,b)）和按引用（如：(&a,&b)）两种方式
进行传递。  
三、mutable或exception声明，这部分可以省略。按值传递函数对象参数时，加上mutable修饰符后，可以修改按值传递进来的拷贝（注意是能修改拷贝
，而不是值本身）。exception声明用于指定函数抛出的异常，如抛出整数类型的异常，可以使用throw(int)。  
四、->返回值类型，标识函数返回值的类型，当返回值为void，或者函数体中只有一处return的地方（此时编译器可以自动推断出返回值类型）时，这部分可以省略
。  
五、{函数体}，标识函数的实现，这部分不能省略，但函数体可以为空。  

下面给出一个例子：

** [cpp] ** [ view plain ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ copy ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ ![在CODE上查看代码片](https://code.csdn.net/assets/CODE_ico.png) ](https://code.csdn.net/snippets/164677) [ ![派生到我的代码片](https://code.csdn.net/assets/ico_fork.svg) ](https://code.csdn.net/snippets/164677/fork)

  1. class  CTest 
  2. { 
  3. public  : 
  4. CTest() : m_nData(20) { NULL; } 
  5. void  TestLambda() 
  6. { 
  7. vector< int  > vctTemp; 
  8. vctTemp.push_back(1); 
  9. vctTemp.push_back(2); 
  10.   11. // 无函数对象参数，输出：1 2 
  12. { 
  13. for_each(vctTemp.begin(), vctTemp.end(), [](  int  v){ cout << v << endl; }); 
  14. } 
  15.   16. // 以值方式传递作用域内所有可见的局部变量（包括this），输出：11 12 
  17. { 
  18. int  a = 10; 
  19. for_each(vctTemp.begin(), vctTemp.end(), [=](  int  v){ cout << v+a << endl; }); 
  20. } 
  21.   22. // 以引用方式传递作用域内所有可见的局部变量（包括this），输出：11 13 12 
  23. { 
  24. int  a = 10; 
  25. for_each(vctTemp.begin(), vctTemp.end(), [&](  int  v)  mutable  { cout << v+a << endl; a++; }); 
  26. cout << a << endl; 
  27. } 
  28.   29. // 以值方式传递局部变量a，输出：11 13 10 
  30. { 
  31. int  a = 10; 
  32. //注意：在lambda表达式中的 a 只是一个拷贝，添加mutable之后，可以修改a的值，但只是修改拷贝的a 
  33. for_each(vctTemp.begin(), vctTemp.end(), [a](  int  v)  mutable  { cout << v+a << endl; a++; }); 
  34. cout << a << endl; 
  35. } 
  36.   37. // 以引用方式传递局部变量a，输出：11 13 12 
  38. { 
  39. int  a = 10; 
  40. for_each(vctTemp.begin(), vctTemp.end(), [&a](  int  v){ cout << v+a << endl; a++; }); 
  41. cout << a << endl; 
  42. } 
  43.   44. // 传递this，输出：21 22 
  45. { 
  46. for_each(vctTemp.begin(), vctTemp.end(), [  this  ](  int  v){ cout << v+m_nData << endl; }); 
  47. } 
  48.   49. // 除b按引用传递外，其他均按值传递，输出：11 12 17 
  50. { 
  51. int  a = 10; 
  52. int  b = 15; 
  53. for_each(vctTemp.begin(), vctTemp.end(), [=, &b](  int  v){ cout << v+a << endl; b++; }); 
  54. cout << b << endl; 
  55. } 
  56.   57. // 操作符重载函数参数按值传递，输出：1 2 
  58. { 
  59. for_each(vctTemp.begin(), vctTemp.end(), [](  int  v){ cout << v << endl; }); 
  60. } 
  61.   62. // 操作符重载函数参数按引用传递，输出：2 3 
  63. { 
  64. for_each(vctTemp.begin(), vctTemp.end(), [](  int  &v){ v++; cout<<v<<endl;}); 
  65. } 
  66.   67.   68. // 空的Lambda表达式 
  69. { 
  70. [](){}(); 
  71. []{}(); 
  72. } 
  73. } 
  74.   75. private  : 
  76. int  m_nData; 
  77. }; 

  
  

二、auto 关键字

C++ 11中引入的auto主要有两种用途：自动类型推断和返回值占位。  

auto自动类型推断，用于从初始化表达式中推断出变量的数据类型。通过auto的自动类型推断，可以大大简化我们的编程工作。下面是一些使用auto的例子。

** [cpp] ** [ view plain ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ copy ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ ![在CODE上查看代码片](https://code.csdn.net/assets/CODE_ico.png) ](https://code.csdn.net/snippets/164677) [ ![派生到我的代码片](https://code.csdn.net/assets/ico_fork.svg) ](https://code.csdn.net/snippets/164677/fork)

  1. auto a;  // 错误，没有初始化表达式，无法推断出a的类型 
  2. auto  int  a = 10  // 错误，auto临时变量的语义在C++ 11中已不存在 
  3. auto a = 10 
  4. auto c =  'A' 
  5. auto s(  "hello"  ); 
  6. vector< int  > vctTemp; 
  7. auto it = vctTemp.begin(); 
  8. auto ptr = [](){ cout << "hello world"  << endl; }; 

使用auto经常意味着较少的代码量（除非你需要的类型是int这种只有一个单词的）。当你想要遍历STL容器中元素的时候，想一想你会怎么写迭代器代码，老式的方法
是用很多typedef来做，而auto则会大大简化这个过程。  

** [cpp] ** [ view plain ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ copy ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ ![在CODE上查看代码片](https://code.csdn.net/assets/CODE_ico.png) ](https://code.csdn.net/snippets/164677) [ ![派生到我的代码片](https://code.csdn.net/assets/ico_fork.svg) ](https://code.csdn.net/snippets/164677/fork)

  1. std::map<std::string, std::vector< int  >> map; 
  2. for  (auto it = begin(map); it != end(map); ++it) 
  3. { 
  4. } 

另外，在使用模板技术时，如果某个变量的类型依赖于模板参数，不使用auto将很难确定变量的类型（使用auto后，将由编译器自动进行确定）。

下面是一个具体的例子。

** [cpp] ** [ view plain ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ copy ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ ![在CODE上查看代码片](https://code.csdn.net/assets/CODE_ico.png) ](https://code.csdn.net/snippets/164677) [ ![派生到我的代码片](https://code.csdn.net/assets/ico_fork.svg) ](https://code.csdn.net/snippets/164677/fork)

  1. template  < class  T,  class  U>
  2. void  Multiply(T t, U u) 
  3. { 
  4. auto v = t*u; 
  5. } 

auto返回值占位，主要与  decltype  配合使用，用于返回值类型后置时的占位。

** [cpp] ** [ view plain ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ copy ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ ![在CODE上查看代码片](https://code.csdn.net/assets/CODE_ico.png) ](https://code.csdn.net/snippets/164677) [ ![派生到我的代码片](https://code.csdn.net/assets/ico_fork.svg) ](https://code.csdn.net/snippets/164677/fork)

  1. template  < typename  T1,  typename  T2>
  2. auto compose(T1 t1, T2 t2) -> decltype(t1 + t2) 
  3. { 
  4. return  t1+t2; 
  5. } 
  6. auto v = compose(2, 3.14);  // v's type is double 

你应该注意到，auto并不能作为函数的返回类型，但是你能用auto去代替函数的返回类型，当然，在这种情况下，函数必须有返回值才可以。auto不会告诉编译器去
推断返回值的实际类型，它会通知编译器在函数的末段去寻找返回值类型。在上面的那个例子中，函数返回值的构成是由T1类型和T2类型的值，经过+操作符之后决定的。

  

自动化推导decltype

关于 ` decltype  ` 是一个操作符，其可以评估括号内表达式的类型，其规则如下：

  1. 如果表达式e是一个变量，那么就是这个变量的类型。 
  2. 如果表达式e是一个函数，那么就是这个函数返回值的类型。 
  3. 如果不符合1和2，如果e是左值，类型为T，那么decltype(e)是T&；如果是右值，则是T。 

原文给出的示例如下，我们可以看到，这个让的确我们的定义变量省了很多事。

  

** [cpp] ** [ view plain ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ copy ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ ![在CODE上查看代码片](https://code.csdn.net/assets/CODE_ico.png) ](https://code.csdn.net/snippets/164677) [ ![派生到我的代码片](https://code.csdn.net/assets/ico_fork.svg) ](https://code.csdn.net/snippets/164677/fork)

  1. const  vector< int  > vi; 
  2. typedef  decltype (vi.begin()) CIT; 
  3. CIT another_const_iterator; 

还有一个适合的用法是用来typedef函数指针，也会省很多事。比如：

** [cpp] ** [ view plain ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ copy ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ ![在CODE上查看代码片](https://code.csdn.net/assets/CODE_ico.png) ](https://code.csdn.net/snippets/164677) [ ![派生到我的代码片](https://code.csdn.net/assets/ico_fork.svg) ](https://code.csdn.net/snippets/164677/fork)

  1. decltype(&myfunc) pfunc = 0; 
  2. typedef  decltype(&A::func1) type; 

  

三、std::function

类模版  std::  function  是一种通用、多态的函数封装。  std::function  的实例可以对任何可以调用的  目标
进行存储、复制、和调用操作，这些目标包括函数、  lambda  表达式、绑定表达式、以及其它函数对象等。

用法示例：

①保存自由函数

** [cpp] ** [ view plain ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ copy ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ ![在CODE上查看代码片](https://code.csdn.net/assets/CODE_ico.png) ](https://code.csdn.net/snippets/164677) [ ![派生到我的代码片](https://code.csdn.net/assets/ico_fork.svg) ](https://code.csdn.net/snippets/164677/fork)

  1. void  printA(  int  a) 
  2. { 
  3. cout<<a<<endl; 
  4. } 
  5.   6. std::function< void  (  int  a)> func; 
  7. func = printA; 
  8. func(2); 

运行输出： 2

②保存lambda表达式  

** [cpp] ** [ view plain ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ copy ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ ![在CODE上查看代码片](https://code.csdn.net/assets/CODE_ico.png) ](https://code.csdn.net/snippets/164677) [ ![派生到我的代码片](https://code.csdn.net/assets/ico_fork.svg) ](https://code.csdn.net/snippets/164677/fork)

  1. std::function< void  ()> func_1 = [](){cout<< "hello world"  <<endl;}; 
  2. func_1(); 

运行输出：hello world

③保存成员函数

** [cpp] ** [ view plain ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ copy ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ ![在CODE上查看代码片](https://code.csdn.net/assets/CODE_ico.png) ](https://code.csdn.net/snippets/164677) [ ![派生到我的代码片](https://code.csdn.net/assets/ico_fork.svg) ](https://code.csdn.net/snippets/164677/fork)

  1. struct  Foo { 
  2. Foo(  int  num) : num_(num) {} 
  3. void  print_add(  int  i)  const  { cout << num_+i << '\n'  ; } 
  4. int  num_; 
  5. }; 
  6.   7. // 保存成员函数 
  8. std::function< void  (  const  Foo&,  int  )> f_add_display = &Foo::print_add; 
  9. Foo foo(2); 
  10. f_add_display(foo, 1); 

运行输出： 3

  

四、bind

bind是一组用于函数绑定的模板。在对某个函数进行绑定时，可以指定部分参数或全部参数，也可以不指定任何参数，还可以调整各个参数间的顺序。对于未指定的参数，可
以使用占位符_1、_2、_3来表示。_1表示绑定后的函数的第1个参数，_2表示绑定后的函数的第2个参数，其他依次类推。  

下面通过程序例子了解一下用法：

** [cpp] ** [ view plain ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ copy ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ ![在CODE上查看代码片](https://code.csdn.net/assets/CODE_ico.png) ](https://code.csdn.net/snippets/164677) [ ![派生到我的代码片](https://code.csdn.net/assets/ico_fork.svg) ](https://code.csdn.net/snippets/164677/fork)

  1. #include <iostream>
  2. using  namespace  std; 
  3. class  A 
  4. { 
  5. public  : 
  6. void  fun_3(  int  k,  int  m) 
  7. { 
  8. cout<<k<< " "  <<m<<endl; 
  9. } 
  10. }; 
  11.   12. void  fun(  int  x,  int  y,  int  z) 
  13. { 
  14. cout<<x<< "  "  <<y<< "  "  <<z<<endl; 
  15. } 
  16.   17. void  fun_2(  int  &a,  int  &b) 
  18. { 
  19. a++; 
  20. b++; 
  21. cout<<a<< "  "  <<b<<endl; 
  22. } 
  23.   24. int  main(  int  argc,  const  char  * argv[]) 
  25. { 
  26. auto f1 = bind(fun,1,2,3);  //表示绑定函数 fun 的第一，二，三个参数值为： 1 2 3 
  27. f1();  //print:1  2  3 
  28.   29. auto f2 = bind(fun, placeholders::_1,placeholders::_2,3); 
  30. //表示绑定函数 fun 的第三个参数为 3，而fun 的第一，二个参数分别有调用 f2 的第一，二个参数指定 
  31. f2(1,2);  //print:1  2  3 
  32.   33. auto f3 = bind(fun,placeholders::_2,placeholders::_1,3); 
  34. //表示绑定函数 fun 的第三个参数为 3，而fun 的第一，二个参数分别有调用 f3 的第二，一个参数指定 
  35. //注意： f2  和  f3 的区别。 
  36. f3(1,2);  //print:2  1  3 
  37.   38.   39. int  n = 2; 
  40. int  m = 3; 
  41.   42. auto f4 = bind(fun_2, n,placeholders::_1); 
  43. f4(m);  //print:3  4 
  44.   45. cout<<m<<endl;  //print:4  说明：bind对于不事先绑定的参数，通过std::placeholders传递的参数是通过引用传递的 
  46. cout<<n<<endl;  //print:2  说明：bind对于预先绑定的函数参数是通过值传递的 
  47.   48.   49. A a; 
  50. auto f5 = bind(&A::fun_3, a,placeholders::_1,placeholders::_2); 
  51. f5(10,20);  //print:10 20 
  52.   53. std::function< void  (  int  ,  int  )> fc = std::bind(&A::fun_3, a,std::placeholders::_1,std::placeholders::_2); 
  54. fc(10,20);  //print:10 20 
  55.   56. return  0; 
  57. } 

  

五、nullptr -- ** 空指针标识 **

空指针标识(nullptr)（其本质是一个内定的常量）是一个表示空指针的标识，它不是一个整数。（译注：这里应该与我们常用的NULL宏相区别，虽然它们都是用来
表示空置针，但NULL只是一个定义为常整数0的宏，而nullptr是C++0x的一个关键字，一个内建的标识符。下面我们还将看到nullptr与NULL之间更
多的区别。）  
char* p = nullptr;  
int* q = nullptr;  
char* p2 = 0;           //这里0的赋值还是有效的，并且p=p2  
  
void f(int);  
void f(char*);  
  
f(0);         //调用f(int)  
f(nullptr);   //调用f(char*)  
  
void g(int);  
g(nullptr);       //错误：nullptr并不是一个整型常量  
int i = nullptr;  //错误：nullptr并不是一个整型常量  
（译注：实际上，我们这里可以看到nullptr和NULL两者本质的差别，NULL是一个整型数0，而nullptr可以看成是一个空指针。）

  

六、final 和 override

两者都是用在对于继承体系的控制。

##  final

** 用来标明被这个修饰符修饰的class/struct和虚函数已经是最终版本，无法被进一步继承.  **

** [html] ** [ view plain ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ copy ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ ![在CODE上查看代码片](https://code.csdn.net/assets/CODE_ico.png) ](https://code.csdn.net/snippets/164677) [ ![派生到我的代码片](https://code.csdn.net/assets/ico_fork.svg) ](https://code.csdn.net/snippets/164677/fork)

  1. class Base final 
  2. { 
  3. public: 
  4. virtual void test(){} 
  5. }; 
  6.   7. class D1:public Base 
  8. { 
  9. void test(){} 
  10. }; 

  

如这个例子，Base类被final修饰，表示其已经无法被继承，编译器会提示如下错误：error C3246: ‘D1′ : cannot inherit
from ‘Base’ as it has been declared as ‘final’

再看另外一个例子:

** [cpp] ** [ view plain ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ copy ](http://blog.csdn.net/crayondeng/article/details/18563121#) [ ![在CODE上查看代码片](https://code.csdn.net/assets/CODE_ico.png) ](https://code.csdn.net/snippets/164677) [ ![派生到我的代码片](https://code.csdn.net/assets/ico_fork.svg) ](https://code.csdn.net/snippets/164677/fork)

  1. class  Base 
  2. { 
  3. public  : 
  4. virtual  void  test(){} 
  5. }; 
  6. 

