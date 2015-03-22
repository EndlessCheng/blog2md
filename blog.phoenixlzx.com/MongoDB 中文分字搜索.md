title: MongoDB 中文分字搜索

date: 2014-03-22T05:05:43.000Z

tags: [MongoDB, Node.js, ]

description: 

---
为工作室开发的 [ iDocument ](http://idoc.nuister.org) 文档分享平台，因为后端数据库是 MongoDB 所以没有做站内搜索，只是放了个百度站内搜索的工具。不过后来发现BAKA百度根本不收录站内链接，所以主席强烈要求做站内搜索 _ (:з」∠) _

MongoDB 的分词搜索不支持中文，而精确匹配的话基本上就没啥意义了。所以考虑一下几种方法。 

  * 同义词匹配，高端的玩不转，初步想法是为每个文档对象添加一个 ` tag ` 来做搜索关键字，例如「高等数学」的文档可以有「高数」这个tag，搜索「高等数学」和「高数」都能得到这个文档。 
  * 分字匹配，可能会有少许误差，但是对于程序开发和网站运营人员来说都能减轻负担，因为不需要手动维护tag了。 

考虑到数据库中已经有之前的一些数据 (以及主席表示上传文档实在太累了所以强烈要求我保留原数据) 所以这里选择了分字搜索方式。 

按照喵菊给的方法，基本的步骤如下 

  1. 分字函数名称为 ` split() ` ，文档标题为 ` title ` ，搜索字段为 ` querytext ` 。 
  2. 存入新的文档对象时，包含一个 attribute 名为 ` searchIndex ` ，值为 ` split(title) ` 。也就是将 ` title ` 分字后得到的数组。 
  3. 将 ` searchIndex ` 编入索引。 ` ensureIndex({searchIndex: 1}) ` ，顺序的话，喵菊之前提到过，但是这里暂不考虑。 
  4. 搜索时把 ` split(querytext) ` 交给数据库来 ` find() `

由于 Javascript 自带一个超级好用的 ` String.prototype.split() ` 方法，所以分字就是 ` title.split('') ` 。 

以及，喵菊说如果用数组的话就不能用 ` /variable/i ` 这样的正则来忽略大小写了。所以存进去新index的时候要全部转换成小写，搜索的时候也要转换成小写来实现 Case-insensitive search. 

修改路由函数，添加一个新的属性 ` searchIndex ` ： 
    
    
    var newdoc = {
    
        title: req.body.title,
    
        updateTime: Math.round((new Date()).getTime() / 1000),
    
        fileType: req.body.fileType,
    
        belongs: req.body.belongs,
    
        course: req.body.courseId,
    
        type: req.body.type,
    
        link: req.body.link,
    
        downloads: 0,
    
        searchIndex: req.body.title.toLowerCase().split('').clean(" ") // Remove space element after split to single text.
    
    };
    
    Array.prototype.clean = function (deleteValue) {
    
        for (var i = 0; i < this.length; i++) {
    
            if (this[i] == deleteValue) {
    
                this.splice(i, 1);
    
                i--;
    
            }
    
        }
    
        return this;
    
    };  
  
---  
  
修改文档模型函数，添加时将 ` searchIndex ` 编入索引： 
    
    
    exports.addnew = function(newdoc, callback) {
    
        collection.insert(newdoc, {safe: true}, function(err) {
    
            if (err) {
    
                return callback(err);
    
            }
    
            collection.ensureIndex({
    
                searchIndex: 1
    
            }, function(err) {
    
                if (err) {
    
                    return callback(err);
    
                }
    
                callback(null);
    
            });
    
        });
    
    }  
  
---  
  
新建文档搜索函数。 ** 坑：如果直接把分好字的数组交给数据库来 find 那么一样是精确匹配的效果。这里应该是我对 MongoDB 还不够熟悉才掉坑里… **

正确的匹配方法是 ` db.documents.find({ searchIndex: {$all: splittedTextArray} }) ` 。 
    
    
    exports.searchdoc = function(splittedTextArray, callback) {
    
        collection.find({
    
            searchIndex: {$all: splittedTextArray}
    
        })
    
            .sort({ downloads: -1 })
    
            .toArray(function(err, docs) {
    
                if (err) {
    
                    return callback(err, null);
    
                }
    
                callback(null, docs);
    
            });
    
    }  
  
---  
  
然后按照主席的要求，写了个脚本来更新之前的数据。方法是将原来的数据全部取出，然后遍历写回的同时添加 ` searchIndex ` 。看了下原来有的数据大约就100多条，所以直接全部取了没考虑分段的问题嗯。 

据喵菊说，数组处理是 MongoDB 的强项所以非常快～ 

整个项目的源码在 [ 这里 ](https://github.com/DuoHuoStudio/iDocument)

修改完毕，测试效果非常赞w 不过就是BAKA的blueed还没写搜索列表页的样式就是了… <del> 据说前端苦逼 </del>
