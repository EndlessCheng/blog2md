title: re.compile() 函数的一个小改进

date: 2015-03-19T13:35:00.000Z

tags: [Python, 正则表达式, ]

description: Python 中的 re.compile() 函数可以「格式化」复杂的正则表达式，从而方便理解。但是像 literal 48 这句话，还需要我们自己转换一下 ASCII 对应的字符。不妨自己 DIY 一下源码。

---
Python 中的 ` re.compile() ` 函数可以「格式化」复杂的正则表达式，从而方便理解。 

比如执行 ` re.compile(r"0\d{2}-\d{8}|0\d{3}-\d{7}", re.DEBUG) ` 后得到： 
    
    
    literal 48
    
    branch
    
      max_repeat 2 2
    
        in
    
          category category_digit
    
      literal 45
    
      max_repeat 8 8
    
        in
    
          category category_digit
    
    or
    
      max_repeat 3 3
    
        in
    
          category category_digit
    
      literal 45
    
      max_repeat 7 7
    
        in
    
          category category_digit  
  
---  
  
但是像 ` literal 48 ` 这句话，还需要我们自己转换一下 ASCII 对应的字符。不妨自己 DIY 一下源码。 

将 ` Lib/sre_parse.py ` 的 ` SubPattern ` 类中的 ` dump() ` 函数末尾的 ` print av, ; nl = 0 ` 修改成 
    
    
    print av,
    
    if op == "literal" or op == "not_literal":
    
        print "(%s)" % repr(chr(av)),
    
    nl = 0  
  
---  
  
就可以显示 ASCII 码对应的字符。（10 会以 ` \n ` 打印出来） 
