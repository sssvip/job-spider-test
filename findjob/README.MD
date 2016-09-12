##README

为方便获取公司职位信息，便于自己找校招工作哈哈，制作简单爬虫。

### 更新说明：2016-09-12
新增独立测试模块，新增txt文本输出方法，完善公司职位信息
新增company_test.py，position_test.py
outer板块相关类增加out_txt()方法，便于输出txt文档，便于转化excel查看，便于后期插入自己数据库分析什么的，哈哈


### 此次模块简单说明图
![这里写图片描述](http://img.blog.csdn.net/20160909112957688)

#### HtmlDownloader:专门负责html资源下载的类
#### UrlManager:负责爬虫URL管理类，放置重复爬取相同网页
#### HtmlOutputer:专门负责输出类，为方便展示数据，采用html输出
##### 1.Company_Outputer: 具体特殊业务逻辑类，针对公司信息进行输出
##### 2.Position_Outputer: 具体特殊业务逻辑类，针对职位信息进行输出
#### Parser:解析网页类
##### 1.CompanyUrl_Parser: 针对信息解析网页Url，返回公司Url集合
##### 2.CompanyInfo_Parser: 针对信息解析网页信息，返回公司信息实体类
##### 3.Position_Parser: 针对信息解析网页信息，返回职位信息实体类
#### Model:建立相关实体类，方便数据的打包传输
#### Main:程序入口模块

代码详情见于：https://github.com/sssvip/spider/tree/master/findjob


###简单效果展示

![1-10页信息爬取](http://img.blog.csdn.net/20160909131554122)

####公司信息的获取

![这里写图片描述](http://img.blog.csdn.net/20160909120032706)

####对应公司职位信息的获取

![这里写图片描述](http://img.blog.csdn.net/20160909120045159)
