#  Java dom4j解析xml文档 

[ Find ](http://www.findspace.name/author/find) |  2015年2月5日  |  [ Java ](http://www.findspace.name/category/easycoding/java) , [ 随意Coding ](http://www.findspace.name/category/easycoding) |  [ 没有评论  ](http://www.findspace.name/easycoding/1073#comments)

#  dom4j项目地址 

** [ sourceforge ](http://sourceforge.net/projects/dom4j/?source=navbar) **

#  简单使用教程 

##  一个xml文档 
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <resp>
    <city>济南</city>
    <updatetime>10:10</updatetime>
    <wendu>2</wendu>
    <fengli>4-5级</fengli>
    <shidu>30%</shidu>
    <fengxiang>东北风</fengxiang>
    <sunrise_1>07:11</sunrise_1>
    <sunset_1>17:43</sunset_1>
    <environment>
        <aqi>51</aqi>
        <pm25>24</pm25>
        <suggest>极少数敏感人群应减少户外活动</suggest>
        <quality>良</quality>
        <MajorPollutants>颗粒物(PM10)</MajorPollutants>
        <o3>26</o3>
        <co>1</co>
        <pm10>50</pm10>
        <so2>44</so2>
        <no2>48</no2>
        <time>09:00:00</time>
    </environment>
    

这个文档是抓取天气并短信通知恶劣天气项目的测试xml 

[ 项目仍在开发中 ](https://git.oschina.net/findspace/WeatherGet)

##  解析的代码 
    
    
    
    import java.util.Iterator;
    
    import org.dom4j.Document;
    import org.dom4j.DocumentException;
    import org.dom4j.Element;
    import org.dom4j.io.SAXReader;
    import org.xml.sax.InputSource;
    
    import datastructure.WeatherInfo;
    
    /**@author find
     * 解析获取的xml，提取出里面的信息
     * */
    public class ResolveXML {
    
        static final int MAXLAYER=100;
    
    
    
        InputSource in;
        SAXReader reader;
        Document doc;
        Element root,tempElement;
        //这里的weatherinfo是自定义的类。
        WeatherInfo weather;
        /**内层元素遍历*/
        public ResolveXML(String filename) {
            //初始化
            in=new InputSource(filename);
            reader=new SAXReader();
            reader.setEncoding("utf-8");
            weather=new WeatherInfo();
    
    
            try {
                doc=reader.read(in);
                //根
                root=doc.getRootElement();
    //          System.out.println(root.getName());
                //第一层，利用遍历器遍历
                Iterator<Element> item1=root.elementIterator();
                int i=0;
                while(item1.hasNext()){
                    tempElement=(Element)item1.next();
                                   //区分不同的孩子，这里是利用的序号，因为源文件的孩子类型的顺序是固定的。
                    switch (i) {
                    case 0:weather.setCity(tempElement.getText());                  break;
                    case 1:weather.setUpdateTime(tempElement.getText());break;
                    case 2:weather.setTemperature(Integer.parseInt(tempElement.getText()));break;
                    case 3:weather.setWindForce(tempElement.getText());break;
                    case 4:weather.setHumidity(Integer.parseInt(tempElement.getText().substring(0, tempElement.getText().length()-1)));break;
                    case 5:weather.setWindDirection(tempElement.getText());break;
                    case 10:setEnvironment(tempElement.elementIterator(), weather);break;
                    case 12:break;
                    case 13:break;
                    default:
                        break;
                    }
    
                    System.out.println("The layer1's son:"+tempElement.getName()+"\t num:"+i);
                    i++;
                }       
            } catch (DocumentException e) {
                System.out.println("Here's error in reading xml.");
    //          e.printStackTrace();
            }
        }
        /**处理environment这个分支*/
        public void setEnvironment(Iterator<Element>tempit,WeatherInfo tempweather){
            Element tempelement;
            int i=0;
            while(tempit.hasNext()){
                tempelement=(Element)tempit.next();
                switch(i){
                case 1:tempweather.setPM2_5(Integer.parseInt(tempelement.getText()));
    //          System.out.println(tempelement.getText());
                break;
                case 2:tempweather.setSuggest(tempelement.getText());break;
                case 3:tempweather.setQuality(tempelement.getText());break;
                case 9:tempweather.setUpdateTime(tempelement.getText());break;
                default :break;
                }
                i++;
            }
        }
        public void setForecast(Iterator<Element>tempit,WeatherInfo tempweather){
            Element tempelement;
            int i=0;
            while(tempit.hasNext()){
    
            }
        }
    
    
    }
    

weatherinfo类是自定义类，关于它的方法可以忽略。 

Tags:  [ Java ](http://www.findspace.name/tag/java)

####  About The Author 

![](http://bcs.duapp.com/findspace//blog/201502//gravatar.png)

#####  Find 

在读于山东大学，准程序猿，喜欢Coding 热爱生活，不甘平庸，喜欢折腾，也乐得清闲 更多资料请查看“福利&&关于”页面 
#### 原文：[http://www.findspace.name/easycoding/1073](http://www.findspace.name/easycoding/1073)