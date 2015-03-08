#  [ [Cocos2d-x]Cocos2d-x 3.2 学习笔记 ](/pleasecallmewhy/article/details/34931021)

###  [ 获取屏幕大小 ](http://www.cocos2d-x.org/wiki/Coordinate_System) （Visible） 
    
    
    Size visibleSize = Director::getInstance()->getVisibleSize();
    Vec2 origin = Director::getInstance()->getVisibleOrigin();
    

###  [ 打印调试 ](http://www.cocos2d-x.org/wiki/How_to_use_CCLOG) （CCLOG） 
    
    
    CCLOG("Characters: %c %c", 'a', 65);
    CCLOG("Decimals: %d %ld", 1977, 650000L);
    CCLOG("Preceding with blanks: %10d", 1977);
    CCLOG("Preceding with zeros: %010d", 1977);
    CCLOG("Some different radixes: %d %x %o %#x %#o", 100, 100, 100, 100, 100);
    CCLOG("Floats: %4.2f %.0e %E", 3.1416, 3.1416, 3.1416);
    CCLOG("%s","A string");
    

###  [ 创建菜单 ](http://www.cocos2d-x.org/wiki/Menu_and_MenuItems) （Menu Item） 
    
    
    // 创建菜单
    auto menuItem = MenuItemImage::create( "MenuNormal.png",
                                           "MenuSelected.png",
                                           CC_CALLBACK_1(HelloWorld::menuCallback, this) );
    // 设置坐标
    menuItem->setPosition( Vec2(x,y) );
    // 创建菜单
    auto menu = Menu::create(menuItem, NULL);
    menu->setPosition(Vec2::ZERO);
    this->addChild(menu, 1);
    

###  [ 创建标签 ](http://www.cocos2d-x.org/wiki/Text_Labels) （Label） 
    
    
    auto label = LabelTTF::create("Hello World", "Arial", 24);
    label->setPosition(Vec2(x,y));
    this->addChild(label, 1);
    

###  [ 添加精灵 ](http://www.cocos2d-x.org/wiki/Sprite) （Sprite） 
    
    
    auto sprite = Sprite::create("Me.jpg");
    sprite->setPosition(Vec2(visibleSize.width / 2 , visibleSize.height / 2));
    sprite->setAnchorPoint(Vec2(0.5,0.5));
    this->addChild(sprite, 0);
    

###  [ 精灵动画 ](http://www.cocos2d-x.org/wiki/Actions) （Action） 
    
    
    auto  actionBy = MoveBy::create(1, Point(100,100));
    auto  easeAction = EaseIn::create(actionBy, 2.5f);
    sprite->runAction(Repeat::create(easeAction, 5));
    

###  [ 添加监听 ](http://www.cocos2d-x.org/wiki/EventDispatcher_Mechanism) （Listener） 
    
    
    auto listener1 = EventListenerTouchOneByOne::create();
    
    listener1->onTouchBegan = [](Touch* touch, Event* event){
        auto target = static_cast<Sprite*>(event->getCurrentTarget());
        Point locationInNode = target->convertToNodeSpace(touch->getLocation());
        Size s = target->getContentSize();
        Rect rect = Rect(0, 0, s.width, s.height);
                if (rect.containsPoint(locationInNode))
        {
            log("sprite began... x = %f, y = %f", locationInNode.x, locationInNode.y);
            target->setOpacity(180);
            return true;
        }
        return false;
    };
    
    listener1->onTouchMoved = [](Touch* touch, Event* event){
        auto target = static_cast<Sprite*>(event->getCurrentTarget());
        target->setPosition(target->getPosition() + touch->getDelta());
    };
    
    listener1->onTouchEnded = [=](Touch* touch, Event* event){
        auto target = static_cast<Sprite*>(event->getCurrentTarget());
        if (target == sprite)
        {
            log("Click on the sprite");
        }
    };
    
    _eventDispatcher->addEventListenerWithSceneGraphPriority(listener1, sprite);
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/34931021](http://blog.csdn.net/pleasecallmewhy/article/details/34931021)