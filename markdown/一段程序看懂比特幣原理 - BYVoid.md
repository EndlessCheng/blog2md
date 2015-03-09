三月  ** 20 ** 2014 

  *   *   *     * [ 比特幣 ](/blog/tag/比特幣)
    * [ 原理 ](/blog/tag/原理)
    * [ 挖礦 ](/blog/tag/挖礦)
    * [ 區塊 ](/blog/tag/區塊)
    * [ 區塊鏈 ](/blog/tag/區塊鏈)
    * [ 交易 ](/blog/tag/交易)
    * [ 散列 ](/blog/tag/散列)
    * [ 挖礦難度 ](/blog/tag/挖礦難度)
    * [ 私鑰 ](/blog/tag/私鑰)
    * [ 簽名 ](/blog/tag/簽名)

#  [ 一段程序看懂比特幣原理 ](/blog/bitcoin-principle-program)

自從比特幣火起來以後，網上對比特幣的解釋可謂汗牛充棟，紛繁複雜。但對於程序員來說，最直接的方式莫過於直接看程序代碼了。嫌比特幣代碼龐雜沒關係，我找到一段簡明扼要的代碼，用來理解比特幣再好不過了。 

以下這段程序轉自 [ 知乎上Wu Hao的回答 ](http://www.zhihu.com/question/20941124/answer/16668373) 。 
    
    
    function mine()
    {
        while(true)
        {
            longestChain = getLongestValidChain()
    
            -- A number that changes every time, so that you don't waste 
            -- time trying to calculate a valid blockHash with the same
            -- input.
            nonce = getNewNonce()
    
            currentTXs = getUnconfirmedTransactionsFromNetwork()
    
            newBlock = getNewBlock(longestChain, currentTXs, nonce)
    
            -- http://en.wikipedia.org/wiki/SHA-2
            -- and this is what all the "mining machines" are doing.
            blockHash = sha256(newBlock)
    
            if (meetReqirements(blockHash))
            {
                broadcast(newBlock)
                -- Now the height the block chain is incremented by 1
                -- (if the new block is accepted by other peers),
                -- and all the TXs in the new block are "confirmed"
            }
        }
    }
    ////////////////////////////////////////////////////////////////
    function sendBTC(amount)
    {
        sourceTXs = pickConfirmedTransactionsToBeSpent(amount)
        tx = generateTX(sourceTXs, targetAddrs, amount, fee)
        signedTx = sign(tx, privateKeysOfAllInputAddress)
        broadcast(signedTx)
    }
    ////////////////////////////////////////////////////////////////

下面是我的解釋： 

挖礦過程就是不斷從比特幣網絡中獲取所有未確認交易 ` getUnconfirmedTransactionsFromNetwork() ` ，把它們打包成一個區塊並掛載目前最長的區塊鏈上 ` getNewBlock(longestChain, currentTXs, nonce) ` ，然後計算新的區塊的散列值 ` sha256(newBlock) ` ，如果散列值正好滿足挖礦難度了 ` meetReqirements(blockHash) ` ，那麼就挖礦成功了。所謂挖礦難度，指的是要求的二進制散列值小於某個閾值，閾值越小，挖礦的難度就越大。 

付款過程就是把一些有餘額的已確認交易拿出來作爲發送地址 ` pickConfirmedTransactionsToBeSpent(amount) ` ，然後根據目標地址支付一定交易費生成新的交易 ` generateTX(sourceTXs, targetAddrs, amount, fee) ` ，並用錢包私鑰對交易簽名 ` sign(tx, privateKeysOfAllInputAddress) ` ，然後廣播出去。 
#### 原文：[https://www.byvoid.com/blog/bitcoin-principle-program](https://www.byvoid.com/blog/bitcoin-principle-program)