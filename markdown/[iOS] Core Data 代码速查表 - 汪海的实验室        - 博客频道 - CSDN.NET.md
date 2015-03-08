#  [ [iOS] Core Data 代码速查表 ](/pleasecallmewhy/article/details/40584119)

[ CoreData ](http://www.csdn.net/tag/CoreData)

文中代码均来源于： [ http://www.appcoda.com/introduction-to-core-data/ ](http://www.appcoda.com/introduction-to-core-data/)

  


希望学习 Core Data 的同学不要错过：）以下是我个人记录的一些常用代码片段。 

有一个 Entity：Device，有三个属性：company、name、version。 

  


1.获取 context 的方法： 
    
    
    - (NSManagedObjectContext *)managedObjectContext {
        NSManagedObjectContext *context = nil;
        id delegate = [[UIApplication sharedApplication] delegate];
        if ([delegate performSelector:@selector(managedObjectContext)]) {
            context = [delegate managedObjectContext];
        }
        return context;
    }

  
2.增加一条数据： 
    
    
        NSManagedObjectContext *context = [self managedObjectContext];
        
        // Create a new managed object
        NSManagedObject *newDevice = [NSEntityDescription insertNewObjectForEntityForName:@"Device" inManagedObjectContext:context];
        [newDevice setValue:self.nameTextField.text forKey:@"name"];
        [newDevice setValue:self.versionTextField.text forKey:@"version"];
        [newDevice setValue:self.companyTextField.text forKey:@"company"];
        
        NSError *error = nil;
        // Save the object to persistent store
        if (![context save:&error]) {
            NSLog(@"Can't Save! %@ %@", error, [error localizedDescription]);
        }

  
3.删除一条数据： 
    
    
    NSManagedObjectContext *context = [self managedObjectContext];
    
    // Delete object from database
    [context deleteObject:[self.devices objectAtIndex:indexPath.row]];
    
    NSError *error = nil;
    if (![context save:&error]) {
        NSLog(@"Can't Delete! %@ %@", error, [error localizedDescription]);
        return;
    }
    

  
4.修改一条数据： 
    
    
    NSManagedObjectContext *context = [self managedObjectContext];
        
    // Update existing device
    [self.device setValue:self.nameTextField.text forKey:@"name"];
    [self.device setValue:self.versionTextField.text forKey:@"version"];
    [self.device setValue:self.companyTextField.text forKey:@"company"];
    
    
    NSError *error = nil;
    // Save the object to persistent store
    if (![context save:&error]) {
        NSLog(@"Can't Save! %@ %@", error, [error localizedDescription]);
    }

  
  


5\. 查询一堆数据： 
    
    
    // Fetch the devices from persistent data store
    NSManagedObjectContext *managedObjectContext = [self managedObjectContext];
    NSFetchRequest *fetchRequest = [[NSFetchRequest alloc] initWithEntityName:@"Device"];
    self.devices = [[managedObjectContext executeFetchRequest:fetchRequest error:nil] mutableCopy];
    

  
  


  


  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/40584119](http://blog.csdn.net/pleasecallmewhy/article/details/40584119)