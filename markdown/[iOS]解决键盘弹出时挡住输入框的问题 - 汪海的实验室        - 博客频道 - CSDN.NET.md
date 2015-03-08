#  [ [iOS]解决键盘弹出时挡住输入框的问题 ](/pleasecallmewhy/article/details/17467663)

[ ios ](http://www.csdn.net/tag/ios)

做ios的时候总会遇到这样打问题：用户点了文本输入框之后键盘遮挡住了原来输入的位置。 

为了解决这个问题，具体需要一下几步： 

  


1.给当前的UIViewController添加委托 
    
    
    @interface SignupViewController : UIViewController<UITextFieldDelegate>
    

  
2.在xib或storyboard里面将textfield的delegate与controller相连 

![]()   


3.在m文件里实现委托的方法 
    
    
    - (BOOL)textFieldShouldReturn:(UITextField *)textField 
    {        
        // When the user presses return, take focus away from the text field so that the keyboard is dismissed.        
        NSTimeInterval animationDuration = 0.30f;        
        [UIView beginAnimations:@"ResizeForKeyboard" context:nil];        
        [UIView setAnimationDuration:animationDuration];        
        CGRect rect = CGRectMake(0.0f, 0.0f, self.view.frame.size.width, self.view.frame.size.height);        
        self.view.frame = rect;        
        [UIView commitAnimations];        
        [textField resignFirstResponder];
        return YES;        
    }
    
    
    - (void)textFieldDidBeginEditing:(UITextField *)textField
    {        
            CGRect frame = textField.frame;
            int offset = frame.origin.y + frame.size.height - (self.view.frame.size.height - 216.0);//键盘高度216
            NSTimeInterval animationDuration = 0.30f;                
            [UIView beginAnimations:@"ResizeForKeyBoard" context:nil];                
            [UIView setAnimationDuration:animationDuration];
            float width = self.view.frame.size.width;                
            float height = self.view.frame.size.height;        
            if(offset > 0)
            {
                    CGRect rect = CGRectMake(0.0f, -offset,width,height);                
                    self.view.frame = rect;        
            }        
            [UIView commitAnimations];                
    }

  
  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/17467663](http://blog.csdn.net/pleasecallmewhy/article/details/17467663)