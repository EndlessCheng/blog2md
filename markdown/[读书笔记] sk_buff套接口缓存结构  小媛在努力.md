#  [读书笔记] sk_buff套接口缓存结构 

_ _ [ zxy_snow ](http://www.xysay.com/author/zxy_snow) _ _ [ Linux ](http://www.xysay.com/category/linux%e5%ad%a6%e4%b9%a0) , [ 学习笔记 ](http://www.xysay.com/category/%e5%ad%a6%e4%b9%a0%e7%ac%94%e8%ae%b0) _ _ 围观 _ 183 _ 次  _ _ [ 5 条评论 ](http://www.xysay.com/sk-buff-struct.html#comments) _ _ 编辑日期：  2014-10-11  _ _ 字体： [ 大 ](javascript:;) [ 中 ](javascript:;) [ 小 ](javascript:;)

《Linux 内核源码剖析- TCP/IP 实现》这书很好啊，根据网络部分的源码讲解的，觉得记录下来笔记可能会更有帮助些，文中图片均来自此书。 

此书用的是2.6.20的内核，我在看的同时对比了3.14.17的内核源码，所以内容有变动，都是基于3.14.17内核源码。 

##  sk_buffer    


include/linux/skbuff.h 

net/core/skbuff.c 

套接口缓存，主要用途是保存在进程和网络接口之间相互传递的用户数据以及其他的一些信息。 

SKB  在不同网络协议层之间传递，传的过程中某些成员变量会发生改变。 

假如  A  选项会生成  B  宏，而某些程序有  #ifdef B  这条语句，则  A  选项是不能被编译成内核模块的。因为若某些选项所控制的数据结构是固定的而不是动态变化的。 

在一个  SKB  结点前面会插入一个辅助的  sk_buff_head  的头结点，方便查找。就类似普通双链表的头结点。 

struct sk_buff_head { /* These two members must be first. */ struct sk_buff *next; struct sk_buff *prev; __u32 qlen; //SKB链表中的结点数 spinlock_t lock; //用来控制对SKB链表并发操作的自旋锁 }; 

1 

2 

3 

4 

5 

6 

7 

8 

| 

struct  sk_buff_head  { 

/* These two members must be first. */ 

struct  sk_buff  *  next  ; 

struct  sk_buff  *  prev  ; 

__u32  qlen  ;  //SKB链表中的结点数 

spinlock_t  lock  ;  //用来控制对SKB链表并发操作的自旋锁 

}  ;   
  
---|---  
  
即如下图： 

![](https://farm3.staticflickr.com/2949/15297292750_b54da1cf75_z.jpg)

sk_buff结构，将成员变量的含义说明了一下，来自Linux-3.14.17源码。 

struct sk_buff { /* These two members must be first. */ struct sk_buff *next; struct sk_buff *prev; ktime_t tstamp; //接收时间戳或者发送时间戳 struct sock *sk; //sk是SKB的宿主传输控制块，在由本地发出或者本地接收时才有效，使传输控制块与套接口及用户应用程序相关。 struct net_device *dev; //网络设备指针，指向收到数据包的设备（接收包）或者输出数据包的设备（发送包） /* * This is the control buffer. It is free to use for every * layer. Please put your private variables there. If you * want to keep them across layers you have to do a skb_clone() * first. This is owned by whoever has the skb queued ATM. */ char cb[48] __aligned(8); //SKB信息控制块，是每层协议的私有信息存储空间，由每一层协议自己维护并使用，并只在本层有效。 unsigned long _skb_refdst; //目的地 #ifdef CONFIG_XFRM struct sec_path *sp; //IPSec协议用来跟踪传输的信息 #endif unsigned int len, //SKB中数据部分长度，包括现行缓存区中的数据长度，data_len以及协议首部长度 data_len; //SG类型和FRAGLIST类型聚合分散I/O存储区中的数据长度 __u16 mac_len, //链路层报头的长度。 hdr_len; //克隆skb时可写报头的长度 union { //校验 __wsum csum; struct { __u16 csum_start; __u16 csum_offset; }; }; __u32 priority; //数据包队列的优先级 kmemcheck_bitfield_begin(flags1); __u8 local_df:1, //表示该SKB在本地允许分片 cloned:1, //标记所属SKB是否已经克隆 ip_summed:2, //标记传输层校验和的状态 nohdr:1, //标记payload是否被单独饮用 nfctinfo:3; //skb与连接的信息关系 __u8 pkt_type:3, //帧类型，是由二层目的地址决定的 fclone:2, //当前克隆状态 ipvs_property:1, //SKB是否属于虚拟服务器 peeked:1, //包已经被抓到了，不需要再次抓取了 nf_trace:1; //netfilter数据包跟踪标识 kmemcheck_bitfield_end(flags1); __be16 protocol; //上层协议，典型的包括IP，IPv6，ARP void (*destructor)(struct sk_buff *skb); //类似析构函数 #if defined( ) || defined(CONFIG_NF_CONNTRACK_MODULE) struct nf_conntrack *nfct; //相关联的连接（如果有的话） #endif #ifdef CONFIG_BRIDGE_NETFILTER struct nf_bridge_info *nf_bridge; //关于桥接帧保存的数据 #endif int skb_iif; //目的地网络设备的接口索引 __u32 rxhash; //包的哈希值 __be16 vlan_proto; //虚拟局域网封装协议 __u16 vlan_tci; //虚拟局域网标签控制信息 #ifdef CONFIG_NET_SCHED __u16 tc_index; /* traffic control index */ //用于输入流量控制 #ifdef CONFIG_NET_CLS_ACT __u16 tc_verd; /* traffic control verdict */ //用于输入流量控制 #endif #endif __u16 queue_mapping; //多设备的队列映射 kmemcheck_bitfield_begin(flags2); #ifdef CONFIG_IPV6_NDISC_NODETYPE __u8 ndisc_nodetype:2; //路由的类型（从链路层开始） #endif __u8 pfmemalloc:1; __u8 ooo_okay:1; //允许socket的映射队列改变 __u8 l4_rxhash:1; //说明rxhash是个四元组的哈希值 __u8 wifi_acked_valid:1; //设置wifi_acked __u8 wifi_acked:1; //wifi的帧是否ack __u8 no_fcs:1; //帧校验序列 __u8 head_frag:1; /* Encapsulation protocol and NIC drivers should use * this flag to indicate to each other if the skb contains * encapsulated packet or not and maybe use the inner packet * headers if needed */ __u8 encapsulation:1; /* 6/8 bit hole (depending on ndisc_nodetype presence) */ kmemcheck_bitfield_end(flags2); #if defined CONFIG_NET_DMA || defined CONFIG_NET_RX_BUSY_POLL union { unsigned int napi_id; //这个SKB的NAPI的ID dma_cookie_t dma_cookie; //DMA操作的一个cookie }; #endif #ifdef CONFIG_NETWORK_SECMARK __u32 secmark; //安全标识 #endif union { __u32 mark; //通用分组标记 __u32 dropcount; //sk_receive_queue溢出的数量 __u32 reserved_tailroom; // }; __be16 inner_protocol; //封装的协议 __u16 inner_transport_header; //封装的内部传输报头 __u16 inner_network_header; //封装的网络层报头 __u16 inner_mac_header; //封装的链路层报头 __u16 transport_header; //传输层报头 __u16 network_header; //网络层报头 __u16 mac_header; //链路层报头 /* These elements must be at the end, see alloc_skb() for details. */ sk_buff_data_t tail; sk_buff_data_t end; unsigned char *head, *data; //这四个用来指向线性数据缓存区及数据部分的边界 unsigned int truesize; //整个数据缓存区的总长度 atomic_t users; //引用计数，用来标识有多少实体引用了该SKB }; 

1 

2 

3 

4 

5 

6 

7 

8 

9 

10 

11 

12 

13 

14 

15 

16 

17 

18 

19 

20 

21 

22 

23 

24 

25 

26 

27 

28 

29 

30 

31 

32 

33 

34 

35 

36 

37 

38 

39 

40 

41 

42 

43 

44 

45 

46 

47 

48 

49 

50 

51 

52 

53 

54 

55 

56 

57 

58 

59 

60 

61 

62 

63 

64 

65 

66 

67 

68 

69 

70 

71 

72 

73 

74 

75 

76 

77 

78 

79 

80 

81 

82 

83 

84 

85 

86 

87 

88 

89 

90 

91 

92 

93 

94 

95 

96 

97 

98 

99 

100 

101 

102 

103 

104 

105 

106 

107 

108 

109 

110 

111 

112 

113 

114 

115 

116 

117 

118 

119 

120 

121 

122 

| 

struct  sk_buff  { 

/* These two members must be first. */ 

struct  sk_buff  *  next  ; 

struct  sk_buff  *  prev  ; 

ktime_t  tstamp  ;  //接收时间戳或者发送时间戳 

struct  sock  *  sk  ;  //sk是SKB的宿主传输控制块，在由本地发出或者本地接收时才有效，使传输控制块与套接口及用户应用程序相关。 

struct  net_device  *  dev  ;  //网络设备指针，指向收到数据包的设备（接收包）或者输出数据包的设备（发送包） 

/* 

* This is the control buffer. It is free to use for every 

* layer. Please put your private variables there. If you 

* want to keep them across layers you have to do a skb_clone() 

* first. This is owned by whoever has the skb queued ATM. 

*/ 

char  cb  [  48  ]  __aligned  (  8  )  ;  //SKB信息控制块，是每层协议的私有信息存储空间，由每一层协议自己维护并使用，并只在本层有效。 

unsigned  long  _skb_refdst  ;  //目的地 

#ifdef CONFIG_XFRM 

struct  sec_path  *  sp  ;  //IPSec协议用来跟踪传输的信息 

#endif 

unsigned  int  len  ,  //SKB中数据部分长度，包括现行缓存区中的数据长度，data_len以及协议首部长度 

data_len  ;  //SG类型和FRAGLIST类型聚合分散I/O存储区中的数据长度 

__u16  mac_len  ,  //链路层报头的长度。 

hdr_len  ;  //克隆skb时可写报头的长度 

union  {  //校验 

__wsum  csum  ; 

struct  { 

__u16  csum_start  ; 

__u16  csum_offset  ; 

}  ; 

}  ; 

__u32  priority  ;  //数据包队列的优先级 

kmemcheck_bitfield_begin  (  flags1  )  ; 

__u8  local_df  :  1  ,  //表示该SKB在本地允许分片 

cloned  :  1  ,  //标记所属SKB是否已经克隆 

ip_summed  :  2  ,  //标记传输层校验和的状态 

nohdr  :  1  ,  //标记payload是否被单独饮用 

nfctinfo  :  3  ;  //skb与连接的信息关系 

__u8  pkt_type  :  3  ,  //帧类型，是由二层目的地址决定的 

fclone  :  2  ,  //当前克隆状态 

ipvs_property  :  1  ,  //SKB是否属于虚拟服务器 

peeked  :  1  ,  //包已经被抓到了，不需要再次抓取了 

nf_trace  :  1  ;  //netfilter数据包跟踪标识 

kmemcheck_bitfield_end  (  flags1  )  ; 

__be16  protocol  ;  //上层协议，典型的包括IP，IPv6，ARP 

void  (  *  destructor  )  (  struct  sk_buff  *  skb  )  ;  //类似析构函数 

#if defined( ) || defined(CONFIG_NF_CONNTRACK_MODULE) 

struct  nf_conntrack  *  nfct  ;  //相关联的连接（如果有的话） 

#endif 

#ifdef CONFIG_BRIDGE_NETFILTER 

struct  nf_bridge_info  *  nf_bridge  ;  //关于桥接帧保存的数据 

#endif 

int  skb_iif  ;  //目的地网络设备的接口索引 

__u32  rxhash  ;  //包的哈希值 

__be16  vlan_proto  ;  //虚拟局域网封装协议 

__u16  vlan_tci  ;  //虚拟局域网标签控制信息 

#ifdef CONFIG_NET_SCHED 

__u16  tc_index  ;  /* traffic control index */  //用于输入流量控制 

#ifdef CONFIG_NET_CLS_ACT 

__u16  tc_verd  ;  /* traffic control verdict */  //用于输入流量控制 

#endif 

#endif 

__u16  queue_mapping  ;  //多设备的队列映射 

kmemcheck_bitfield_begin  (  flags2  )  ; 

#ifdef CONFIG_IPV6_NDISC_NODETYPE 

__u8  ndisc_nodetype  :  2  ;  //路由的类型（从链路层开始） 

#endif 

__u8  pfmemalloc  :  1  ; 

__u8  ooo_okay  :  1  ;  //允许socket的映射队列改变 

__u8  l4_rxhash  :  1  ;  //说明rxhash是个四元组的哈希值 

__u8  wifi_acked_valid  :  1  ;  //设置wifi_acked 

__u8  wifi_acked  :  1  ;  //wifi的帧是否ack 

__u8  no_fcs  :  1  ;  //帧校验序列 

__u8  head_frag  :  1  ; 

/* Encapsulation protocol and NIC drivers should use 

* this flag to indicate to each other if the skb contains 

* encapsulated packet or not and maybe use the inner packet 

* headers if needed 

*/ 

__u8  encapsulation  :  1  ; 

/* 6/8 bit hole (depending on ndisc_nodetype presence) */ 

kmemcheck_bitfield_end  (  flags2  )  ; 

#if defined CONFIG_NET_DMA || defined CONFIG_NET_RX_BUSY_POLL 

union  { 

unsigned  int  napi_id  ;  //这个SKB的NAPI的ID 

dma_cookie_t  dma_cookie  ;  //DMA操作的一个cookie 

}  ; 

#endif 

#ifdef CONFIG_NETWORK_SECMARK 

__u32  secmark  ;  //安全标识 

#endif 

union  { 

__u32  mark  ;  //通用分组标记 

__u32  dropcount  ;  //sk_receive_queue溢出的数量 

__u32  reserved_tailroom  ;  // 

}  ; 

__be16  inner_protocol  ;  //封装的协议 

__u16  inner_transport_header  ;  //封装的内部传输报头 

__u16  inner_network_header  ;  //封装的网络层报头 

__u16  inner_mac_header  ;  //封装的链路层报头 

__u16  transport_header  ;  //传输层报头 

__u16  network_header  ;  //网络层报头 

__u16  mac_header  ;  //链路层报头 

/* These elements must be at the end, see alloc_skb() for details.  */ 

sk_buff_data_t  tail  ; 

sk_buff_data_t  end  ; 

unsigned  char  *  head  , 

*  data  ;  //这四个用来指向线性数据缓存区及数据部分的边界 

unsigned  int  truesize  ;  //整个数据缓存区的总长度 

atomic_t  users  ;  //引用计数，用来标识有多少实体引用了该SKB 

}  ;   
  
---|---  
  
![](https://farm3.staticflickr.com/2945/15483644412_96de5ceac5_n.jpg)

其中end指针指向了skb_shared_info结构体，保存了数据块的附加信息。 

在网络模块中，有很多函数有两个版本，名字分别是do_something()和__do_something()，通常前者是一个封装函数，会在后者的基础上加上合法性校验或者获取锁等操作。 

##  SKB  缓存池、分配函数    


在网络模块中，分配  SKB  描述符的高速缓存在  skb_init()  函数中创建。 

其中第二个  kmem_cache_create  中创建了  2  倍的  sk_buff  的大小，以便用来克隆，这样效率会得到提高。 

void __init skb_init(void) { skbuff_head_cache = kmem_cache_create("skbuff_head_cache", sizeof(struct sk_buff), 0, SLAB_HWCACHE_ALIGN|SLAB_PANIC, NULL); skbuff_fclone_cache = kmem_cache_create("skbuff_fclone_cache", (2*sizeof(struct sk_buff)) + sizeof(atomic_t), 0, SLAB_HWCACHE_ALIGN|SLAB_PANIC, NULL); } 

1 

2 

3 

4 

5 

6 

7 

8 

9 

10 

11 

12 

13 

14 

| 

void  __init  skb_init  (  void  ) 

{ 

skbuff_head_cache  =  kmem_cache_create  (  "skbuff_head_cache"  , 

sizeof  (  struct  sk_buff  )  , 

0  , 

SLAB_HWCACHE_ALIGN  |  SLAB_PANIC  , 

NULL  )  ; 

skbuff_fclone_cache  =  kmem_cache_create  (  "skbuff_fclone_cache"  , 

(  2  *  sizeof  (  struct  sk_buff  )  )  \+ 

sizeof  (  atomic_t  )  , 

0  , 

SLAB_HWCACHE_ALIGN  |  SLAB_PANIC  , 

NULL  )  ; 

}   
  
---|---  
  
alloc_skb()  ：用来分配  SKB  描述符和数据缓存区这两块内存。 

kmem_cache_alloc_node()  ：用来分配头部 

/* Get the HEAD */ skb = kmem_cache_alloc_node(cache, gfp_mask & ~__GFP_DMA, node); 

1 

2 

| 

/* Get the HEAD */ 

skb  =  kmem_cache_alloc_node  (  cache  ,  gfp_mask  & ~  __GFP_DMA  ,  node  )  ;   
  
---|---  
  
kmalloc_reserve()  中的  kmalloc_node_track_caller()  用来分配数据缓存区。 

size = SKB_DATA_ALIGN(size); size += SKB_DATA_ALIGN(sizeof(struct skb_shared_info)); data = kmalloc_reserve(size, gfp_mask, node, &pfmemalloc); 

1 

2 

3 

| 

size  =  SKB_DATA_ALIGN  (  size  )  ; 

size  +=  SKB_DATA_ALIGN  (  sizeof  (  struct  skb_shared_info  )  )  ; 

data  =  kmalloc_reserve  (  size  ,  gfp_mask  ,  node  ,  &pfmemalloc  )  ;   
  
---|---  
  
可以看到  size  中包含了  struct skb_shared_info  的大小。 

![](https://farm3.staticflickr.com/2946/15480856611_b826b8d18d.jpg)

dev_alloc_skb()  ：也是一个缓存区分配函数，通常被设备驱动用在中断上下文中。是  alloc_skb()  的封装函数，增加了原子操作。 

dev_kfree_skb(),kfree_skb()  ：  dev_kfree_skb()  是  consume_skb()  的一个宏，这两个函数最终都是调用  __kfree_skb()  用以释放  SKB  。 

##  数据预留和对齐    


skb_reserve()  ：用于空的  SKB  ，向下移动  tail  指针，把空间让给数据区。 

skb_push()  ：将数据区的一部分空间让给其他层用来增加头部信息。 

skb_put()  ：扩大了数据区。 

skb_pull()  ：数据区首部忽略一部分空间。 

##  克隆和复制  SKB    


skb_clone()  ：克隆过程只赋值  SKB  描述符，同时增加数据缓存区的引用计数，以免共享数据被提前释放。 

pskb_copy()  ：复制数据缓存区。 

skb_copy()  ：完全复制一个  SKB  ，包括局和分散  I/O  存储区中的数据。 

  * 本文固定链接: [ http://www.xysay.com/sk-buff-struct.html ](http://www.xysay.com/sk-buff-struct.html)
  * 转载请注明: [ zxy_snow ](http://www.xysay.com/author/zxy_snow) 2014年10月09日  于 [ 小媛在努力 ](http://www.xysay.com/) 发表 

_ _ [ linux ](http://www.xysay.com/tag/linux) ， [ 内核 ](http://www.xysay.com/tag/%e5%86%85%e6%a0%b8) ， [ 网络协议栈 ](http://www.xysay.com/tag/%e7%bd%91%e7%bb%9c%e5%8d%8f%e8%ae%ae%e6%a0%88)

  

#### 原文：[http://www.xysay.com/sk-buff-struct.html](http://www.xysay.com/sk-buff-struct.html)