#  [ [iOS]通过UIScrollView和UIPageControl实现滑动切换的效果 ](/pleasecallmewhy/article/details/37807621)

UIPageControl是自带的控件，可以查看官方文档，下载官方示例学习。 

如果对Xcode自带的文档不熟悉可以参见： [ 苹果Xcode帮助文档阅读指南 ](http://ourcoders.com/thread/show/117/)

接下来是我学习笔记，使用Storyboard实现滑动切换的效果。 

  


\----------------------------------------------------------------------------- 

  


新建一个项目，拖上一个UIScrollView和UIPageControl，并且建立关联： 

![](http://img.blog.csdn.net/20140715091659218?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


新建一个ContentViewController，作为页面切换的内容视图： 

![](http://img.blog.csdn.net/20140715170948576?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


  


也就是说，当滑动屏幕切换的时候，其实就是多个ContentViewController在切换。 

  


基本结构是： 

![](http://img.blog.csdn.net/20140715163737250?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


在主页面，我们首先初始化一些设置： 
    
    
    - (void)viewDidLoad
    {
        [super viewDidLoad];
    	// Do any additional setup after loading the view, typically from a nib.
        
        // 初始化page control的内容
        _contentList = [NSArray arrayWithObjects:@"1",@"2",@"3",@"4", nil];
        
        
        // 一共有多少页
        NSUInteger numberPages = self.contentList.count;
        
        // 存储所有的controller
        NSMutableArray *controllers = [[NSMutableArray alloc] init];
        for (NSUInteger i = 0; i < numberPages; i++)
        {
    		[controllers addObject:[NSNull null]];
        }
        self.viewControllers = controllers;
        
        // 一个页面的宽度就是scrollview的宽度
        self.myScrollView.pagingEnabled = YES;  // 自动滚动到subview的边界
        self.myScrollView.contentSize =
        CGSizeMake(CGRectGetWidth(self.myScrollView.frame) * numberPages, CGRectGetHeight(self.myScrollView.frame));
        self.myScrollView.showsHorizontalScrollIndicator = NO;
        self.myScrollView.showsVerticalScrollIndicator = NO;
        self.myScrollView.scrollsToTop = NO;
        self.myScrollView.delegate = self;
        
        _numberOfPages = numberPages;
        _myPageControl.numberOfPages = numberPages;
        _currentPage = 0;
        
        
        [self loadScrollViewWithPage:0];
        [self loadScrollViewWithPage:1];
        
    }

  
  


  


  


  


  


接下来，我们需要一个函数，来加载ContentView页面上的元素： 
    
    
    // 加载ScrollView中的不同SubViewController
    - (void)loadScrollViewWithPage:(NSUInteger)page
    {
        if (page >= self.contentList.count)
            return;
        
        // replace the placeholder if necessary
        LContentViewController *controller = [self.viewControllers objectAtIndex:page];
        if ((NSNull *)controller == [NSNull null])
        {
            controller = [[LContentViewController alloc] init];
            [self.viewControllers replaceObjectAtIndex:page withObject:controller];
        }
        
        // add the controller's view to the scroll view
        if (controller.view.superview == nil)
        {
            CGRect frame = self.myScrollView.frame;
            frame.origin.x = CGRectGetWidth(frame) * page;
            frame.origin.y = 0;
            controller.view.frame = frame;
            [controller setLabel:[_contentList objectAtIndex:page]];
            [self.myScrollView addSubview:controller.view];
        }
    }
    

  
然后先来处理一下PageControl的切换事件： 
    
    
    - (void)gotoPage:(BOOL)animated
    {
        NSInteger page = self.myPageControl.currentPage;
        
        // load the visible page and the page on either side of it (to avoid flashes when the user starts scrolling)
        [self loadScrollViewWithPage:page - 1];
        [self loadScrollViewWithPage:page];
        [self loadScrollViewWithPage:page + 1];
        
    	// update the scroll view to the appropriate page
        CGRect bounds = self.myScrollView.bounds;
        bounds.origin.x = CGRectGetWidth(bounds) * page;
        bounds.origin.y = 0;
        [self.myScrollView scrollRectToVisible:bounds animated:animated];
    }
    
    // page control 选项修改监听
    - (IBAction)changePage:(id)sender
    {
        [self gotoPage:YES];    // YES = animate
    }

  
滑动ScrollView的事件监听： 
    
    
    // 滑动结束的事件监听
    - (void)scrollViewDidEndDecelerating:(UIScrollView *)scrollView
    {
        // switch the indicator when more than 50% of the previous/next page is visible
        CGFloat pageWidth = CGRectGetWidth(self.myScrollView.frame);
        NSUInteger page = floor((self.myScrollView.contentOffset.x - pageWidth / 2) / pageWidth) + 1;
        self.myPageControl.currentPage = page;
        NSLog(@"当前页面 = %d",page);
        // a possible optimization would be to unload the views+controllers which are no longer visible
        
        [self loadScrollViewWithPage:page - 1];
        [self loadScrollViewWithPage:page];
        [self loadScrollViewWithPage:page + 1];
    }
    

  
  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/37807621](http://blog.csdn.net/pleasecallmewhy/article/details/37807621)