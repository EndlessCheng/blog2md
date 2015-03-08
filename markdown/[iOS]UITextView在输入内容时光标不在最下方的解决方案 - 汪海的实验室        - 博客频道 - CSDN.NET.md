#  [ [iOS]UITextView在输入内容时光标不在最下方的解决方案 ](/pleasecallmewhy/article/details/43503143)

使用UITextView的时候经常出现光标不在最下方的情况。。。(iPhone6+iOS8) 

解决方法： 

首先去除所有的Padding： 
    
    
    _textView.textContainerInset = UIEdgeInsetsZero;
    _textView.textContainer.lineFragmentPadding = 0;
    

然后在委托方法里加上一行： 
    
    
    -(void)textViewDidChange:(UITextView *)textView {
        // 各种业务
        ...
        [self.textView scrollRangeToVisible:self.textView.selectedRange];
    }
    
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/43503143](http://blog.csdn.net/pleasecallmewhy/article/details/43503143)