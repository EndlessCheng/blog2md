title: 基于斐波那契数列给 MyPet 写了新的 exp.js

date: 2014-02-06 16:15:44

tags: [Minecraft, MyPet, Fibonacci, Algorithm, ]

description: 

---
今天开始陆续得到玩家的反馈表示 MyPet 技能树坏掉了.. 不过 Hexadecimal 这次提交的技能树多了好多种，而且设定最高等级100级，确实很难写…或者说.. 写完了估计会累死什么的…

所以更好的办法就是更改升级算法。MyPet 给出的 [exp.js](https://github.com/xXKeyleXx/MyPet/blob/master/experience-scripts/exp.js) 实在是让人看不懂，而且相当不好用。

如果说有比较方便的递增数列，那么数得上斐波那契数列了吧～于是用斐波那契数列写了一个 exp.js。算法是从别处抄来的，<del>反正是比递归快多了</del>

特意加了10 这样不会一开始的时候一下子升好几级。不过到20级之后升级就会相当困难了… 

文件 exp.js
    
    
    // fibo exp.js by phoenixlzx
    
    function calculate(exp) {
    
        var level = 0;
    
        var requiredExp = 0;
    
        var currentExp = 0;
    
        for (var i = 1; i < Math.floor(exp); i++) {
    
    	if (Math.floor(exp) <= fastfibo(i)) {
    
    		level = i;
    
    		requiredExp = fastfibo(level + 1);
    
    		currentExp = fastfibo(level);
    
    		break;
    
    	}
    
        }
    
        return new Array(level, requiredExp, currentExp);
    
    }
    
    function fastfibo(n) {
    
        var fibs = new Array();
    
        fibs.push(0);
    
        fibs.push(1);
    
        
    
        for(var i = 0; i <= n; i++) {
    
          fibs.push(fibs[0] + fibs[1]);
    
          fibs.shift();
    
        }
    
        
    
        return fibs[0] + 10;
    
    }
    
    //   |------------------|
    
    //   |  Return Methods  |
    
    //   |------------------|
    
    function getRequiredExp(exp, mypet) {
    
        return calculate(exp)[1];
    
    }
    
    function getLevel(exp, mypet) {
    
        return calculate(exp)[0];
    
    }
    
    function getCurrentExp(exp, mypet) {
    
        return calculate(exp)[2];
    
    }
    
    function getExpByLevel(level, mypet) {
    
        return fastfibo(level);
    
    }  
  
---  
  
坑人之处在于，如果不按照这个格式来写，就会直接报错，类似 `Cannot convert null to int` 之类的。另外真心觉得java写的东西都渣爆了… 还是java这个语言渣爆了…以至于我不敢写 `var fibs = [0, 1]` 这样的语句我怕 rhino 不识别。

不过我在管理组里发了这段js之后就被二小姐和静琴狠狠的鄙视了——原因，二小姐说：「你那程序会让CPU君愉快的死一死的喵～」

所以再来贴静琴的 exp.js
    
    
    // Copyright 2014 Jingqin Lynn
    
    // MyPet exp.js
    
    var phi = (1 + Math.sqrt(5)) / 2;
    
    var fib = function (n) {
    
      var tmp = (Math.pow(phi, n) - Math.pow(1 - phi, n));
    
      return Math.floor(tmp * Math.sqrt(1 / 5)) | 0;
    
    };
    
    var fibSum = function (n) {
    
      return fib(n + 2) - 1;
    
    };
    
    var fibPos = function (fn) {
    
      var tmp = (fn * Math.sqrt(5) + Math.sqrt(5 * fn * fn + 4)) / 2;
    
      return Math.floor(Math.log(tmp) / Math.log(phi)) | 0;
    
    };
    
    function getLevel(exp, mypet) {
    
      return fibPos(exp + 2) - 2;
    
    }
    
    function getRequiredExp(exp, mypet) {
    
      return getExpByLevel(getLevel(exp, mypet) + 1) - exp;
    
    }
    
    function getCurrentExp(exp, mypet) {
    
      return exp - getExpByLevel(getLevel(exp, mypet));
    
    }
    
    function getExpByLevel(level, mypet) {
    
      return fibSum(level) - 1;
    
    }  
  
---  
  
连一段exp.js都带 copyright 真是龘龘的作风啊。

咱真心不懂算法，从小学开始数学一直不及格，咋考上的大学也不知道。大学里教算法和数据结构的老师是学院里最水货老师之一，所以咱到现在也不知道所谓 O(n) 是个什么玩意儿。算法之类的书么怪咱自己笨，就是看不下去。也许咱根本就不适合做程序这条路吧。谁知道呢？我在这上面花费的时间已经太多了，多到我现在没有其他任何技能。否定了这一点，我真的就是废人一个了。

嘛。抱怨到此为止。咱活这么大了一直被鄙视什么的还不是怪咱脑子笨，又不用功… 后面怎么走，只好努力加油了呗。暂时还不想变成废人的说。
