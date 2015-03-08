#  [ [iOS] 使用UIRefreshControl 实现 UITableView下拉刷新（Swift版本） ](/pleasecallmewhy/article/details/39480631)

[ Swift ](http://www.csdn.net/tag/Swift) [ iOS ](http://www.csdn.net/tag/iOS)

首先，在viewDidLoad中初始化相关数据： 

  

    
    
      override func viewDidLoad() {
            super.viewDidLoad()
            // Do any additional setup after loading the view.
            
            //添加刷新
            refreshControl.addTarget(self, action: "refreshData", forControlEvents: UIControlEvents.ValueChanged)
            refreshControl.attributedTitle = NSAttributedString(string: "松手刷新新闻")
            newsTableView.addSubview(refreshControl)
            
        }
    

  
这样下拉刷新已经可以看到了： 

![](http://img.blog.csdn.net/20140922193708680?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


  


接下来把Selector 完善一下，添加refreshData方法： 
    
    
     // 刷新数据
        func refreshData() {
            let bquery = BmobQuery(className: "News")
            bquery.findObjectsInBackgroundWithBlock({array, error in
                self.dataArray = array
                self.newsTableView.reloadData()
                self.refreshControl.endRefreshing()
            })
        }

  
  


完整的代码如下，因为涉及到 BMOB API 的调用，所以有些代码可能看不懂，但是并不影响基本功能的使用。 
    
    
    //
    //  NewsViewController.swift
    //  WomenWorkerGuide
    //
    //  Created by why on 9/20/14.
    //  Copyright (c) 2014 why. All rights reserved.
    //
    
    import UIKit
    
    /**
    *  新闻
    */
    class NewsViewController: UIViewController,UITableViewDelegate,UITableViewDataSource {
    
        @IBOutlet weak var newsTableView: UITableView!
        
        var refreshControl = UIRefreshControl()
        
        var dataArray:[AnyObject] = [AnyObject]()
        
        override func viewDidLoad() {
            super.viewDidLoad()
            // Do any additional setup after loading the view.
            self.automaticallyAdjustsScrollViewInsets = false
            
            //添加刷新
            refreshControl.addTarget(self, action: "refreshData", forControlEvents: UIControlEvents.ValueChanged)
            refreshControl.attributedTitle = NSAttributedString(string: "松开后自动刷新")
            newsTableView.addSubview(refreshControl)
            refreshData()
        }
    
        override func didReceiveMemoryWarning() {
            super.didReceiveMemoryWarning()
            // Dispose of any resources that can be recreated.
        }
        
        // 刷新数据
        func refreshData() {
            let bquery = BmobQuery(className: "News")
            bquery.findObjectsInBackgroundWithBlock({array, error in
                self.dataArray = array
                self.newsTableView.reloadData()
                self.refreshControl.endRefreshing()
            })
        }
    
        // MARK: - UITableViewDataSource
        func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
            return dataArray.count;
        }
        
        func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
            
            let cell = UITableViewCell(style: UITableViewCellStyle.Subtitle, reuseIdentifier: "newsCell")
            
            let obj: BmobObject = dataArray[indexPath.row] as BmobObject
       
            cell.textLabel?.text = obj.objectForKey("title") as? String
           
            
            let dateFormatter = NSDateFormatter()
            dateFormatter.dateFormat = "yyyy年 MM月 dd日"
            let str = dateFormatter.stringFromDate(obj.createdAt)
            cell.detailTextLabel?.text = str
            return cell;
        }
        
        
        
        
        /*
        // MARK: - Navigation
    
        // In a storyboard-based application, you will often want to do a little preparation before navigation
        override func prepareForSegue(segue: UIStoryboardSegue!, sender: AnyObject!) {
            // Get the new view controller using segue.destinationViewController.
            // Pass the selected object to the new view controller.
        }
        */
    
    }
    

  
  


  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/39480631](http://blog.csdn.net/pleasecallmewhy/article/details/39480631)