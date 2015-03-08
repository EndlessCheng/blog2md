#  [ [PHP]如何使用Face++接口开发微信公共平台的人脸识别系统 ](/pleasecallmewhy/article/details/18862539)

效果图如下： 

![](http://img.blog.csdn.net/20140129142358343?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![](http://img.blog.csdn.net/20140129142430328?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcGxlYXNlY2FsbG1ld2h5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   


  


  


具体步骤如下：   


首先，先登录Face++的官网注册账号： [ 官网链接 ](http://www.faceplusplus.com.cn/)

注册之后会获取到api_secret和api_key，这些在调用接口的时候需要用到。   


然后接下来的就是使用PHP脚本调用API了。 

在使用PHP开发微信公共平台的时候，推荐使用Github上的一款不错的框架： [ wechat-php-sdk ](https://github.com/dodgepudding/wechat-php-sdk)

对于微信的常用接口做了一些封装，核心文件wechat.class.php如下： 

  

    
    
    <?php
    /**
     *	微信公众平台PHP-SDK, 官方API部分
     *  @author  dodge <dodgepudding@gmail.com>
     *  @link https://github.com/dodgepudding/wechat-php-sdk
     *  @version 1.2
     *  usage:
     *   $options = array(
     *			'token'=>'tokenaccesskey', //填写你设定的key
     *			'appid'=>'wxdk1234567890', //填写高级调用功能的app id
     *			'appsecret'=>'xxxxxxxxxxxxxxxxxxx', //填写高级调用功能的密钥
     *		);
     *	 $weObj = new Wechat($options);
     *   $weObj->valid();
     *   $type = $weObj->getRev()->getRevType();
     *   switch($type) {
     *   		case Wechat::MSGTYPE_TEXT:
     *   			$weObj->text("hello, I'm wechat")->reply();
     *   			exit;
     *   			break;
     *   		case Wechat::MSGTYPE_EVENT:
     *   			....
     *   			break;
     *   		case Wechat::MSGTYPE_IMAGE:
     *   			...
     *   			break;
     *   		default:
     *   			$weObj->text("help info")->reply();
     *   }
     *   //获取菜单操作:
     *   $menu = $weObj->getMenu();
     *   //设置菜单
     *   $newmenu =  array(
     *   		"button"=>
     *   			array(
     *   				array('type'=>'click','name'=>'最新消息','key'=>'MENU_KEY_NEWS'),
     *   				array('type'=>'view','name'=>'我要搜索','url'=>'http://www.baidu.com'),
     *   				)
      *  		);
     *   $result = $weObj->createMenu($newmenu);
     */
    class Wechat
    {
    	const MSGTYPE_TEXT = 'text';
    	const MSGTYPE_IMAGE = 'image';
    	const MSGTYPE_LOCATION = 'location';
    	const MSGTYPE_LINK = 'link';
    	const MSGTYPE_EVENT = 'event';
    	const MSGTYPE_MUSIC = 'music';
    	const MSGTYPE_NEWS = 'news';
    	const MSGTYPE_VOICE = 'voice';
    	const MSGTYPE_VIDEO = 'video';
    	const API_URL_PREFIX = 'https://api.weixin.qq.com/cgi-bin';
    	const AUTH_URL = '/token?grant_type=client_credential&';
    	const MENU_CREATE_URL = '/menu/create?';
    	const MENU_GET_URL = '/menu/get?';
    	const MENU_DELETE_URL = '/menu/delete?';
    	const MEDIA_GET_URL = '/media/get?';
    	const QRCODE_CREATE_URL='/qrcode/create?';
    	const QR_SCENE = 0;
    	const QR_LIMIT_SCENE = 1;
    	const QRCODE_IMG_URL='https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=';
    	const USER_GET_URL='/user/get?';
    	const USER_INFO_URL='/user/info?';
    	const GROUP_GET_URL='/groups/get?';
    	const GROUP_CREATE_URL='/groups/create?';
    	const GROUP_UPDATE_URL='/groups/update?';
    	const GROUP_MEMBER_UPDATE_URL='/groups/members/update?';
    	const CUSTOM_SEND_URL='/message/custom/send?';
    	const OAUTH_PREFIX = 'https://open.weixin.qq.com/connect/oauth2';
    	const OAUTH_AUTHORIZE_URL = '/authorize?';
    	const OAUTH_TOKEN_PREFIX = 'https://api.weixin.qq.com/sns/oauth2';
    	const OAUTH_TOKEN_URL = '/access_token?';
    	const OAUTH_REFRESH_URL = '/refresh_token?';
    	const OAUTH_USERINFO_URL = 'https://api.weixin.qq.com/sns/userinfo?';
    	
    	private $token;
    	private $appid;
    	private $appsecret;
    	private $access_token;
    	private $user_token;
    	private $_msg;
    	private $_funcflag = false;
    	private $_receive;
    	public $debug =  false;
    	public $errCode = 40001;
    	public $errMsg = "no access";
    	private $_logcallback;
    	
    	public function __construct($options)
    	{
    		$this->token = isset($options['token'])?$options['token']:'';
    		$this->appid = isset($options['appid'])?$options['appid']:'';
    		$this->appsecret = isset($options['appsecret'])?$options['appsecret']:'';
    		$this->debug = isset($options['debug'])?$options['debug']:false;
    		$this->_logcallback = isset($options['logcallback'])?$options['logcallback']:false;
    	}
    	
    	/**
    	 * For weixin server validation 
    	 */	
    	private function checkSignature()
    	{
            $signature = isset($_GET["signature"])?$_GET["signature"]:'';
            $timestamp = isset($_GET["timestamp"])?$_GET["timestamp"]:'';
            $nonce = isset($_GET["nonce"])?$_GET["nonce"]:'';
            		
    		$token = $this->token;
    		$tmpArr = array($token, $timestamp, $nonce);
    		sort($tmpArr, SORT_STRING);
    		$tmpStr = implode( $tmpArr );
    		$tmpStr = sha1( $tmpStr );
    		
    		if( $tmpStr == $signature ){
    			return true;
    		}else{
    			return false;
    		}
    	}
    	
    	/**
    	 * For weixin server validation 
    	 * @param bool $return 是否返回
    	 */
    	public function valid($return=false)
        {
            $echoStr = isset($_GET["echostr"]) ? $_GET["echostr"]: '';
            if ($return) {
            		if ($echoStr) {
            			if ($this->checkSignature()) 
            				return $echoStr;
            			else
            				return false;
            		} else 
            			return $this->checkSignature();
            } else {
    	        	if ($echoStr) {
    	        		if ($this->checkSignature())
    	        			die($echoStr);
    	        		else 
    	        			die('no access');
    	        	}  else {
    	        		if ($this->checkSignature())
    	        			return true;
    	        		else
    	        			die('no access');
    	        	}
            }
            return false;
        }
        
    	/**
    	 * 设置发送消息
    	 * @param array $msg 消息数组
    	 * @param bool $append 是否在原消息数组追加
    	 */
        public function Message($msg = '',$append = false){
        		if (is_null($msg)) {
        			$this->_msg =array();
        		}elseif (is_array($msg)) {
        			if ($append)
        				$this->_msg = array_merge($this->_msg,$msg);
        			else
        				$this->_msg = $msg;
        			return $this->_msg;
        		} else {
        			return $this->_msg;
        		}
        }
        
        public function setFuncFlag($flag) {
        		$this->_funcflag = $flag;
        		return $this;
        }
        
        private function log($log){
        		if ($this->debug && function_exists($this->_logcallback)) {
        			if (is_array($log)) $log = print_r($log,true);
        			return call_user_func($this->_logcallback,$log);
        		}
        }
        
        /**
         * 获取微信服务器发来的信息
         */
    	public function getRev()
    	{
    		if ($this->_receive) return $this;
    		$postStr = file_get_contents("php://input");
    		$this->log($postStr);
    		if (!empty($postStr)) {
    			$this->_receive = (array)simplexml_load_string($postStr, 'SimpleXMLElement', LIBXML_NOCDATA);
    		}
    		return $this;
    	}
    	
    	/**
    	 * 获取微信服务器发来的信息
    	 */
    	public function getRevData()
    	{
    		return $this->_receive;
    	}
    		
    	/**
    	 * 获取消息发送者
    	 */
    	public function getRevFrom() {
    		if (isset($this->_receive['FromUserName']))
    			return $this->_receive['FromUserName'];
    		else 
    			return false;
    	}
    	
    	/**
    	 * 获取消息接受者
    	 */
    	public function getRevTo() {
    		if (isset($this->_receive['ToUserName']))
    			return $this->_receive['ToUserName'];
    		else 
    			return false;
    	}
    	
    	/**
    	 * 获取接收消息的类型
    	 */
    	public function getRevType() {
    		if (isset($this->_receive['MsgType']))
    			return $this->_receive['MsgType'];
    		else 
    			return false;
    	}
    	
    	/**
    	 * 获取消息ID
    	 */
    	public function getRevID() {
    		if (isset($this->_receive['MsgId']))
    			return $this->_receive['MsgId'];
    		else 
    			return false;
    	}
    	
    	/**
    	 * 获取消息发送时间
    	 */
    	public function getRevCtime() {
    		if (isset($this->_receive['CreateTime']))
    			return $this->_receive['CreateTime'];
    		else 
    			return false;
    	}
    	
    	/**
    	 * 获取接收消息内容正文
    	 */
    	public function getRevContent(){
    		if (isset($this->_receive['Content']))
    			return $this->_receive['Content'];
    		else if (isset($this->_receive['Recognition'])) //获取语音识别文字内容，需申请开通
    			return $this->_receive['Recognition'];
    		else
    			return false;
    	}
    	
    	/**
    	 * 获取接收消息图片
    	 */
    	public function getRevPic(){
    		if (isset($this->_receive['PicUrl']))
    			return $this->_receive['PicUrl'];
    		else 
    			return false;
    	}
    	
    	/**
    	 * 获取接收消息链接
    	 */
    	public function getRevLink(){
    		if (isset($this->_receive['Url'])){
    			return array(
    				'url'=>$this->_receive['Url'],
    				'title'=>$this->_receive['Title'],
    				'description'=>$this->_receive['Description']
    			);
    		} else 
    			return false;
    	}
    	
    	/**
    	 * 获取接收地理位置
    	 */
    	public function getRevGeo(){
    		if (isset($this->_receive['Location_X'])){
    			return array(
    				'x'=>$this->_receive['Location_X'],
    				'y'=>$this->_receive['Location_Y'],
    				'scale'=>$this->_receive['Scale'],
    				'label'=>$this->_receive['Label']
    			);
    		} else 
    			return false;
    	}
    	
    	/**
    	 * 获取接收事件推送
    	 */
    	public function getRevEvent(){
    		if (isset($this->_receive['Event'])){
    			return array(
    				'event'=>$this->_receive['Event'],
    				'key'=>$this->_receive['EventKey'],
    			);
    		} else 
    			return false;
    	}
    	
    	/**
    	 * 获取接收语言推送
    	 */
    	public function getRevVoice(){
    		if (isset($this->_receive['MediaId'])){
    			return array(
    				'mediaid'=>$this->_receive['MediaId'],
    				'format'=>$this->_receive['Format'],
    			);
    		} else 
    			return false;
    	}
    	
    	/**
    	 * 获取接收视频推送
    	 */
    	public function getRevVideo(){
    		if (isset($this->_receive['MediaId'])){
    			return array(
    					'mediaid'=>$this->_receive['MediaId'],
    					'thumbmediaid'=>$this->_receive['ThumbMediaId']
    			);
    		} else
    			return false;
    	}
    	
    	/**
    	 * 获取接收TICKET
    	 */
    	public function getRevTicket(){
    	if (isset($this->_receive['Ticket'])){
    		return $this->_receive['Ticket'];
    	} else
    		return false;
        }
    	
        /**
         * 获取二维码的场景值
         */
        public function getRevSceneId (){
        	if (isset($this->_receive['EventKey'])){
        		return str_replace('qrscene_','',$this->_receive['EventKey']);
        	} else{
        		return false;
        	}
        }
        
    	public static function xmlSafeStr($str)
    	{   
    		return '<![CDATA['.preg_replace("/[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f]/",'',$str).']]>';   
    	} 
    	
    	/**
    	 * 数据XML编码
    	 * @param mixed $data 数据
    	 * @return string
    	 */
    	public static function data_to_xml($data) {
    	    $xml = '';
    	    foreach ($data as $key => $val) {
    	        is_numeric($key) && $key = "item id=\"$key\"";
    	        $xml    .=  "<$key>";
    	        $xml    .=  ( is_array($val) || is_object($val)) ? self::data_to_xml($val)  : self::xmlSafeStr($val);
    	        list($key, ) = explode(' ', $key);
    	        $xml    .=  "</$key>";
    	    }
    	    return $xml;
    	}	
    	
    	/**
    	 * XML编码
    	 * @param mixed $data 数据
    	 * @param string $root 根节点名
    	 * @param string $item 数字索引的子节点名
    	 * @param string $attr 根节点属性
    	 * @param string $id   数字索引子节点key转换的属性名
    	 * @param string $encoding 数据编码
    	 * @return string
    	*/
    	public function xml_encode($data, $root='xml', $item='item', $attr='', $id='id', $encoding='utf-8') {
    	    if(is_array($attr)){
    	        $_attr = array();
    	        foreach ($attr as $key => $value) {
    	            $_attr[] = "{$key}=\"{$value}\"";
    	        }
    	        $attr = implode(' ', $_attr);
    	    }
    	    $attr   = trim($attr);
    	    $attr   = empty($attr) ? '' : " {$attr}";
    	    $xml   = "<{$root}{$attr}>";
    	    $xml   .= self::data_to_xml($data, $item, $id);
    	    $xml   .= "</{$root}>";
    	    return $xml;
    	}
    	
    	/**
    	 * 设置回复消息
    	 * Examle: $obj->text('hello')->reply();
    	 * @param string $text
    	 */
    	public function text($text='')
    	{
    		$FuncFlag = $this->_funcflag ? 1 : 0;
    		$msg = array(
    			'ToUserName' => $this->getRevFrom(),
    			'FromUserName'=>$this->getRevTo(),
    			'MsgType'=>self::MSGTYPE_TEXT,
    			'Content'=>$text,
    			'CreateTime'=>time(),
    			'FuncFlag'=>$FuncFlag
    		);
    		$this->Message($msg);
    		return $this;
    	}
    	
    	/**
    	 * 设置回复音乐
    	 * @param string $title
    	 * @param string $desc
    	 * @param string $musicurl
    	 * @param string $hgmusicurl
    	 */
    	public function music($title,$desc,$musicurl,$hgmusicurl='') {
    		$FuncFlag = $this->_funcflag ? 1 : 0;
    		$msg = array(
    			'ToUserName' => $this->getRevFrom(),
    			'FromUserName'=>$this->getRevTo(),
    			'CreateTime'=>time(),
    			'MsgType'=>self::MSGTYPE_MUSIC,
    			'Music'=>array(
    				'Title'=>$title,
    				'Description'=>$desc,
    				'MusicUrl'=>$musicurl,
    				'HQMusicUrl'=>$hgmusicurl
    			),
    			'FuncFlag'=>$FuncFlag
    		);
    		$this->Message($msg);
    		return $this;
    	}
    	
    	/**
    	 * 设置回复图文
    	 * @param array $newsData 
    	 * 数组结构:
    	 *  array(
    	 *  	[0]=>array(
    	 *  		'Title'=>'msg title',
    	 *  		'Description'=>'summary text',
    	 *  		'PicUrl'=>'http://www.domain.com/1.jpg',
    	 *  		'Url'=>'http://www.domain.com/1.html'
    	 *  	),
    	 *  	[1]=>....
    	 *  )
    	 */
    	public function news($newsData=array())
    	{
    		$FuncFlag = $this->_funcflag ? 1 : 0;
    		$count = count($newsData);
    		
    		$msg = array(
    			'ToUserName' => $this->getRevFrom(),
    			'FromUserName'=>$this->getRevTo(),
    			'MsgType'=>self::MSGTYPE_NEWS,
    			'CreateTime'=>time(),
    			'ArticleCount'=>$count,
    			'Articles'=>$newsData,
    			'FuncFlag'=>$FuncFlag
    		);
    		$this->Message($msg);
    		return $this;
    	}
    	
    	/**
    	 * 
    	 * 回复微信服务器, 此函数支持链式操作
    	 * @example $this->text('msg tips')->reply();
    	 * @param string $msg 要发送的信息, 默认取$this->_msg
    	 * @param bool $return 是否返回信息而不抛出到浏览器 默认:否
    	 */
    	public function reply($msg=array(),$return = false)
    	{
    		if (empty($msg)) 
    			$msg = $this->_msg;
    		$xmldata=  $this->xml_encode($msg);
    		$this->log($xmldata);
    		if ($return)
    			return $xmldata;
    		else
    			echo $xmldata;
    	}
    	
    
    	/**
    	 * GET 请求
    	 * @param string $url
    	 */
    	private function http_get($url){
    		$oCurl = curl_init();
    		if(stripos($url,"https://")!==FALSE){
    			curl_setopt($oCurl, CURLOPT_SSL_VERIFYPEER, FALSE);
    			curl_setopt($oCurl, CURLOPT_SSL_VERIFYHOST, FALSE);
    		}
    		curl_setopt($oCurl, CURLOPT_URL, $url);
    		curl_setopt($oCurl, CURLOPT_RETURNTRANSFER, 1 );
    		$sContent = curl_exec($oCurl);
    		$aStatus = curl_getinfo($oCurl);
    		curl_close($oCurl);
    		if(intval($aStatus["http_code"])==200){
    			return $sContent;
    		}else{
    			return false;
    		}
    	}
    	
    	/**
    	 * POST 请求
    	 * @param string $url
    	 * @param array $param
    	 * @return string content
    	 */
    	private function http_post($url,$param){
    		$oCurl = curl_init();
    		if(stripos($url,"https://")!==FALSE){
    			curl_setopt($oCurl, CURLOPT_SSL_VERIFYPEER, FALSE);
    			curl_setopt($oCurl, CURLOPT_SSL_VERIFYHOST, false);
    		}
    		if (is_string($param)) {
    			$strPOST = $param;
    		} else {
    			$aPOST = array();
    			foreach($param as $key=>$val){
    				$aPOST[] = $key."=".urlencode($val);
    			}
    			$strPOST =  join("&", $aPOST);
    		}
    		curl_setopt($oCurl, CURLOPT_URL, $url);
    		curl_setopt($oCurl, CURLOPT_RETURNTRANSFER, 1 );
    		curl_setopt($oCurl, CURLOPT_POST,true);
    		curl_setopt($oCurl, CURLOPT_POSTFIELDS,$strPOST);
    		$sContent = curl_exec($oCurl);
    		$aStatus = curl_getinfo($oCurl);
    		curl_close($oCurl);
    		if(intval($aStatus["http_code"])==200){
    			return $sContent;
    		}else{
    			return false;
    		}
    	}
    	
    	/**
    	 * 通用auth验证方法，暂时仅用于菜单更新操作
    	 * @param string $appid
    	 * @param string $appsecret
    	 */
    	public function checkAuth($appid='',$appsecret=''){
    		if (!$appid || !$appsecret) {
    			$appid = $this->appid;
    			$appsecret = $this->appsecret;
    		}
    		//TODO: get the cache access_token
    		$result = $this->http_get(self::API_URL_PREFIX.self::AUTH_URL.'appid='.$appid.'&secret='.$appsecret);
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (!$json || isset($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			$this->access_token = $json['access_token'];
    			$expire = $json['expires_in'] ? intval($json['expires_in'])-100 : 3600;
    			//TODO: cache access_token
    			return $this->access_token;
    		}
    		return false;
    	}
    
    	/**
    	 * 删除验证数据
    	 * @param string $appid
    	 */
    	public function resetAuth($appid=''){
    		$this->access_token = '';
    		//TODO: remove cache
    		return true;
    	}
    		
    	/**
    	 * 微信api不支持中文转义的json结构
    	 * @param array $arr
    	 */
    	static function json_encode($arr) {
    		$parts = array ();
    		$is_list = false;
    		//Find out if the given array is a numerical array
    		$keys = array_keys ( $arr );
    		$max_length = count ( $arr ) - 1;
    		if (($keys [0] === 0) && ($keys [$max_length] === $max_length )) { //See if the first key is 0 and last key is length - 1
    			$is_list = true;
    			for($i = 0; $i < count ( $keys ); $i ++) { //See if each key correspondes to its position
    				if ($i != $keys [$i]) { //A key fails at position check.
    					$is_list = false; //It is an associative array.
    					break;
    				}
    			}
    		}
    		foreach ( $arr as $key => $value ) {
    			if (is_array ( $value )) { //Custom handling for arrays
    				if ($is_list)
    					$parts [] = self::json_encode ( $value ); /* :RECURSION: */
    				else
    					$parts [] = '"' . $key . '":' . self::json_encode ( $value ); /* :RECURSION: */
    			} else {
    				$str = '';
    				if (! $is_list)
    					$str = '"' . $key . '":';
    				//Custom handling for multiple data types
    				if (is_numeric ( $value ) && $value<2000000000)
    					$str .= $value; //Numbers
    				elseif ($value === false)
    				$str .= 'false'; //The booleans
    				elseif ($value === true)
    				$str .= 'true';
    				else
    					$str .= '"' . addslashes ( $value ) . '"'; //All other things
    				// :TODO: Is there any more datatype we should be in the lookout for? (Object?)
    				$parts [] = $str;
    			}
    		}
    		$json = implode ( ',', $parts );
    		if ($is_list)
    			return '[' . $json . ']'; //Return numerical JSON
    		return '{' . $json . '}'; //Return associative JSON
    	}
    	
    	/**
    	 * 创建菜单
    	 * @param array $data 菜单数组数据
    	 * example:
    	 {
    	 "button":[
    	 {
    	 "type":"click",
    	 "name":"今日歌曲",
    	 "key":"MENU_KEY_MUSIC"
    	 },
    	 {
    	 "type":"view",
    	 "name":"歌手简介",
    	 "url":"http://www.qq.com/"
    	 },
    	 {
    	 "name":"菜单",
    	 "sub_button":[
    	 {
    	 "type":"click",
    	 "name":"hello word",
    	 "key":"MENU_KEY_MENU"
    	 },
    	 {
    	 "type":"click",
    	 "name":"赞一下我们",
    	 "key":"MENU_KEY_GOOD"
    	 }]
    	 }]
    	 }
    	 */
    	public function createMenu($data){
    		if (!$this->access_token && !$this->checkAuth()) return false;
    		$result = $this->http_post(self::API_URL_PREFIX.self::MENU_CREATE_URL.'access_token='.$this->access_token,self::json_encode($data));
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (!$json || !empty($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			return true;
    		}
    		return false;
    	}
    	
    	/**
    	 * 获取菜单
    	 * @return array('menu'=>array(....s))
    	 */
    	public function getMenu(){
    		if (!$this->access_token && !$this->checkAuth()) return false;
    		$result = $this->http_get(self::API_URL_PREFIX.self::MENU_GET_URL.'access_token='.$this->access_token);
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (!$json || isset($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			return $json;
    		}
    		return false;
    	}
    	
    	/**
    	 * 删除菜单
    	 * @return boolean
    	 */
    	public function deleteMenu(){
    		if (!$this->access_token && !$this->checkAuth()) return false;
    		$result = $this->http_get(self::API_URL_PREFIX.self::MENU_DELETE_URL.'access_token='.$this->access_token);
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (!$json || !empty($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			return true;
    		}
    		return false;
    	}
    
    	/**
    	 * 根据媒体文件ID获取媒体文件
    	 * @param string $media_id 媒体文件id
    	 * @return raw data
    	 */
    	public function getMedia($media_id){
    		if (!$this->access_token && !$this->checkAuth()) return false;
    		$result = $this->http_get(self::API_URL_PREFIX.self::MEDIA_GET_URL.'access_token='.$this->access_token.'&media_id='.$media_id);
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (isset($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			return $json;
    		}
    		return false;
    	}	
    	
    	/**
    	 * 创建二维码ticket
    	 * @param int $scene_id 自定义追踪id
    	 * @param int $type 0:临时二维码；1:永久二维码(此时expire参数无效)
    	 * @param int $expire 临时二维码有效期，最大为1800秒
    	 * @return array('ticket'=>'qrcode字串','expire_seconds'=>1800)
    	 */
    	public function getQRCode($scene_id,$type=0,$expire=1800){
    		if (!$this->access_token && !$this->checkAuth()) return false;
    		$data = array(
    			'action_name'=>$type?"QR_LIMIT_SCENE":"QR_SCENE",
    			'expire_seconds'=>$expire,
    			'action_info'=>array('scene'=>array('scene_id'=>$scene_id))
    		);
    		if ($type == 1) {
    			unset($data['expire_seconds']);
    		}
    		$result = $this->http_post(self::API_URL_PREFIX.self::QRCODE_CREATE_URL.'access_token='.$this->access_token,self::json_encode($data));
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (!$json || !empty($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			return $json;
    		}
    		return false;
    	}
    	
    	/**
    	 * 获取二维码图片
    	 * @param string $ticket 传入由getQRCode方法生成的ticket参数
    	 * @return string url 返回http地址
    	 */
    	public function getQRUrl($ticket) {
    		return self::QRCODE_IMG_URL.$ticket;
    	}
    	
    	/**
    	 * 批量获取关注用户列表
    	 * @param unknown $next_openid
    	 */
    	public function getUserList($next_openid=''){
    		if (!$this->access_token && !$this->checkAuth()) return false;
    		$result = $this->http_get(self::API_URL_PREFIX.self::USER_GET_URL.'access_token='.$this->access_token.'&next_openid='.$next_openid);
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (isset($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			return $json;
    		}
    		return false;
    	}
    	
    	/**
    	 * 获取关注者详细信息
    	 * @param string $openid
    	 * @return array
    	 */
    	public function getUserInfo($openid){
    		if (!$this->access_token && !$this->checkAuth()) return false;
    		$result = $this->http_get(self::API_URL_PREFIX.self::USER_INFO_URL.'access_token='.$this->access_token.'&openid='.$openid);
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (isset($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			return $json;
    		}
    		return false;
    	}
    	
    	/**
    	 * 获取用户分组列表
    	 * @return boolean|array
    	 */
    	public function getGroup(){
    		if (!$this->access_token && !$this->checkAuth()) return false;
    		$result = $this->http_get(self::API_URL_PREFIX.self::GROUP_GET_URL.'access_token='.$this->access_token);
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (isset($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			return $json;
    		}
    		return false;
    	}
    	
    	/**
    	 * 新增自定分组
    	 * @param string $name 分组名称
    	 * @return boolean|array
    	 */
    	public function createGroup($name){
    		if (!$this->access_token && !$this->checkAuth()) return false;
    		$data = array(
    				'group'=>array('name'=>$name)
    		);
    		$result = $this->http_post(self::API_URL_PREFIX.self::GROUP_CREATE_URL.'access_token='.$this->access_token,self::json_encode($data));
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (!$json || !empty($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			return $json;
    		}
    		return false;
    	}
    	
    	/**
    	 * 更改分组名称
    	 * @param int $groupid 分组id
    	 * @param string $name 分组名称
    	 * @return boolean|array
    	 */
    	public function updateGroup($groupid,$name){
    		if (!$this->access_token && !$this->checkAuth()) return false;
    		$data = array(
    				'group'=>array('id'=>$groupid,'name'=>$name)
    		);
    		$result = $this->http_post(self::API_URL_PREFIX.self::GROUP_UPDATE_URL.'access_token='.$this->access_token,self::json_encode($data));
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (!$json || !empty($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			return $json;
    		}
    		return false;
    	}
    	
    	/**
    	 * 移动用户分组
    	 * @param int $groupid 分组id
    	 * @param string $openid 用户openid
    	 * @return boolean|array
    	 */
    	public function updateGroupMembers($groupid,$openid){
    		if (!$this->access_token && !$this->checkAuth()) return false;
    		$data = array(
    				'openid'=>$openid,
    				'to_groupid'=>$groupid
    		);
    		$result = $this->http_post(self::API_URL_PREFIX.self::GROUP_MEMBER_UPDATE_URL.'access_token='.$this->access_token,self::json_encode($data));
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (!$json || !empty($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			return $json;
    		}
    		return false;
    	}
    	
    	/**
    	 * 发送客服消息
    	 * @param array $data 消息结构{"touser":"OPENID","msgtype":"news","news":{...}}
    	 * @return boolean|array
    	 */
    	public function sendCustomMessage($data){
    		if (!$this->access_token && !$this->checkAuth()) return false;
    		$result = $this->http_post(self::API_URL_PREFIX.self::CUSTOM_SEND_URL.'access_token='.$this->access_token,self::json_encode($data));
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (!$json || !empty($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			return $json;
    		}
    		return false;
    	}
    	
    	/**
    	 * oauth 授权跳转接口
    	 * @param string $callback 回调URI
    	 * @return string
    	 */
    	public function getOauthRedirect($callback,$state='',$scope='snsapi_userinfo'){
    		return self::OAUTH_PREFIX.self::OAUTH_AUTHORIZE_URL.'appid='.$this->appid.'&redirect_uri='.urlencode($callback).'&response_type=code&scope='.$scope.'&state='.$state.'#wechat_redirect';
    	}
    	
    	/*
    	 * 通过code获取Access Token
    	 * @return array {access_token,expires_in,refresh_token,openid,scope}
    	 */
    	public function getOauthAccessToken(){
    		$code = isset($_GET['code'])?$_GET['code']:'';
    		if (!$code) return false;
    		$result = $this->http_get(self::OAUTH_TOKEN_PREFIX.self::OAUTH_TOKEN_URL.'appid='.$this->appid.'&secret='.$this->appsecret.'&code='.$code.'&grant_type=authorization_code');
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (!$json || !empty($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			$this->user_token = $json['access_token'];
    			return $json;
    		}
    		return false;
    	}
    	
    	/**
    	 * 刷新access token并续期
    	 * @param string $refresh_token
    	 * @return boolean|mixed
    	 */
    	public function getOauthRefreshToken($refresh_token){
    		$result = $this->http_get(self::OAUTH_TOKEN_PREFIX.self::OAUTH_REFRESH_URL.'appid='.$this->appid.'&grant_type=refresh_token&refresh_token='.$refresh_token);
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (!$json || !empty($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			$this->user_token = $json['access_token'];
    			return $json;
    		}
    		return false;
    	}
    	
    	/**
    	 * 获取授权后的用户资料
    	 * @param string $access_token
    	 * @param string $openid
    	 * @return array {openid,nickname,sex,province,city,country,headimgurl,privilege}
    	 */
    	public function getOauthUserinfo($access_token,$openid){
    		$result = $this->http_get(self::OAUTH_USERINFO_URL.'access_token='.$access_token.'&openid='.$openid);
    		if ($result)
    		{
    			$json = json_decode($result,true);
    			if (!$json || !empty($json['errcode'])) {
    				$this->errCode = $json['errcode'];
    				$this->errMsg = $json['errmsg'];
    				return false;
    			}
    			return $json;
    		}
    		return false;
    	}
    }
    

  
  
  
接下来就是接口对应的index.php文件，处理微信服务器发送来的信息。 

因为是工作室的微信公共账号，所以未做任何修改源码搬上来，截取有用的部分即可： 
    
    
    <?php
    /**
     *	WeeGo工作室微信公众平台接口源码
     *  @author  CallMeWhy <wanghaiyang@139.me>
     *  @link http://blog.csdn.net/pleasecallmewhy/article/details/18862539
     *  @version 1.0
     */
    include "wechat.class.php";
    
    $options = array
    (
    	'token'=>'weego',
    	'debug'=>true,
    	'logcallback'=>'logdebug'
    );
    
    $weObj = new Wechat($options);
    // 验证
    $weObj->valid();
    // 获取内容
    $weObj->getRev();
    // 获取用户的OpenID	
    $fromUsername = $weObj->getRevFrom();
    // 获取接受信息的类型
    $type = $weObj->getRev()->getRevType();
    
    
    //**********关注操作则写入数据库**********/
    if($weObj->getRevSubscribe())
    {
    	// 获取用户OPENID并写入数据库
    	$mysql = new SaeMysql();
    	$sql = "INSERT INTO `users` (`wxid`) VALUES ('" . $fromUsername . "');";
    	$mysql->runSql($sql);
    	$mysql->closeDb();
    
    	// 获得信息的类型
    	$news = array
    	(
    		array
    		(
    			'Title'=>'欢迎关注WeeGo工作室',
    			'Description'=>'发送任意内容查看最新开发进展',
    			'PicUrl'=>'http://233.weego.sinaapp.com/images/weego_400_200.png',
    		)
    	);
    	$weObj->news($news)->reply();
    }
    
    //**********取消关注操作则删除数据库**********/
    if($weObj->getRevUnsubscribe())
    {
    	// 获取用户OPENID并从数据库删除
    	$mysql = new SaeMysql();
    	$sql = "DELETE FROM `users` WHERE `wxid` = '" . $fromUsername . "'";
    	$mysql->runSql($sql);
    	$mysql->closeDb();
    }
    
    switch($type) {
        case Wechat::MSGTYPE_TEXT:
            /**********文字信息**********/
    		$news = array
    		(
    			array
    			(
    				'Title'=>"欢迎光临WeeGo工作室",
    				'PicUrl'=>'http://233.weego.sinaapp.com/images/weego_400_200.png',
    				//'Url'=>'http://233.weego.sinaapp.com/web/home.php?wxid='.$fromUsername
    			),		
    			array
    			(
    				'Title'=>"功能1：发送图片可以查询照片中人脸的年龄和性别信息哦",
    				'PicUrl'=>'http://233.weego.sinaapp.com/images/face.jpg',
    				//'Url'=>'http://233.weego.sinaapp.com/web/home.php?wxid='.$fromUsername
    			),	
    			array
    			(
    				'Title'=>"功能2：发送一张两人合影的照片可以计算两人的相似程度",
    				'PicUrl'=>'http://233.weego.sinaapp.com/images/mask.png',
    				//'Url'=>'http://233.weego.sinaapp.com/web/home.php?wxid='.$fromUsername
    			),	
    			array
    			(
    				'Title'=>"功能3：山东大学绩点查询签到等功能正在开发中敬请期待",
    				'PicUrl'=>'http://233.weego.sinaapp.com/images/sdu.jpg',
    				//'Url'=>'http://233.weego.sinaapp.com/web/home.php?wxid='.$fromUsername
    			)
    		);
    		// 开发人员通道
    		if($weObj->getRev()->getRevContent() === "why"){
    			$news = array
    			(
    				array
    				(
    					'Title'=>'开发人员通道',
    					'Description'=>'开发人员通道',
    					'PicUrl'=>'http://233.weego.sinaapp.com/images/weego_400_200.png',
    					'Url'=>'http://233.weego.sinaapp.com/web/home.php?wxid='.$fromUsername
    				)
    			);
    		}
    		$weObj->news($news)->reply();
            exit;
            break;
        case Wechat::MSGTYPE_EVENT:
    		break;
        case Wechat::MSGTYPE_IMAGE:
            /**********图片信息**********/
    		$imgUrl = $weObj->getRev()->getRevPic();
    		$resultStr = face($imgUrl);
            $weObj->text($resultStr)->reply();
            break;
        default:
            $weObj->text("Default")->reply();
    }
    
    // 调用人脸识别的API返回识别结果
    function face($imgUrl)
    {
    	// face++ 链接
    	$jsonStr =
    		file_get_contents("http://apicn.faceplusplus.com/v2/detection/detect?url=".$imgUrl."&api_key=5eb2c984ad24ffc08c352bdb53ee52f8&api_secret=ViX19uvxkT_A0a6d55Hb0Q0QGMTqZ95f&&attribute=glass,pose,gender,age,race,smiling");
    	
    	$replyDic = json_decode($jsonStr);
    	$resultStr = "";
    	$faceArray = $replyDic->{'face'};
    
    	$resultStr .= "图中共检测到".count($faceArray)."张脸！\n";
    	for ($i= 0;$i< count($faceArray); $i++){
    		$resultStr .= "第".($i+1)."张脸\n";
    		$tempFace = $faceArray[$i];
    		// 获取所有属性
    		$tempAttr = $tempFace->{'attribute'};
    
    		// 年龄：包含年龄分析结果
    		// value的值为一个非负整数表示估计的年龄, range表示估计年龄的正负区间
    		$tempAge = $tempAttr->{'age'};
    
    		// 性别：包含性别分析结果
    		// value的值为Male/Female, confidence表示置信度
    		$tempGenger	= $tempAttr->{'gender'};	
    
    		// 种族：包含人种分析结果
    		// value的值为Asian/White/Black, confidence表示置信度
    		$tempRace = $tempAttr->{'race'};		
    
    		// 微笑：包含微笑程度分析结果
    		//value的值为0-100的实数，越大表示微笑程度越高
    		$tempSmiling = $tempAttr->{'smiling'};
    
    		// 眼镜：包含眼镜佩戴分析结果
    		// value的值为None/Dark/Normal, confidence表示置信度
    		$tempGlass = $tempAttr->{'glass'};	
    
    		// 造型：包含脸部姿势分析结果
    		// 包括pitch_angle, roll_angle, yaw_angle
    		// 分别对应抬头，旋转（平面旋转），摇头
    		// 单位为角度。
    		$tempPose = $tempAttr->{'pose'};
    		
    		//返回年龄
    		$minAge = $tempAge->{'value'} - $tempAge->{'range'};
    		$minAge = $minAge < 0 ? 0 : $minAge;
    		$maxAge = $tempAge->{'value'} + $tempAge->{'range'};
    		$resultStr .= "年龄：".$minAge."-".$maxAge."岁\n";
    
    		// 返回性别
    		if($tempGenger->{'value'} === "Male")
    			$resultStr .= "性别：男\n";	
    		else if($tempGenger->{'value'} === "Female")
    			$resultStr .= "性别：女\n";
    
    		// 返回种族
    		if($tempRace->{'value'} === "Asian")
    			$resultStr .= "种族：黄种人\n";	
    		else if($tempRace->{'value'} === "Male")
    			$resultStr .= "种族：白种人\n";	
    		else if($tempRace->{'value'} === "Black")
    			$resultStr .= "种族：黑种人\n";	
    
    		// 返回眼镜
    		if($tempGlass->{'value'} === "None")
    			$resultStr .= "眼镜：木有眼镜\n";	
    		else if($tempGlass->{'value'} === "Dark")
    			$resultStr .= "眼镜：目测墨镜\n";	
    		else if($tempGlass->{'value'} === "Normal")
    			$resultStr .= "眼镜：普通眼镜\n";	
    
    		//返回微笑
    		$resultStr .= "微笑：".round($tempSmiling->{'value'})."%\n";
    	}	
    	
    	if(count($faceArray) === 2){
    		// 获取face_id
    		$tempFace = $faceArray[0];
    		$tempId1 = $tempFace->{'face_id'};
    		$tempFace = $faceArray[1];
    		$tempId2 = $tempFace->{'face_id'};
    
    
    		// face++ 链接
    		$jsonStr =
    			file_get_contents("https://apicn.faceplusplus.com/v2/recognition/compare?api_secret=ViX19uvxkT_A0a6d55Hb0Q0QGMTqZ95f&api_key=5eb2c984ad24ffc08c352bdb53ee52f8&face_id2=".$tempId2 ."&face_id1=".$tempId1);
    		$replyDic = json_decode($jsonStr);
    
    		//取出相似程度
    		$tempResult = $replyDic->{'similarity'};
    		$resultStr .= "相似程度：".round($tempResult)."%\n";
    
    		//具体分析相似处
    		$tempSimilarity = $replyDic->{'component_similarity'};
    		$tempEye = $tempSimilarity->{'eye'};
    		$tempEyebrow = $tempSimilarity->{'eyebrow'};
    		$tempMouth = $tempSimilarity->{'mouth'};
    		$tempNose = $tempSimilarity->{'nose'};
    		
    		$resultStr .= "相似分析：\n";
    		$resultStr .= "眼睛：".round($tempEye)."%\n";
    		$resultStr .= "眉毛：".round($tempEyebrow)."%\n";
    		$resultStr .= "嘴巴：".round($tempMouth)."%\n";
    		$resultStr .= "鼻子：".round($tempNose)."%\n";
    	}
    
    
    	//如果没有检测到人脸
    	if($resultStr === "")
    		$resultStr = "照片中木有人脸=.=";
    	return $resultStr;
    };
    
    
    
    // 写入本地日志文件的函数
    function logdebug($text)
    {
    	file_put_contents('log.txt', $text."\n", FILE_APPEND);		
    };
    
    

  
  

#### 原文：[http://blog.csdn.net/pleasecallmewhy/article/details/18862539](http://blog.csdn.net/pleasecallmewhy/article/details/18862539)