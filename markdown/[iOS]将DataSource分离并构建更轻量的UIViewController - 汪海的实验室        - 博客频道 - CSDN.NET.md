#  [ [iOS]将DataSource分离并构建更轻量的UIViewController ](/pleasecallmewhy/article/details/38487385)

在objccn.io中看到一篇文章， [ 构建更轻量的View Controllers ](http://objccn.io/issue-1-1/) ，在此自己实践一下加深理解。 

  


  


新疆项目，learn--tableview，类前缀为LT，开始我们的实验。 

  


首先需要在StoryBoard中拖拽一个UITableView，在头文件中申明tableView变量并建立连接： 

![](http://img.blog.csdn.net/20140811094423545?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


  


  


新建ArrayDataSource类，作为TableView的DataSource。目的是将DataSource从原本的ViewController中分离出来： 
    
    
    //
    //  ArrayDataSource.h
    //  objc.io example project (issue #1)
    //
    
    #import <Foundation/Foundation.h>
    
    
    typedef void (^TableViewCellConfigureBlock)(id cell, id item);
    
    
    @interface ArrayDataSource : NSObject <UITableViewDataSource>
    
    - (id)initWithItems:(NSArray *)anItems
         cellIdentifier:(NSString *)aCellIdentifier
     configureCellBlock:(TableViewCellConfigureBlock)aConfigureCellBlock;
    
    - (id)itemAtIndexPath:(NSIndexPath *)indexPath;
    
    @end
    

  

    
    
    //
    //  ArrayDataSource.h
    //  objc.io example project (issue #1)
    //
    
    #import "ArrayDataSource.h"
    
    
    @interface ArrayDataSource ()
    
    @property (nonatomic, strong) NSArray *items;
    @property (nonatomic, copy) NSString *cellIdentifier;
    @property (nonatomic, copy) TableViewCellConfigureBlock configureCellBlock;
    
    @end
    
    
    @implementation ArrayDataSource
    
    - (id)init
    {
        return nil;
    }
    
    - (id)initWithItems:(NSArray *)anItems
         cellIdentifier:(NSString *)aCellIdentifier
     configureCellBlock:(TableViewCellConfigureBlock)aConfigureCellBlock
    {
        self = [super init];
        if (self) {
            self.items = anItems;
            self.cellIdentifier = aCellIdentifier;
            self.configureCellBlock = [aConfigureCellBlock copy];
        }
        return self;
    }
    
    - (id)itemAtIndexPath:(NSIndexPath *)indexPath
    {
        return self.items[(NSUInteger) indexPath.row];
    }
    
    
    #pragma mark UITableViewDataSource
    
    - (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
    {
        return self.items.count;
    }
    
    - (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
    {
        UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:self.cellIdentifier
                                                                forIndexPath:indexPath];
        id item = [self itemAtIndexPath:indexPath];
        self.configureCellBlock(cell, item);
        return cell;
    }
    
    @end
    

  
可以看得出来，这个DataSource的管理类接受三个变量进行初始化，分别是： 

1.anItems，存储表格数据的对象，是一个NSArray，里面存储封装好的对象，我们并不知道它是什么类型的，所以在使用的时候用id取出其中的元素。 

2.cellIdentifier，单元格的标示符，用来指定TableView使用的单元格，是单元格的唯一标识，在创建和设计Cell的时候可以指定。 

3.configureCellBlock，一个用来设置每个单元格的block，因为具体的item格式我们并不知道，所以我们也就不知道该如何初始化一个cell里面的数据，需要用block进行设置，因为这个block的目的是为了将item的数据应用到cell上，所以block接受两个参数，cell和item。 

  


接下来在添加一个LTMyCell类，作为自定义的单元格类。在xib中添加两个label用来显示数据： 

![](http://img.blog.csdn.net/20140811102303409?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


  


  


将xib中的两个label与.h头文件建立连接，连接后的头文件如下： 
    
    
    + (UINib *)nib;
    
    @property (weak, nonatomic) IBOutlet UILabel *photoTitleLabel;
    @property (weak, nonatomic) IBOutlet UILabel *photoDateLabel;
    

  
  


修改.m文件，实现相关方法如下： 
    
    
    + (UINib *)nib
    {
        return [UINib nibWithNibName:@"PhotoCell" bundle:nil];
    }
    
    - (void)setHighlighted:(BOOL)highlighted animated:(BOOL)animated
    {
        [super setHighlighted:highlighted animated:animated];
        if (highlighted) {
            self.photoTitleLabel.shadowColor = [UIColor darkGrayColor];
            self.photoTitleLabel.shadowOffset = CGSizeMake(3, 3);
        } else {
            self.photoTitleLabel.shadowColor = nil;
        }
    }
    

  
  


  


接着，新建LTPhoto的封装类，我们需要把用来展示的数据进行分装： 
    
    
    //
    //  LTPhoto.h
    //  learn-tableview
    //
    //  Created by why on 8/11/14.
    //  Copyright (c) 2014 why. All rights reserved.
    //
    
    #import <Foundation/Foundation.h>
    
    @interface LTPhoto : NSObject <NSCoding>
    
    @property (nonatomic, copy) NSString* name;
    @property (nonatomic, strong) NSDate* creationDate;
    
    @end
    
    
    
    //
    //  LTPhoto.m
    //  learn-tableview
    //
    //  Created by why on 8/11/14.
    //  Copyright (c) 2014 why. All rights reserved.
    //
    
    #import "LTPhoto.h"
    
    
    static NSString * const IdentifierKey = @"identifier";
    static NSString * const NameKey = @"name";
    static NSString * const CreationDateKey = @"creationDate";
    static NSString * const RatingKey = @"rating";
    
    
    @implementation LTPhoto
    
    
    - (void)encodeWithCoder:(NSCoder*)coder
    {
        [coder encodeObject:self.name forKey:NameKey];
        [coder encodeObject:self.creationDate forKey:CreationDateKey];
    }
    
    - (BOOL)requiresSecureCoding
    {
        return YES;
    }
    
    - (id)initWithCoder:(NSCoder*)coder
    {
        self = [super init];
        if (self) {
            self.name = [coder decodeObjectOfClass:[NSString class] forKey:NameKey];
            self.creationDate = [coder decodeObjectOfClass:[NSDate class] forKey:CreationDateKey];
        }
        return self;
    }
    
    @end
    
    

  
  


在写完了LTPhoto这个封装对象之后，我们可以对原来的MyCell进行Category扩展。新建一个Category： 

![](http://img.blog.csdn.net/20140811111758198?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  
具体代码如下： 
    
    
    #import "LTMyCell.h"
    
    @class LTPhoto;
    
    @interface LTMyCell (ConfigureForPhoto)
    - (void)configureForPhoto:(LTPhoto *)photo;
    
    @end
    
    
    //
    //  LTMyCell+ConfigureForPhoto.m
    //  learn-tableview
    //
    //  Created by why on 8/11/14.
    //  Copyright (c) 2014 why. All rights reserved.
    //
    
    #import "LTMyCell+ConfigureForPhoto.h"
    #import "LTPhoto.h"
    
    
    @implementation LTMyCell (ConfigureForPhoto)
    
    - (void)configureForPhoto:(LTPhoto *)photo
    {
        self.photoTitleLabel.text = photo.name;
        self.photoDateLabel.text = [self.dateFormatter stringFromDate:photo.creationDate];
    }
    
    - (NSDateFormatter *)dateFormatter
    {
        static NSDateFormatter *dateFormatter;
        if (!dateFormatter) {
            dateFormatter = [[NSDateFormatter alloc] init];
            dateFormatter.timeStyle = NSDateFormatterMediumStyle;
            dateFormatter.dateStyle = NSDateFormatterMediumStyle;
        }
        return dateFormatter;
    }
    
    @end
    

  
  


  


  


接下来就是在ViewController中指定TableView的DataSource。修改m文件代码如下： 

  

    
    
    //
    //  LTViewController.m
    //  learn-tableview
    //
    //  Created by why on 8/11/14.
    //  Copyright (c) 2014 why. All rights reserved.
    //
    
    #import "LTViewController.h"
    #import "ArrayDataSource.h"
    #import "LTMyCell.h"
    #import "LTMyCell+ConfigureForPhoto.h"
    #import "LTPhoto.h"
    
    
    static NSString * const PhotoCellIdentifier = @"LTMyCell";
    
    
    
    @interface LTViewController ()<UITableViewDelegate>
    
    @property (nonatomic, strong) ArrayDataSource *photosArrayDataSource;
    
    
    @end
    
    @implementation LTViewController
    
    - (void)viewDidLoad
    {
        [super viewDidLoad];
    	// Do any additional setup after loading the view, typically from a nib.
        [self setupTableView];
    
    }
    
    
    - (void)setupTableView
    {
        
        TableViewCellConfigureBlock configureCell = ^(LTMyCell *cell, LTPhoto *photo) {
            [cell configureForPhoto:photo];
        };
        
        NSMutableArray *photos = [[NSMutableArray alloc] init];
        for (int i = 0; i < 10; i++) {
            LTPhoto *photo = [[LTPhoto alloc] init];
            photo.name = @"Hello";
            photo.creationDate = [NSDate date];
            [photos addObject:photo];
        }
        
        self.photosArrayDataSource = [[ArrayDataSource alloc] initWithItems:photos
                                                             cellIdentifier:PhotoCellIdentifier
                                                         configureCellBlock:configureCell];
        
        _tableVIew.dataSource = self.photosArrayDataSource;
        
        [_tableVIew registerNib:[LTMyCell nib] forCellReuseIdentifier:PhotoCellIdentifier];
        
    }
    
    #pragma mark UITableViewDelegate
    
    - (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
    {
        NSLog(@"Click!");
    }
    
    
    
    
    - (void)didReceiveMemoryWarning
    {
        [super didReceiveMemoryWarning];
        // Dispose of any resources that can be recreated.
    }
    
    @end
    

  
这样就实现了基本的DataSource分离。 

  


项目源码地址： [ learn-tableview ](https://code.csdn.net/wxg694175346/learn-tableview/tree/master)

  


  


  


  


  


  


  


  


  


  


  


  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/38487385](http://blog.csdn.net/pleasecallmewhy/article/details/38487385)