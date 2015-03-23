title: IPv4 存在而 IPv6 不存在时对于 AAAA 记录查询的响应

date: 2014-02-02 11:55:02

tags: [DNS, Network, ]

description: 

---
昨天收到了仙子酱 forward 给我的来自 prosody 开发者的回复，关于 Google 无法连接到 `talk.archlinuxcn.org` 的问题。开发者指出是 DNS 响应不规范，在 IPv4 存在而 IPv6 不存在时，如果首先查询 `AAAA` 记录而得到了 `NXDOMAIN`，则会停止继续查询记录。

根据 [RFC 4074](http://www.ietf.org/rfc/rfc4074.txt)，在 IPv4 存在而 IPv6 不存在时，对于 `AAAA` 记录的响应 RCODE 应为`0`，即 `NOERROR` 而不是 `NXDOMAIN`。

根据RFC的说明对略萌DNS的程序做了部分修改，commit #`[a5a81172d5`](https://github.com/phoenixlzx/minimoedns/commit/a5a81172d5b4ab0fee375a70b7065883ff0fbc97)
    
    
    connection.query('SELECT * from `records` WHERE `paused` IS NOT TRUE AND `name` = ? AND (`type` = "A" OR `type` = "AAAA" OR `type` = "CNAME")',
    
        name,
    
        function(err, result) {
    
          if (err) { 
    
    	  ...  
  
---  
      
    
    result.forEach(function(record) {
    
        switch (record.type) {
    
    	case "A": 
    
    	break;
    
    	case "AAAA":
    
    	...  
  
---  
  
一个简单的改动，没做什么测试就提交了。然后发现 Google DNS 等缓存DNS给`AAAA`查询返回了`SERVFAIL`…

`dig +trace` 查了下发现死循环了… 再去看 RFC 同时用猫的 NS 服务器做了测试，发现对于这种情况，返回的记录是 Authority 部分 SOA，其他全部是空，格式和 `NXDOMAIN` 一样，只不过RCODE是 `NOERROR` 而已。

嘛。commit #`[5f50bbaa89`](https://github.com/phoenixlzx/minimoedns/commit/5f50bbaa89ac7b51259aeaaa54b08d65476300da)
    
    
    case "A":
    
        var content = SOAresult[0].content.split(" ");
    
        response.authority.push(dns.SOA({
    
    	name: SOAresult[0].name,
    
    	primary: content[0],
    
    	admin: content[1].replace("@", "."),
    
    	serial: content[2],
    
    	refresh: content[3],
    
    	retry: content[4],
    
    	expiration: content[5],
    
    	minimum: content[6],
    
    	ttl: SOAresult[0].ttl||config.defaultTTL
    
        }));
    
        response.header.rcode = consts.NAME_TO_RCODE.NOERROR;
    
        return response.send();
    
        break;  
  
---  
  
然后发现把 `case "A"` 写到前面不对… 然后把这段改到了 `case "AAAA"` 和 `case "CNAME"` 后面，另外在 MySQL 模块中也做了修改，防止在有 IPv6 时返回 IPv4。咱基本不会写 SQL 于是做了两步查询。
    
    
    exports.queryAAAA = function(name, callback) {
    
        pool.getConnection(function(err, connection) {
    
            if (err) {
    
                console.log(err.message);
    
            }
    
            connection.query('SELECT * from `records` WHERE `paused` IS NOT TRUE AND `name` = ? AND (`type` = "AAAA" OR `type` = "CNAME")',
    
                name,
    
                function(err, result) {
    
                    if (err) {
    
                        connection.release();
    
                        return callback(err, null);
    
                    }
    
                    if (result[0]) {
    
                        connection.release();
    
                        callback(null, result);
    
                    } else {
    
                        connection.query('SELECT * from `records` WHERE `paused` IS NOT TRUE AND `name` = ? AND `type` = "A"',
    
                            name,
    
                            function(err, resultA) {
    
                                if (err) {
    
                                    connection.release();
    
                                    return callback(err, null);
    
                                }
    
                                connection.release();
    
                                callback(null, resultA);
    
                            });
    
                    }
    
                });
    
        });
    
    }  
  
---  
  
看起来处理的有点 ugly 不过咱才疏学浅只好先这样了。 commit 之后所有略萌DNS节点更新，于是再次查询就正常了w
    
    
    ~> dig @8.8.8.8 talk.archlinuxcn.org AAAA
    
    ; <<>> DiG 9.9.2-P2 <<>> @8.8.8.8 talk.archlinuxcn.org AAAA
    
    ; (1 server found)
    
    ;; global options: +cmd
    
    ;; Got answer:
    
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26181
    
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1
    
    ;; OPT PSEUDOSECTION:
    
    ; EDNS: version: 0, flags:; udp: 512
    
    ;; QUESTION SECTION:
    
    ;talk.archlinuxcn.org.          IN      AAAA
    
    ;; AUTHORITY SECTION:
    
    archlinuxcn.org.        1800    IN      SOA     ns1.moedns.net. admin.moedns.com. 1391266676 3600 360 1209600 180
    
    ;; Query time: 224 msec
    
    ;; SERVER: 8.8.8.8#53(8.8.8.8)
    
    ;; WHEN: Sun Feb  2 12:23:18 2014
    
    ;; MSG SIZE  rcvd: 115  
  
---
