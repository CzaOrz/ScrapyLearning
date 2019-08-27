__FILE__ = "Unfinished Schedule"

"""
所有渴望别人理解的行为都是弱智的行为，人的强大第一步，要学会孤独，第二步，要学会不理解，第三步，用结果去碾压
"""

# todo
"""
2019.07.03 - aiohttp中部分源码，还是可以了解下
2019.07.14 - 从新定义新目标，Scrapy源码需要尽快拿下，之后还有Django源码解析。这个又是一个巨无霸，哎，何时是个头
2019.07.14 - 逐渐构造散乱的知识点，是否可以联合起来（bootstrap、Vue、js、css、eCharts），进行一次自我突破?????主要是前端知识，后端也很多都是零散的知识点
2019.07.15 - 杨辉三角，找盘子问题，求素数。codepen  --- atom   前端不错的编辑器
2019.07.16 - 各种后端知识，如缓存、优化之路，太多了，学不完啊都不会啊
2019.07.19 - Scrapy虽然说最基本的流程走通了，但是还有很多细节处理没有抓到，他的通用中间件是如何工作的，等等
2019.07.19 - 能不能在数据统计图中加入像xs写的那样的数据过滤功能，感觉很不错的样子
2019.07.20 - 理下最近思路。爬虫：就是scrapy框架问题。后端：Django源码尝试看看。前端：特效部分不谈，太坑了。
2019.07.22 - KNN整理下
2019.07.23 - socket维护分布式队列，
2019.07.28 - 技能Http协议，还有数据库，我的天呢，都是坑，还多不知道，面试咋搞啊
2019.07.29 - Scrapy系列教程应该出了。模仿源码：基本的Request或Response对象管理|实现异步下载|加入引擎管理|加入调度器管理|加入下载器管理|
2019.07.31 - 廖雪峰老师的java，有点掉啊
2019.08.01 - blog注册页似乎有点问题，那个点
2019.08.12 - Mongodb的位算法是什么意思，位算法，感觉本来就很扯淡的样子
2019.08.13 - Scrapy中间件写的太少了，没有感觉，体会不到精髓
2019.08.13 - self.stats.inc_value(key) - 这行代码有点眼熟啊，这是干啥作用的呢
2019.08.13 - 可以搭建聊天的系统吗，这个好像超级掉的样子
2019.08.14 - import socketserver / from http.server import HTTPServer, BaseHTTPRequestHandler 这来年各个有点神奇的库，应该可以直接处理socket
2019.08.17 - mysql数据类型有哪些，什么组电选择什么类型，类型字节大小、限制条件。索引问题。
2019.08.19 - rabbitmq怎么玩啊，各种exchange还有key，晒意思  https://www.cnblogs.com/huanggy/p/9695712.html
2019.08.20 - css动态图https://www.jianshu.com/p/3a0fb1e30ec5     https://www.zhangxinxu.com/wordpress/2010/11/css3-transitions-transforms-animation-introduction/
2019.08.22 - scrapy如何做持久化数据的保存，有待研究哦
2019.08.27 - 微信爬虫和展示可以提上进程了，对于如何重新架构也可以提上进程了，还是以aiohttp为主，flask和django为辅，进行web开发。前端倒是一个需要好好构造的地方
2019.08.27 - 学习mysql不错的计划教程：https://blog.csdn.net/hw478983/article/details/78813938
"""

"""DONE!
2019.08.18 - flask部署，参考官方文档http://www.pythondoc.com/flask/deploying/  ，或者这货的似乎也不错https://www.cnblogs.com/xmxj0707/p/8452881.html
             command=gunicorn -c gunc.py hello:app    ; supervisor启动命令
             supervisord -c supervisor.conf
             supervisorctl reload :修改完配置文件后重新启动supervisor
2019.08.02 - 周末应该干点啥：
             scrapy爬虫的流程，要自觉点搞出来，只要把这个搞出来了，那干啥基本都好说。
             Django的官方文档，还没有吃完，只吃了一点点啊，这个还需要努力一把
             Java代码，这个有必要看吗，可以尝试性看下吧，毕竟还是主看python
             文书网那反爬咋搞啊
2019.07.29 - scrapy什么时候发送各种信号，signal.spider_open，有几种，分别什么时候发送，这个应该了解下
2019.07.18 - 反爬哪里似乎有点bug，误操可能导致无限回调??????
2019.08.14 - 现在问题就集中在，如何对Mongodb数据进行分页，查询，获取对应的数据 
            - SQL代码1：平均用时6.6秒 SELECT * FROM `cdb_posts` ORDER BY pid LIMIT 1000000 , 30 
            - SQL代码2：平均用时0.6秒 SELECT * FROM `cdb_posts` WHERE pid >= (SELECT pid FROM 
              `cdb_posts` ORDER BY pid LIMIT 1000000 , 1) LIMIT 30
2019.08.14 - 看下如何使用redis设置时间，一定时间过后就删除对应的数据  -- 设计：redis存入时间为访问的时间，时间超过一个月没有二次访问就删除
2019.08.12 - from scrapy.interfaces import ISpiderLoader - from zope.interface import implementer - @implementer(ISpiderLoader) - 这是个什么骚操作，接口吗?
2019.08.12 - 爬虫是在哪一步被实例化的，什么时候会执行__init__初始化函数。在init之前，执行了一次update_setting，对custom_setting进行了初始化，所以把custom_setting写在init里面是没有用的，但是把heartbeat写在init里面，这个倒是没有问题
2019.07.27 - 创建mongodb用户
            db.createUser({user:'admin',pwd:'admin',roles:[{role:'userAdminAnyDatabase',db:'admin'}]})
            db.auth("user","password")
            mongodb://user:password@localhost:27017/admin 
2019.07.27 - 完成proxy—pool开源项目 https://github.com/CzaOrz/ioco/tree/t426/open_source_project/proxy_pool/
2019.07.19 - 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware' 爬虫代理，我的天哪，我居然还不会，醉了。代理是个大问题啊！
        url_list = ['http://www.xicidaili.com/nn/',  # 高匿 'http://www.xicidaili.com/nt/',  # 透明 ]
        url_list = ['https://www.kuaidaili.com/free/inha/','https://www.kuaidaili.com/free/intr/']
2019.07.22 - blog模板苏沪有点问题
2019.07.19 - 二叉树的三种排序
2019.07.21 - 自如改版，价格居然放在了css里面，真是无语
2019.07.18 - 可以对文章进行分类，再来一个汇总的，这样就很nice了，还需要见一个数据库做统计分类
2019.07.18 - 删除评论模块有BUG，只删除了父评论，子评论还在！！！！
2019.06.04 - 百度那位小哥的代码，看看是不是可以加入Item组件，感觉很牛
2019.07.17 - scrapy如何停止，这是个问题
2019.07.14 - sx富文本编辑器，使用了Vue的初始化等没怎么建国的函数，尝试了解然后部署到自己机器上把，哈哈哈
2019.07.17 - 直接调用别人的js，太贱了吧，哈哈哈，害怕
2019.07.15 - Vue的几个实例，研究研究，copy过来，很吊哦
2019.07.15 - 为网站添加反爬机制 - 添加最简单的cookie反爬，后期看是否有必要再深入
2019.07.15 - root用户管理界面有问题，访问500
2019.07.12 - 如何关注前沿知识，什么是持续跟进一个项目？？？？  -- 居然还是在github上面找，哎，哪里找得到啊
2019.06.03 - md说明文件的编写规范与格式
2019.06.13 - pdf2html这个处理下 https://blog.csdn.net/silentacit/article/details/80309929
2019.06.17 - 工作所需：scrapy基本原理、反爬知识（涉及js重定向，加密，投毒等）、爬虫selenium模块、后端aiohttp、flask、Django模块，前端js，Vue模块，简单的异步实现
2019.07.03 - fiddler抓包工具到底怎么用啊啊啊啊啊啊啊啊啊   网易云爬虫 - https://www.jianshu.com/p/a45714d16294-
2019.06.25 - 前端页面太牛逼了，各种游戏！！！！！可以看看最后一页  -- 可以，见识到了各种牛逼的操作，前端是一个无底洞，知识太多了
2019.06.03 - redis集群，这个怎么玩啊  -- 集群这玩意暂时用不到啊
2019.05.29 - 解析附件部分代码需要整理docx，excel  -- 解析附件再见吧宝贝
2019.06.03 - 附件转化，doc转docx，pdf转html，还有pdf的相关操作，这些我是不是写过啊，再整理一下吧
2019.07.02 - IOCO爬虫流程图，可以用md文件写了放在首页啊，nice啊马飞
2019.01.12 - 前段炸裂特效，，这个需要从长计议啊，怎么展示是个问题
2019.06.18 - scrapy.extensions.logstats，scrapt的extension快怎么使用
2019.06.25 - src="../js/echarts.min.js"，数据可视化的插件https://www.echartsjs.com/tutorial.html这个太牛逼了      axios.min.js 是Vue的插件，异步请求。化柱形图和折线图，暂时只需要这两个把。
2019.06.26 - 插入视屏是个啥玩意：<video src="http://vjs.zencdn.net/v/oceans.mp4" type="video/mp4" autoplay="autoplay" controls="controls" loop="-1" poster="false.png">
2019.06.06 - <input type="text" ref="input1"/>  this.$refs.input1.value ="22"; 减少获取dom节点的消耗  - Vue props, mounted()
2019.06.25 - 在首页做一个统计算了，博客统计，访问统计、爬虫统计，然后最下面放一些细分模块。得好好想象到底怎么部署整个页面。
2019.06.24 - IOCO动图有BUG，左边评论栏也有bug，这玩意居然在屏幕缩小后出现在下面
2019.06.17 - 算法题，各种计算机基础（算法原理，计算机基础），太重要了把，你只会一些大家都有的东西有什么意义，Django，Flask等，都太普遍了，意义是找工作，而且也只能去打杂的工作！
2019.06.23 - 后序涉及到如何上传如片了，如何在手机端进行较良的展示，太丑了，好吧，电脑端也丑，那就以电脑为起始进行优化把。主要是脑子里就没有思路，重来没有好好勾画过整个结构
2019.06.17 - 工作经历：中软是测试，测GPS、充电、开关机，舆情日报，AndroidStudio。数博科技：爬虫工程师，
2019.06.17 - 对scrapy的理解还是不深，很多都不会
2019.06.02 - 爬虫框架中还有raise Exception模块需要写，对各种异常的定义，要个性化一点
2019.06.03 - Scrapy框架signal模块是个什么原理，怎么实际开发中还能用的到，怎么用，参考巨潮年报
2019.07.11 - 爬虫工厂可以放一些数据分析解析出来的图片，这个是不是可以弄一个缓存机制?
2019.06.12 - 爬虫的数据分析结果，可以将分析结果返回，传到前段，这个怎么搞
2019.06.12 - 介绍resume.html页面（写一写历史线就差不多了=0=）
2019.07.02 - 不能舍进求远，自己的框架有大问题，scrapy怎么会跳转这么慢，把其他逻辑偶读好好完善下，问题越来越多了
2019.07.09 - 呵呵，居然定时任务不会启动，真是醉了，今天再研究研究吧没改写爬虫了，没有输出
2019.06.12 - （首先新的爬虫可以开始看看了，以先看职位，如boss直招和智联招聘这两个，房天下爬虫也可以看看，那么爬虫就有4个了）
2019.06.12 - 3个新爬虫（boss直招、智联招聘、房天下，共计四个在线爬虫）。
2019.06.12 - 今天再把搜索功能移植过去，基本已有的就都OK了，然后就是添加新的功能。
2019.07.09 - 能不能部署心跳啊，感觉怪怪的，把邮件模块去除把，这个定时真是搞事，要不今天搞定?
2019.07.03 - pip install pycryptodome 安装网易云解析音乐的爬虫包.
2019.07.01 - 现阶段的主要任务就是编写文档，储存补给站 -- 文档卸载这边感觉不太合适啊，可以适当的卸载博客园里面吧
2019.07.03 - "select name from sqlite_master where type='table' order by name"  -- 神奇的sql指令
2019.07.01 - 发展历史线，可以使用ol/li有序表？还是ul无序表
2019.06.30 - 邮件模块记得拿到手，别浪费了
2019.06.18 - 微信可以了解验证码，微博可以练selenium -- 没有遇到验证码，说明有cookie，下午可以试一试
2019.06.26 - 监听回车键进行登陆完成
2019.06.24 - wangEditor 富文本编辑器  background-color: #f4f3f4  xs 使用的背景颜色，很好看啊，浅灰色
2019.06.25 - 富文本编辑器有一个坑，我似乎没法获取文本内容，阿卡宁夏xs泽呢么获取的，怎么获取怎么编辑。图片视频什么都可以直接插入，神奇
2019.06.26 - python邮件功能发出去
2019.06.25 - 添加统计模块 - alter table blogs add count bigint not null default 0;
2019.06.03 - 现在的框架不支持post请求下载，这个显然不太合理，可以研究研究怎么下载post请求的数据 - post请求就算了，这种直接存为bytes
2019.06.05 - 关于各高校高考分数的信息，可以做一个数据分析，这个就没必要做持续，因为每年就一次高考，或许可以提供某些服务。爬985高校，211高校
2019.06.05 - 前端那种折线图，动态展示是怎么做的啊，折线，柱状图，饼状图等等 - js搞定，不会，但是会扣
2019.06.06 - 各高校的分数等情况，是时候提上日程了 - 反爬没搞定==
2019.06.11 - 绘图软件SAI，怎么说 - 打扰，应该比想象中的难
2019.06.22 - 如何在右上角显示最新评论，这个可以有，或者可以设置点赞评论?
2019.06.23 - # -*-coding: utf-8-*-
2019.06.17 - bootstrap wysiwyg 富文本编辑器
2019.06.18 - 普通用户管理界面的完善，博客如何添加其他字体或文本，富文本编辑器?
2019.06.18 - numberAnimate数字滚动插件, 动态折线图 https://www.html5tricks.com/html5-canvas-animated-line.html,  临时https://blog.csdn.net/vhwfr2u02q/article/details/79492303
2019.06.18 - 评论回复并拼接是如何实现的
2019.06.21 - 子评论时间bug
2019.06.17 - 博客编辑页面，root管理博客页面，个人管理个人博客页面
2019.06.05 - bs还是需要重新再看一遍啊，这次只看那些细节，我发现似乎只需要name点东西就可以拼出我想要的，如首页三列，左边是章节内容栏，右边是导航栏目，侧滑菜单是大方向，中间是内容
2019.06.05 - 正则学习，零宽断言 -- re.compile("var\s+(rand\d+)\s*=\"(.+?)\";(?=[\s\S]+document\.write\(\"(.+?)：.+\"\+\\1\+)") 零宽断言，中间居然能隔这么远，这已经是扣了
2019.06.02 - BoopStrap/JavaScript插件
2019.05.30 - 用户注册和登陆模块，前端的编写，后端需要在整理整理，别的不说，起码把注册页面再次搞出来把
2019.06.11 - 百度地图模块
2019.06.12 - Vue的学习
2019.06.12 - Jquery学习
2019.06.11 - inspect模块害的再斟酌斟酌
2019.06.03 - scrapy如何增加日志模块，可以在下载中执行指令-s LOG_FILE= --loglevel=INFO来启动吗
2019.06.04 - 廖老师的git和sql还是要再看看啊，这玩意有用的很
2019.06.03 - 如何使用logging模块兵输出具体的文件 from logging.handlers import TimedRotatingFileHandler 模块
2019.06.02 - BoopStrap组件
2019.06.03 - window下如何开启定时任务
2019.06.03 - 百度那位小哥的模拟Scrapy框架，可以学习学习精髓，有点小经典
2019.06.02 - 爬虫框架解析部分多线程或者多进程跑。- 对每一个线程传入标记位，以id最后一位作为判断计算此任务属于哪个线程，从而人为分配任务而非操作系统分配
2019.06-02 - BoopStrap全局CSS样式
2019.05.29 - 中国裁判文书网，对key的获取，需要处理
2019.05.30 - scrapy的deffer，或者说twisted模块如何使用
2019.05.31 - Failure - 该框架，解析部分是否可以使用异步，下载部分是否有必要使用异步。异步是使用twisted还是使用简单的async，这两个那种好一点，可以先研究上面的twisted再下结论
2019.05.31 - 把相应的js反爬，写一个中间件可以，name每次只需要调用该中间件即可，而不是每个模块都去写一遍处理逻辑
2019.05.29 - 把对计算云的辅助操作单独写一个模块，包含压缩与推送
2019.05.30 - 对工具进行适当地整理，把不要的删除，或者重新命名整合下
2019.05.30 - scrapy中间件需要在写一个模块，用于熟悉与练习
2019.05.30 - 计算云中新建线上环境的git仓，用于部署，还有专门链接文件的仓。即一个专门接受文件，用于链接这里面的文件，来实现部署
2019.05.30 - 今晚学习了集中算法冒泡、直接插入、希尔排序、快速排序、简单排序
"""

"""不错的学习平台
html学习平台        https://www.html5tricks.com/
js转化平台          http://tool.oschina.net/codeformat/js    
爬虫学习            https://github.com/Jack-Cherish/python-spider/commit/10610ab354fc1bb8264edc566766df6588111914     https://cuijiahua.com/blog/ml/
百度AI开放平台       https://ai.baidu.com/docs#/Face-Detect-V3/top
JS                  https://github.com/SUNNERCMS/30daysJavascript

"""

"""
645948
You Are An Apple In My Eyes
Courage is not the absence of fear, but rather the judgment that something else is more important than fear.
"""

#todo
"""
在我不能丢弃当前工作的前提下，考研的可能基本是0. 但是数据结构是一门基础课程，还是需要学习的。面试笔试都没得谈。
构建已有的web端：我到底需要一个怎样的前台和后端的功能
后端：等部署好了，要开始接触flask和Django了
爬虫：scrapy需要逐渐写完总结，初步就可
爬虫requests小模块是否有必要完善。
有关自动化部署的selenium，博个可能也需要我完成一个自动抢票的玩具

首先首页不能是现在这样的，首页应该是展示页，展示这里的内容，模块，功能，意义
左上角可以跳转，或者展示页力可以跳转

不能有左边的导航栏，在上面添加导航栏，然后
第一个作者没问题，怎么写这个就是个问题了。一片骚气的自我介绍哦？
第二个改名叫知识工厂

/ 可以指向作者，如果你前端写的够靓仔的话
"""

# todo
"""
085212  软件工程
思想政治理论/英语二/数学二/887数据结构与算法分析

《数据结构与算法分析》
术语解释         15%
选择、填空       30%
论述、简答       30%
设计及应用       25%

（一）基本概念和术语
（二）线形表
（三）栈和队列
（四）串
（五）树和二叉树
（六）查找
（七）图
（八）内部排序
"""


"""
（一）基本概念和术语
1．数据结构的概念
2．抽象数据结构类型的表示与实现
3．算法，算法设计的要求，算法效率的度量，存储空间要求。
（二）线形表
1．线形表的类型定义
2．线形表的顺序表示和实现
3．线形表的链式表示和实现 
（三）栈和队列
1．栈的定义，表示和实现
2．栈的应用：数制转换，括号匹配，行编辑，迷宫求解，表达式求值
3．栈与递归实现
4．队列。 
（四）串
1．串的定义，表示和实现 
2．串的模式匹配算法
（五）树和二叉树
1．树的定义和基本术语 
2．二叉树，遍历二叉树和线索二叉树
3．树和森林：存储结构，与二叉树的转换，遍历 
4．霍夫曼树和霍夫曼编码
5．回溯法与树的遍历
（六）查找
1．静态查找表
2．动态查找表
3．哈希表
（七）图
1．图的定义和术语 
2．图的存储结构 
3．图的遍历
4．图的连通性问题
5．拓扑排序与关键路径
6．最短路径
（八）内部排序
1．排序的概念
2．插入排序
3．快速排序 
4．选择排序：简单选择，树形选择，堆排序
5．归并排序
6．基数排序 
7．各种排序方法的比较
"""

"""（一）基本概念和术语
数据结构：数据结构是相互之间存在一种或多种特定关系的数据元素的集合。
数据：是对客观实物的符号表示。在计算机科学中指所有能够输入到计算机中并被计算机程序处理的符号的总称。
数据元素：是数据的基本单位。
数据对象：是性质相同的的数据元素的集合，是数据的一个子集。

数据元素相互之间的关系称为结构。4类基本结构：集合、线性结构、树形结构、图形结构。
Data_structure = (D, S)  // D是数据元素的有限集，S是D上关系的有限集
复数：Complex = (C, R)  // C为两个实数的集合{c1, c2}，R={P}，P是定义在集合C上的一种关系，即c1是复数的实部，c2是复数的虚部
简单事物管理：Group = (P, R) // P={T,G1,..,Gn,S11,..,Snm}, R={R1, R2}, R1={<T, Gi>}, R2={<Gi, Gij>}, 1 <= n <= 3, 1 <= m <= 2  // 可以描述为一位导师管理3位研究生，而每位研究生管理两位学生

逻辑结构：数据元素之间的逻辑关系
数据结构在计算机中的映象，称为物理结构，也称春存储结构。包括数据元素的表示和关系的表示。  
在计算机中表示信息的最小单位是二进制位的一位，叫bit位。我们可以用一个由若干位组合起来形成的一个位串表示一个数据元素（常见：一个字长的位表示一个整数，用8位二进制数表示一个字符串），通常称这个位串为元素或节点。当数据元素（位串）是由若干数据项组成的时候，位串中对应各个数据项的子位串称为数据域，因此元素或节点可以看成是数据元素在计算机中的映象。
关系在计算机中有两种不同的表示方法：顺序映象和非顺序映象，对应顺序存储结构和链式存储结构。顺序映象特点是借助元素在存储器中的相对位置来表示数据元素之间的逻辑关系。非顺序映象的特点是借助指示元素存储地址的指针的指针来表示数据元素之间的逻辑关系。

数据类型：最早出现在高级程序语言中，描述操作对象的特性。每种数据类型都明显或隐含的规定了程序执行期间变量或表达式所有可能取值的范围，以及在这些值上允许进行的操作。因此
数据类型是某一类值的集合和定义在这个值集上的一组操作的总称。

某种意义上，数据结构可以看成是一组具有相同结构的值，而结构类型可以看成是一种数据结构和定义在其上的一组操作组成。
高级程序语言中数据类型可分为两类：非结构的原子类型、结构类型。原子类型是不可分解的，是最基本的类型。结构类型的值是由若干成分按某种结构组成的，是可拆解的，组成他的成分，可以是非结构的，也可以是结构的。
抽象数据类型，是指一个数学模型以及定义在该模型上的一组操作。如：不同计算机上的整数类型是一个抽象数据类型。因为尽管他们实现的方法可能不能，但他们所表达的含义，对于用户来说是相同的。因此是一个抽象类型。那么抽象的意义就在于数据类型的数学抽象特性。
抽象数据类型的定义由一个值域和定义在该值域上的一组操作组成。根据值的不同特性，可分为：原子类型、固定聚合类型、可变聚合类型。
原子类型：不可分子。
固定聚合类型：由确定数目的成分按某种结构组成。如复数由两个实数依确定的次序关系组成。
可变聚合类型：其值的成分的数目是可变的。
(D, S, P) // D数数据对象，S是D上的关系集，P是对D的基本操作集

多行数据类型：指其值的成分不确定的数据类型，如某一数组，其每一子元素都可以不同，但从抽象数据类型的角度看，是具有相同的数学特性的，故称之为多行数据类型。



数据结构是计算机存储、组织数据的方式。数据结构是指相互之间存在一种或多种特定关系的数据元素的集合。往往同高效的检索算法和索引技术有关。
数据结构是指相互之间存在着一种或多种关系的数据元素的集合和该集合中数据元素之间的关系组成。可记为（D，R）。D是数据元素的集合，R是该集合中所有元素之间的关系的有限集合
数据的逻辑结构，反应数据元素之间的逻辑关系的数据结构，其中逻辑关系是指数据元素之间前后件关系，与在计算机中的存储位置无关
集合：数据结构中的元素除了同属一个集合的相互关系外，别无其他关系
线性结构：数据结构中的元素存在一对一的相互关系
树形结构：数据结构中的元素存在一对多的相互关系
图形结构：数据结构中的元素存在多对多的相关关系

数据的物理结构，指数据的逻辑结构在计算机存储空间的存放形式。数据的物理结构是数据结构在计算机上的映像，它包括数据元素的机内表示和关系的机内表示。由于具体的实现方法有顺序、链接、索引、散列等等，所以一种数据结构可以表示成一种或多种存储结构。机内表示，也叫映像方法。
数据元素的机内表示，用二进制bit的位串表示数据元素，通常称这种位串为节点node。当数据有若干个数据项组成时，位串中与个数据项对应的子位串称为数据域data field，因此，节点是数据元素的机内表示
关系的机内表示，数据元素之间的关系的机内表示可以分为顺序映像和非顺序映像，常用两种存储结构，即顺序存储与链式存储结构。顺序映像借助元素在存储器中的相对位置来表示数据元素之间的逻辑关系。非顺序映像借助指示元素存储位置的指针pointer来表示数据元素之间的逻辑关系

数据结构具体指同一类数据元素中，各元素之间的相互关系，包含三个组成成分：数据的逻辑结构’数据的存储结构、数据的运算结构
"""


"""resume
熟悉http协议，这句话有点难啊

中软国际
测试工程师
1、负责测试华为荣耀畅玩系列产品GPS、充电等模块功能完整性
2、驱动开发接口人，对接各个开发员工，追踪日常舆情，及时

数博科技
爬虫工程师
1、负责政府处罚类领域爬虫的开发、数据清洗。
2、监控爬虫调度的正常运行

项目经验：
--------------------------------------------------
分布式爬虫： -- 这玩意项目应该是没得的，这咋办嘛
分布式爬虫，怎么设计。scrapy-redis是一个 -- 在琢磨琢磨这方面的文章吗

--------------------------------------------------
爬虫：
中国裁判文书网（js加密，重定向，cookie反爬）、（截止7.25，今年已更新三次，sojson.v5反爬）涉及js加密重定向获取cookie，请求参数加密
自如网（图像识别）：（截止7.25，今年更新一次，数据加密）涉及数据加密，图像识别
IP代理（后端）：个人维护（这玩意怎么维护，IP推出去之后怎么进来，怎么进行打分啊。这倒是个问题）

-------------------------------------------------
监控系统：
心跳监控（被动监控）：维护爬虫的正常运行 - 应该把裁判文书网，自如，IP等都加入进去

裁判文书网是否改版，这个可以有，写个爬虫轮询下

-------------------------------------------------
个人网站：
部署有多个线上爬虫（目前只在维护一个，其余已挂）
简易数据展示
博客内容（无博客，都是test内容）

前段也需要添补添补，等域名下来应该就好很多了

"""



"""
二手书、校服、班服定做
冰淇淋、奶茶
生活用品
情感指导
礼品包装
培训班
实体店面
大一新生办公网吧
"""
"""
爬虫、前端、后端、微信小程序、视频
项目：电商项目、视频剪辑、ps
"""

"""
2019.08.27 - 新爬虫框架设计
爬虫默认使用随机User-Agent，可以提供Fixed固定UA
动态加载应该使用一个开关，没有必要实时开启，默认也不需要整个流程走通
原生流程一定需要走通。

"""















