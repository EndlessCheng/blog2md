#  [ [iOS]Objective-C基础回顾：继承和委托 ](/pleasecallmewhy/article/details/28649393)

#  背景 

大一的时候第一次接触iOS编程，当时的感觉就是：Xode真乃神兵利器也！ 时隔三载，今日故地重游，不妨就用Xcode造一把“神兵利器”：无敌大锤子，回顾一下iOS编程中常见的问题。 

#  基础 

再厉害的神兵利器，说到底也就是一把普通的武器。 我们可以抽象出所有武器共有的特性，作为神兵利器的父类。 首先我们先创建一个最简单的武器 ` Weapon ` 类。 
    
    
    //
    //  Weapon.h
    //  Weapon
    //
    //  Created by WHY on 14-3-21.
    //  Copyright (c) 2014年 WHY. All rights reserved.
    //
    
    #import <Foundation/Foundation.h>
    
    //宏定义
    #define DEFAULT_WEAPON_NAME     @""     //默认武器名称
    #define DEFAULT_WEAPON_PRODUCER @""     //默认武器名称
    #define DEFAULT_WEAPON_LONG     1.0     //默认武器名称
    #define DEFAULT_WEAPON_WEIGHT   10.0    //默认武器名称
    
    //枚举类
    typedef enum WeaponQuality{
        kPoorQuality = 1,   //品质差
        kNormalQuality,     //品质一般
        kGoodQuality,       //品质好
    }weaponQualityType;
    
    @interface Weapon : NSObject
    {
        NSString            *_strName;          //武器名字
        NSString            *_strProducer;      //武器制作人
        NSDate              *_dateBirth;        //武器制作时间
        weaponQualityType    _quality;          //武器品质
        float               _fLong;              //武器长度
        float               _fWeight;            //武器重量
    
    }
    
    //打造武器
    -(id)initWithName:(NSString*)aWeaponName
         producerName:(NSString*)aProducerName
      producerAbility:(int)abilityValue;
    
    //攻击
    -(void)attack;
    
    //武器的攻击力
    -(int)attackValue;
    
    @end
    
    
    
    
    //
    //  weapon.m
    //  Weapon
    //
    //  Created by WHY on 14-3-21.
    //  Copyright (c) 2014年 WHY. All rights reserved.
    //
    
    #import "Weapon.h"
    
    @implementation Weapon
    
    //打造武器
    -(id)initWithName:(NSString *)aWeaponName
         producerName:(NSString *)aProducerName
      producerAbility:(int)abilityValue{
        self = [super init];
        if(self){
            //武器名字赋值
            if(aWeaponName){
                _strName = [[NSString alloc] initWithString:aWeaponName];
            }else{
                _strName = DEFAULT_WEAPON_NAME;
            }
    
            //武器制作人赋值
            if(aProducerName){
                _strProducer = [[NSString alloc] initWithString:aProducerName];
            }else{
                _strProducer = DEFAULT_WEAPON_PRODUCER;
            }
    
            //当前时间
            _dateBirth = [NSDate date];
    
            //根据制作人的实力决定武器的品质
            if (abilityValue <= 60) {
                _quality = kPoorQuality;
            } else if (abilityValue <= 80) {
                _quality = kNormalQuality;
            } else {
                _quality = kGoodQuality;
            }
    
            //默认武器的属性
            _fLong = DEFAULT_WEAPON_LONG;
            _fWeight = DEFAULT_WEAPON_WEIGHT;
        }
    
        return self;
    }
    
    //攻击
    -(void)attack{
        NSLog(@"%@制造的武器%@造成%d点伤害",_strProducer,_strName,[self attackValue]);
    }
    
    //武器的攻击力
    -(int)attackValue{
        //根据品质决定攻击力
        switch (_quality) {
            case kPoorQuality:
                return 50;
                break;
            case kNormalQuality:
                return 80;
                break;
            case kGoodQuality:
                return 120;
                break;
            default:
                return 20;
                break;
        }
    }
    
    @end
    

调用的方法很简单，import头文件之后使用如下代码初始化并调用 ` attack ` 方法： 
    
    
    Weapon *oneWeapon = [[Weapon alloc] initWithName:@"菜刀" producerName:@"汪海" producerAbility:100];
    [oneWeapon attack];
    

输出如下内容： 
    
    
    汪海制造的武器菜刀造成120点伤害
    

#  继承和重写 

接下来我们需要进一步细化神兵利器的细节。 从Xcode的标志来看，这把神兵利器应该是个锤子，所以我们新建 ` Weapon ` 类的子类 ` Hammer ` ，没错就是个锤子： 
    
    
    //
    //  Hammer.h
    //  Weapon
    //
    //  Created by WHY on 14-3-22.
    //  Copyright (c) 2014年 WHY. All rights reserved.
    //
    
    #import <Foundation/Foundation.h>
    
    #import "Weapon.h"
    
    @interface Hammer : Weapon{
    
        UIColor *_colorHead;        //锤子的榔头的颜色
        NSString *_materialHead;    //锤子的榔头的材质
    
        UIColor *_colorBody;        //锤子的把手的颜色
        NSString *_materialBody;    //锤子的把手的材质
    
    }
    
    //初始化锤子的属性
    -(void)initHammerAttr;
    
    @end
    
    
    
    
    //
    //  Hammer.m
    //  Weapon
    //
    //  Created by WHY on 14-3-22.
    //  Copyright (c) 2014年 WHY. All rights reserved.
    //
    
    #import "Hammer.h"
    
    @implementation Hammer
    
    //重写父类的初始化方法
    -(id)initWithName:(NSString *)aWeaponName
         producerName:(NSString *)aProducerName
      producerAbility:(int)abilityValue{
    
        self = [super initWithName:aWeaponName
                      producerName:aProducerName
                   producerAbility:abilityValue];
    
        [self initHammerAttr];
    
        return self;
    }
    
    //初始化锤子的属性
    -(void)initHammerAttr{
        //对于锤子属性的初始化
        _colorHead = [UIColor lightGrayColor];
        _materialHead = @"铁";
        _colorBody = [UIColor lightGrayColor];
        _materialBody = @"木头";
    
        _fLong = 0.5f;
        _fWeight = 20.0f;
    }
    
    
    //重写锤子的攻击力
    -(int)attackValue{
        //根据品质决定攻击力
        switch (_quality) {
            case kPoorQuality:
                return 500;
                break;
            case kNormalQuality:
                return 800;
                break;
            case kGoodQuality:
                return 1200;
                break;
            default:
                return 200;
                break;
        }
    }
    
    @end
    

至此，一把简单的神兵利器：大锤子，就算造好啦。 

#  分类和扩展 

我们现在光有了锤子，但是还没有被锤子攻击的对象。   
我们可以扩展现有的类，比如NSObject类，给它加上receiveAttack的方法。 新建NSObject+Enemy扩展类，头文件代码如下： 
    
    
    //
    //  NSObject+Enemy.h
    //  Weapon
    //
    //  Created by WHY on 14-3-22.
    //  Copyright (c) 2014年 WHY. All rights reserved.
    //
    
    #import <Foundation/Foundation.h>
    
    @interface NSObject (Enemy)
    
    //接受伤害的处理接口
    -(void)receiveAttack:(int)attackValue;
    
    @end
    
    
    //
    //  NSObject+Enemy.m
    //  Weapon
    //
    //  Created by WHY on 14-3-22.
    //  Copyright (c) 2014年 WHY. All rights reserved.
    //
    
    #import "NSObject+Enemy.h"
    
    @implementation NSObject (Enemy)
    
    -(void)receiveAttack:(int)attackValue{
        NSLog(@"我收到了%d点伤害！", attackValue);
    }
    
    @end
    

这样我们就实现了NSObject类的扩展。 接下来我们修改一下Weapon文件的 ` attack ` 方法，给它加上一些参数： 
    
    
    //攻击
    -(void)attack:(id)hitTarget{
        NSLog(@"%@制造的武器%@造成%d点伤害",_strProducer,_strName,[self attackValue]);
        [hitTarget receiveAttack:[self attackValue]];
    }
    

当然，在调用的时候别忘了给它传个 ` NSObject ` 的参数。 OK，运行一下看下结果，非常Nice： 
    
    
    汪海制造的武器菜刀造成120点伤害
    我收到了120点伤害！
#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/28649393](http://blog.csdn.net/pleasecallmewhy/article/details/28649393)