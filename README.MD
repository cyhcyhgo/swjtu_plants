# 西南交通大学植物导览网站
## 网站简介
本网站基于西南交通大学地图来介绍校园内植物分布情况，盘点西南交通大学不同区域的植物分布以及植物简介。利用Pycham和MySQL数据库开发设计网页，对不同植物进行比上一学期更加细化的描述，网页比以前更加简洁明了，功能更加优化，后台使用数据库能更加方便快捷地存储数据，此外，我们引入高德地图添加GPS定位功能，让浏览者更迅速、清晰地了解植物的具体分布区域 ，熟悉学校的地理环境，从而使用户可以更便捷地找到并欣赏植物。

## 界面图片展示
以下为展示图片<br>

### 网站主页面展示
这个是网站的主界面，用户点进网页后浏览到的界面是这个，用户可通过主界面完成一系列操作
![主页面展示](https://cyhcyhgo.github.io/Images/index.jpg)

<br><br>

### 网站的登录界面展示
这个是网站的登录界面，用户可通过登录界面进入本网站，浏览网站相关信息<br>
![登录页面展示](https://cyhcyhgo.github.io/Images/login.jpg)

<br><br>

### 网站的注册界面展示
这个是网站的注册界面，用户可通过注册界面成为本网站用户，浏览网站相关信息，同时可提交相关植物信息<br>
![登录页面展示](https://cyhcyhgo.github.io/Images/register.jpg)

<br><br>

### 详情页面展示
这个是网站的详情界面，用户可通过该页面来获得交大植物的详细信息
![注册页面展示](https://cyhcyhgo.github.io/Images/detail.jpg)

<br><br>


### 搜索页面展示
这个是搜索界面，用户可通过搜索界面寻找交大相关的植物<br>
![搜索页面展示是](https://cyhcyhgo.github.io/Images/search.jpg)

<br><br>

### 植物库页面展示
这个是植物库页面，收录了我们所收集的植物<br>
![植物库页面展示](https://cyhcyhgo.github.io/Images/library.jpg)

<br><br>

### 用户投稿页面展示
这个是用户投稿页面，用户可向我们投稿自己所收集到的植物信息<br>
![用户投稿页面展示](https://cyhcyhgo.github.io/Images/contribute.jpg)

<br><br>

## 项目日志
* 2021年  9月 24日 成员招募完毕，项目立项成功
* 2021年 10月  1日 网页前端基本框架搭建完毕
* 2021年 10月  5日 网页前端一级界面搭建完毕
* 2021年 10月 12日 网页三级界面搭建完毕
* 2021年 10月 26日 网页二级界面搭建完毕
* 2021年 11月 16日 网页一、二、三级界面连接成功，网页前端基本搭建完成
* 2021年 12月 24日 网页测试完成，所有预期功能均可正常实现。前端开发完成
* 2022年  3月 18日 将网页框架移植至flask框架下，开始后端开发
* 2022年  3月 25日 完成表单提交，验证功能，简化了详情展示界面（由原来的每个植物单独做一个页面简化为只有4个季节模板） 
* 2022年  4月  1日 以MYSQL数据库为基础搭建后端数据库
* 2022年  4月  8日 将MYSQL数据库与前端连接，完成数据库搭建
* 2022年  4月 20日 搭建用户注册，登录界面基本框架
* 2022年  5月  1日 进一步简化详情页面，只需要一个模板页面
* 2022年  5月  3日 用户注册界面基本完成
* 2022年  5月  4日 重新优化项目文件系统，分离各部分代码
* 2022年  5月 10日 使用蓝本配置路由
* 2022年  5月 12日 加入图形验证码功能
* 2022年  5月 14日 加入天气显示功能
* 2022年  5月 15日 完成管理员页面，管理员可修改，删除用户信息